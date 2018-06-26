# Author: Andral Orelus

#CLASSED & OBJECTS


class Person:
    """docstring for ClassName"""
    __name = ''
    __email = ''

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)


andrizzy = Person()
andrizzy.set_name('Andral Orelus')
andrizzy.set_email('andrizzyworld@info.com')

print(andrizzy.get_name())
print(andrizzy.get_email())
print(andrizzy.toString())


# ANOTHER WAY OF DOING THE SAME THING.

# class Customer(Person):
#     __balance = 0

#     def __init__(self, name, email, balance):
#         self.__name = name
#         self.__email = email
#         self.__balance = balance
#         super(Customer, self).__init__(name, email)

#     def sef_balance(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def toString(self):
#         return '{} Has a balance of {} and can be contacted at {}'.format(self.__name, self.__email)

# andrizzy = Customer('EaseBreezy', 'easybreezy@gmail.com', 100)
# print(andrizzy.toString())
