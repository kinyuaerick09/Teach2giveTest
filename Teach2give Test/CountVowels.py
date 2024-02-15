def countvowels(sentence):
    vowels = "aeiouAEIOU"
    count=0
    for char in sentence:
        for vowel in vowels:
            if char == vowel:
                count+=1
                break
    return count

print(countvowels("hello erick"))        