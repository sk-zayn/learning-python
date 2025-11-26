# Any thing that is written in quotes can be called string 
# Operators in string
'''
1. concatination
2. Repetition
3. indexing
4. slicing
5. in 
6. not in
'''

# 1. concatinate there are 2 methods using +operator and ""

s1 = 'hello'
s2= 'world'
s3 = s1 + s2
print(s3)

s5 = 'hello' 'world'
print(s5)

print(dir(str))# dir is a function that prints all the method you can use for the given parameter

s = 'Hi how are you, what are you doing tomorrow, lets play volleyball '
x = len(s)
count = 0
print(s.find('y'))
for i in range(x+1):
    if s.find('o') == True:
        print(s[i])
        count += 1

s = 'Hi how are you, what are you doing tomorrow, lets play volleyball '
index = 0

while True:
    pos = s.find('y', index)
    if pos == -1:
        break
    print("y at index", pos)
    index = pos + 1
