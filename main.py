#Imports
import random
from bs4 import BeautifulSoup
import requests
import datetime 
import calendar  




## Instructions ##

"""
This is a chatbot that will intiate a conversation with
the user. The bot will ask the user various questions, which can be seen
in the questions array. 


"""
## End of Instructions ##

## Greeting/Introduction Phase ##

# Make an array of jokes and choose a random one to tell the user
def joke():
  jokes = ["Why did the kid throw his clock out the window? Because he wanted to see time fly!", "Why are fish so smart? Because they live in schools!", "Where do polar bears keep their money? In a snow bank!", "Why did the pony get sent to his room? He wouldn’t stop horsing around!"]
  joke_choice = random.choice(jokes)
  print(joke_choice)

# Define the function age which will tell the user which day they were born on 
def age():
  age = input("Please input your birthday in the form of dd mm yyyy ")
  
  #from GeeksForGeeks (https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/) (This function will find which day the user was born on)
  def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

  print(f"According to your birthdate, that means you were born on {findDay(age)}")

# Define the function color which will tell a user a fun fact about their favorite color. If the color isn't in the list, the bot will simply say that color is their favorite too
def color():
  favorite_color = input(questions[2] + " ")
  
  colors = {
    "red": "Red makes things appear closer than they really are.",
    "orange": "Orange was a symbol of glory and fruits of the earth in early Christian church and was also known as the wisdom ray.",
    "yellow": "Yellow is the best color to create enthusiasm for life and can awaken greater confidence and optimism.",
    "green": "In China, green jade represents virtue and beauty",
    "blue": "Blue is the favored color choice for toothbrushes.",
    "purple": "Carrots used to be purple, now most are orange!",
    "black": "The color black represents strength, seriousness, power, and authority.",
    "white": "The color white is cleanliness personified, the ultimate in purity!! This is why it is traditionally worn by western brides, and the reason why doctors wear white jackets.",
    "pink": "The color pink is symbolizes joy and happiness."
  }

  for key in colors:
    if(key == favorite_color.lower()):
      print(colors[key])
    
  else:
    print(f"{favorite_color} is my favorite color too!")

def greeting():
  greeting = input("How are you doing today? ")

  good_responses = ["well", "good", "fantastic", "ok"]
  bad_responses = ["bad", "not so well", "horrible", "sad", "unhappy"]

  for x in good_responses:
    if x == greeting.lower():
      print("I'm glad to hear that!")

  
  for x in bad_responses:
    if x == greeting.lower():
      print("I'm sorry to hear that. Hopefully, this bot can make your day better!")
  


def hobbies():
  hobbies = input("What is your favorite hobby? ")

  print(f"{hobbies} is very interesting!")

def food():
  food = input("What is your favorite food? ")
  
  print(f"{food} is a great food!")




# Detects to see if the user would like to end the conversation
stop_conversation = "0"
# Choose a random question from this array to ask the user 
questions = ["Would you like to hear a joke?", "How old are you?", "What is your favorite color?", "How are you?", "What are your hobbies?", "What is your favorite food?"]

# Chooses a random element from the array to ask the user
bot_choice = random.choice(questions)

print("Hello I am chatbot!")
while(stop_conversation != "1"):

  if(bot_choice == questions[0]):
    joke()
    break

  if (bot_choice == questions[1]):
    age()
    break

  if (bot_choice == questions[2]):
    color()
    break
  
  if (bot_choice == questions[3]):
    greeting()
    break
  
  if (bot_choice == questions[4]):
    hobbies()
    break
  
  if (bot_choice == questions[5]):
    food()
    break






