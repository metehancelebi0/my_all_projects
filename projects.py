# FINDING THE AREA OF RECTANGLE

# height = float(input("Enter the height of rectangle"))
# width = float(input("Enter the width of rectangle"))
#
# area_of_rectangle = height*width
# print(area_of_rectangle)



#FINDING THE MPG FOR CARS
#
# fuel = float(input("Enter the full of fuel"))
# distance = float(input("Enter the distance"))
# burning_fuel_per_km = 0.2
# burning_fuel = distance * burning_fuel_per_km
# remaining_fuel = fuel - burning_fuel
# print(remaining_fuel)



#FAHRENHEİT TO DEGREE CELSİUS

# fahrenheit = float(input("Enter the value of Fahrenheit: "))
# celsius = (fahrenheit - 32) * 5 / 9
# print(celsius)



#FINDING LAST DAY OF VACATION

# length_of_vacation = int(input("Enter the length of the vacation: "))
# day_end = length_of_vacation % 7
#
# if day_end == 0:
#     print("vacation ends sunday")
# elif day_end == 1:
#     print("vacation ends moday")
# elif day_end == 2:
#     print("vacation ends tuesday")
# elif day_end == 3:
#     print("vacation ends wednesday")
# elif day_end == 4:
#     print("vacation ends thursday")
# elif day_end == 5:
#     print("vacation ends friday")
# else:
#     print("vacation ends saturday")



#FINDING THE CİRCUMFERENCE OF CIRCLE

# import math
# radius = float(input("Enter radius: "))
# circle_of_the_circumference = 2 * math.pi * radius
# print(circle_of_the_circumference)



#FINDING AGE

# birth_year = int(input("Enter your birth year: "))
# age = 2024 - birth_year
# print(age)



#DRAWİNG SQUARE WITH TURTLE

# import turtle
#
# alex = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(4):
#     alex.forward(100)
#     alex.left(90)
# turtle.done()



#ALARM

# current_time = float(input("Enter the current time: "))
# how_many_hours_later_clock_rings = int(input("Enter the number of hours later clock rings: "))
# clock_shows = (current_time + (how_many_hours_later_clock_rings % 24))
# print(float(clock_shows%24))



#BASİC CALCULATION

# print(2 + (3 - 1) * 10 / 5 * (2 + 3))



#STORING THE WORDS

# word1 = "ALL"
# word2 = "WORK"
# word3 = "AND"
# word4 = "NO"
# word5 = "PLAY"
# word6 = "MAKES"
# word7 = "JACK"
# word8 = "A"
# word9 = "DULL"
# word10 = "BOY"
#
# print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)



#CHANGING THE VALUE

# first_value = 6*1-2
# second_value = 6*(1-2)
# print(first_value)
# print(second_value)



#FINDING AREA OF THE CIRCUMFERENCE

# import math
# radius = float(input("Enter radius: "))
# area = math.pi * radius ** 2
# print("The area of the circle is:", area)



#DRAWING EQUILATERAL TRIANGLE WITH TURTLE

# import turtle
#
# alex = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(3):
#     alex.forward(100)
#     alex.left(120)
# turtle.done()



#DRAWING A SQUARE WITH TURTLE

# import turtle
#
# alex = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(4):
#     alex.forward(100)
#     alex.left(90)
# turtle.done()



#LOOP

# for i in range(100):
#     print("We like Python's turtles!")



#MONTHS IN LOOP

# months = ("January","February","March","April","May","June","July","August","September","October","December")
# for i in months:
#     print("One of the months of the year is" , i)



#LIST LOOP

# my_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for item in my_list:
#     print(item)
# print("")
# for item in my_list:
#     print((item*item))



#CREATING SHAPES

# import turtle
#
# wn = turtle.Screen()
#
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)
#
# t.penup()
# t.goto(-300, 100)
# t.pendown()
#
# for i in range(3):
#     t.forward(100)
#     t.left(120)
#
# t.penup()
# t.goto(-150, 100)
# t.pendown()
#
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.penup()
# t.goto(50, 100)
# t.pendown()
#
# for i in range(6):
#     t.forward(100)
#     t.left(60)
#
# t.penup()
# t.goto(300, 100)
# t.pendown()
#
# for i in range(8):
#     t.forward(100)
#     t.left(45)
#
# t.hideturtle()
#
# wn.mainloop()



