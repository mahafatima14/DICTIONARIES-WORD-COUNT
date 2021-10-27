import re

def get_word_count_from_poem(poem_file):
    """Count words in file."""

    poem = open(poem_file)

    poem_dict = {}

    for line in poem:                          #iterate over each line in the filecd
        line = line.rstrip()                            #remove right white space
        word_list = line.split(" ")                  #split each line by |
    
        for i, word in enumerate(word_list):
            word_list[i] = re.sub('[^\w+]', '', word_list[i]).lower()

        for word in word_list:
            poem_dict[word] = poem_dict.get(word, 0) + 1
    
    for word, count in poem_dict.items():
        print(f'{word}: {count}')
            
    return poem_dict


get_word_count_from_poem("twain.txt")




# >>> # Find the ten most common words in Hamlet
# >>> import re
# >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# >>> Counter(words).most_common(10)
# [('the', 1143), ('and', 966), ('to', 762)