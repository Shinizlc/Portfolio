import requests
from pprint import pprint

class Metrics_evaluation:
    base = 'https://data.messari.io/api/v2/'
    headers = {'x-messari-api-key':'04cb6b0d-9412-4ff3-a824-3650e11ef909'}
    def get_data(self,field):
        # try:
        list_agg=[]
        with requests.get(Metrics_evaluation.base+field,headers=Metrics_evaluation.headers,params={'limit':500}) as data:
            #pprint(data.json()['data'][0]['profile']['economics']['launch']['fundraising']['sales_rounds'])
            # for raw_data in data.json()['data']:
            #     dict_agg = {}
            #     dict_agg['Symbol']=raw_data['symbol']
            #     dict_agg['MarketCap']=raw_data['metrics']['marketcap']['current_marketcap_usd']
            #     dict_agg['TokenSales']=raw_data['profile']['economics']['launch']['fundraising']['sales_rounds']
            #     dict_agg['EmittedTokens']=raw_data['metrics']['supply']['circulating']
            #     dict_agg['MaxSupply']=raw_data['profile']['economics']['consensus_and_emission']['supply']['max_supply']
            #     dict_agg['FROM_ATH']=raw_data['metrics']['all_time_high']['percent_down']
            #     dict_agg['ATH'] = raw_data['metrics']['all_time_high']['price']
            #     list_agg.append(dict_agg)
            return data.json()#list_agg


    # def iterator_through_metrics(self):
    #     if self.get_data('assets') is not None :
    #         try:
    #             for token in self.get_data('assets'):
    #                if len(token['TokenSales'])>0 and token['MarketCap']>0:
    #                     print(self.get_marketcap_tokensale_percentage(token['TokenSales'],token['MarketCap']))
    #                     #print(token['TokenSales'],token['MarketCap'])
    #                else:
    #                    pass
    #         except:
    #             pass



    # def get_marketcap_tokensale_percentage(self,TokenSales:list,MarketCap:float)->float:
    #     total_sales_funded = 0
    #     for token_sale in TokenSales:
    #         for k,v in token_sale.items():
    #             if k == 'amount_collected_in_usd':
    #                 total_sales_funded+=v
    #         return MarketCap/total_sales_funded








    def get_top_n_marketcap(self,top_n=30):
        token_list = self.get_data('assets')
        by_marketcap =[token for token in sorted(token_list,key=lambda token:token['MarketCap'],reverse=True)][:top_n]
        return by_marketcap


    def get_emitted_percentage(self):
        top_tokens = self.get_top_n_marketcap()
        for token in top_tokens:
            print(token['EmittedTokens'],token['MaxSupply'])
            #print ((token['EmittedTokens']/token['MaxSupply'])*100)







    def get_avg_ico_price(self):
        pass

if __name__ == '__main__':
    metics = Metrics_evaluation()
    pprint(metics.get_data('assets/BNB/profile'))