#DRAWING POLYGONE

# import turtle
#
# length = int(input("Enter the length"))
# sides = int(input("Enter the sides"))
# color = input("Enter the color")
# fill_color = input("Enter the fill color")
#
# alex = turtle.Turtle()
# wn = turtle.Screen()
# alex.color(color)
# alex.fillcolor(fill_color)
# angle = 360/sides
# alex.begin_fill()
#
# for i in range(sides):
#     alex.forward(length)
#     alex.left(angle)
#
# alex.end_fill()
# turtle.done()



#DRUNK PİRATE GAME

# import turtle
#
# steps = 100
#
# wn = turtle.Screen()
# wn.title("Adım Adım Korsan Yolu")
# pirate = turtle.Turtle()
# pirate.shape("turtle")
# pirate.color("brown")
# pirate.speed(1)
#
# pirate.left(160)
# pirate.forward(steps)
#
# pirate.left(-43)
# pirate.forward(steps)
#
# pirate.left(270)
# pirate.forward(steps)
#
# pirate.left(-97)
# pirate.forward(steps)
#
# pirate.left(-43)
# pirate.forward(steps)
#
# pirate.left(200)
# pirate.forward(steps)
#
# pirate.left(-940)
# pirate.forward(steps)
#
# pirate.left(17)
# pirate.forward(steps)
#
# pirate.left(-86)
# pirate.forward(steps)
#
# turtle.done()



#DRAWING STAR

# import turtle
#
# alex = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(5):
#     alex.forward(100)
#     alex.left(216)
#
# turtle.done()



#CLOCK WITH TURTLES

# import turtle
#
# alex = turtle.Turtle()
# wn = turtle.Screen()
# alex.shape("turtle")
# alex.color("blue")
#
# for i in range(12):
#     alex.penup()
#     alex.forward(100)
#     alex.stamp()
#     alex.backward(100)
#     alex.left(30)
#
# turtle.done()



#SIMPLE SPIDER SHAPE

# import turtle
#
# legs = int(input("Enter the number of legs: "))
# alex = turtle.Turtle()
# wn = turtle.Screen()
#
# angle = 360 / legs
# alex.color("red")
# alex.speed(0)
#
# for i in range(legs):
#     alex.pendown()
#     alex.forward(100)
#
#     alex.penup()
#     alex.backward(100)
#
#     alex.left(angle)
#
# alex.hideturtle()
# wn.mainloop()


#PRINT RANDOM NUMBERS

# import random
# random_size = 10
# for i in range(random_size):
#    random_number = random.randint(1,10)
#    print(random_number)



#RANDOM NUMBERS BETWEEN 25-35

# import random
#
# random_size = 10
# for i in range(random_size):
#     random_number = random.randint(25,35)
#     print(random_number)



#PYTHAGOREAN THEOREM

# import math
# side_a = float(input("Enter the side length of a: "))
# side_b = float(input("Enter the side length of b: "))
#
# side_c = math.hypot(side_a, side_b)
# print(side_c)



#CALCULATION OF THE CIRCLE AREA

# def areaOfCircle(r):
#     radius = float(input("Enter the radius of the circle: "))
#     area = math.pi * radius * radius
#     return area
#
# area = areaOfCircle(5)
# print(area)



#DRAWING A STAR WITH FUNCTION IN TURTLE

# import turtle
# alex = turtle.Turtle()
# wn = turtle.Screen()
# def DrawStar(length):
#     for i in range(5):
#         alex.forward(length)
#         alex.left(216)
#
# DrawStar(100)
# turtle.done()



#DRAWING SQUARES WITH FUNCTION

# import turtle
#
# t = turtle.Turtle()
# wn = turtle.Screen()
# t.color("pink")
# wn.bgcolor("green")
# t.pensize(5)
#
# def draw_square(t,length):
#     for i in range(5):
#         for s in range(4):
#             t.forward(length)
#             t.right(90)
#
#         t.penup()
#         t.forward(length*2)
#         t.pendown()
#
# draw_square(t,20)
# wn.exitonclick()



