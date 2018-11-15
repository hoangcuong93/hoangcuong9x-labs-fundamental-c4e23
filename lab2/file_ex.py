content ='''
Tieu de,
Noi dung
'''

with open("content.txt", "r") as f:
    c = f.read()
    print(c)
    #f.write(content)

#1. open file
#f = open("content.txt", "w") #write
#2. write file
#f.write(content)
#3. close file
#f.close()