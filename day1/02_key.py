words = ['pottery', 'jazz', 'zumba']

print(max(words))
# Prediction:
# Actual:

print(max(words, key=lambda word: len(word)))
# Prediction:
# Actual:

print(sorted(words))
# Prediction:
# Actual:

print(sorted(words, key=lambda word: len(word)))
# Prediction:
# Actual:

print(sorted(words, key=lambda word: len(word), reverse=True))
# Prediction:
# Actual:


# Replace each None with one call to min(), max(), or sorted() that uses key=lambda ...

# 1. The shortest word → 'jazz'
shortest = None
print(shortest)

# 2. The words sorted by their last letter → ['zumba', 'pottery', 'jazz']
by_last_letter = None
print(by_last_letter)

# 3. The word with the most z's → 'jazz'   (hint: 'banana'.count('a') gives 3)
most_zs = None
print(most_zs)
