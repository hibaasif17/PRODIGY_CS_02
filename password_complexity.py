import re
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "letmein", "monkey",
    "iloveyou", "admin", "welcome", "12345", "1234", "1q2w3e4r", "password1",
    "qwerty123", "12345678", "sunshine", "princess", "football", "123123",
    "dragon", "passw0rd", "password123", "123321" }

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    common_password_criteria = password in COMMON_PASSWORDS
    strength_score = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                          digit_criteria, special_char_criteria])

    if common_password_criteria or strength_score < 3:
        strength = "Weak"
        feedback = ("Your password is weak. Consider using at least 8 characters, "
                    "including upper and lower case letters, numbers, and special characters. "
                    "Avoid using common passwords.")
    elif strength_score == 3:
        strength = "Moderate"
        feedback = ("Your password is moderate. Try to include more variety, "
                    "such as upper case letters and special characters.")
    else:
        strength = "Strong"
        feedback = "Your password is strong. Good job!"
    return strength, feedback

if __name__ == "__main__":
    while True:
        password = input("Enter a password to assess its strength: ")
        strength, feedback = assess_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        print(feedback)

        try_again = input("\nDo you want to try another password? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thank you for using the password strength checker!")
            break
