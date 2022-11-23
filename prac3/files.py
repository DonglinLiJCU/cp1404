name = input("Please input your name: ")
file = open("name.txt", 'w')
file.write(name)
file.close()

file = open("name.txt", 'r')
name = file.readline()
print(f"Your name is {name}")
file.close()

file = open("numbers.txt", 'r')
first = int(file.readline())
second = int(file.readline())
print(str(first+second))
file.close()

file = open("numbers.txt", 'r')
total = 0
lines = file.readlines()
for line in lines:
    total += int(line)
print(total)