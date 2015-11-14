# Probability-of-Anagram-Being-a-Palindrome
PROBLEM
From set of strings provide in a text file, calculate the probability of a string having a palindrome for any of its anagrams

APPROACH
- Read the text file
- Store the strings in a list 
- get size of list, numOfStr
- For each string determine whether any of its anagram can be a palindrome.
- Count all strings whose any of their anagrams result to a palindrome, numOfPalindromeStr
- Solve the problem numOfPalindromeStr/numOfStr

LOGIC FOR THE SOLUTION

- A palindrome, if broken down into 2 halves, each halve is the reverse of the other. 
- If size of palindrome is odd, discard the mid character for the above statement to hold true.
- These statements have the following implication:
- All unique characters must have even occurrence,  except the mid character if size of string is odd
- At most only one character can have odd occurrence. 
