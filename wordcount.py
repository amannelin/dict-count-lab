
poem = open('test.txt')   
word_counts = {}
    
for line in poem:
    words = line.rstrip().split(" ")
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
    


