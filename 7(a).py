with open("output.txt", "r") as file:
    content = file.read()
print("Content read from the file:")
print(content)

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text.")

print("Content written to the file.")
