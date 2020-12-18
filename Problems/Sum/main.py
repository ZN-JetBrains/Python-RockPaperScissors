# read sums.txt
my_file = open("sums.txt", "r")

for line in my_file:
    line_list = line.split(" ")
    print(int(line_list[0]) + int(line_list[1]))

my_file.close()
