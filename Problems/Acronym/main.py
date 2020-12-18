# read test.txt
my_file = open("test.txt", "r")

for line in my_file:
    print(line[0])

my_file.close()