#DRAWING SQUARES

# def draw_polygon(t , side_length , number_of_sides):
#     angle = 360 / number_of_sides
#     for i in range(number_of_sides):
#         t.left(angle)
#         t.forward(side_length)
#
# def growing_squares(t, length=20):
#     for i in range(5):
#         draw_polygon(t , length, 4)
#         t.penup()
#         t.right(45)
#         t.forward(15)
#         t.left(45)
#         t.pendown()
#         length += 20
#
# import turtle
# turtle_orange = turtle.Turtle()
# turtle_orange.speed(1)
# growing_squares(turtle_orange)
#
# turtle.done()



#DRAWING POLYGONE WITH FUNCTION

# def draw_poly(someturtle,somesides,somesize):
#     angle = 360 / somesides
#     for side in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.left(angle)
#
# tess = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("green")
# tess.color("blue")
#
# draw_poly(tess,8,50)
# wn.exitonclick()



#DRAWING SPİRAL

# import turtle
#
# def drawsquare(alex,sideLength):
#     for i in range(4):
#      alex.forward(sideLength)
#      alex.left(90)
#
# def drawCircleSquares(alex,num):
#     for i in range(num):
#         drawsquare(alex,sideLength=90)
#         alex.right(360/num)
#
# wn = turtle.Screen()
# wn.bgcolor("green")
# alex = turtle.Turtle()
# drawCircleSquares(alex,20)
# alex.color("blue")
# wn.exitonclick()



#DRAWING SPIRAL

# import turtle
#
# def drawSpiral(t,size,num,angle):
#     for i in range(num):
#         t.forward(size*i)
#         t.left(angle)
#
# wn=turtle.Screen()
# wn.bgcolor("green")
# wn.setworldcoordinates(-300,-300,300,300)
# t=turtle.Turtle()
# t.speed(100)
# t.color("blue")
# t.penup()
# t.goto(-150,0)
# t.down()
#
# tess=turtle.Turtle()
# tess.color("blue")
# tess.speed(10)
# tess.up()
# tess.goto(150,0)
# tess.down()
#
# drawSpiral(t,2,100,90)
# drawSpiral(tess,2,100,91)
#
# wn.exitonclick()



#DRAWING POLY

# import turtle
# def drawEquitriangle(t,length,num):
#     for i in range(3):
#         t.forward(length)
#         t.left(num)
#
# t = turtle.Turtle()
# wn = turtle.Screen()
#
# wn.bgcolor("green")
# t.color("pink")
#
# drawEquitriangle(t,100,120)
#
# wn.exitonclick()



#DRAWING STAR

# import turtle
#
# def drawStar(t):
#
#     for i in range(5):
#         t.forward(100)
#         t.right(144)
#
# def draw_five_star(t):
#     t.penup()
#     t.goto(-180,50)
#     t.pendown()
#     for i in range(5):
#         drawStar(t)
#         t.penup()
#         t.forward(350)
#         t.right(144)
#         t.pendown()
#
#
# wn= turtle.Screen()
# t=turtle.Turtle()
# wn.bgcolor("green")
# t.color("blue")
#
# draw_five_star(t)
#
# wn.exitonclick()



#DRAWING SPRITE

# import turtle
#
# def drawSprite(t,numLeg,leglength):
#     angle=360/numLeg
#     for i in range(numLeg):
#         t.forward(leglength)
#         t.penup()
#         t.forward(-leglength)
#         t.right(angle)
#         t.pendown()
#
#
#
# wn=turtle.Screen()
# alex=turtle.Turtle()
# alex.color("red")
# drawSprite(alex,15,100)
# wn.exitonclick()



#SUM FUNCTION X TO Y

# def sum(n):
#     sum = n*(n+1)/2
#     return sum
# result = sum(10)
# print(result)



#DRAWING STAR
#
# import turtle
# def draw_star(t,lenght,num):
#     for i in range(num):
#         t.forward(lenght)
#         t.left(180-180/num)
# t = turtle.Turtle()
# wn = turtle.Screen()
#
# draw_star(t,100,8)
# wn.exitonclick()



