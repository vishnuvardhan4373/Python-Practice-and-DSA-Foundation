with open("data.txt","w") as file:
    file.write("Hello Python\n")
    file.write("I am Learning Python File Handling.")

try:
    with open("hello.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File doesn't exist.")