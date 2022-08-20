def test():
    try:
        #inner_func(323)
        def inner_func(val):
            try:
                return val/12
            except:
                print(f'we cannot divide string by int')
        return inner_func('some shit')
    except:
        print(f'outer exception there is no such function')


print(test())