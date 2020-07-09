
def no_dups(s):
    # Your code here
    seen = {}
    words = s.split()
    output = []
    for word in words:
        if word not in seen:
            seen[word] = True
            output.append(word)
    return ' '.join(output)
    
#     s = [x.strip(' ') for x in s]
#     s = ' '.join([str(x) for x in s])
    
    
#     no_dupe = [] 
#     for i in s: 
#         if i not in no_dupe: 
#             no_dupe.append(i) 
#     return no_dupe
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))