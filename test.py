from controller import Controller


controller = Controller()
controller.create_workstations(2)
ws1 = controller.workstations[0]
ws2 = controller.workstations[1]
controller.create_lnk(ws1, ws2)
link1 = controller.links[0]
print("\n!!!!!-Controller info: ")
controller.print_info()
ws1.create_message("1", ws2, "сообщение")
ws1.create_message("2", ws2, "сообщение2")
ws1.create_message("3", ws2, "сообщение3")
print("\n!!!!!-WS1's messages:")
ws1.show_message("1")
print()
ws1.show_message("2")
print()
ws1.show_message("3")
ws1.send_message("2", link1)
print("\n!!!!!-WS1's messages after sending:")
ws1.show_message("1")
print()
ws1.show_message("2")
print()
ws1.show_message("3")
print("\n!!!!!-Message in 00 connection: ")
link1.show_message("2")
controller.check_links()
print("\n!!!!!-Message received by WS2: ")
ws2.messages_received[0].print_message()
