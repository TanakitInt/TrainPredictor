#-------------------------------------------------------------------------------
#Copyright (c) 2017. All rights reserved.
#Do not distribute without permission.
#
#For business inquires please contact :
#Tanakit.Int@hotmail.com
#
#-------------------------------------------------------------------------------
#Purpose :
#Predict a train arrival time when arrive at the input station
#
#Development Tools :
#Python 3, Visual Studio Code and Sublime text editor 3.
#
#Components:
#Advanced Installer 14. FREE VERSION.
#Download : https://www.advancedinstaller.com/
#
#Input Specification :
#1. Lastest input time or Lastest time of train departed from start
#   at the input station
#
#Output Specification :
#1. Predicted train arrival time at the input station
#2. Train status (Ticket)
#
#-------------------------------------------------------------------------------
#Program Introduction

print(
"""
Welcome to train arrival prediction tool!
Developed by :
TanakitInt.

Current version :
Stable 1.0.0 (Public Release version)

If you wish to see a real Fare Table or User Manual, please go to program's 
installation folder (Right click and select "Open file location")

For business inquires please contact :
Tanakit.Int@hotmail.com

Please input your command :
"start"         start the program
"copyright"     show the copyright
"version"       show the current version
"information"   show the program information
"contact"       show the developer's contact
"changelog"     show the program change log
"help"          show the available command
"exit"          exit the program
"""
)

#import module

#import sys
import os
#import math

from tkinter import *

def contact():
    """Show contact UI"""

    #def meassage(root):
        #textOut = Label(root, text = "Button OK!").pack()
    try:
        def ui():
            """Contact UI"""
            # initialize window

            root = Tk()
            root.title("Contact")
            root.iconbitmap('icon_train.ico')

            #initialize the window size
            root.geometry('{}x{}'.format(720, 360))

            #define maxinum and minimum size of window
            root.maxsize(width = 1920, height = 1080)
            root.minsize(width = 480, height = 240)

            #fixed window size (currently not fixed)
            root.resizable(width = True, height = True)

            #topFrame
            topFrame = Frame(root, height = 100)
            topFrame.pack()

            #Label
            textHeader = """

        Train arrival 
        prediction
        """
            container = """
        TanakitInt.

        Year 1. 2017.
        Faculty of Information Techonology.

        For business inquires please contact :
        Tanakit.Int@hotmail.com

        Copyright (c) 2017. All rights reserved.
        Free for educational use only.
        """

            Label(topFrame,
                text = textHeader,
                fg = '#FFFFFF', #white
                bg = '#FF9800', #Orange
                font = "Verdana 12 bold",
                justify = "left"
                ).pack(side = "left")

            Label(topFrame,
                text = container,
                fg = '#000000', #black
                font = "Verdana 8",
                justify = "left"
                ).pack(side = "left")

            #define image path
            logo = PhotoImage(file = "it.gif")
            Label(topFrame, 
                image = logo,
                justify = "right"
                ).pack(side = "right")

            #middleFrme
            middleFrame = Frame(root, 
                height = 20)
            middleFrame.pack()

            #define button
            #hello_button = Button(root, 
            #    text = "Click Me!", 
            #    command = lambda: meassage(root))
            #hello_button.pack()

            #bottom frame
            bottomFrame = Frame(root, 
                height = 20)
            bottomFrame.pack(side = "right")

            root.mainloop()

        ui()

    except Exception as e:
        #All error start for contact! Especially for user modify or remove a file.
        print(
    """
    An error ocurred when starting a start screen.
    Please reinstall the program and then try again.

    If you believe this is a bug, contact us immediately.
    (See ReadMe.txt)
    """
        )
        
        print("Error information :")
        print(e)
        print("")
        print("Press enter to quit..." '\n')

        userExit = input()

        quit()

contact()

