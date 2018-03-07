number_file = open('numbers.txt','r')
file_contents = number_file.readlines()
total = int(file_contents[0]) + int(file_contents[1])
print(total)
    
