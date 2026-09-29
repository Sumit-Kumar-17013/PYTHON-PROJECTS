f = open("C:\\Users\sumit\\OneDrive\\Desktop\\Python\\Projects\\[09] Madlibs Generator\\story.txt" , "r")
data = f.read()

words = set()
start_words = -1

target_start = "<"
target_ends =  ">"

for i, char in enumerate(data):
    if char == target_start:
        start_words = i

    if char == target_ends and target_start != -1:
        word = data[start_words: i + 1 ]
        words.add(word)
        start_words = -1

answers = {}

for word in words:
    answer = input("enter a word for " + word + ":")
    answers[word] = answer

for word in words:
    data = data.replace(word , answers[word])

print(data)