#File validation check
def check():
    """File validation check"""

    count = 0
    try:
        #file Version.txt
        filename = open('Resource\Version', 'r')
        filename.close()
        count = count + 1

        #file Changelog.txt
        filename = open('Changelog.txt', 'r')
        filename.close()
        count = count + 1

        #file Website.txt
        filename = open('Resource\Website', 'r')
        filename.close()
        count = count + 1

        #file ReadMe.txt
        filename = open('ReadMe.txt', 'r')
        filename.close()
        count = count + 1

        #file Information.txt
        filename = open('Resource\Information', 'r')
        filename.close()
        count = count + 1

        #file serial.txt
        filename = open('serial.txt', 'r')
        filename.close()
        count = count + 1

        #file Ticket.txt
        filename = open('Ticket.txt', 'r')
        filename.close()
        count = count + 1

    except Exception as e:
        #For all exception
        print(
    """
    An error ocurred when starting a start screen.
    Please reinstall the program and then try again.

    If you believe this is a bug, contact us immediately.
    (See ReadMe.txt)
    """
        )
        print("Error information :")
        print(e)
        print("")
        print("Press enter to quit..." '\n')

        userExit = input()

        quit()

    else:
        #No error return to main(): function
        print("File validation completed with " + str(count) + " pass(es).")
        main()


#For program main function
def main():
    """program header for enter a command"""

    #try-except is for file name error, not found or invalid directory.
    try:
        while True:
            input_ = input("Input command : ")

            if input_ == "copyright":
                
                print("")
                filename = open('Resource\Copyright', 'r')
                print(filename.read())
                filename.close()
                print("")
                
            elif input_ == "version":

                print("")
                filename = open('Resource\Version', 'r')
                print(filename.read())
                filename.close()
                print("")

            elif input_ == "information":

                print("")
                filename = open('Resource\Information', 'r')
                print(filename.read())
                filename.close()
                print("")

            elif input_ == "contact":
                
                    #contact UI
                    contact()

    #            print(
    #    """
    #    For business inquires please contact :
    #    Tanakit.Int@hotmail.com
    #    """
    #                )

            elif input_ == "changelog":
                
                print("")
                filename = open('Changelog.txt', 'r')
                print(filename.read())
                filename.close()
                print("")

            elif input_ == "help":

                print("")
                filename = open('Resource\Help', 'r')
                print(filename.read())
                filename.close()
                print("")

                #given to a menu function
            elif input_ == "start":
                menu()

                #for completely exit the program
            elif input_ == "exit":
                quit()

            else:
                print(
    """
    Command error!
    """
                )

    except Exception as e:
        #FileExistsError, FileNotFoundError
        print(
    """
    File ERROR! Please check your program's directory then,
    check the file name and try again.

    Please note that removing or renaming a file might cause an error.
    """
        )

        print("Error information :")
        print(e)
        print("")
        print("Press enter to quit..." '\n')

        userExit = input()

        quit()

#Reset a variable when user return to menu
#
#trConstantEast = []
#trainNumber = ""
#m = 0
#n = 0
#stationColectorStart = ""
#stationColectorStop = ""

def menu():
    """main menu ***NOT main(): function***"""
    print(
"""
Menu :
(1) Select train line
(2) Related website
(3) See the user manual
(9) Go back 
To enter a command or exit the program please go back (9).
"""
    )
    while True:
        input_ = input("Input menu number : ")
        if input_ == "1":
            line()

        elif input_ == "2":
            print("")
            filename = open('Resource\Website', 'r')
            print(filename.read())
            filename.close()
            print("")

        elif input_ == "3":
            os.startfile("User Manual.pdf")

        elif input_ == "9":
            return main()
                
        #elif input_ == "0":
        #    quit()

        else:
            print(
    """
    Please input a valid number.
    """
            )

#selected train line
def line():
    """select a train line"""
    print(
"""
Select train line :
(1) Eastern line
(2) Airport Rail link
(9) Go back
"""
    )
    while True:
        input_ = input("Input line number : ")
        if input_ == "1":
            east()

        elif input_ == "2":
            #return airlink()
            print("Coming soon!")

        elif input_ == "9":
            menu()

        else:
            print(
    """
    Please input a valid number.
    """
            )

