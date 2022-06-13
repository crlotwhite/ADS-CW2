def box(func):
    def wrapper(*args):
        print('=' * 25)
        r = func(*args)
        print('=' * 25, end='\n\n')
        return r

    return wrapper


def dialog_box(title, menus):
    def outer_wrapper(func):
        def inner_wrapper():
            func()
            print('=' * 25)
            print(title, end='\n\n')
            for i, menu in enumerate(menus):
                print(f'{i+1}.{menu}')
            print('=' * 25, end='\n\n')
            return input('=> ')

        return inner_wrapper

    return outer_wrapper
