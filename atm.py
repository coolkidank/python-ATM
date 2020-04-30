class Atm():
    users = {'1601': {'Name': 'anchal', 'Account': 6665554365, 'Mobile': 9123456780, 'Balance': 660000},
             '1105': {'Name': 'shrtuika', 'Account': 5645687609, 'Mobile': 9673536564, 'Balance': 900900},
             '2730': {'Name': 'Parishi', 'Account': 4532156789, 'Mobile': 9678573456, 'Balance': 400000},
             '3215': {'Name': 'honey', 'Account': 1235436789, 'Mobile': 9223367894, 'Balance': 700000},
             '9557': {'Name': 'sakshi', 'Account': 8769564367, 'Mobile': 9001829457, 'Balance': 143000}}

    def information(self, pin):
        print('Name:', self.users[pin]['Name'])
        print('Account:', self.users[pin]['Account'])
        print('Mobile:', self.users[pin]['Mobile'])
        print('Current Balance:', self.users[pin]['Balance'])

    def pinchange(self, pin):
        newpin = input("Enter New PIN")
        self.users[newpin] = self.users[pin]
        new2pin = input("Enter New Pin again")
        self.users[newpin] = self.users[pin]
        if newpin == new2pin:
            print("PIN changed Successfully")
        else:
            print("pin match invalid ... please type correctly")
            del self.users[pin]
        return newpin

    def balance(self, pin):
        print("Your current balance in account is", self.users[pin]['Balance'])
        print("press 0 to quit")
        back = input()
        if back == 0:
            return exit


    def withdrawal(self, pin):
        amount = float(input("Enter the amount you wish to withdraw: "))
        balance = float(self.users[pin]['Balance'])
        if (balance - amount) < 0:
            print("Your current balance is low to proceed with the transaction,Please check your account balance.")
        else:
            print("Please Wait for Cash and remove your card.....")
        print("Please press 0 to display your current balance")
        current_balance = input()
        if current_balance == "0":
            print("your current balance now is",balance-amount)
        else:
            return exit


    def deposit(self):
        print("Please enter the cash and press Enter")
        input()

    def pin_validation(self, pin):
        validated = False
        if pin in self.users.keys():
            validated = True
        return validated


if __name__ == '__main__':
    while True:
        count = 0
        i = 3
        pin = input("Enter your PIN: ")
        user = Atm()
        validate = user.pin_validation(pin)
        if validate:
            try:
                op = input(''' 
    Press a number according to your operation required:
    	1.Account Information.
    	2.PIN Change
    	3.Balance Inquiry
    	4.Withdrawal
    	5.Deposit
    	6.Exit
    Your Option: ''')
                if op == '1':
                    user.information(pin)
                elif op == '2':
                    pin = user.pinchange(pin)
                elif op == '3':
                    user.balance(pin)
                elif op == '4':
                    user.withdrawal(pin)
                elif op == '5':
                    user.deposit()
                elif op == '6':
                    break
                else:
                    print("Wrong input,please select valid option")
            except Exception as e:
                print("Account Error:", e)
        else:
            count += 1
            if count == 3:
                print("WARNING! Account has been blocked")
            else:
                print("Wrong pin entered, Attempts remaining {}".format(i - count))