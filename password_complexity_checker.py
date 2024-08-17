import re
def password_complexity(password):
    if len(password) < 8:
        return "Password is too short, it should be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password should have at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password should have at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Password should have at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should have at least one special character."
    return "Password is strong."
password = input("Enter a password to check its complexity: ")
result = password_complexity(password)
print(result)