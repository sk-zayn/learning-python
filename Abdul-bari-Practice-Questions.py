num = int (input('Enter a number here '))
m = num

reverse = 0
while num > 0 :
  r = num % 10 
  num = num // 10
  reverse = reverse * 10 + r
print(reverse)

if m == reverse:
  print('number is palindrome ')
else :
  print('number is not a palindrome')
  

number = int(input('Enter a number '))
count = 0 
sum = 0
while count < number:
  n = int(input('enter a number here '))
  sum = sum + n
  count = count + 1
print(sum)


number = int (input('enter a number here '))
count = 0
pnum = 0
nnum = 0
while count < number:
  n = int(input('Enter number here '))
  if n >= 0 :
    pnum = pnum + n
  else :
    nnum = nnum + n
  count = count + 1
print('sum of positive number is', pnum)
print('sum of negative numbre is', nnum)

