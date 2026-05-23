#to count vowels and consonants in a string and digits in a string
def count(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1

    return vowel_count, consonant_count, digit_count
# Example usage
string = input("Enter a string: ")
vowels, consonants, digits = count(string)
print(f'Vowels: {vowels}')
print(f'Consonants: {consonants}')
print(f'Digits: {digits}')