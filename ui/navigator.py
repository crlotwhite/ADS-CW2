from ui.dialog.common import *
from .dialog.customer import *
from .dialog.dvd import *


def route_main(context):
    while True:
        match ask_user_type_menu():
            case '1':
                if user_get_user_name(context):
                    route_user(context)
                else:
                    pass
            case '2':
                route_admin(context)
            case '3':
                route_exit()
            case _:
                print('Wrong Input..\n\n')


def route_admin(context):
    while True:
        match admin_menu():
            case '1':
                route_admin_customer(context)
            case '2':
                route_admin_dvd(context)
            case '3':
                return
            case '4':
                route_exit()
            case _:
                print('Wrong Input..\n\n')


def route_user(context):
    while True:
        match user_menu():
            case '1':
                user_dvd_browse_menu(context)
            case '2':
                user_management_my_rented_menu(context)
            case '3':
                return
            case '4':
                route_exit()
            case _:
                print('Wrong Input..\n\n')


def route_admin_customer(context):
    while True:
        match admin_customer_menu():
            case '1':
                admin_customer_add_menu(context)
            case '2':
                admin_customer_search_menu(context)
            case '3':
                admin_customer_update_menu(context)
            case '4':
                return
            case _:
                print('Wrong Input..\n\n')


def route_admin_dvd(context):
    while True:
        match admin_dvd_menu():
            case '1':
                admin_dvd_add_menu(context)
            case '2':
                admin_dvd_search_menu(context)
            case '3':
                admin_dvd_update_menu(context)
            case '4':
                admin_dvd_remove_menu(context)
            case '5':
                return
            case _:
                print('Wrong Input..\n\n')


def route_exit():
    from sys import exit
    print('Good Bye')
    exit()