#for eastern line
def east():
    """for eastern line"""
    print(
"""
Bangkok                                                          To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 
Station :
1  - Bangkok
2  - Urupong
3  - PhayaThai
4  - Makkasan
5  - Asok
6  - KlongTan
7  - Sukumwit 71
8  - HuaMak
9  - BanThapChang
10 - Soi WatLanBoon
11 - LadKrabang
12 - PraChomKlao
13 - HuaTakae

Select option :
(1) Select train number (See (2) first!)
(2) See the original time table and train number
(9) Go back
"""
        )
    while True:
        input_ = input("Input option : ")
        if input_ == "1":

            while True:            
                inputTrain = input("Input train number (1-32): ")

                if inputTrain == '':    
                    print(
    """
    Please input a valid train number.
    """
                    )

                else:
                    #From Bangkok to Huatakae
                    if inputTrain == "1":
                        _379()
                    
                    elif inputTrain == "2":
                        _275()
                        
                    elif inputTrain == "3":
                        print("From Rangsit, Not available!")
                    
                    elif inputTrain == "4":
                        _283()
                    
                    elif inputTrain == "5":
                        _281()

                    elif inputTrain == "6":
                        _367()
                    
                    elif inputTrain == "7":
                        _389()
                        
                    elif inputTrain == "8":
                        _279()
                        
                    elif inputTrain == "9":
                        _277()
                    
                    elif inputTrain == "10":
                        _391()
                        
                    elif inputTrain == "11":
                        _371()
                        
                    elif inputTrain == "12":
                        _383()

                    #From Huatakae to Bangkok
                    elif inputTrain == "21":
                        #_380()
                        print("Coming soon!")
                        
                    elif inputTrain == "22":
                        #_384()
                        print("Coming soon!")
                       
                    elif inputTrain == "23":
                        #_372()
                        print("Coming soon!")
                        
                    elif inputTrain == "24":
                        #_388()
                        print("Coming soon!")
                        
                    elif inputTrain == "25":
                        #_378()
                        print("Coming soon!")
                        
                    elif inputTrain == "26":
                        #_278()
                        print("Coming soon!")
                        
                    elif inputTrain == "27":
                        #_280()
                        print("Coming soon!")
                        
                    elif inputTrain == "28":
                        #_368()
                        print("Coming soon!")
                        
                    elif inputTrain == "29":
                        #_390()
                        print("Coming soon!")
                        
                    elif inputTrain == "30":
                        #_282()
                        print("Coming soon!")
                        
                    elif inputTrain == "31":
                        #_284()
                        print("Coming soon!")
                        
                    elif inputTrain == "32":
                        #_276()
                        print("Coming soon!")
                        
                    else:
                        print(
    """
    Please input a valid train number.
    """
                        )

        elif input_ == "2":
            print("")
            filename = open('Timetable\EasternLine', 'r')
            print(filename.read())
            filename.close()
            print("")

        elif input_ == "9":
            line()

        else:
            print(
    """
    Please input a valid number.
    """
            )


