"""
dict searching is O(1), list searching iterates from the beginning to end
Question
You are given words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word.
"""

# use list 
# one list stores input words, the other stores the occurance
word_list = []
word_count = []
N = int(input())
for i in range(N):
    word = input()
    try:
        ind = word_list.index(word)
        word_count[ind] += 1
    except:
        word_list.append(word)
        word_count.append(1)
        
print(len(word_list))
print(*word_count)


# use dict
# words as key, values is tuples storing order and occurance
word_list = {}
N = int(input())
for i in range(N):
    word = input()
    occur = word_list.get(word, (0,0))
    word_list[word] = (occur[0], occur[1] + 1) if occur != (0,0) else (i,1) 
    
nums = word_list.values()
final = sorted(nums, key=lambda m : m[0])
result = [i[1] for i in final]
print(len(result))
print(*result)
