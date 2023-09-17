1. Write a Python program to calculate the total number of Vowels and Count of each individual vowel A,E,I,O,U in the String "Guvi Geeks Network Private Limited"?

def count_vowels(a):
    dict_vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}		# create a dictionary
    vowel_count = 0
    for i in a:				# iterating over the input value
        for j in dict_vowels:			# iterating over the dictionary
            if i == j:	
                dict_vowels[j]=dict_vowels[j]+1		# updating the values of the dict
                vowel_count=vowel_count+1		# counting the number of vowels
    print("Total number of vowels are : %d" %vowel_count)
    print(dict_vowels)
            
val=input()
count_vowels(val.lower())			# converting to lower case and calling the function


Output:

GUVI GEEK NETWORK PRIVATE LIMITED
Total number of vowels are : 12
{'a': 1, 'e': 5, 'i': 4, 'o': 1, 'u': 1}


2. Create a Pyramid of Numbers 1 to 20 using For Loop?

for i in range(1,20):		# iterating over the range
    for j in range(1,i+1):	# iterating the number in each line
        print(i,"",end="")
    print("\n")


Output:

1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 

6 6 6 6 6 6 

7 7 7 7 7 7 7 

8 8 8 8 8 8 8 8 

9 9 9 9 9 9 9 9 9 

10 10 10 10 10 10 10 10 10 10 

11 11 11 11 11 11 11 11 11 11 11 

12 12 12 12 12 12 12 12 12 12 12 12 

13 13 13 13 13 13 13 13 13 13 13 13 13 

14 14 14 14 14 14 14 14 14 14 14 14 14 14 

15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 

16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 

17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 

18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 

19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 


3. Write a function that takes a string and returns a new string with all the vowels removed.

def strvowel(ins):
    list1=['a','A','e','E','i','I','o','O','u','U']	# list with all the vowels
    s1=""				# empty string variable
    for i in ins:			# iterating over the input value 
        if i not in list1:			# not a vowel then add the letter to the variable
            s1=s1+i
    print(s1)
  
ins =input()
strvowel(ins)

Output:

Guvi Geeks Network
Gv Gks Ntwrk

4. Write a function that takes a string and returns the number of unique character in it.

def unique_char(inp):
    list1=[""]		# create an empty list
    for i in inp:		
        if i not in list1:		# if the character not in list1
            list1.append(i)	# append the char in the list
    print("".join(list1))
    
inp=input()
unique_char(inp)
 
Output:

GUVI GEEK NETWORK PRIVATE LIMITED
GUVI EKNTWORPALMD

5. Write a function that takes a string and returns True if it is a palindrome, False otherwise.

def palindrome(inp):	
    rinp = inp[::-1]		# reverse the input string using -1
    if inp == rinp:		# if both the reversed string and input string matches return true
      print("True")
    else:
      print("False")
    
inp=input()
palindrome(inp)

Output:

madam
True

6.Write a function that takes two strings and returns the longest common substring between them.

def comsubs(inp1,inp2):
    a=""		# create an string variable
    for i in inp1:
        if i in inp2:	# iterate over the first string then if the char in string1 is present in string2 
            a=a+i	# add it to the variable
    print(a)
    
inp1=input()
inp2=input()
comsubs(inp1,inp2)

Output:
bappless
capples
apples


7.Write a function that takes a string and return the most frequent character in it.

def freqchar(inp,inp1):
    dic={}				# empty dictionary
    val=0				# create number variable
    for i in inp:	
        if i != " ":			# if char is not a space
            if i not in dic:			# if char not in dict
                dic[i]=1			# create a key in the dict and value as 1
            else:
                val=dic.get(i)		# else update the value of the key
                dic[i]=val+1
    maxvalue = max(dic.values())		# find the max value in the dict and display the frequent char
    for key,value in dic.items():
        if value == maxvalue:
            print(key,":",value, end=" ")
            
inp=input()
inp1=list(inp)
freqchar(inp,inp1)

Output:

hi how are you i am fine
i : 3 

8. Write a function that takes a string and returns True if it is an anagram of another string, False otherwise.

def anagramwords(inp,inp1):	
    anag="False"		# create a variable and assign to false
    if len(inp)==len(inp1):	# if both the string are of the same length
        for i in inp:		# iterate the 1st string
            if i not in inp1:	# if the char in is not in the 2nd string
                anag="False"	# return false
                print(anag)
                return
            else:
                anag="True"	# return true
    else:
        anag="False"
    print(anag) 
    
inp = input()
inp1=input()
anagramwords(inp,inp1)

Output:

silent
listen
True


9.Write a function that takes a string and returns the number of words in it.

def numberwords(inp):
    spaces=0		# space variable to 0
    if len(inp) == 0:		# if length is 0 no words
        print("0")	
    else:	
        for i in inp:		# iterating the string and finding the spaces
            if i ==" ":
                spaces =spaces + 1	# update the space with 1
    print (spaces+1)		# the number of spaces +1 are the number of words
        
  
  
inp = input()
numberwords(inp)

OUTPUT:
hi how are you I am fine.
7


