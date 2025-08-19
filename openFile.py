# file = open('newfile.pdf', 'w') #to open a file n write content in it
# file.write("Hello world!, this is Affy\n") #\n means 'next add should be in a new line
# file.write(uppercase) #writs your message in uppercase

# # #Reading a  file
# # file = open('new file.pdf', 'r')
# # data = file.read() #'read' writes lines continually n 'readline' writes just a line
# # print(data)

# # # to append or add content to a file
# # file = open('newfile.pdf', 'a')
# # file.write("Invite JsMammie to my room")

# # handling error with try-except
try:
    file = open('newfile.pdf', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
        print('File Operation Completed') #can be any other cacthphrase
        file.close()  #used to clean up/cllose a file


# # #with automatically handles closing
# # with open('newfile.pdf', 'w')
# # as file: file.write('Hello python!')
