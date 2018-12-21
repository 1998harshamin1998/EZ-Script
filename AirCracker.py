import subprocess
import os
import time


class AirCracker:
    procc = None

    def __init__(self, file):
        self.file = file

    def dictionary(self):
        while True:
            try:
                wordList = raw_input("Enter the name of your wordlist file: ")
                file = open(wordList, 'r')
                file.close()
                break
            except:
                print "Invalid word list file name."

        # aircrack-ng -w wordlist -b bsssid filename.cap
        temp = os.getcwd() + "/"
        wordList = temp + wordList
        print wordList
        time.sleep(1)
        print self.file
        time.sleep(5)
        tmp = "aircrack-ng " + self.file + " -w " + wordList
        print tmp
        AirCracker.procc = subprocess.Popen(tmp, shell=True)
        print "Actual Done\n\n"

    def bruteForce(self):
        bssid = raw_input("Enter bssid: ")
        minl = raw_input("Enter minimum length: ")
        maxl = raw_input("Enter maximum length: ")
        command = "crunch " + minl + " " + maxl + " "

        print '''
                \n\n
                NOTE:  

                The order MUST BE:
                    lower case characters
                    upper case characters
                    numbers
                    and then symbols.  
                If you don't follow this order you will not get the results you want.  You MUST specify  either  values  for
                the character type or a plus sign.  NOTE: If you want to include the space character in your character set you
                must escape it using the \\ character or enclose your character set in quotes i.e. "abc ".

        '''
        charset = raw_input("\nEnter the charset as per the given instructions[optional]: ")
        if len(charset) > 0:
            command += charset + " "
        print '''\n\n 
                NOTE: 
                @,%^
                Specifies a pattern, eg: @@god@@@@ where the only the @'s, ,'s, %'s, and ^'s will change.
                @ will insert lower case characters
                , will insert upper case characters
                % will insert numbers
                ^ will insert symbols
            '''
        pattern = raw_input("\n\nEnter your pattern as per the given instructions[optional]: ")

        if len(pattern) > 0:
            command += "-t " + pattern + " "

        command += "| aircrack-ng -b " + bssid + " -w- " + self.file
        print command
        print self.file
        time.sleep(1)
        AirCracker.procc = subprocess.Popen(command, shell=True)





