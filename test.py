from controller import Controller
from workstation import WorkStation
from link import Link

controller = Controller()
ws1 = WorkStation("1")
ws2 = WorkStation("2")
ws1.create_message("1", ws2, "сообщение")
ws1.create_message("2", ws2, "сообщение2")
ws1.create_message("3", ws2, "сообщение3")
ws1.show_message("1")
ws1.show_message("2")
ws1.show_message("3")
link1 = Link(controller, "00", ws1, ws2)
controller.print_info()
ws1.send_message("2", link1)
ws1.show_message("1")
ws1.show_message("2")
ws1.show_message("3")
link1.show_message("2")
controller.check_links()
ws2.messages_received[0].print_message()