def _379():
    """for Eastern line train No.379"""
    print(
        """                                                           
Bangkok 379                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     N     N     Y     N     N     N     N     N     N      N      N      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  5, 0,   5, 0,   4, 2,   3, 0,   5, 0,   5, 0,   5, 0,   
                       9, 0,    4,  0,     4,  0,     4,  0,     2]
    trainNumber = "379"
    serialKey = "E1"
    departTime = "4.15"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _275():
    """for Eastern line train No.275"""
    print(
        """                                                           
Bangkok 275                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     N     Y     Y     Y     Y     N     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  5, 0,   9, 1,   9, 1,   5, 1,   7, 1,   4, 0,   4, 1,   
                       4, 1,    3,  1,     2,  1,     4,  1,     1]
    trainNumber = "275"
    serialKey = "E1"
    departTime = "5.55"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _283():
    """for Eastern line train No.283"""
    print(
        """                                                           
Bangkok 283                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     N     Y     Y     Y     Y     Y     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  5, 0,   7, 1,   7, 1,   5, 1,   9, 9,   2, 1,   6, 1,   
                       7, 1,    3,  1,     3,  1,     3,  1,     3]
    trainNumber = "283"
    serialKey = "E1"
    departTime = "6.55"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _281():
    """for Eastern line train No.281"""
    print(
        """                                                           
Bangkok 281                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     N     Y     Y     Y     Y     N     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...]
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8,
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]
    trConstantEast = [5, 0,   5, 1,   4, 1,   3, 1,   5, 1,   4, 0,   4, 1,
                       8, 1,    3,  1,     2,  1,     3,  1,     1]
    trainNumber = "281"
    serialKey = "E1"
    departTime = "8.00"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)

        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _367():
    """for Eastern line train No.367"""
    print(
        """                                                           
Bangkok 367                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     Y     Y     Y     Y     Y     Y     Y     Y     N      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  9, 1,   2, 1,   5, 2,   3, 1,   5, 1,   2, 1,   5, 1,   
                       5, 1,    2,  0,     4,  1,     4,  1,     1]
    trainNumber = "367"
    serialKey = "E1"
    departTime = "10.10"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _389():
    """for Eastern line train No.389"""
    print(
        """                                                           
Bangkok 389                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     N     Y     Y     Y     Y     N     Y     Y     N      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  5, 0,   4, 1,   6, 2,   3, 1,   3, 1,   2, 0,   5, 1,   
                       4, 1,    2,  0,     5,  1,     3,  1,     1]
    trainNumber = "389"
    serialKey = "E1"
    departTime = "12.10"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _279():
    """for Eastern line train No.279"""
    print(
        """                                                           
Bangkok 279                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     N     Y     Y     Y     Y     N     Y     Y     N      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  3, 0,   4, 1,   3, 1,   2, 1,   3, 1,   2, 0,   3, 1,   
                       5, 1,    3,  0,     2,  1,     3,  1,     1]
    trainNumber = "279"
    serialKey = "E1"
    departTime = "13.05"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _277():
    """for Eastern line train No.277"""
    print(
        """                                                           
Bangkok 277                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     Y     Y     Y     Y     Y     Y     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [ 12, 1,   2, 1,   3, 1,   2, 1,   2, 1,   1, 1,   4, 1,   
                       5, 1,    2,  1,     3,  1,     3,  1,     1]
    trainNumber = "277"
    serialKey = "E1"
    departTime = "15.25"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _391():
    """for Eastern line train No.391"""
    print(
        """                                                           
Bangkok 391                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     Y     Y     Y     Y     Y     Y     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
        )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  8, 1,   2, 1,   4, 2,   3, 1,   3, 1,   2, 1,   5, 1,   
                       5, 1,    3,  1,     4,  1,     3,  1,     2]
    trainNumber = "391"
    serialKey = "E1"
    departTime = "16.55"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _371():
    """for Eastern line train No.371"""
    print(
        """                                                           
Bangkok 371                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     Y     Y     Y     Y     Y     Y     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  8, 1,   3, 1,   5, 4,   3, 1,   4, 1,   1, 1,   4, 1,   
                       5, 1,    4,  1,     4,  1,     4,  1,     2]
    trainNumber = "371"
    serialKey = "E1"
    departTime = "17.40"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")

def _383():
    """for Eastern line train No.383"""
    print(
        """                                                           
Bangkok 383                                                      To Chachoengsao
|1-----2-----3-----4-----5-----6-----7-----8-----9-----10-----11-----12-----13->
 Y     Y     Y     Y     Y     Y     Y     Y     Y     Y      Y      Y      Y
                                ------Direction----->
Y = Yes, train stop.
N = No, train skip.
        """
    )
    print(
    """
Select option :
(1) Predict arrive time
(9) Go back
    """
    )

    #train constant will be here
    #minite(s) of each station
    #form = [station, stop, station, stop...] 
    #for eastern line
    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]   
    trConstantEast = [  8, 1,   2, 1,   4, 2,   3, 1,   4, 1,   3, 1,   5, 1,   
                       6, 1,    3,  1,     3,  1,     4,  1,     1]
    trainNumber = "383"
    serialKey = "E1"
    departTime = "18.25"

    input_ = input("Input option : ")
    while True:
        if input_ == "1":
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
        elif input_ == "9":
            return east()

        else:
            print(
    """
    Please input a valid number.
    """
            )
            input_ = input("Input option : ")


