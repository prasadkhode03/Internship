'''🏢 Part F: Realistic Challenges
12.	Online Shopping System:
o	Abstract class: User
	Abstract method: get_user_type()
o	Subclasses:
	Customer returns Customer for user type.
	Admin returns Admin for user type.
o	Encapsulate user_id and user_email as private.'''
from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, user_id, user_email):
        self.__user_id = user_id
        self.__user_email = user_email

    @abstractmethod
    def get_user_type(self):
        pass
    
    def get_user_id(self):
        return self.__user_id

    def get_user_email(self):
        return self.__user_email

class Customer(User):
    def __init__(self, user_id, user_email):
        super().__init__(user_id, user_email)

    def get_user_type(self):
        return "Customer"

class Admin(User):
    def __init__(self, user_id, user_email):
        super().__init__(user_id, user_email)

    def get_user_type(self):
        return "Admin"

customer = Customer(1, "adityanigale12@gmail.com")
print(f"User ID: {customer.get_user_id()}")
print(f"User Email: {customer.get_user_email()}")
print(f"User Type: {customer.get_user_type()}")

admin = Admin(2, "rutviktidke33@gmail.com")
print(f"User ID: {admin.get_user_id()}")
print(f"User Email: {admin.get_user_email()}")
print(f"User Type: {admin.get_user_type()}")
