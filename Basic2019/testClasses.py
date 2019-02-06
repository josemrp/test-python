from classes.UserManager import UserManager

manager = UserManager()

manager.add_user('Jhon')
manager.add_user('Kathy')
manager.add_user('Robert')

manager.print_messages()

manager.make_messages()

manager.print_messages()