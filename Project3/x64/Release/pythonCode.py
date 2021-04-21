# -----------------------------------------------------------
# 
# Reads the "inputfile.text" and displays a corresponding list of the different grocery items and the number of purchases for the day.

# Makes a histogram using the data that was analyzed, and then writes the data to "frequency.dat".
# 
# -----------------------------------------------------------
import re
import string
import filecmp
import fileinput
import array

def printsomething():
    """ Prints hello from Python."""

    print("Hello from python!")

def PrintMe(v):
    """ Prints hello from Python."""
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    """ Returns the value squared."""
    return v * v

def myFile():
    """ Opens and reads a file and prints the data. """
    #filename = "Input File.text"
    # f = open(filename, "r")
    # print(f.readline())
    # f.close()
    groceries= {}
    key=""
    value =0
    tempI=0
    space=" "
    factor=1
    factorI=1
    tempKey= ""
    tempVal=1
    a = open("inputfile.txt", "r")
 
    for x in a:
        if x in groceries: 
       
            tempI = groceries.get(x)
           
            value = tempI + 1
            groceries[x]= value
        else:

            value = 1
            temp = {x , value }
            groceries[x] = value
    for x in groceries.keys():
        tempKey = x
        tempVal = groceries.get(x)
        #print (tempKey.replace("\n","") + "    " + str(tempVal))
        factorIS= tempKey.replace("\n","")
        factorI = len(factorIS)
        factor=  13 - factorI
        #print("%s: %10d\n" % (tempKey.replace("\n",""), tempVal))
        if factor == 1 :
            print("%s:%1s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 2:
             print("%s:%2s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 3:
             print("%s:%3s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 4:
             print("%s:%4s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 5 :
            print("%s:%5s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 6:
             print("%s:%6s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 7:
             print("%s:%7s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 8:
             print("%s:%8s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 9 :
            print("%s:%9s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        else:
            print("%s:%10s%10d\n" % (tempKey.replace("\n",""),space, tempVal))

    a.close()
    
def createDict():

    """ Opens and reads a file and prints the data. Returns a dictionary that reperests the Key:Value pair as Grocery Name: Frequency Number"""
    #filename = "Input File.text"
    # f = open(filename, "r")
    # print(f.readline())
    # f.close()
    groceries= {}
    key=""
    value =0
    tempI=0
    space=" "
    factor=1
    factorI=1
    tempKey= ""
    tempVal=1
    a = open("inputfile.txt", "r")
 
    for x in a:
        if x in groceries: 
       
            tempI = groceries.get(x)
           
            value = tempI + 1
            groceries[x]= value
        else:

            value = 1
            temp = {x , value }
            groceries[x] = value
    a.close()
    return groceries
def printAllList():
    """ Calls function createDict() prints the data in dictionary"""
    groceries = createDict()
    key=""
    value =0
    tempI=0
    space=" "
    factor=1
    factorI=1
    tempKey= ""
    tempVal=1
    print("Printing grocercy items and number of items purchased:")

    for x in groceries.keys():
        tempKey = x
        tempVal = groceries.get(x)
        #print (tempKey.replace("\n","") + "    " + str(tempVal))
        factorIS= tempKey.replace("\n","")
        factorI = len(factorIS)
        factor=  13 - factorI
        #print("%s: %10d\n" % (tempKey.replace("\n",""), tempVal))
        if factor == 1 :
            print("%s:%1s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 2:
             print("%s:%2s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 3:
             print("%s:%3s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 4:
             print("%s:%4s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 5 :
            print("%s:%5s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 6:
             print("%s:%6s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 7:
             print("%s:%7s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 8:
             print("%s:%8s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        elif factor == 9 :
            print("%s:%9s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
        else:
            print("%s:%10s%10d\n" % (tempKey.replace("\n",""),space, tempVal))
    print("Done.")

def printSpecItem(name):
    """ Calls the function createDict() and uses name to find the specific Item in that list. Prints the Grocery Name: Frequency Number. If No name exisits then displays that the item is not found."""
    groceries = createDict()
    tempI=1
    value = -999
    key =""
    print("For %s :\n" % (name))
    tempKey=""
    userN=name
    #print (tempKey.replace("\n","") + "    " + str(tempVal))
    for x in groceries.keys():
        tempKey = x
        if (userN.lower() in tempKey.lower()):
           value = 1
           key=x
    
    if value == 1:
         tempVal = groceries.get(key)
         print("%s:%10d\n" % (key.replace("\n",""), tempVal))

    else:
        print ("The item was not found in the list!")
    return value

def makeHistogram():
    """Makes a text histogram by the dictiornary created with the function createrDict(). Returns no value. """

    f = open("frequency.dat", "w")
 
    groceries = createDict()
    hist = {}
    key=""
    tempStr=""
    val=1

    i = 0
    for x in groceries.keys():
        key = x
        val=groceries.get(x)
        for x in range(val):
            tempStr= tempStr +"="
        hist[key]= tempStr
        tempStr=""

    for x in hist.keys():
        key = x
        space = " "
        val=hist.get(key)
        tempKey = x
        tempVal = groceries.get(x)
        #print (tempKey.replace("\n","") + "    " + str(tempVal))
        factorIS= tempKey.replace("\n","")
        factorI = len(factorIS)
        factor=  13 - factorI
        #print("%s: %10d\n" % (tempKey.replace("\n",""), tempVal))
        if factor == 1 :
            print("%s:%1s%10s\n" % (tempKey.replace("\n",""),space, val))
            f.write("%s:%1s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 2:
             print("%s:%2s%10s\n" % (tempKey.replace("\n",""),space, val))
             f.write("%s:%2s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 3:
             print("%s:%3s%10s\n" % (tempKey.replace("\n",""),space, val))
             f.write("%s:%3s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 4:
             print("%s:%4s%10s\n" % (tempKey.replace("\n",""),space, val))
             f.write("%s:%4s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 5 :
            print("%s:%5s%10s\n" % (tempKey.replace("\n",""),space, val))
            f.write(("%s:%5s%10s\n" % (tempKey.replace("\n",""),space, val)))
        elif factor == 6:
             print("%s:%6s%10s\n" % (tempKey.replace("\n",""),space, val))
             f.write("%s:%5s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 7:
             print("%s:%7s%10s\n" % (tempKey.replace("\n",""),space, val))
             f.write("%s:%7s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 8:
             print("%s:%8s%10s\n" % (tempKey.replace("\n",""),space, val))
             f.write("%s:%8s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 9 :
            print("%s:%9s%10s\n" % (tempKey.replace("\n",""),space, val))
            f.write("%s:%9s%10s\n" % (tempKey.replace("\n",""),space, val))
        else:
            print("%s:%10s%10s\n" % (tempKey.replace("\n",""),space, val))
            f.write("%s:%10s%10s\n" % (tempKey.replace("\n",""),space, val))
    print("Done.")



    f.close()  
def readFreq():
   """ Reads the file "frequency.dat" and displays the data. """
   print("Reading Frequency Data: \n")
   f = open("frequency.dat", "r")
   groceries= {}
   hist={}
   histVal=""
   val=0
   name=""
   i = 0
   end=0
   tempVal=0
   tempVal2=0
   for x in f:
       length = len(x)
       while i < length:
          temp = x[i]
          if temp == "=":
              tempVal+=1
            
          i += 1
       i = 0
       
       while i < length:
          temp = x[i]
          if temp == ":":
              end=i
              break;
 
          i += 1
       name = x[0:end]
       tempx = ""

       for j in range(val):
           tempx=tempx+"="
       
       histVal= tempx
       val= tempVal
 
       groceries[name]= val
       hist[name]=histVal
       tempVal=0
   for x in hist.keys():
        key = x
        space = " "
        val=hist.get(key)
        tempKey = x
        tempVal = groceries.get(x)
        #print (tempKey.replace("\n","") + "    " + str(tempVal))
        factorIS= tempKey.replace("\n","")
        factorI = len(factorIS)
        factor=  13 - factorI
        #print("%s: %10d\n" % (tempKey.replace("\n",""), tempVal))
        if factor == 1 :
            print("%s:%21s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 2:
             print("%s:%20s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 3:
             print("%s:%23s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 4:
             print("%s:%24s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 5 :
            print("%s:%25s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 6:
             print("%s:%26s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 7:
             print("%s:%27s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 8:
             print("%s:%28s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 9 :
            print("%s:%29s%10s\n" % (tempKey.replace("\n",""),space, val))
        else:
            print("%s:%30s%10s\n" % (tempKey.replace("\n",""),space, val))
   
   for x in groceries.keys():
        key = x
        space = " "
        val=groceries.get(key)
        tempKey = x
        tempVal = groceries.get(x)
        #print (tempKey.replace("\n","") + "    " + str(tempVal))
        factorIS= tempKey.replace("\n","")
        factorI = len(factorIS)
        factor=  13 - factorI
        #print("%s: %10d\n" % (tempKey.replace("\n",""), tempVal))
        if factor == 1 :
            print("%s:%1s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 2:
             print("%s:%2s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 3:
             print("%s:%3s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 4:
             print("%s:%4s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 5 :
            print("%s:%5s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 6:
             print("%s:%6s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 7:
             print("%s:%7s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 8:
             print("%s:%8s%10s\n" % (tempKey.replace("\n",""),space, val))
        elif factor == 9 :
            print("%s:%9s%10s\n" % (tempKey.replace("\n",""),space, val))
        else:
            print("%s:%10s%10s\n" % (tempKey.replace("\n",""),space, val))
   
            
            
   print("Done.")

