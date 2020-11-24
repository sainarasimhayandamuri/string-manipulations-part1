"""
String manipulation:
"""

mystr = """urjanet software solutions,
bigenergydataresource,
        chennaitidelpark"""
l1 = mystr.split("\n") #split function : splits the string into our required format and stores in list.
print("String after performing split function",l1)
l2 = mystr.splitlines() # splitlines : It splits the string based on line by line and stores it in list.
print("String after performing splitline function",l2)

mystr = """urjanet software solutions,
bigenergydataresource,
        chennaitidelpark"""
#Partiton function : It divides the string into tuple with three elements
l3 = mystr.partition("a")
print("String after partitioning",l3)

normstr = "jai ballaya"
l4 = normstr.partition("a")
print(l4)

#Letter case conversion 
mystr2 = str.capitalize(mystr) #Capitalize is a function which converts the first character into upper case.
print(mystr2)

mystr3 = mystr.capitalize()
print(mystr3)

mystr4 = mystr.upper() #Upper is a function which converts the entire characters into upper case i.e capital letters.
print(mystr4)

mystr5 = mystr4.lower() #Lower is a function which converts the entire characters into lower case i.e small letters.
print(mystr5)

mystr6 = mystr2.swapcase() #Swapcase will convert the uppercase to lowercase and lowercase to uppercase in a given string.
print(mystr6)

