from workstation import WorkStation

"""
de1 = DataExchanger("DE1")
de2 = DataExchanger("DE2")
lnk_12 = Link("1-2", de1, de2)
de1.create_message("00", de2, "сообщение")
"""
ws1 = WorkStation("1")
ws2 = WorkStation("2")
ws1.create_message("1", ws2, "сообщение")
ws1.show_message(0)