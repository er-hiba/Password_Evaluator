# Function to count the number of lowercase letters in the password
def C_lowercase(password):
    counter = 0
    for char in password :
        if char >= "a" and char <= "z" :
            counter += 1
    return counter

# Function to count the number of uppercase letters in the password
def C_uppercase(password):
    counter = 0
    for char in password :
        if char >= "A" and char <= "Z" :
            counter += 1
    return counter

# Function to count the number of non-alphabetic characters in the password
def not_letter(password):
    return len(password) - C_lowercase(password) - C_uppercase(password)

# Function to find the longest consecutive sequence of uppercase letters
def longest_uppercase_sequence(password):
    longest_sequence = ""
    current_sequence = ""
    
    for char in password:
        if char.isupper():
            current_sequence += char
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = ""
    
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    
    return longest_sequence


# Function to find the longest consecutive sequence of lowercase letters
def longest_lowercase_sequence(password):
    longest_sequence = ""
    current_sequence = ""
    
    for char in password:
        if char.islower():
            current_sequence += char
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = ""
    
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    
    return longest_sequence

# Function to calculate the password score based on bonus and penalty criteria
def score(password):
    
    bonus = len(password)*4 + (len(password) - C_uppercase(password))* 2 \
            + (len(password) - C_lowercase(password))* 3 + not_letter(password) * 5

    penalty = len(longest_uppercase_sequence(password)) * 2\
              + len(longest_lowercase_sequence(password)) * 2

    # Calculate the final score by subtracting the penalty from the bonus
    return bonus - penalty

# Get user input for the password
password = input("Enter a password: ")

# Display password statistics
print("The number of characters in this password is:", len(password))
print("The number of lowercase characters in this password is:", C_lowercase(password))
print("The number of uppercase characters in this password is:", C_uppercase(password))
print("The number of non-alphabetic characters in this password is:", not_letter(password))
print("The longest uppercase sequence is:", longest_uppercase_sequence(password))
print("The longest lowercase sequence is:", longest_lowercase_sequence(password))

# Calculate and display the password score and strength assessment
print("The score is:", score(password))
if score(password) < 20:
    print("The password is very weak")
elif score(password) >= 20 and score(password) < 40 :
    print("The password is weak")
elif score(password) >= 40 and score(password) <= 80 :
    print("The password is strong")
else:
    print("The password is very strong")
