from datetime import date
# day three of learning python

name = 'Jason Callahan'
birth_day = 8
birth_month = 3
birth_year = 1983
current_mood = "alive, thrivin' and fired-up, baby!"
birth_date = date(birth_year, birth_month, birth_day)

# look! I grouped all my functions together for better readability!
# new learning - function to calculate age
def calculate_age(birth_date):
    """
    Calculate age based on birth date against system timestamp.
    
    :param birth_date: The birth date as a date object.
    :return: Age in years as an integer.
    """
    today = date.today()
    age = today.year - birth_date.year -(
    (today.month, today.day) < (birth_date.month, birth_date.day)
    )
     
    return age
age = calculate_age(birth_date)

# new learning - function to get ordinal suffix for day and year
def ordinal_suffix(day):
    """
    Turns day into ordinal string for print output.
    
    :param day: Turns day into ordinal string
    :return: Ordinal string representation of the day
    """
    if 11 <= day <= 13:
        return 'th'
    last_digit = day % 10
    if last_digit == 1:
        return 'st'
    elif last_digit == 2:
        return 'nd'
    elif last_digit == 3:
        return 'rd'
    else:
        return 'th'
day = str(birth_day) + ordinal_suffix(birth_day)
today_day = str(date.today().day) + ordinal_suffix(date.today().day)

def get_ordinal_year(year):
    """
    Turns year into ordinal string for print output.
     
    Yes, I know years aren't typically represented this way in modern english, 
    and that it's egregious, but I did for the funsies of it. :P
 
    :param year: Year as an integer
    :return: Ordinal string representation of the year
    """
    return str(year) + ordinal_suffix(year % 100)
year = get_ordinal_year(birth_year)


# new learning - function to get month name from month integer
def get_month_name(month):
    """
    Turns month integer into month name string for print output.
    
    :param month: Month as an integer (1-12)
    :return: Month name as a string
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_names.get(month, "")
month = get_month_name(birth_month)
today_month = get_month_name(date.today().month)

# new learning - function to determine if access is granted based on age
def is_access_granted(age):
    """
    Function to determine if access is granted based on age.
    
    :param age: Validates if age is 18 or older
    :return: True if age is 18 or older, False otherwise
    """
    return age >= 18
access_granted = is_access_granted(age) 

# oh, look! I figured out f-strings!  Neat!:
# how do I skip lines in the output for readability? is it really just "print()"" with nothing in it?
# also, is it a normal convention to type comments in all lowercase, for the consistency of coding?

print()
print("hissss....")
print()
print("I am a snake!")
print("You are not a snake!")
print()
print(f"I am {name} and I am {age} years old.")
print(f"My birthday is on the {day} day of {month} of the {year} year of the muthafuckin' lerd!")
print("Hail to the king, baby!")
print(f"and right meow, on {today_month}, {today_day}, of {date.today().year}, I am feeling {current_mood}")
print("alright, meow I'm outtie!")
print()
print("hissss....")
print()
print(f"Access granted? {access_granted}")
print()
if access_granted:
    print("Hey! Look at that level, access granted homie! ")
    print("Welcome to the secret lair of Hephastos!")
else:
    print("You are are too young!")
    print("Sorry, loser. You gotta be at least 18 years old to enter the lair of Hephastos.")
    print()
    
# <--------- Notes on old code below ---------->

# Before I learned about f-strings
# print("hissss....")
# print("I am a snake!")
# print("You are not a snake!")
# print("I am " + name + " and I am " + str(age) + " years old.")
# print("My birthday is on the " + birth_day + " day of " + birth_month + " of the year " + str(birth_year) + " of the muthafuckin' lerd!")
# print("Hail to the king, baby!")
# print("and right meow, I am feeling " + current_mood)
# print("alright, meow I'm outtie!")
# print("hissss....")

# access_granted = age >= 18

# This is the old code that was replaced by the more efficient function that calculated the ordinal year 
# using the previously defined ordinal_suffix function for days. 
# Removed for the obvious heinous crime of redundancy.
# new learning - function to get ordinal year
# def get_ordinal_year(year):
#     """
#     Turns year into ordinal string for print output.
 
#     Yes, I know years aren't typically represented this way in modern english, 
#     and that it's egregious, but I did for the funsies of it. :P

#     :param year: Year as an integer
#     :return: Ordinal string representation of the year
#     """
#     if 11 <= year % 100 <= 13:
#         return str(year) + 'th'
#     last_digit = year % 10
#     if last_digit == 1:
#         return str(year) + 'st'
#     elif last_digit == 2:
#         return str(year) + 'nd'
#     elif last_digit == 3:
#         return str(year) + 'rd'
#     else:
#         return str(year) + 'th'    
# year = get_ordinal_year(birth_year)
# ---
