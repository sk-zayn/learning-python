# num = 12

# for i in range (1, 4):
#   guess = int(input("Enter your guess "))
#   if guess == num :
#     print("You Won")
#     break
# else:
#   print("You've Lost")

# fruits = ["apple", "banana", "guava", "cherry"]
# adj = ["bitter", "sour", "sweet"]

# for i in fruits:
#   for j in adj:
#     print(i,j)
#   else:
#     print("Inner loop is over")
# else:
#   print("Outer loop is over")


# for i in range (1,11):
#   for j in range(1,i):
#     print (j, end="")
#   print()

# list = [[1, 2, 3,], [4, 5, 6,], [7, 8, 9]]
# for i in list:
#   for j in i:
#     print (j)

# i = 1
# while i<=5 :
#   print(i)
#   i = i+1

# # Infinite loop with break 
# i = 1
# while i>=0:
#   print(i)
#   if i == 10:
#     break
#   i = i+1

# i = 1
# while True:
#   print(i)
#   if i == 10:
#     break
#   i = i+1
4# num = 7
# i = 1
# while i <= 3:
#   guess = int (input("Enter your guess "))
#   if guess == num:
#     print("You won")
#     break
#   i = i + 1
# else:
#   print("you lost")

total = 0

while True:
  num = int(input("Enter a number here "))
  if num < 0:
    print("Its a negative number so we skipped it ")
    continue
  if num == 0:
    break
  total = total + num

print(total)