def predictEast(trConstantEast, trainNumber, serialKey, departTime):
    """For eastren line station selection"""

    #trConstantEast= [1-2, 2, 2-3, 3, 3-4, 4, 4-5, 5, 5-6, 6, 6-7, 7, 7-8, 8, 
    #                8-9, 9, 9-10, 10, 10-11, 11, 11-12, 12, 12-13]
    #
    #Start                          Bangkok
    #trConstantEast[0]  is 1  >>> 2
    #trConstantEast[1]  is 2        Urupong
    #trConstantEast[2]  is 2  >>> 3
    #trConstantEast[3]  is 3        PhayaThai
    #trConstantEast[4]  is 3  >>> 4
    #trConstantEast[5]  is 4        Makkasan
    #trConstantEast[6]  is 4  >>> 5
    #trConstantEast[7]  is 5        Asok
    #trConstantEast[8]  is 5  >>> 6
    #trConstantEast[9]  is 6        KlongTan
    #trConstantEast[10] is 6  >>> 7
    #trConstantEast[11] is 7        Sukumwit 71
    #trConstantEast[12] is 7  >>> 8
    #trConstantEast[13] is 8        HuaMak
    #trConstantEast[14] is 8  >>> 9
    #trConstantEast[15] is 9        BanThapChang
    #trConstantEast[16] is 9  >>> 10
    #trConstantEast[17] is 10       Soi WatLanBoon
    #trConstantEast[18] is 10 >>> 11
    #trConstantEast[19] is 11       LadKrabang
    #trConstantEast[20] is 11 >>> 12
    #trConstantEast[21] is 12       PraChomKlao
    #trConstantEast[22] is 12 >>> 13
    #Stop                           HuaTakae
    
    print(
    """
    Station number
    (1) - Bangkok
    (2) - Urupong
    (3) - PhayaThai
    (4) - Makkasan
    (5) - Asok
    (6) - KlongTan
    (7) - Sukumwit 71
    (8) - HuaMak
    (9) - BanThapChang
    (10)- Soi WatLanBoon
    (11)- LadKrabang
    (12)- PraChomKlao
    (13)- HuaTakae
    """
    )

    #for start station
    station = input("Please enter your current station number(1-13): " '\n')
    stationColectorStart = ""
    m = 0

    while True:
        #m is for start station
        if station == "1":
            print("You are at Bangkok.")
            m = 0
            stationColectorStart = "Bangkok"
            break
        elif station == "2":
            print("You are at Urupong.")
            m = 1
            stationColectorStart = "Urupong"
            break
        elif station == "3":
            print("You are at PhayaThai.")
            m = 3
            stationColectorStart = "PhayaThai"
            break
        elif station == "4":
            print("You are at Makkasan.")
            m = 5
            stationColectorStart = "Makkasan"
            break
        elif station == "5":
            print("You are at Asok.")
            m = 7
            stationColectorStart = "Asok"
            break
        elif station == "6":
            print("You are at KlongTan.")
            m = 9
            stationColectorStart = "KlongTan"
            break
        elif station == "7":
            print("You are at Sukumwit 71.")
            m = 11
            stationColectorStart = "Sukumwit 71"
            break
        elif station == "8":
            print("You are at HuaMak.")
            m = 13
            stationColectorStart = "HuaMak"
            break
        elif station == "9":
            print("You are at BanThapChang.")
            m = 15
            stationColectorStart = "BanThapChang"
            break
        elif station == "10":
            print("You are at Soi WatLanBoon.")
            m = 17
            stationColectorStart = "Soi WatLanBoon"
            break
        elif station == "11":
            print("You are at LadKrabang.")
            m = 19
            stationColectorStart = "LadKrabang"
            break
        elif station == "12":
            print("You are at PraChomKlao.")
            m = 21
            stationColectorStart = "PraChomKlao"
            break
        elif station == "13":
            print("You are at HuaTakae.")
            print("To Chachoengsao... >>>")
            m = 22
            stationColectorStart = "HuaTakae"
            break
            
        else:
            print(
    """
    Please input a valid number.
    """
            )
            #reset and return to input
            station = ""
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            break
        
    #for destination station
    stationStop = input("Please enter your destination station number(1-13): " '\n')
    stationColectorStop = ""
    n = 0

    while True:
        #n is for stop station
        if stationStop == "1":
            print("You are going to Bangkok.")
            n = 0
            stationColectorStop = "Bangkok"
            break
        elif stationStop == "2":
            print("You are going to Urupong.")
            n = 1
            stationColectorStop = "Urupong"
            break
        elif stationStop == "3":
            print("You are going to PhayaThai.")
            n = 3
            stationColectorStop = "PhayaThai"
            break
        elif stationStop == "4":
            print("You are going to Makkasan.")
            n = 5
            stationColectorStop = "Makkasan"
            break
        elif stationStop == "5":
            print("You are going to Asok.")
            n = 7
            stationColectorStop = "Asok"
            break
        elif stationStop == "6":
            print("You are going to KlongTan.")
            n = 9
            stationColectorStop = "KlongTan"
            break
        elif stationStop == "7":
            print("You are going to Sukumwit 71.")
            n = 11
            stationColectorStop = "Sukumwit 71"
            break  
        elif stationStop == "8":
            print("You are going to HuaMak.")
            n = 13
            stationColectorStop = "HuaMak"
            break  
        elif stationStop == "9":
            print("You are going to BanThapChang.")
            n = 15
            stationColectorStop = "BanThapChang"
            break
        elif stationStop == "10":
            print("You are going to Soi WatLanBoon.")
            n = 17
            stationColectorStop = "Soi WatLanBoon"
            break  
        elif stationStop == "11":
            print("You are going to LadKrabang.")
            n = 19
            stationColectorStop = "LadKrabang"
            break  
        elif stationStop == "12":
            print("You are going to PraChomKlao.")
            n = 21
            stationColectorStop = "PraChomKlao"
            break
        elif stationStop == "13":
            print("You are going to HuaTakae.")
            n = 22
            stationColectorStop = "HuaTakae"
            break

        else:
            print(
    """
    Please input a valid number.
    """
            )
            #reset and return to input
            station = ""
            predictEast(trConstantEast, trainNumber, serialKey, departTime)
            break

    #return to fucntion detector():
    detector(trConstantEast, trainNumber, serialKey, departTime,
             m, n, stationColectorStart, stationColectorStop)