#SUM FUNCTION X TO Y

# def sum(n):
#     total = 0
#     for i in range(1,1+n):
#         total += i
#     return total
# print(sum(10))



#APPROXİMATE THE SQUARE ROOT OF A NUMBER

# def mySqrt(n,t):
#     for i in range(t):
#         old_guess = n / 2
#         new_guess = (1 / 2) * (old_guess + (n / old_guess))
#     return new_guess
#
# print(mySqrt(9,2))



#DRAWING FANCY SQUARE

# import turtle
#
# def drawSprite(t,numLegs,legLength):
#     angle = 360 / numLegs
#     for i in range(numLegs):
#         t.forward(legLength)
#         t.backward(legLength)
#         t.left(angle)
#
# def drawfancySquare(t,sz,lcz,lgl):
#     for i in range(4):
#         t.forward(sz)
#         drawSprite(t,lcz,lgl)
#         t.left(90)
#
# wn = turtle.Screen()
# turtle_pink = turtle.Turtle()
# drawfancySquare(turtle_pink,200,10,80)
# wn.exitonclick()



#CALCULATION

# def calculate(n):
#     if n == 0:
#         return "ZERO"
#     elif n > 0:
#         return "POSİTİVE"
#     elif n < 0:
#         return "NEGATIVE"
#
# print(calculate(-5))



#DRAWING BAR

# def drawBar(t,height,width):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(str(height))
#     t.right(90)
#     t.forward(width)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# height_list = [48,117,200,240,160,260,220]
# maxheight =(height_list)
# numBars = len(height_list)
# border = 10
# wn=turtle.Screen()
# wn.setworldcoordinates(0,0,40,40)
# wn.bgcolor("lightgreen")
# turtle_blue = turtle.Turtle()
# turtle_blue.color("red")
# turtle_blue.pensize(3)
#
# for height in height_list:
#     drawBar(turtle_blue,height,40)
#
# wn.exitonclick()



#CALCULATION OF THE GRADES

# def calculation_grades(mark):
#     if mark >= 90:
#         return "A"
#     elif mark > 80:
#         return "B"
#     elif mark > 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# mark = 50
# print(calculation_grades(mark))



#MODIFYING THE TURTLE BAR

# import turtle
#
# def drawBar(t, height, width):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(str(height))
#     t.right(90)
#     t.forward(width)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# turtle_blue = turtle.Turtle()
# turtle_blue.pensize(3)
#
# turtle_blue.penup()
# turtle_blue.goto(-200, 0)
# turtle_blue.pendown()
#
# height_list = [48,117,200,240,160,260,220]
#
# for height in height_list:
#     if height >= 200:
#         turtle_blue.fillcolor("red")
#     elif height >= 100:
#         turtle_blue.fillcolor("yellow")
#     else:
#         turtle_blue.fillcolor("green")
#
#     drawBar(turtle_blue, height, 40)
#     turtle_blue.forward(10)
#
# wn.exitonclick()



#FINDING HYPOTENUSE

# import math
# def findHpot(a,b):
#     c = math.hypot(a,b)
#     return c
#
# print(findHpot(3,4))



#GUESSING GAME

# import random
#
# target = random.randint(1, 10)
#
# def estimate_number():
#     while True:
#         number = int(input("Enter a number: "))
#         if number < target:
#             print("Too low")
#         elif number > target:
#             print("Too high!")
#         else:
#             print("You guessed the number!")
#             break
# print(estimate_number())



#DRAWING RANDOM 20 STARS

# import turtle
# import random
#
# wn = turtle.Screen()
# wn.bgcolor("black")
# t = turtle.Turtle()
# t.speed(0)
# t.width(2)
#
# colors = ["red","yellow","green","pink","purple","brown"]
#
# def drawStar(size,color):
#     t.color(color)
#     t.begin_fill()
#     for i in range(5):
#         t.forward(size)
#         t.right(144)
#     t.end_fill()
#
# count = 0
# while count < 20:
#
#     x = random.randint(-300, 300)
#     y = random.randint(-250, 250)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#
#     color = random.choice(colors)
#     size = random.randint(15, 50)
#
#     drawStar(size, color)
#
#     count += 1
#
# t.hideturtle()
# turtle.done()



