import os


class macChanger:

    def __init__(self):
        pass

    @staticmethod
    def current():
        interface = raw_input("Enter the name of the interface: ")
        os.system("macchanger -s " + interface)

    @staticmethod
    def randomT():
        interface = raw_input("Enter the name of the interface: ")
        command = "ifconfig " + interface + " down ; macchanger -r " + interface + " ; ifconfig " + interface + " up"
        os.system(command)

    @staticmethod
    def reset():
        interface = raw_input("Enter the name of the interface: ")
        command = "ifconfig " + interface + " down ; macchanger -p " + interface + " ; ifconfig " + interface + " up"
        os.system(command)

    @staticmethod
    def listV():
        command = "macchanger -l | less"
        os.system(command)
        os.system('clear')
    @staticmethod
    def manual():
        interface = raw_input("Enter the name of the interface: ")
        mac = raw_input("Enter the mac address in this format[XX:XX:XX:XX:XX:XX]: ")
        command = "ifconfig " + interface + " down ; macchanger -m " + mac + " " + interface + " ; ifconfig " + interface + " up"
        os.system(command)


