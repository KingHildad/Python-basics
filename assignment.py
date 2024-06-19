# a python program that prompts you to enter a letter then checks whether it is a consonant or a vowel
def check_vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"

    if len(letter) == 1 and letter.isalpha():
        if letter in vowels:
            return f"The letter '{letter}' is a vowel."
        else:
            return f"The letter '{letter}' is a consonant."
    else:
        return "Please enter a single alphabetical character."

input_letter = input("Enter a letter: ")

result = check_vowel_or_consonant(input_letter)
print(result)



#encaplusation......simple python program to demonstrate encapsulation in OOP.

