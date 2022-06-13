from dvd.container import DVListType
from dvd.type import DVD
from ui.dialog.deco import box


@box
def admin_dvd_add_menu(context):
    print('Admin - DVD - Add', end='\n\n')
    print('Enter the information of the DVD you want to add.')
    name = input('- Name: ')
    stars = input('- Stars: ')
    producer = input('- Producer: ')
    director = input('- Director: ')
    production_company = input('- Production Company: ')
    total_quantity = int(input('- Total Quantity: '))

    container: DVListType = context['dvd']
    if container.add(DVD(
        name,
        stars,
        producer,
        director,
        production_company,
        total_quantity
    )):
        print('Success')
    else:
        print('Failed..')


@box
def admin_dvd_search_menu(context):
    print('Admin - DVD - Search', end='\n\n')
    print('Enter the name of the dvd you want to find.')
    name = input('- Name: ')
    container: DVListType = context['dvd']
    result = container.search(name)
    if result is not None:
        print(result)
    else:
        print('There is not result..')


@box
def admin_dvd_update_menu(context):
    print('Admin - DVD - Update', end='\n\n')
    print('Enter the name of the dvd\'s information you want to edit.')
    name = input('- Name: ')
    container: DVListType = context['dvd']
    dvd = container.search(name)
    if dvd is None:
        print('There is no result...')
        return

    kwargs = {}
    print('What do you want to change?')
    while True:
        attrs = [
            'name',
            'stars',
            'producer',
            'director',
            'production_company',
            'copies',
            'total_quantity',
            'Cancel'
        ]
        for i, attr in enumerate(attrs):
            print(f'{i+1}. {attr}')

        option = input('=> ')
        match option:
            case '1' | '2' | '3' | '4' | '5' | '6' | '7':
                print('What would you like to change to?')
                new_value = input('=> ')
                kwargs[attrs[int(option)-1]] = new_value
            case '8':
                return
            case _:
                print('Wrong Input..\n\n')

        print('Anything Else? [y/N]')
        if input('=> ').lower() != 'y':
            break

    if container.update(dvd, **kwargs):
        print('Success')
    else:
        print('Failed..')


@box
def admin_dvd_remove_menu(context):
    print('Admin - DVD - Remove', end='\n\n')
    print('Enter the name of the dvd\'s information you want to edit.')
    name = input('- Name: ')
    container: DVListType = context['dvd']
    dvd = container.search(name)
    if dvd is None:
        print('There is no result...')
        return

    if input('Are you sure? [y/N]: ').lower() == 'y':
        if container.remove(dvd):
            print('Success')
        else:
            print('Failed..')


@box
def user_dvd_browse_menu(context):
    print('User - Browse DVD', end='\n\n')
    print('Select start character')
    print('- Alphabet: lowcase e.g. a')
    print('- Number: *')
    print('- All: (empty)')
    container: DVListType = context['dvd']
    user_input = input('=> ')
    if user_input.isalpha() or user_input == '*':
        cache = container.listing(user_input[0])
    elif not any(user_input):
        cache = container.show_all()
    else:
        print('Wrong Input..\n\n')
        return

    user_dvd_list_menu(context, cache)


@box
def user_dvd_list_menu(context, cache):
    print('User - Browse DVD', end='\n\n')
    line_count = 10
    current_page = {}

    while True:
        # slice page from cache
        for i, dvd in enumerate(cache):
            if len(current_page) == line_count:
                break
            else:
                current_page.update({f'{i+1}': dvd})

        # show current page
        if any(current_page):
            for k, v in current_page.items():
                print(f'{k}. {v}')
        else:
            print('There is no result...')

        user_input = input('Please select the DVD you want. (q: back): ')
        if current_page.get(user_input, None) is not None:
            user_dvd_detail(context, current_page[user_input])
        else:
            if user_input.lower() == 'q':
                return
            else:
                print('Wrong Input..\n\n')


@box
def user_dvd_detail(context, dvd):
    print(f'User - Browse DVD - {dvd.name}', end='\n\n')
    print(f'Title: {dvd.name}')
    print(f'Stars: {dvd.stars}')
    print(f'Producer: {dvd.producer}')
    print(f'Directer: {dvd.director}')
    print(f'Production Company: {dvd.production_company}')
    print(f'Copies: {dvd.copies}')
    print(f'Total Quantity: {dvd.total_quantity}')
    print(f'Available: {dvd.isavailable}')

    while True:
        user_input = input('Please select the job you want. (r: rent, q: back): ')
        match user_input:
            case 'r':
                from customer.type import Customer

                user: Customer = context['user']
                if user.rent(dvd):
                    print('Rent DVD Successfully')
                    context['dvd'].update(dvd, copies=dvd.copies)
                    context['customer'].update(user, rented_dvd=user.rented_dvd_str)
                    return
                else:
                    print('The DVD is not Available..')
            case 'q':
                return
            case _:
                print('Wrong Input..\n\n')


