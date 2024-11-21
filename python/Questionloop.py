# age = int(input ("enter the age:"))
# if age < 13:
#     print("You are a child.")
#     print("You can play with toys.")

# elif age >= 13 and age <= 19:
#     print("You are a teenager.")
#     print("You can play video games.")
# elif age >= 19 and age <=60:
#     print("You are an adult.")
#     print("You can do whatever you want.")


# Question2

# age = int(input ("enter the age :"))
# day = int(input ("enter the day :"))
# if day == wednesday or day == thursday:
#     print("It's a weekend. You can buy ticket of 10$")
# if age >=18:
#     print("You are 18. you can buy ticket of 12$")

# elif age <=13 and   age <=18:
#     print("You are under 18. you can buy ticket of 8$")
# else:
#     print("You haven't selected correct option")

# question3

# age = 26
# day = "wednesday"

# price = 12 if age >= 18 else 8

# if day == "wednesday":
#     price = price-2
    

# print("ticket price for you is $",price)

# question 4

# score = int(input ("enter your marks: "))
# if score >=90:
#     print("You have got A grade verry well done ")
# elif score >=75:
#     print("You have got B grade well done ")
# elif score >=60:
#     print("You have got C grade keep it up ")
# elif score >=45:
#     print("You have got D grade you need to work hard ")
# else:
#     print("You have got F grade better luck next time ")


# question5
# fruit = str(input("Enter the color of the fruit: "))

# if fruit == "red":
#     print("The fruit is apple")

# elif fruit == "yellow":
#     print("The fruit is banana")

# elif fruit == "green":
#     print("The fruit is grapes")

# elif fruit == "orange":
#     print("The fruit is orange")

# else:
#     print("I don't know that fruit")

# question 6

# wheather = str(input(("enter the wheather: ")))

# if wheather == "rainy":
#     print("It's raining outside. You should bring an umbrella.")

# elif wheather == "sunny":
#     print("It's sunny outside. You can enjoy your day.")

# elif wheather == "cloudy":
#     print("It's cloudy outside. You should take your umbrella with you.")

# elif wheather == "cold":
#     print("It's cold outside. You should wear a coat and hat.")
# else:
#     print("I don't know that weather")


# question 7

# Choose_mode_of_transport = int(input(("Enter the distance you wanted to travel: ")))

# if Choose_mode_of_transport <= 100:
#     print("You can take a bus for 50% less cost than a car.")
# elif Choose_mode_of_transport <= 3:
#     print("You can walk for 100% less cost than a car.")
# elif Choose_mode_of_transport <= 10 or Choose_mode_of_transport >=15:
#     print("You can take a bike for 70% less cost than a car.")
# elif Choose_mode_of_transport >= 30:
#     print("You can take a car ")
# else:
#     print("I don't know that distance")

# question 8

# order_size = "medium" 
# extra_shot = True
# if extra_shot:
#     coffee = order_size + "coffee with an extra shot"
# else:  
#     coffee = order_size + "coffee"

# print("order: ",coffee)

# question 9

# password checker

# password = input("Enter your password: ")

# if len(password) < 8:
#     print("Password should be at least 8 characters long.")

# elif not any(char.isdigit() for char in password):
#     print("Password should contain at least one digit.")

# elif not any(char.isalpha() for char in password):
#     print("Password should contain at least one letter.")

# elif not any(char.isupper() for char in password):
#     print("Password should contain at least one uppercase letter.")

# elif not any(char.islower() for char in password):
#     print("Password should contain at least one lowercase letter.")

# question 9
# leap year or not

# year = int(input("enter the year you want to check : "))
# if year < 0:
#     print("Invalid year")
#     exit()

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")