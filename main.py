import time
from os import system

def encoder(string):
    string = string.replace('1', '#')
    string = string.replace('2', '>')
    string = string.replace('3', '+')
    string = string.replace('4', '%')
    string = string.replace('5', '&')
    string = string.replace('6', '(')
    string = string.replace('7', ')')
    string = string.replace('8', '=')
    string = string.replace('9', '?')
    string = string.replace('0', '_')
    string = string.replace(' ', '/!$')
    string = string.replace('a', '148')
    string = string.replace('b', '432')
    string = string.replace('c', '543')
    string = string.replace('d', '305')
    string = string.replace('e', '320')
    string = string.replace('f', '209')
    string = string.replace('g', '846')
    string = string.replace('h', '327')
    string = string.replace('i', '749')
    string = string.replace('j', '103')
    string = string.replace('k', '021')
    string = string.replace('l', '492')
    string = string.replace('m', '108')
    string = string.replace('n', '438')
    string = string.replace('o', '079')
    string = string.replace('p', '010')
    string = string.replace('q', '194')
    string = string.replace('r', '324')
    string = string.replace('s', '777')
    string = string.replace('t', '818')
    string = string.replace('u', '887')
    string = string.replace('v', '865')
    string = string.replace('w', '945')
    string = string.replace('x', '906')
    string = string.replace('y', '919')
    string = string.replace('z', '935')
    return string

def decoder(string):
    string = string.replace('#', '1')
    string = string.replace('>', '2')
    string = string.replace('+', '3')
    string = string.replace('%', '4')
    string = string.replace('&', '5')
    string = string.replace('(', '6')
    string = string.replace(')', '7')
    string = string.replace('=', '8')
    string = string.replace('?', '9')
    string = string.replace('_', '0')
    string = string.replace('/!$', ' ')
    string = string.replace('148', 'a')
    string = string.replace('432', 'b')
    string = string.replace('543', 'c')
    string = string.replace('305', 'd')
    string = string.replace('320', 'e')
    string = string.replace('209', 'f')
    string = string.replace('846', 'g')
    string = string.replace('327', 'h')
    string = string.replace('749', 'i')
    string = string.replace('103', 'j')
    string = string.replace('021', 'k')
    string = string.replace('492', 'l')
    string = string.replace('108', 'm')
    string = string.replace('438', 'n')
    string = string.replace('079', 'o')
    string = string.replace('010', 'p')
    string = string.replace('194', 'q')
    string = string.replace('324', 'r')
    string = string.replace('777', 's')
    string = string.replace('818', 't')
    string = string.replace('887', 'u')
    string = string.replace('865', 'v')
    string = string.replace('945', 'w')
    string = string.replace('906', 'x')
    string = string.replace('919', 'y')
    string = string.replace('935', 'z')
    return string

while True:
    choice = input("---------------------------"
                   "\n|github.com/KontDragonSuat|"
                   "\n---------------------------"
                    "\n-----Encoder & Decoder-----"
                    "\n1- Encoding\n2- Decoding\n3- Exit"
                    "\nYapmak istediğiniz işlemi seçin: ")
    time.sleep(1.5)
    system('cls||clear')
    if choice=="1":
        encod= input("\nŞifrelemek istediğiniz metni girin: ")
        cikti = encoder(encod)
        time.sleep(1.5)
        print(cikti + "\n")
    elif choice=="2":
        decode= input("\nÇözülmesini istediğiniz metni girin: ")
        cikti = decoder(decode)
        time.sleep(1.5)
        print(cikti + "\n")
    elif choice=="3":
        print("\nÇıkılıyor...")
        break
    else:
        print("Yanlış tuşlama!")
        time.sleep(1.5)
