# password validator

import re

# Validate password based on specific criteria
def validate_password(password, min_length=8, weak_password=None) :
    # list to append error messages
    errors =[]

    # validate password length
    if len(password) < min_length :
        errors.append(f"Password length must br at least {min_length} characters")

    # validate password for lower case inclusions
    if not re.search(r'[a-z]', password):
        errors.append(f"Password must contain at least a lowercase")

    # validate password for upper case inclusions
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least an upper case letter")

    # validate password for special characters
    if not re.search(r"[r'[!@#$%^&*(),.?:{}|<>]", password):
        errors.append("Password must contain at least one special character")

    # check against weak passwords
    if weak_password and password in weak_password :
        errors.append("Password is weak")

    return {
        "is_valid": not errors,
        "errors": errors
    }

# script to prompt user and validate password

def main():
    # List of common passwords
    common_passwords = ["password", "iloveyou", "password123", "qwerty123","noname123"]
    
    print("Password validator")
    print("-" * 30)

    password = input("Enter your password: ")
    result = validate_password(password, weak_password=common_passwords)

    if result ["is_valid"] :
        print("Your password is valid and strong")
    else:
        print("Your password is invalid:")
        for error in result["errors"]:
            print(f"- {error}")

if __name__ == "__main__":
    main()