import zipfile, os


def zipCrack():
    os.system('clear')
    filename = raw_input("Enter encrypted zip file name with extention: ")  # getting the Filename
    try:
        File = open(filename, 'r')  # reading the word list
    except IOError:
        print "Invalid zip file name\nExiting!!!....."
        return 0

    wordlist = raw_input("Enter word list of passwords file name with extention: ")  # getting the wordlist file
    zipFile = zipfile.ZipFile(filename)  # creating the zipfile object for the entered file

    try:
        passFile = open(wordlist, 'r')  # reading the word list
    except IOError:
        print "Invalid word list file name\nExiting!!!....."
        return 0
        # sys.exit()

    flag = 0

    for passw in passFile:
        pw = passw.strip('\n')
        print "Trying Password: ", pw

        try:
            zipFile.extractall(pwd=pw)  # Tring passowrds one by one
            print "Hurray password cracked successfully. Enjoy!"
            print "Correct password is: ", pw
            flag = 1
            break
        except:
            print "Incorrect password!\ngoing for next Password......"
            continue
    if flag == 0:
        print "Unable to crack the password try different wordlist.Thank You!!"

    else:
        temp = raw_input("\n\npress a key to exit zip cracker: ")
        os.system('clear')

# passFile = open('password.txt','r')
# for passw in passFile:
#     print passw.strip('\n')

