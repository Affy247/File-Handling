# to open and read contents of input.txt
try:
    file = open("input.txt", "r")   # open the file in read mode
    content = file.read()           # read everything in the file
    print("File content:\n", content)  # show the content in the terminal
except FileNotFoundError:
    print("input.txt not found. Please check the file path.")
finally:
    file.close()  

# to count the number of words in the file
words = content.split()   # split text into list of words
word_count = len(words)   # count how many words are in the list
print("Total words in file:", word_count)

# to convert all text to uppercase
upper_content = content.upper()
print("\nUppercase version:\n", upper_content)

# Write the processed text + word count into output.txt
with open("output.txt", "w") as outfile:   # 'w' means write mode (creates file if not exists)
    outfile.write("Processed Text:\n")
    outfile.write(upper_content + "\n\n")
    outfile.write("Word Count: " + str(word_count) + "\n")
print("\n output.txt has been created successfully!")
