import random
# NOTE: This project was done out of boredom.
# This code should in no way be used to generate your random passwords in todays world. 
# A strong password in todays world would be around 10 characters, not 8. Computers are becoming more powerful.
# Don't use this code to generate your passwords.

# Upper Case Letters
upperCaseLetter1 = chr(random.randint(65,90))
upperCaseLetter2 = chr(random.randint(65,90))

# Lower Case Letters
lowerCaseLetter1 = chr(random.randint(97,122))
lowerCaseLetter2 = chr(random.randint(97,122))

# Digits
dig1 = chr(random.randint(48, 57))
dig2 = chr(random.randint(48, 57))

# Special Characters
specchar1 = chr(random.randint(33, 38))
specchar2 = chr(random.randint(33, 38))

password = upperCaseLetter1 + upperCaseLetter2 + lowerCaseLetter1 + lowerCaseLetter2 + dig1 + dig2 + specchar1 + specchar2
print(password)
