
with open("D:\\Python\\Python Course with Notes\\9. Chapter 9\\another2.txt", 'r') as f: # do not need to close the file , it will automatically closed
    a = f.read()
with open("D:\\Python\\Python Course with Notes\\9. Chapter 9\\another2.txt", 'w') as f:
    a = f.write("me")
print(a)