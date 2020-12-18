numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_name = "file_with_list.txt"
my_file = open(file_name, mode="w", encoding="utf-8")

print(str(numbers), file=my_file, end="")

my_file.close()

