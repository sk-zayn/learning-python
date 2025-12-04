def prime_number (num):
  for i in range(2, num):
    if num % i == 0:
      print(f'{num} is not a prime number')
      break
  else:
    print(f'{num} is a prime number')

prime_number(11)

def is_perfect (num):
  sum = 0
  for i in range(1, num):
    if num % i == 0:
      sum += i
  if sum == num :
    return f'{num} is a perfect number'
  else:
    return f'{num} is not a perfect number'
  
print (is_perfect(20))

def greatest_number (num):
  max = num[0]
  for i in num :
    if i > max :
      max = i
  return f'{max} is the greatest number'

print(greatest_number([1, 4, 12, 29, 13, 18, 7]))


def great_num (num):
  max = 0
  print(num)
  for i in num:
    for j in i:
      if j > max:
        max = j 
  return max

def great_num(num):
    return max(max(inner) for inner in num) #chat gpt version

print(great_num([[1, 3, 5], [87, 23, 6], [12, 67, 8]]))
  

      
