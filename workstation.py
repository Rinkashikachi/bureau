from link import Link
from message import Message


class WorkStation:
    def __init__(self, name):
        self.name = name
        self.ws_type = "WorkStation"
        self.links = []
        self.messages = []

    def print_data(self):
        print("name: " + self.name)
        print("ws_type: " + self.ws_type)

    def create_message(self, number, receiver, content):
        self.messages.append(Message(number, self, receiver, content))

    def show_message(self, number):
        print(self.messages[number].print_message())

#    def send_message(self, number):
#        self.messages[number]

    def attach_link(self, link):
        self.links.append(link)
        return self
