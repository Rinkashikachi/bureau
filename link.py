class Link:
    def __init__(self, name, first_node, second_node):
        self.name = name
        self.first_node = first_node
        self.second_node = second_node

    def print_data(self):
        print("---")
        print("link name: " + self.name)
        print("Узлы:")
        print("1ый узел:")
        self.first_node.print_data()
        print("2ой узел:")
        self.second_node.print_data()
        print("---")
