'''One approach to analysing some encrypted data where a substitution is suspected is frequency analysis. A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters. In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text. 
Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same. 
Hint: There are many ways to do this. It is obviously a dictionary, but we will want zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so best to ignore that initially, and then check the usual resources for the runes. 
'''
def analyze_frequency(text):
    char_counts = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch in char_counts:
                char_counts[ch] += 1
            else:
                char_counts[ch] = 1

    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    top_six = sorted_chars[:6]

    print("Top six most frequent letters:")
    for char, freq in top_six:
        print(f"'{char}': {freq}")

text_input = "She sells seashells by the seashore"
analyze_frequency(text_input)