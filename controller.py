from workstation import WorkStation
from link import Link


class Controller:
    def __init__(self):
        print("---Controller is online---")
        self.workstations = []
        self.links = []

    def create_workstations(self, number=0):
        if number == 0:
            print("How many workstations do you want to create? ")
            number = input()
        for i in range(int(number)):
            self.workstations.append(WorkStation("WS"+str(i+1)))

    def create_link(self, name, first_node, second_node):
        self.links.append(Link(name, first_node, second_node))

    def check_links(self):
        for link in self.links:
            if link.messages:
                """link.send_message(link.messages.pop())"""
                """link.messages.pop().print_message()"""
                link.send_message()

    def print_info(self):
        print("Number of Workstations: " + str(len(self.workstations)))
        print("Number of Links: " + str(len(self.links)))
