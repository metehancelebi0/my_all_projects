#CALCULATION AVERAGE GRADE OF FİLES

# def calculate_average_grade(studentdata):
#     with open("studentdata.txt", "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             data = line.split()
#             name = data[0]
#             grades = []
#             for grade in data[1:]:
#                 grades.append(int(grade))
#             average = int(sum(grades))/len(grades)
#             print(name, ":", average)
#
# calculate_average_grade("studentdata.txt")



#FINDING MAX AND MIN VALUES İN FİLES

# file = open("studentdata.txt", "r")
# for line in file:
#     items = line.split()
#     name = items[0]
#     scores = list(map(int, items[1:]))
#     for i in range(len(items[1:])):
#         items[i+1] = int(items[i+1])
#     print(name , "max is", max(scores),"min is", min(scores))
# file.close()



#TAKES THE İNPUTS FROM THE FİLES

# import turtle
# alex = turtle.Turtle()
# wn = turtle.Screen()
# file = open("mystery.txt","r")
# for line in file:
#     items = line.split()
#     if items[0] == "UP":
#         alex.up()
#     else:
#         if items[0] == "DOWN":
#             alex.down()
#         else:
#             alex.goto(int(items[0]),int(items[1]))
# file.close()
# wn.exitonclick()



#SAVING DATAS FROM FİLE

# def int_save(filename):
#     numbers = []
#     for i in range(5):
#         number = int(input("Enter a number: "))
#         numbers.append(number)
#
#     with open(filename, "w") as file:
#         for num in numbers:
#             file.write(str(num)+"\n")
#
# def read_and_sum(filename):
#     total = 0
#     with open(filename, "r") as file:
#         for line in file:
#             total += int(line)
#         return total
#
# int_save("numbers.txt")
# result = read_and_sum("numbers.txt")
# print("sum is", result)



#HOW MANY TİMES WRİTTEN PYTHON İN FİLE

# def count(filename):
#     count = 0
#     with open(filename) as f:
#         for line in f:
#             words = line.split()
#             count += words.count("Python")
#
#         return count
# result = count("text.txt")
# print(result)



#READİNG SORTİNG AND WRİTİNG ON FİLES

# def read_files(filename):
#     with open(filename,"r") as f:
#         return f.read().splitlines()
#
# def sort_students(students):
#     students.sort()
#     return students
#
# def write_students(filename, students):
#     with open(filename,"w") as f:
#         for name in students:
#             f.write(name + "\n")
#
# students = read_files("students.txt")
# sorted_students = sort_students(students)
# write_students("students.txt", sorted_students)



#REMOVİNG BLANK LİNES FROM A FİLE

# def remove_blank_lines(sourceFİle,destinationFİle):
#     with open(sourceFİle,"r") as inputFile, open(destinationFİle,"w") as outputFile:
#         for line in inputFile:
#             if line.strip():
#                 outputFile.write(line)
#
# remove_blank_lines("input.txt","output.txt")



#FILTER EVEN NUMBERS FROM A FİLE

# def filter_even(filename):
#     with open(filename,"r") as f:
#         for line in f:
#             number = int(line)
#             if number % 2 == 0:
#                 print(number)
#
# filter_even("numbers.txt")



#KEEPİNG THE LETTERS AS A KEY

# def add_fruit(inventory, fruit_name, quantity):
#     if fruit_name in inventory:
#         inventory[fruit_name] += quantity
#     else:
#         inventory[fruit_name] = quantity
#
# new_inventory = {}
# add_fruit(new_inventory, 'strawberries', 10)
# print(new_inventory)
# print("strawberries" in new_inventory)
# print(new_inventory['strawberries'])
#
# add_fruit(new_inventory, "strawberries", 25)
# print(new_inventory["Strawberries"])



#CALCULATING THE FREQUENCY OF THE LETTERS

# def letter_frequency(sentence):
#     sentence = sentence.lower()
#     frequency = {}
#
#     for char in sentence:
#         if char >= 'a' and char <= 'z':
#             if char in frequency:
#                 frequency[char] += 1
#             else:
#                 frequency[char] = 1
#
#     for letter in sorted(frequency):
#         print(letter, frequency[letter])
#
# text = input("Enter a sentence: ")
# letter_frequency(text)



#CREATİNG A TRANSLATOR

# def translator(sentence):
#     pirate_dict = {
#     "sir": "matey",
#     "hotel": "fleabaginn",
#     "student": "swabbie",
#     "boy": "matey" ,
#     "madam": "proud",
#     "beauty": "professor",
#     "foul": "blaggart",
#     "hello": "avast",
#     "students": "swabbies",
#     }
#     words = sentence.split()
#     translated_words = []
#     for word in words:
#         if word in pirate_dict:
#             translated_words.append(pirate_dict[word])
#         else:
#             translated_words.append(word)
#
#     return " ".join(translated_words)
# sentence = "hello there students"
# result = translator(sentence)
# print(result)



#CREATING STUDENT LİST ON FİLE

# def createStudentList(filename):
#     student_dict = {}
#     file = open(filename,'r')
#     for line in file:
#         parts = line.strip().split()
#         student_id = parts[0]
#         name = parts[1]
#         last_name = parts[2]
#         student_dict[student_id] = name +""+ last_name
#     file.close()
#     return student_dict
# my_dict = createStudentList("students.txt")
# for key, value in my_dict.items():
#     print(key + ' ' + value)



#SHOWİNG THE COURSES AND İDs İN FİLES

# registeredStudents = {
#     "CENG1009": ["117987","124876"],
#     "CENG3500": ["124876"],
#     "CENG2005": []
# }
#
# course_code = input("Enter course code: ")
# student_id = input("Enter student ID: ")
# registeredStudents[course_code].append(student_id)
# print(registeredStudents)



#AVOİDİNG ERRORS

# def safe_divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Error: cannot divide by zero"
#     except TypeError:
#         return "Error: İnvalid İnput"
#
# print(safe_divide(4, 0))
# print(safe_divide(4, 1))
# print(safe_divide(4, 2))



#TYPE OF ERROR AND EXCEPTİONS

# treasure_chest = {
#     "gold_coin": 100,
#     "silver_coin": 50,
#     "emerald": 200
#         }
#
# def open_chest(treasure_chest,treasure_name):
#     try:
#         return treasure_chest[treasure_name]
#     except KeyError:
#         return "Error: Treasure not found"
#     except TypeError:
#         return "Error: İnvalid Error"
#
# print(open_chest(treasure_chest,"gold_coin"))



# ARMSTRONG NUMBERS

# number = int(input("Enter a number: "))
#
# total = 0
# temp = number
# digits = len(str(number))
#
# while temp > 0:
#     digit = temp % 10
#     total = total + (digit ** digits)
#     temp = temp // 10
#
# print(total == number)