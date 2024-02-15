#Question 4: Capitalize words
def capitalize_letter(sentence):
    words = sentence.split()
    capitalize_words = [word.capitalize()for word in words]
    capitalized_sentence = ''.join(capitalize_words)
    return capitalized_sentence
input_string = input("Enter a string")
result = capitalize_letter(input_string)
print ("Result", result)