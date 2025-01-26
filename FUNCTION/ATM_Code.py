class atm:
    def __init__(self):
        self.pin=''
        self.amount=0
        self.menu()
    def menu(self):
        user_input=input('''
how can i help you
                         1.press 1 for create pin
                         2.press 2 to change pin
                         3.press 3 to cheak balance
                         4.press 4 to withdraw
                         5.press anything exit''' )

obj=atm()