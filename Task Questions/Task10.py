#Input a paragraph, and let Python find letter count, word count, and repeated words with their counts

# Letter count
letter_count = len(paragraph.replace(" ", ""))

# Word count
word_count = len(paragraph.split())

# Repeated words with their counts
word_counts = {}
for word in paragraph.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("Letter count:", letter_count)
print("Word count:", word_count)
print("Repeated words with their counts:")
for word, count in word_counts.items():
    if count > 1:
        print(f"{word}: {count}")
