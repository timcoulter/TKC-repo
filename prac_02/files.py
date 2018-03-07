name_file = open("name.txt",'w')
name = input(str("Enter your name here: "))
print(name, file = name_file)
name_file.close()
