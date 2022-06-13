from ui.dialog.deco import dialog_box


@dialog_box(title='Who are you ?', menus=['Customer', 'Admin', 'Exit'])
def ask_user_type_menu():
    pass


@dialog_box(title='Admin Menu', menus=['Customer', 'DVD', 'Back', 'Exit'])
def admin_menu():
    pass


@dialog_box(title='Admin - Customer', menus=[f'{s} Customer' for s in ['Add', 'Search', 'Update']] + ['Back'])
def admin_customer_menu():
    pass


@dialog_box(title='Admin - DVD', menus=[f'{s} DVD' for s in ['Add', 'Search', 'Update', 'Remove']] + ['Back'])
def admin_dvd_menu():
    pass


@dialog_box(title='User Menu', menus=['Browse DVD', 'Management My Rented', 'Back', 'Exit'])
def user_menu():
    pass
