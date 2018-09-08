#!/usr/bin/env python
# Simple hashing data
# Made with love by wahyuief

import hashlib, os

rechoice = ''
while rechoice != 'n':
    print("1. Md5")
    print("2. Sha1")
    print("3. Sha224")
    print("4. Sha256")
    print("5. Sha384")
    print("6. Sha512")
    choice = int(input("Choice: "))
    
    if choice == 1:
        string = raw_input("\nYour string: ")
        print "~> " + hashlib.md5(string).hexdigest()

    elif choice == 2:
        string = raw_input("\nYour string: ")
        print "~> " + hashlib.sha1(string).hexdigest()

    elif choice == 3:
        string = raw_input("\nYour string: ")
        print "~> " + hashlib.sha224(string).hexdigest()

    elif choice == 4:
        string = raw_input("\nYour string: ")
        print "~> " + hashlib.sha256(string).hexdigest()

    elif choice == 5:
        string = raw_input("\nYour string: ")
        print "~> " + hashlib.sha384(string).hexdigest()

    elif choice == 6:
        string = raw_input("\nYour string: ")
        print "~> " + hashlib.sha512(string).hexdigest()

    else:
        break

    rechoice = raw_input("\nRechoice? (y/n) ")
    os.system('clear')
