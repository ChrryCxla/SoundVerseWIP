# Resembles a chat bot, and suggests songs/artists each day.

import random

greetings = ["Hi", "Hello", "Nice to meet you", "Howdy", "Greetings", "Pleased to meet you", "It's good to see you"]
compliments = ["Love the name!", "Gorgeous name.", "What a lovely name!", "Splendid name you've got there.",
               "That's a name I havent heard in a while!", "That name suits you."]
goodbyes = ["Bye now!", "Take care.", "See you next time!", "Have a wonderful day!", "Best wishes.",
            "Goodbye."]
responses = ["Good to know.", "That's lovely!", "Excellent!", "Hmm okay, it's not my first choice personally...",
             "Alrighty! I'm in no place to judge.", "Oooh!", "What a shame, I can't agree with that myself.",
             "Okay, that's something I can get behind!"]


print("Versi: Welcome to SoundVerse. My name is Versi. Lets start by getting to know you.")
print("Versi: What is your name?")
user_name = input("You: ")
print("Versi: " + random.choice(greetings) + " " + str(user_name) + "! " + random.choice(compliments))

user_say = print("Versi: Tell me what day of the month it is, and I will pick you a song for the day. ")
date = int(input("You: "))
if date > 31:
    print("Versi: That's not possible silly! There is a maximum of 31 days in a month.")
    user_say = print("Versi: Tell me what day of the month it is, and I will pick you a song for the day. ")
    date = int(input("You: "))

if date < 1:
    print("That isn't quite right, try again.")
    user_say = print("Versi: Tell me what day of the month it is, and I will pick you a song for the day. ")
    date = int(input("You: "))



def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

print("Versi: Alright " + user_name + "." + " For today, listen to " + random_line('songs.txt') + ".")

print("Versi: Did you like the song?")
input("You: ")

print("Versi: " + random.choice(responses))
print("Versi: Well, that's all for today. " + random.choice(goodbyes))



