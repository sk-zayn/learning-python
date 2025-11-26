import random
print(random.random()) #Generates a random number between 0 and 1 
print(random.randint(1,5)) # Generates a random number between the given parameter

list = ['zain', 'zaid', 'zahid', 'zainab', 'parveen']
print(random.choice(list)) #prints any one random value 

lsit2 = ['zain', 'zaid', 'zahid', 'zainab', 'parveen']
print(random.sample(lsit2, k=3)) #prints howmany random values you want according to k you wrote 

list3 = ['zain', 'zaid', 'zahid', 'zainab', 'parveen']
print(random.choices(list3, k=3)) #difference etween this and sample is that choices can print the same value multiple times even if the other options are available

list4 = ['zain', 'zaid', 'zahid', 'zainab', 'parveen']
random.shuffle(list4)
print(list4)

menu = input('if you want to play press y or yes if you dont press n or no ')
while menu.upper() == 'Y' or menu.upper()== 'YES':
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print('dice 1 has value ', dice1, 'dice 2 has value ', dice2)
  menu = input ('Do you want to play again ')
  if menu != 'Y' and menu != 'YES':  
    print('come again next time ')
    break
else :
  print('Ek time to khel le bhai')


output = ''
for i in range(1,5):
  output = output + str(random.randint(1,9))
print(output)