import datetime
# day three of learning python

current_year = datetime.datetime.now().year
name = 'Jason Callahan'
birth_day = '8th'
birth_month = 'March'
birth_year = 1983
age = current_year - birth_year
current_mood = 'a-okay, baby!'

# trying to figure out how to get current_year pull to calculate age from day, month, and year of birth
# added some comments to help myself figure out what I was doing and trying to achieve when I come back to this...
# Oh, look! I figured out f-strings!  Neat!:

print("hissss....")
print("I am a snake!")
print("You are not a snake!")
print(f"I am {name} and I am {age} years old.")
print(f"My birthday is on the {birth_day} day of {birth_month} of the year {birth_year} of the muthafuckin' lerd!")
print("Hail to the king, baby!")
print(f"and right meow, I am feeling {current_mood}")
print("alright, meow I'm outtie!")
print("hissss....")


access_granted = age >= 18
print(f"Access granted? {access_granted}")
if access_granted:
    print("Hey! Look at that level, access granted homie! "
          "Welcome to the secret lair of Hephastos!"
          )
else:
    print("You are are too young! "
          "Sorry, loser. You gotta be at least 18 years old to enter the lair of Hephastos."
          )
    
# old code below, before I learned about f-strings
# print("hissss....")
# print("I am a snake!")
# print("You are not a snake!")
# print("I am " + name + " and I am " + str(age) + " years old.")
# print("My birthday is on the " + birth_day + " day of " + birth_month + " of the year " + str(birth_year) + " of the muthafuckin' lerd!")
# print("Hail to the king, baby!")
# print("and right meow, I am feeling " + current_mood)
# print("alright, meow I'm outtie!")
# print("hissss....")
# ---
