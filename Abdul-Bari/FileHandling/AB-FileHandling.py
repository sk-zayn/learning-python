# r = read mode it only lets you read the content of the file. it only works if file exists.

# w = write mode it only lets you write content in the file. if file exist it will delete all the content in it
# and you can write anything you want from start and if file does not exist it will create a new file for you

# a = append it will let you add content in the existing file unlike write(wich deletes everything in it)

file = open('myfile.txt', 'w')
file.write('Hello\n')
file.write('How are you\n')
file.write('My name is zain shaikh\n')

f = open('Tanjiro.jpg', 'rb')
data = f.read()

cf = open('Tanjiro1.jpg', 'wb')
cf.write(data)

f.close()
cf.close()
