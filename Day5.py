#slicing
#negative value runs from right to left 


students = [ "alham", "zayn", "abuzar", "aquib", "saif", "mayank"]

print (students[0:]) #print whole list 
print (students[:]) #print whole list 
print (students[0:3]) #from zero th index till 3 vlues
print (students[2:4])
print (students[1:5])
print (students[3:5])
print (students[-3:-3]) 
print (students[1:-3])
print (students[0:-4])


#reverse iteration 
students1 = [ "alham", "zayn", "abuzar", "aquib", "saif", "mayank"]
print(students1 [:: -1]) # print every thing in reverse 
print (students1 [::-2]) # print every thing in reverse with 1 value gap
print(students1[::-3]) #print every thing in reverse with 2 value gap 

#it also works on string 
name = "zain"
print(name[::-1])
print(name[::-2])

str1 = input ("enter your string ")
reverse = str1[::-1]

if str1 == reverse:
    print("its a palindrome")

else:
    print("its not a palindrome")

