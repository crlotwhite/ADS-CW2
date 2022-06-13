from customer.container import CustomerBTreeType
from customer.type import Customer
from ui.dialog.deco import box


@box
def admin_customer_add_menu(context):
    print('Admin - Customer - Add', end='\n\n')
    print('Enter the name of the customer you want to add.')
    name = input('- Name: ')
    container: CustomerBTreeType = context['customer']
    if container.add(Customer(name=name)):
        print('Success')
    else:
        print('Failed..')


@box
def admin_customer_search_menu(context):
    print('Admin - Customer - Search', end='\n\n')
    print('Enter the name of the customer you want to find.')
    name = input('- Name: ')
    container: CustomerBTreeType = context['customer']
    result = container.search(name)
    if result is not None:
        print(result)
    else:
        print('There is not result..')


@box
def admin_customer_update_menu(context):
    print('Admin - Customer - Update', end='\n\n')
    print('Enter the name of the customer whose information you want to edit.')
    name = input('- Name: ')
    container: CustomerBTreeType = context['customer']
    customer = container.search(name)
    if customer is None:
        print('There is no result...')
        return

    print('What do you want to change?')
    for i, attr in enumerate(['name', 'Cancel']):
        print(f'{i+1}. {attr}')

    option = input('=> ')
    match option:
        case '1':
            print('What would you like to change to?')
            new_name = input('=> ')

            if container.update(customer, name=new_name):
                print('Success')
            else:
                print('Failed..')
        case '2':
            return
        case _:
            print('Wrong Input..\n\n')


@box
def user_get_user_name(context):
    print('User - Get User Info', end='\n\n')
    name = input('What\'s Your Name:: ')
    container: CustomerBTreeType = context['customer']
    customer = container.search(name)
    if customer is None:
        print('There is no result...')
        return False

    context.update({'user': customer})
    return True


@box
def user_management_my_rented_menu(context):
    user: Customer = context['user']

    print('User - Management My Rented', end='\n\n')
    print(f'Name: {user.name}')
    print('list of rented dvd')

    for i, dvd in enumerate(user.rented_dvd):
        print(f'{i+1}. {dvd}')

    while True:
        user_input = input('Please select the job you want. (c: check out, q: back): ')
        match user_input:
            case 'c':
                user_input = input('What dvd you want to check out: ')
                if int(user_input)-1 < len(user.rented_dvd):
                    dvd = context['dvd'].search(user.rented_dvd[int(user_input)-1])
                    if dvd is not None:
                        if user.check_out(dvd):
                            context['dvd'].update(dvd, copies=dvd.copies)
                            context['customer'].update(user, rented_dvd=user.rented_dvd_str)
                            print('Check out successfully!')
                        else:
                            print('Something is wrong.. you should call manager.')
                    else:
                        print('There is no DVD, probably it is db error.')
                else:
                    print('Wrong Input..\n\n')
            case 'q':
                return
            case _:
                print('Wrong Input..\n\n')
