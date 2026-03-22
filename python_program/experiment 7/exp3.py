paragraph = input("Enter a paragraph: ")
words = paragraph.split()
print("List of words:", words)
word_count = len(words)
print("Number of words:", word_count)
palindrome_count = 0
for word in words:
    w = word.lower()
    if w == w[::-1]:
        palindrome_count += 1
print("Number of palindrome words:", palindrome_count)
print("Words in reverse order:")
for word in words:
    print(word[::-1])