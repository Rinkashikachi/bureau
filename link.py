class Link:
    def __init__(self, controller, name, first_node, second_node):
        self.messages = []
        self.name = name
        self.first_node = first_node.attach_link(self)
        self.second_node = second_node.attach_link(self)
        controller.link_creation(self)

    def node(self, asking):
        if self.first_node == asking:
            return self.first_node
        else:
            return self.second_node

    def print_data(self):
        print("---")
        print("link name: " + self.name)
        print("Узлы:")
        print("1ый узел:")
        self.first_node.print_data()
        print("2ой узел:")
        self.second_node.print_data()
        print("---")

    def show_message(self, number):
        for i in range(len(self.messages)):
            if self.messages[i].number == number:
                self.messages[i].print_message()
                break

    def send_message(self):
        print(len(self.messages))
        self.messages.pop()
        print(len(self.messages))
        """print("Апельсин")"""
