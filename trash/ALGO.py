from functools import reduce

# d=defaultdict(list)
# for i in [1,2,3]:
#     d['some data'].append(i)
# print(d)


from time import time


def decor(func1):
    time_start = time()

    def wraper(*args):
        return func1(*args)

    time_end = time() - time_start
    print(time_end)
    return wraper


@decor
def do_smth(*args):
    return .5 * reduce(lambda x, y: x + y, *args)


print(do_smth([1, 24, 4]))
