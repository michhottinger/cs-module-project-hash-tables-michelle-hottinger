
# from nltk.tokenize import word_tokenize
# from spacy.attrs import ORTH, NORM
# from spacy.tokenizer import Tokenizer
# from spacy.lang.en import English
# nlp = English()

import re
    



def word_count(s):
        # Create a blank Tokenizer with just the English vocab
#     tokenizer = Tokenizer(nlp.vocab)
#     # remove all tokens that are not alphabetic
#     case = [{ORTH: "doesn\'t"}]
#     tokenizer.add_special_case("doesn\'t", case)
#     # remove all tokens that are not alphabetic
#     tokens = word_tokenize(s)
    

#'":;,.-+=/\\|[]{}()*^&'

    s = s.translate(str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.lower()
    
    words = s.split()
    print(words)
    #words = [word for word in escaped if word.isalpha()] won't work bc only letters
#     words = [word.lower() for word in escaped]
      
    
    
    
    freq = {}
    for item in words:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
#     for key, value in freq.items():
    return freq
  
             
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))