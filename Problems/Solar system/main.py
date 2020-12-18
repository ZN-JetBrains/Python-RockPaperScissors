# create the planets.txt
my_file = open("planets.txt", "w", encoding="utf-8")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for planet in planets:
    my_file.write(planet + "\n")

my_file.close()
