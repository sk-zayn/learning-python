num = 12

for i in range (1, 4):
  guess = int(input("Enter your guess "))
  if guess == num :
    print("You Won")
    break
else:
  print("You've Lost")