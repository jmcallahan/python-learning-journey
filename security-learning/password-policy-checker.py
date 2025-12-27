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
