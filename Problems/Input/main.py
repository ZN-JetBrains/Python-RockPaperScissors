# write the code here
line = input()
my_file = open("input.txt", "w", encoding="utf-8")
my_file.write(line)
my_file.close()
