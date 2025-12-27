# Python Learning Journey

A chronicle of my Python programming learning as part of my career transition into IT and Cybersecurity.

## About This Repository

This is a **learning repository** that documents my progression from Python beginner to competent programmer. You'll see:
- Early code that's rough and basic
- Progressive improvement over time (that's the plan right?!)
- Learning notes and discoveries
- Projects increasing in complexity

**Start Date:** December 22, 2025  
**Learning Path:** Self-directed study + any other free to veteran resources I can muster up

## Current Focus

- Python fundamentals (syntax, data structures, control flow)
- File I/O and text processing
- Basic scripting for IT automation
- Security-focused applications

## Background

I'm a U.S. Navy veteran (QM2, 2003-2007) and former Rivian operations leader transitioning into IT/Cybersecurity. This repository is part of my broader learning portfolio which includes:

- **Certifications:** Microsoft SC-900 (Dec 2025), AWS CCP, ISC2 CC, CompTIA A+/Net+/Sec+/CySA+ (in progress)
- **Education:** B.A.A.S. in Cybersecurity, Eastern Illinois University (Est. May, 2027)
- **Other repos:**
  - [About Me and TIL repo](https://github.com/jmcallahan/jmcallahan)
  - [Home Lab Notes and Progress](https://github.com/jmcallahan/HomeLab)

## Structure
```
/basics/          # Fundamental syntax and exercises
/projects/        # Small scripts and utilities
/notes/           # TIL (Today I Learned) entries
/challenges/      # Coding challenges and solutions
```
<!-- for holding any copy-paste stuff for daily notes  -->

## Progress Log

<details>
  <summary><h3>12.27.2025</h3></summary>
  
#### Progress notes:
  -  Started freecodecamp.org python course to augment learning curve.
  -  Depending less on the VScode suggestions to tell me what to do.
  -  
  -  Tightened code on [password-policy-checker.py](https://github.com/jmcallahan/python-learning-journey/blob/main/security-learning/password-policy-checker.py) to [security-learning](https://github.com/jmcallahan/python-learning-journey/tree/main/security-learning) folder (see below). 
#### What I learned today:
  -  Dove deeper into functions and global variables vs local variables
#### Code

```python
import hashlib
import secrets
import string

# Example usage of check_policy function
users = [
    {"username": "alice", "password": "Password123!"},
    {"username": "bob", "password": "weak"},
    {"username": "charlie", "password": "Str0ng!Pass"},
    {"username": "diana", "password": "nospecialchar1"},
    {"username": "eve", "password": "ALLCAPS123!"},
    # Add 10 more users with varying password strengths
]

def check_policy(password):
    """ 
    Check if a password meets policy requirements:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character e.g., !@#$%^&*()
    """
    special_chars = "!@#$%^&*()?"
    checks = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(c in special_chars for c in password),
    }
    
    return all(checks.values()), checks

def generate_strong_password(length=12):
    """
    Generate a strong password that meets the policy requirements.
    """
    # define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()?"

    # ensure at least one character from each required type is present
    strong_password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special_chars),
    ]
    # fill the rest of the password length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    strong_password += [secrets.choice(all_chars) for _ in range(length - 4)]
    # shuffle the resulting password list to avoid predictable patterns
    secrets.SystemRandom().shuffle(strong_password)
    return ''.join(strong_password)

for user in users:
    username = user["username"]
    password = user["password"]
    
    is_valid, results = check_policy(password)
    
    print(f"\nUser: {username}")
    print(f"Password: {password}")
    print(f"Valid: {is_valid}")
    
    if is_valid:
        # Hash the password for storage
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Hashed Password: {hashed_password}")
    else:
        print(f"Failed checks: {[check for check, passed in results.items() if not passed]}")
        # Generate a new password for this user
        strong_password = generate_strong_password()
        is_valid_new, results_new = check_policy(strong_password)
        hashed_password_new = hashlib.sha256(strong_password.encode()).hexdigest()
        print(f"Generated Password: {strong_password}")
        print(f"Generated Password Is Valid: {is_valid_new}")
        print(f"Hashed Password: {hashed_password_new}")      
```
#### Next Steps
  - Will continue to work through the Cisco PCEP course along with the freecodecamp.org course to get a better understanding
  -
  - Will continue to peruse YouTube videos on topics while on the treadmill or stationary bike to keep learning via immersion osmosis high.

</details>
---
<details>
  <summary><h3>12.26.2025</h3></summary>
  
#### Progress notes:
  -  Getting a better grasp on variables, loops and defining what goes where.
  -  Depending less on the VScode suggestions to tell me what to do, and telling them what I want to do.
  -  Added [security-learning](https://github.com/jmcallahan/python-learning-journey/tree/main/security-learning) folder.
  -  Added [password-policy-checker.py](https://github.com/jmcallahan/python-learning-journey/blob/main/security-learning/password-policy-checker.py) to [security-learning](https://github.com/jmcallahan/python-learning-journey/tree/main/security-learning) folder.
#### What I learned today:
  -  Looping checks and generating strong passwords and hashing passwords once they pass checks.
#### Code

```python
import hashlib
import secrets
import string

# Example usage of check_policy function
users = [
    {"username": "alice", "password": "Password123!"},
    {"username": "bob", "password": "weak"},
    {"username": "charlie", "password": "Str0ng!Pass"},
    {"username": "diana", "password": "nospecialchar1"},
    {"username": "eve", "password": "ALLCAPS123!"},
    # Add 10 more users with varying password strengths
]

def check_policy(password):
    """ 
    Check if a password meets policy requirements:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character e.g., !@#$%^&*()
    """
    special_chars = "!@#$%^&*()?"
    checks = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(c in special_chars for c in password),
    }
    
    return all(checks.values()), checks

print("Password Policy Checker")
print("-" * 40)

for user in users:
    username = user["username"]
    password = user["password"]
    
    is_valid, results = check_policy(password)
    
    print(f"\nUser: {username}")
    print(f"Password: {password}")
    print(f"Valid: {is_valid}")

    if is_valid:
        #hash the password for storage
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Hashed Password: {hashed_password}")

def generate_strong_password(length=12):
    """
    Generate a strong password that meets the policy requirements.
    """
    # define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()?"

    # ensure at least one character from each required type is present
    strong_password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special_chars),
    ]
    # fill the rest of the password length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    strong_password += [secrets.choice(all_chars) for _ in range(length - 4)]
    # shuffle the resulting password list to avoid predictable patterns
    secrets.SystemRandom().shuffle(strong_password)
    return ''.join(strong_password)

for user in users:
    username = user["username"]
    password = user["password"]
    
    is_valid, results = check_policy(password)
    
    print(f"\nUser: {username}")
    print(f"Password: {password}")
    print(f"Valid: {is_valid}")
    
    if is_valid:
        # Hash the password for storage
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Hashed Password: {hashed_password}")
    else:
        print(f"Failed checks: {[check for check, passed in results.items() if not passed]}")
        # Generate a new password for this user
        strong_password = generate_strong_password()
        is_valid_new, results_new = check_policy(strong_password)
        hashed_password_new = hashlib.sha256(strong_password.encode()).hexdigest()
        print(f"Generated Password: {strong_password}")
        print(f"Generated Password Is Valid: {is_valid_new}")
        print(f"Hashed Password: {hashed_password_new}")    
```
#### Next Steps
  - Will continue to work through the Cisco PCEP course along with the freecodecamp.org course to get a better understanding
  - Will continue to peruse YouTube videos on topics while on the treadmill or stationary bike to keep learning via immersion osmosis high.

</details>
---
<details>
  <summary><h3>12.25.2025</h3></summary>
  
#### Progress notes:
  -  Ayo! Look who's learning python!
  -  Learning to write variables a little cleaner.
  -  While this doesn't initially feel like a lot of progress, I realized that understanding why certain variable react in specfic ways is important.
  -  Also, order matters, you can't print the boolean for "Access granted" if you haven't defined what granted the access.
  -  Dropped old code for variable print strings into comments for version documentation. Will remove from future iterations.
  -  Added [basics](https://github.com/jmcallahan/python-learning-journey/tree/main/basics) folder.
  -  Added [python-day-2.py](https://github.com/jmcallahan/python-learning-journey/blob/main/basics/python-day-2.py) to [basics](https://github.com/jmcallahan/python-learning-journey/tree/main/basics) folder.
#### What I learned today:
  -  Using f-strings to fill variable gaps in a cleaner fasion
  -  How to define one variable by calculating an argument on antoher. e.g.: access_granted becomes a boolean of the age variable if age is greater than or equal to 18
  -  Multi-line print returns inside the same print function
#### Code

```python
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
```
#### Next Steps
  - Will continue to work through the Cisco PCEP course along with the freecodecamp.org course to get a better understanding
  - Will continue to peruse YouTube videos on topics while on the treadmill or stationary bike to keep learning via immersion osmosis high.

</details>
---
<details>
  <summary><h3>12.24.2025</h3></summary>
  
#### Progress notes:
  -  Dug into variables a bit
#### What I learned today:
  -  Variables are case sensitive
  -  How to add notes, who knew programmers were the real hashtag O.G.s? Step aside Paris Hilton.
#### Code

```python
import datetime
# day two of learning python


name = 'Jason Callahan'
birth_day = '8th'
birth_month = 'March'
birth_year = 1983

# trying to figure out how to get current_year to populate automatically
# current_year = datetime.datetime.now().year
# pull current year from system clock and compute age

current_year = datetime.datetime.now().year
age = current_year - birth_year

# trying to figure out how to get age to calculate automatically based on birth_year
# age = current_year - birth_year

current_mood = 'a-okay, baby!'

print("hissss....")
print("I am a snake!")
print("You are not a snake!")
print("I am " + name + " and I am " + str(age) + " years old.")
print("My birthday is on the " + birth_day + " day of " + birth_month + " of the year " + str(birth_year) + " of the muthafuckin lerd!")
print("Hail to the king, baby!")
print("and right meow, I am feeling " + current_mood)
print("alright, meow I'm outtie!")
print("hissss....")

# added some comments to help myself figure out what I was doing and trying to achieve when I come back to this...
```
#### Next Steps
  - Will continue to work through the Cisco PCEP course along with the freecodecamp.org course to get a better understanding
  - Will continue to peruse YouTube videos on topics while on the treadmill or stationary bike to keep learning via immersion osmosis high.

</details>
---
<details>
  <summary><h3>12.22.2025</h3></summary>
  
#### Progress notes:
  - Repository created
#### What I learned today:
  - Slightly faster repo setup
#### Code

```python
print("Hello, world!")
```
#### Next Steps
  - Learn about variables and data types
  - Explore basic operators

</details>

---
  <p>**Note:** This is a learning repository. Code quality improves over time by design.</p>
  
---
<!---


## **Why This README Matters**

✅ **Sets expectations** - "This is learning code, not production code"  
✅ **Shows intentionality** - You're not randomly dabbling, you have a plan  
✅ **Demonstrates context** - Navy vet + ops leader + structured transition  
✅ **Signals progression** - You're documenting growth, not faking expertise  
✅ **Professional framing** - Organized, dated, structured

**Recruiters will see:** "This person is serious about learning, documents their work, and understands professional development."

## **Post-Creation: First Commit Strategy**

**After you create the repo, your first few commits should be:**

1. **Initial README** (auto-created)
2. **Create directory structure:**

mkdir basics projects notes challenges
--->
