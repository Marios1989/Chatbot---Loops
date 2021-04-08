# Intro to Loops
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

# For Loops: Using Range
promise = "I will finish the python loops module!"

for temp in range(5):
    print(promise)

# While Loops: Introduction
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

# While Loops: Lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1

# Infinite Loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)

# Loop Control: Break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
     print("They have the dog I want!")
    break

# Loop Control: Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
     continue
  print(age)

# Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)

# List Comprehensions: Introduction
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grades + 10]
print(scaled_grades)

# List Comprehensions: Conditionals
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

# Review
single_digits = range(10)
squares = []

for item in single_digits:
    print(item)
    squares.append(item ** 2)

print(squares)

cubes = [item ** 3 for item in single_digits]
print(cubes)
