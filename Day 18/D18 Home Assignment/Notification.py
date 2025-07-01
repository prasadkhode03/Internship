'''15.	Create an abstract class Notification:
o	Abstract method: send_message()
o	Subclasses:
	EmailNotification
	SMSNotification
	PushNotification'''
from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self, msg):
        self.msg = msg
    @abstractmethod
    def send_message(self):
        pass
class EmailNotification(Notification):
    def __init__(self, msg):
        super().__init__(msg)
    def send_message(self):
        print("Email Received : {msg}")
class SMSNotification(Notification):
    def __init__(self, msg):
        super().__init__(msg)
    def send_message(self):
        print("SMS Received : {msg}")
class PushNotification(Notification):
    def __init__(self, msg):
        super().__init__(msg)
    def send_message(self):
        print("Push Received : {msg}")