def detector(trConstantEast, trainNumber, serialKey, departTime, 
    m, n, stationColectorStart, stationColectorStop):
    """detect a stop that train really stop? then print the ticket"""

    stopStatusFrom = "YES"
    stopStatusTo = "YES"

    #station verification
    if trConstantEast[m] == 0:
        stopStatusFrom = "NO"
        print("**Train doesn't stop at " + stationColectorStart)
    else:
        pass

    if trConstantEast[n] == 0:
        stopStatusTo = "NO"
        print("**Train doesn't stop at " + stationColectorStop)
    else:
        pass

    #total time spent on the train
    location = sum(trConstantEast[m:n:1])

    print(
    """
    For real time train status, please visit :
    http://tts.railway.co.th/srttts/view
    """
    )

    timeIn = input("Please enter the current depart time in this form HH.MM :" '\n')

    #time verification
    try:
        while True:
            if timeIn == '':
                #for no input or just enter away
                print(
        """
    Please input a valid time.
        """
                )
                #reset and return to input
                detector(trConstantEast, trainNumber, serialKey, departTime,
                         m, n, stationColectorStart, stationColectorStop)
            else:
                #for invalid time e.g. alphabet
                hourIn = timeIn[0]
                minuteIn = timeIn[1]
                if hourIn.isdigit() == True and minuteIn.isdigit() == True:
                    break
                else:
                    print(
        """
    Please input a valid time.
        """
                )
                    #reset and return to input
                    detector(trConstantEast, trainNumber, serialKey, departTime,
                             m, n, stationColectorStart, stationColectorStop)

    except:
        print(
        """
    Please input a valid time.
        """
        )
        #reset and return to input
        detector(trConstantEast, trainNumber, serialKey, departTime,
                 m, n, stationColectorStart, stationColectorStop)

    #time calculation-----------------------------------------------------------
    timeIn = timeIn.split(".")

    #check the length of list must be 2 only!
    if len(timeIn) != 2:
        print(
        """
    Please input a valid time.
        """
        )
        #reset and return to input
        detector(trConstantEast, trainNumber, serialKey, departTime,
                 m, n, stationColectorStart, stationColectorStop)
    else:
        pass

    hourIn = int(timeIn[0])
    minuteIn = int(timeIn[1])

    #for hour is more than 24 or minute is more than 59,
    #input them again.
    if hourIn >= 24 or hourIn < 0:
        print(
        """
    Please input a valid time.
        """
        )
        #reset and return to input
        detector(trConstantEast, trainNumber, serialKey, departTime,
                 m, n, stationColectorStart, stationColectorStop)
    else:
        pass

    if minuteIn >= 60 or minuteIn < 0:
        print(
        """
    Please input a valid time.
        """
        )
        #reset and return to input
        detector(trConstantEast, trainNumber, serialKey, departTime,
                 m, n, stationColectorStart, stationColectorStop)
    else:
        pass

    minuteFromHour = hourIn*60

    allMinute = minuteIn + minuteFromHour

    #new variable for delay computation
    delay = allMinute

    #minute calculation---------------------------------------------------------
    allMinute = allMinute + location

    clock = [allMinute//60 , allMinute%60]

    arriveHour = int(clock[0])
    arriveMinute = int(clock[1])

    #if hour is more than 24 after convertion or minute is more than 60 reset it to 0, 
    #then loop it again.
    nextDay = ""

    if arriveHour >= 24:
        arriveHour = arriveHour%24
        nextDay = " Next day. "
    else:
        pass
    
    if arriveMinute >= 60:
        arriveMinute = arriveMinute%60
    else:
        pass

    #Delay computation (Based-on user input)------------------------------------
    departTime = departTime.split(".")

    departHour = int(departTime[0])
    departMinute = int(departTime[1])

    minuteTimetable = (departHour*60) + departMinute

    minuteDelay = (delay - minuteTimetable) - sum(trConstantEast[0:m:1])

    #for early train and on-time train
    if minuteDelay < -1:                #delay offset early when early more than 1 minute
        minuteDelay = "0 (Early)"
    elif -1 <= minuteDelay <= 1:        #delay offset early when on-time(+-1 minute)
        minuteDelay = "0 (On-Time)"
    else:                               #delay is more than 1 minute
        pass

    minuteDelay = str(minuteDelay)
    
    #Delay computation (Real-life factor only)----------------------------------

    #location   <<< fixed time
    #timeIn     <<< real time
    #if trainNumber == "379" or trainNumber == "367" or trainNumber == "389":
        #HuaTakae-Chachoengsao Rapid
        #delay = "0"
    #elif trainNumber == "275" or trainNumber == "279":
        #Aranyaprathet
        #delay = "7"
    #elif trainNumber == "283" or trainNumber == "281":
        #Late Morning train
        #delay = "5"
    #elif trainNumber == "277" or trainNumber == "391" or trainNumber == "371" or trainNumber == "383":
        #Evening train
        #delay = "10"

    #Fare Computation-----------------------------------------------------------
    fare = 0
    if serialKey == "E1":
    #for eastren line from Bangkok to others.
    #see the fare table for futher information

        if abs(m - n) >= 22:            #more than 12 stations
            fare = 7
        elif 17 <= abs(m - n) < 22:     #9-11 stations
            fare = 6
        elif 15 <= abs(m - n) < 17:     #8 stations
            fare = 5
        elif 11 <= abs(m - n) < 15:     #6-7 stations
            fare = 3
        elif 0 <= abs(m - n) < 11:      #less than 6 stations
            fare = 2

    #elif serialKey == "E2":
    #for eastren line from others to Bangkok.
    #
    #futher...

    else:
        pass

    #Customer name--------------------------------------------------------------
    customerName = input("Please enter customer name : " '\n')
    
    #Current time---------------------------------------------------------------
    from datetime import datetime
    currentTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    #Ticket serial number-------------------------------------------------------
    #if you wish to reset serial number, please rename it in serial.txt to 0.

    #Ticket serial number format :
    #"2E1"
    #2 = Ticket sequence
    #E = Eastren line (Line alphabet)
    #
    #Last number :
    #if 1 = Go to others 
    #if 2 = Back to Bangkok
    
    try:
        with open("serial.txt") as f:
            i = f.read()
            if i.isdigit() == False or int(i) < 0:
                #force pass to error
                pass

            else:
                i = int(i)

        if i >= 0:
            i = i + 1
        
        with open("serial.txt", 'w') as f:
            f.write(str(i))
            
        f.close()

    except Exception as e:
        print(
        """
    Ticket serial number ERROR!, please see serial.txt in program's folder 
    and then try again.
        """
        )
        print("Error information :")
        print(e)
        print("")
        print("Press enter to quit..." '\n')

        userExit = input()

        quit()

    #-----Sample-----#
    #StackOverFlow :
    #https://stackoverflow.com/questions/7194665/read-in-file-change-contents-write-out-to-same-file
    #
    #with open(myfile) as f:
    #   file_str = f.read()
    #
    #do_actions_on_file_str
    #
    #with open(myfile, 'w') as f:
    #   f.write(file_str)

    #Export to the Ticket.txt--------------------------------------------------
    line1  = ""
    line2  = "************************************ Ticket ************************************"
    line3  = currentTime
    line4  = "Station master : #"
    line5  = "Ticket seller : #"
    line6  = ""
    line7  = "Ticket serial number : " + str(i) + serialKey
    line8  = "Customer name : " + customerName
    line9  = ""
    line10 = "Ticket printed at : "+stationColectorStart
    line11 = "Train number : " + trainNumber
    line12 = "Stop at " + stationColectorStart + "? : " + stopStatusFrom
    line13 = "Stop at " + stationColectorStop + "? : " + stopStatusTo
    line14 = "Expected delay = +" + str(minuteDelay) + " minute(s)"
    line15 = "Will be arrived at : " + stationColectorStop + " " + str('%0.2d' % arriveHour) + "." + str('%0.2d' % arriveMinute) + nextDay
    line16 = "Fare : " + str(fare) + " Baht"
    line17 = ""
    line18 = "************************** National Railway Service ****************************"

    f = open('Ticket.txt', 'w')

    nl = '\n'
    f.write(line1+nl+line2+nl+line3+nl+line4+nl+line5+nl+line6+nl+line7+nl+line8+nl+line9+\
    nl+line10+nl+line11+nl+line12+nl+line13+nl+line14+nl+line15+nl+line16+nl+line17+nl+line18+nl)

    f.close()

    #Print ticket-------------------------------------------------------------
    filename = open('Ticket.txt', 'r')
    print(filename.read())
    filename.close()

    print(
    """
Successfully export a ticket to Ticket.txt
Please see the program's folder for the ticket...

Returning to main menu...
    """
    )

    #reset everything---------------------------------------------------------
    trConstantEast = []
    trainNumber = ""
    m = 0
    n = 0
    stationColectorStart = ""
    stationColectorStop = ""

    minuteDelay = 0

    return menu()

check()
menu()
main()

if __name__ == '__main__':
    main()
