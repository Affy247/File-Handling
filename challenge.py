


# Challenge: Read from a text file, process the content, and write results to a new file.
#1: open 'input.txt' in write mode and add text
file = open('inpot.txt', 'w')
file.write("Python is not fun.\n")
file.write("But I am learning file handling.\n")
file.write("This assignment is simple.\n")
file.write("But gives me a tough time.\n")
file.write("Keep coding every day, i guess that does it!.\n")
file.close()  

#2: Read the contents of 'input.txt'
try:
    file = open('inpot.txt', 'r')
    content = file.read()  # reads everything at once
    print("File content:\n", content)  
except FileNotFoundError:
    print("inpot.txt not found!")
finally:
    file.close()

#3: Count the number of words
words = content.split()  # split text into list of words
word_count = len(words)  # get the number of words
print("Word Count:", word_count)

#4: Write processed text + word count into 'output.txt'
with open('outpot.txt', 'w') as outfile:
    outfile.write("Processed Text:\n")
    outfile.write("Word Count: " + str(word_count) + "\n")
print("outpot.txt has been created successfully!")