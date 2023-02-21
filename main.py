import art
from game_data import data
import random
from replit import clear

def decide():
  user_choice = ""
  user_choice = input("Who has more followers? Type 'A' OR 'B': ").lower()
  if follower_count1 > follower_count2:
    return user_choice == "a"
  elif follower_count1 < follower_count2:
    return user_choice == "b"
  else:
    return False
    
def format(rand_data):
  name  = rand_data['name']
  description = rand_data['description']
  country = rand_data['country']
  return f"{name}, {description}, {country}"

count = 0 
logo = art.logo
first_choice = random.choice(data)
Second_choice = random.choice(data)
follower_count1 = first_choice['follower_count']
while follower_count1 == Second_choice['follower_count']:
  Second_choice = random.choice(data)
  if follower_count1 != Second_choice['follower_count']:
    break
QA = format(first_choice)
QB = format(Second_choice)
follower_count2 = Second_choice['follower_count']

if follower_count1 != follower_count2:
  print(logo)
  print(f"Compare A: {QA}")
  print(art.vs)
  print(f"Against A: {QB}")
  x = decide()
  while x == True:
    clear()
    print(logo)
    count += 1
    print(f"You're right! Current Score : {count}")
    QA  = QB
    follower_count1= follower_count2
    Second_choice = random.choice(data)
    QB = format(Second_choice)
    print(f"Compare A: {QA}")
    print(art.vs)
    print(f"Compare B: {QB}")
    x = decide()
  if x  == False:
    clear()
    print(art.logo)
    print(f"Sorry That's Wrong! Final Score = {count}")