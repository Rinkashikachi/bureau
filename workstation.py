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
        for i in self.messages:
            if i.number == number:
                i.print_message()
                break

    def send_message(self, number, link):
        length = len(self.messages)
        for i in range(length):
            if self.messages[i].number == number:
                link.messages.append(self.messages[i])
                del self.messages[i]
                break

    def attach_link(self, link):
        self.links.append(link)
        return self
