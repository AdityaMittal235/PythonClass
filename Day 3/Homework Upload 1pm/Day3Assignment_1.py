#Q1. Write a python program to print only the first two values from the following List
fruits = ["apple","mango","banana","blueberry","orange"]
print(fruits[0:2])

#Q2. Write a python program to remove the value "apple" and insert value "pineapple" in the above list. Print the list once modified
fruits.remove("apple")
fruits.append("pineapple")
print(fruits)

#Q3.  Let's try to do some changes with a string 'LETTER'  word = 'LETTER'
# Try to change the first character to 'B' by assignment
#1st way
word='LETTER'
word=list(word)
word[0]="B"
word="".join(word)
print(word)

#2nd way

word='LETTER'
word='B'+word[1:]
print(word)

#Q4. Do the same with replace() function.
word='LETTER'
word=word.replace("L","B")
print(word)



