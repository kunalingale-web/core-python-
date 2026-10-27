class ATM:

    def __init__(self, pin, balance, account_no, bank_name):
        self.__pin = pin
        self.__balance = balance
        self.__account_no = account_no
        self.__bank_name = bank_name

            #PIN(GET/SET)
    def get_pin(self):
        return self.__pin

    
    def set_pin(self, pin):
        self.__pin = pin


            #BALANCE(GET/SET)
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
            self.__balance = balance


            #ACCOUNT_NUMBER(GET/SET)
    def get_account_no(self):
        return self.__account_no

    def set_account_no(self, account_no):
        self.__account_no = account_no


           #BANK_NAME(GET/SET)
    def get_bank_name(self):
        return self.__bank_name

    def set_bank_name(self, bank_name):
        self.__bank_name = bank_name


a1 = ATM(1234, 50000, 123456, "SBI")



#DISPLAY
print("PIN:", a1.get_pin())
print("Balance:", a1.get_balance())
print("Account No:", a1.get_account_no())
print("Bank Name:", a1.get_bank_name())

#UPDATE
a1.set_pin(5678)
a1.set_balance(60000)


print("\nUpdated Details")
print("PIN:", a1.get_pin())
print("Balance:", a1.get_balance())