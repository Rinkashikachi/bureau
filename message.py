class Message:
    def __init__(self, number, sender, receiver, content):
        self.number = number
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def print_message(self):
        print("Message number: " + self.number+";\nSender name: " +
              self.sender.name + ";\nReceiver name: " + self.receiver.name +
              ";\nMessage content: " + self.content + ".")
