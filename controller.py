class Controller:
    def __init__(self):
        print("---Controller is online---")
        self.links = []

    def link_creation(self, link):
        self.links.append(link)

    def check_links(self):
        for link in self.links:
            if link.messages:
                """link.send_message(link.messages.pop())"""
                link.messages.pop().print_message()

    def print_info(self):
        print("Количество связей: " + str(len(self.links)))
