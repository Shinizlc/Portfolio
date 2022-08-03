import pymongo
from pprint import pprint
from datetime import datetime,timedelta
from LOGGER_MONGO import logger
#insert values
# fill_collection = [{'id_num':'some value '+ str(i)} for i in range(1,1_000_000)]
# calls_collection.insert_many(fill_collection)
####Define connections
connection = pymongo.MongoClient(host='127.0.0.1',port=27017)
callog_db = connection['calllog']
calls_collection = callog_db['calls']

#connection_confg_db = pymongo.MongoClient(host='127.0.0.1',port=27017)
config_db = connection['config']## store information in a database
chunk_collection = config_db['chunks']

mongo_balancer_db = connection['mongo_balancer']
mongo_balancer_collection = mongo_balancer_db['skipped_chunks']


###Check for all old skipped_chunks(older than 1 month)

obsolete_data = mongo_balancer_collection.find({'lastmodified':{'$lte':datetime.utcnow()-timedelta(minutes=10)}}).count()
if obsolete_data>0:
    print(f'need to delete some obsolete data')
    print(obsolete_data)
    mongo_balancer_collection.delete_many({'lastmodified':{'$lte':datetime.utcnow()-timedelta(minutes=10)}})




###Take all not obsolete chunks that should be skipped
skipped_chunks_list = mongo_balancer_collection.find()
skipped_chunks_list = [skipped_chunk for skipped_chunk in skipped_chunks_list]


shards = ['shard1', 'shard2', 'shard3']###take info from config db
threshold = 20 ##difference between shard sizes in percentage ### store in database
shard_size = [{'name':shard,'storageSize': callog_db.command('collstats', 'calls')['shards'][shard]['storageSize'] } for shard in shards]
sorted_shard_size = sorted(shard_size, key=lambda x: x['storageSize'], reverse=True)
biggest_shard = sorted_shard_size[0]['name']
smallest_shard = sorted_shard_size[-1]['name']
minChunkSize = 10_485_760 ##store in database
maxChunkSize = 939_524_096




def shard_diff():
    '''Some check what is a difference in size between biggest and smallest shard'''
    size_first = sorted_shard_size[0]['storageSize']
    size_last = sorted_shard_size[-1]['storageSize']
    diff = (size_last/size_first)*100 # diff between shard_size
    if diff<=threshold:
        print(f' There is no need to migrate any chunks')
    else:
        return chunk_to_migrate()



def chunk_migration(chunk):
    # try: ##create 2 exceptions: chunk to big and others
    '''Procedure for moving '''
    callog_db.admin.command({'moveChunk': chunk['ns'],'bounds':[{'id_num':chunk['min']['id_num']},{'id_num':chunk['max']['id_num']}],'to':smallest_shard})
    print(f'Chunk {chunk["_id"]} was moved from {biggest_shard} to {smallest_shard}')
    # except:
    #     print(f'cannot move chunk {chunk["_id"]}')

def chunk_to_migrate():
    '''find chunks to migrate'''
    list_of_chunks = chunk_collection.find({'ns':'calllog.calls','shard':biggest_shard,'$or':[{'jumbo':False},{'jumbo':{'$exists':False}}]})
    list_of_chunks = [chunk for chunk in list_of_chunks]
    #getting the size of the chunks

    if len(skipped_chunks_list) > 0:
        logger.info("The size of skipped chunks collection is more than 0")
        ##looking for inersection with skipped_chunks_list
        exclude_list = [f for i in skipped_chunks_list for f in list_of_chunks if i['_id'] == f['_id']]
        for chunk in list_of_chunks:
            if chunk not in exclude_list:
                logger.info('Chunk is not in exclude list')##???
                chunk_size = config_db.command({'datasize': chunk['ns'], 'keyPattern': chunk['_id'], 'min': chunk['min'], 'max': chunk['max']})['size']
                if chunk_size>=minChunkSize and chunk_size<=maxChunkSize:
                    print(f'we"ve got candidate to migrate {chunk["_id"]} from {biggest_shard} to {smallest_shard}')
                    chunk_migration(chunk)
                else:
                    print(chunk)
                    mongo_balancer_collection.insert_one(chunk)
                    mongo_balancer_collection.update_one({'_id': chunk['_id']},{'$currentDate':{'lastmodified': {'$type': 'date'}}})###adding lastmodified column
                    print(f'+1')
    else:
        logger.info("The size of skipped chunks collection is equal to 0")
        for chunk in list_of_chunks:
            chunk_size = config_db.command({'datasize': chunk['ns'], 'keyPattern': chunk['_id'], 'min': chunk['min'], 'max': chunk['max']})['size']
            if chunk_size>=minChunkSize and chunk_size<=maxChunkSize:
                print(f'we"ve got candidate to migrate {chunk["_id"]} from {biggest_shard} to {smallest_shard}')
                chunk_migration(chunk)
            else:
                print(chunk)
                mongo_balancer_collection.insert_one(chunk)
                mongo_balancer_collection.update_one({'_id': chunk['_id']},{'$currentDate':{'lastmodified': {'$type': 'date'}}})###adding lastmodified column
                print(f'+1')





if __name__ == '__main__':
    shard_diff()

