from workstation import WorkStation
from link import Link


class Controller:
    def __init__(self):
        print("---Controller is online---")
        self.workstations = []
        self.links = []

    def create_workstations(self, number=0):
        if number == 0:
            number = input("Number of WorkStations you want to create: ")
        for i in range(int(number)):
            self.workstations.append(WorkStation("WS"+str(i+1)))

    def create_link(self):
        first_node = input("Enter the first node: ")
        for node in self.workstations:
            if node.name == first_node:
                first_node = node
        second_node = input("Enter the second node: ")
        for node in self.workstations:
            if node.name == second_node:
                second_node = node
        self.links.append(Link(str(len(self.links)-1), first_node, second_node))

    def create_lnk(self, first_node, second_node):
        self.links.append(Link(str(len(self.links) - 1), first_node, second_node))

    def check_links(self):
        for link in self.links:
            if link.messages:
                """link.send_message(link.messages.pop())"""
                """link.messages.pop().print_message()"""
                link.send_message()

    def print_info(self):
        print("Number of Workstations: " + str(len(self.workstations)))
        print("Number of Links: " + str(len(self.links)))
