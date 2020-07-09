import random

#UPER
#create table in which word one is key and values are word after
#next step will be to combine values into lists associated with key
#once table is made, choose a random start word
#print the text of key and values to a string.
#create a stop word based on punctuation or something


# Read in all the words in one go

with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

cache = {}
words = words.lower().strip().split()
for i in range(len(words)-1):
    key = words[i]
    if key not in cache:
        # print(True)
        cache[key] = [words[i+1]]
    else:
        # print(False)
        cache[key].append(words[i+1])

# TODO: construct 5 random sentences
# Your code here

sentences = [str()]*5
paragraph = str()

for i in range(len(sentences)):
    word_item = random.choice(
        [word for word in words if word[0] == "\"" or word[0].isupper()])
    while True:
        sentences[i] += f"{word_item} "
        if word_item[-1] in [".", "?", "!"]:
            cap = sentences[i][1:].capitalize()
            sentences[i] = f"\"{cap}"
            paragraph += f"{sentences[i].strip()}\" "
            break
        word_item = random.choice(cache[word_item])
        
print(paragraph)
