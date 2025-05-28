# Q4___ Class Variables and Class Methods                                               Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Meezan Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print("Bank name is change: ",name)
    

b1 = Bank()
print(b1.bank_name)
b1.change_bank_name("Alide Bank")
print(b1.bank_name)
