words = {
    "python": "A high-level programming language.",
    "dictionary": "A collection of key-value pairs.",
    "variable": "A named storage location in memory."
}
word = input("Enter a word: ")
if word in words:
    print(f"The meaning of '{word}' is: {words[word]}")
else:
    print("Word not found.")