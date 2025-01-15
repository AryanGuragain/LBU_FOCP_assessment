'''Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively: 
Letters that appear in at least one of the two words. 
Letters that appear in both words. 
Letters that appear in either word, but not in both. 
'''
def common_letters(word1, word2):
    return sorted(set(word1) & set(word2))
def unique_letters(word1, word2):
    return sorted(set(word1) ^ set(word2))
def different_letters(word1, word2):
    return sorted(set(word1) ^ set(word2))
print(common_letters('butterfly', 'dragonfly'))
print(unique_letters('butterfly', 'dragonfly'))
print(different_letters('butterfly', 'dragonfly'))
