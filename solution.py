#!/usr/bin/python3.4

"""
==> Author: Njuguna John Kamau
==> email: johnkama45@gmail.com
==> Date: 2015-9-3
==> Written and tested in python 3.4.3
"""

def createStrList(fileName):
    with open(fileName,'r') as file:                        #open the file then close after reading
        content = file.read()                               #read content
    strList = content.replace('"', '').split(',')           # replace " with nothing then tokenize string to a list of strings
    return strList


def strCanFormPalindrome(keyStr):
    """
        determine if any anagram of keyStr can form a palindrome
        @param keyStr: a string for which to determine if any of its anagram can form a palindrome 
        @return boolean true or false.
        ASSUMPTION: All characters are lower case.
    """    
    charOccurrence = [ 0 for i in range(26)]               # initialize a list of size 26, a-z,  with occurrence of all characters = 0
    
    for ch in keyStr:
        charOccurrence[ ord(ch) - 97 ] = keyStr.count(ch)  # at i_th position store number of occurrence of char 
    
    oddOccurrence = 0                                      # initialize oddOccurrences = 0
    for num in charOccurrence:
        if oddOccurrence > 1:
            return False
        
        if(num % 2 == 1):
            oddOccurrence += 1
            
    return True    
    
    
    
def calculateStrThatCanFormPalindrome(strList):
    """
        Calculates the total number of strings whose any of their 
        anagrams can form a palindrome.
        Return this total, numOfPalindromeStr
    """
    numOfPalindromeStr = 0
    
    for keyStr in strList:
        if( strCanFormPalindrome(keyStr) == True):
            numOfPalindromeStr += 1 
    
    return numOfPalindromeStr
    


"""..........Execute the program.........."""
if __name__ == "__main__":
    strList = createStrList("strings.txt")
    numOfStr = len(strList)
    numOfPalindromeStr = calculateStrThatCanFormPalindrome(strList)    
    probabilityOfPalindromeStr = numOfPalindromeStr/numOfStr       #calculate probability
    
    print("Probability is {0:.10}".format(probabilityOfPalindromeStr))    #Output result to 10 decimal places
    
    
    
    
    
    
    
    
    