#ODD EVEN NUMBERS

# def is_odd(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
#
# print(is_odd(6))



#LEAP YEAR

# def leap_year(year):
#     leap = False
#     if year%400==0:
#         leap = True
#     elif year%100 ==0:
#         leap = False
#     elif year%4==0:
#         leap = True
#     return leap
#
# print(leap_year(2000))



#TRIANGULAR NUMBERS

# def print_triangular_numbers(n):
#     sum=0
#     for i in range(1,n+1):
#         sum += i
#         print(i,"",sum)
#
# print_triangular_numbers(5)



#PRIME NUMBERS

# def is_prime(n):
#     for i in range(2,n):
#         if n % i ==0:
#             return False
#
#     return True
#
# print(is_prime(25))



#REVERSING STRINGS

# def reverse(text):
#     backwards = ""
#     for char in text:
#         backwards = char + backwards
#     return backwards
# print(reverse("Hello World"))



#REMOVING

# def removes(letter,word):
#     return letter.replace(word,"")
#
# print(removes("Hello", "l"))
# print(removes("banana","a"))
# print(removes("apple","p"))



#ENCRYPTING

# def encrypt(message,cipher):
#     alpha = "abcdefghijklmnopqrstuvyzx"
#     enc_message = ""
#     for i in range(len(message)):
#         if message[i] == " ":
#             enc_message += " "
#
#         else:
#             currentidx = alpha.find(message[i])
#             enc_message += cipher[currentidx]
#
#     return enc_message
#
# cipher = "qwertyuıopasdfghjklzxcvbnm"
# message = "ador"
#
# print(encrypt(message,cipher))



#REMOVING DUPS

# def remove_dups(astring):
#     new_string = ""
#     for i in range (len(astring)):
#         if new_string.find(astring[i]) == -1:
#             new_string += astring[i]
#     return new_string
#
# print(remove_dups("mississippi"))
# print(remove_dups("bookkeeping"))



#ADDING AND REMOVING LIST ITEMS

# my_list = [76, 92.3, 'hello', True, 4, 76]
#
# my_list.append("apple")
# my_list.append(76)
# my_list.insert(3,"cat")
# my_list.insert(0,99)
# hello_index = my_list.index("hello")
# my_list.count(76)
# my_list.remove(76)
#
# index_true = my_list.index(True)
# my_list.pop(index_true)
#
# print(my_list)



#SUM OF THE SQUARE OF THE NUMBERS

# def sum_of_squares(list):
#     total = 0
#     for number in list:
#         total += number * number
#     return total
#
# print(sum_of_squares([2, 3, 4]))



#SUM ALL THE EVEN NUMBERS

# def sum_even_num(list):
#     total = 0
#     for num in list:
#         if num % 2 == 0:
#             total += num
#
#     return  total
#
# print(sum_even_num([0,8,5,7,11,23,16]))



#COUNTING HOW MANY WORDS IN A LIST HAVE 5 LENGTH

# def count_words(list):
#     total = 0
#     for num in list:
#         if len(num) == 5:
#             total += 1
#     return total
#
# my_list = ["apple","lemon","grape","watermelon","orange"]
# print(count_words(my_list))



#SUM THE NUMBER TILL EVEN NUMBER

# def sum_all_num(list):
#     total = 0
#     for num in list:
#         if num %2 ==0:
#             break
#         total += num
#     return total
#
# my_list = [1,3,6,5,7,9,4]
# print(sum_all_num(my_list))



#COUNTING WORDS UNTIL SAM

# def sum_words_num(list):
#     total = 0
#     for word in list:
#         total += 1
#         if word == "sam":
#             break
#     return total
#
# words = ["jack","david","donalt","sam"]
# print(sum_words_num(words))



#RETURNING THE MAX VALUE

# def max(nums):
#     max_value = nums[0]
#
#     for num in nums:
#         if num > max_value:
#             max_value = num
#
#     return max_value
#
# list = [1,2,5,6,7,9]
# print(max(list))

