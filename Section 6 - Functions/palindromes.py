def palindrome_sentence(s):
    clean_string = ""

    for letter in s:
       if letter.isalpha():
           clean_string += letter

    if clean_string.lower() == clean_string[::-1].lower():
        return "Is a palindrome"
    
    else:
        return "Is not a palindrome"

print(palindrome_sentence("Sow WOS"))