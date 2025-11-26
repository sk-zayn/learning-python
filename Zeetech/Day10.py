for i in range(1,6):
  print("zain")
else :
  print ("done")

list1 = ["zain", "zahid", "zainab", "parveen", "zaid"]

for i in list1 :
  if i == "zaid" :
    break # when looops breaks else statement wont run 
  print (i)
else :
  print ("list is over")


list1 = ["zain", "zahid", "zainab", "parveen", "zaid"]
for i in list1 :
  if i == "zainab":
    continue
  print(i)
else :
  print ("Else part will get execute in continue statement")


num = int (input("Enter a number here "))

for i in range(2, num):
  if num % i == 0:
    print(f"{num} is not a prime number ")
    break
else :
  print(f"{num} Is a prime number ")