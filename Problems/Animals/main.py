# read animals.txt
# and write animals_new.txt

original_file = open("animals.txt", "r", encoding="utf-8")
animals = original_file.readlines()
animals = "".join(animals)
animals = animals.split()

original_file.close()

new_file = open("animals_new.txt", "w", encoding="utf-8")

for animal in animals:
    new_file.write(animal + " ")

new_file.close()
