import asyncio
# async def test():
#     await asyncio.sleep(5)
#
#
#
#


# asyncio.run(main_func())

#
# def test():
#     for i in range(10):
#         yield i #поставил выполнение функции на паузу и вывел i
#         print(i)
#         yield i
# #
# t = test()
# print(next(t))
# print(next(t))
# print(next(t))

async def main_func():
    print(f'begging of main program')
    # loop = asyncio.get_running_loop()
    task1= asyncio.create_task(first_internal())
    task2 = asyncio.create_task(second_internal())
    # await task1
    # await task1
    # await first_internal()
    # await second_internal()
    print(f'end of main program')



async def first_internal():
    print(f'begging of first internal')
    await asyncio.sleep(10)
    print(f'end of first internal')


async def second_internal():
    print(f'begging of second internal')
    await asyncio.sleep(5)
    print(f'end of second internal')

###то есть main можно вызвать как через asyncio.run так и создав loop_event и добавив его через create_task в список выполнения
### asyncio.create_task в данном случае не работает так как в отличии от asyncio.run тут нужно сперва создать loop_even и привязать уже к нему
###run_until_complete говорит loop_event работать пока работает какой конткретный корутин

# loop = asyncio.get_event_loop()
# task = loop.create_task(main_func())
# loop.run_until_complete(task)

# both_tasks = asyncio.gather(first_internal(),second_internal())
# task = loop.create_task(both_tasks)

# task = loop.create_task(main_func())
# loop.run_until_complete(both_tasks)####запускает loop созданный через get_event_loop()
# asyncio.run(main_func())# сам автоматически создает loop


