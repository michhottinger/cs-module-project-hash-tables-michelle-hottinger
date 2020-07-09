
from nltk.tokenize import word_tokenize
from spacy.attrs import ORTH, NORM
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
nlp = English()
    



def word_count(s):
        # Create a blank Tokenizer with just the English vocab
    tokenizer = Tokenizer(nlp.vocab)
    # remove all tokens that are not alphabetic
    case = [{ORTH: "doesn't"}]
    tokenizer.add_special_case("doesn't", case)
    # remove all tokens that are not alphabetic
    tokens = word_tokenize(s)
    words = [word for word in tokens if word.isalpha()]
    words = [word.lower() for word in words]
    
    
    
    
    freq = {}
    for item in words:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        return freq
  
             
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))