with open('configuration.txt', 'r') as f:
    content = f.read(10)
    print(content)
    print(f.tell())  # prints the position of the cursor
    print(f.closed)
    print(f.seek(5))  # moves the cursor 5 chars
    content = f.read(10)
    print(content)
print(f.closed)

# absolute path
# C:\Users\Alex\Documents\project\file.txt
# /home/alex/Documents/project/file.txt

# relative path
# project/file.txt
# ../another_folder/file.txt
print("#" * 50)
with open('configuration.txt', 'r') as f:
    for line in f:
        print(line, end="")
print()
print("#" * 50)
with open('new_configuration.txt', 'w') as f:
    f.write("ip addr 10.1.1.2 255.255.255.0")

with open('new_configuration.txt', 'a') as f:
    f.write("\n")
    f.write("ip addr 10.1.1.10 255.255.255.0")
