def double(n):
    return n * 2

double_lambda = lambda n: n * 2

print(double(5))
# Prediction:
# Actual:

print(double_lambda(5))
# Prediction:
# Actual:


def word_length(word):
    return len(word)

word_length_lambda = lambda word: len(word)

print(word_length('pottery'))
# Prediction:
# Actual:

print(word_length_lambda('pottery'))
# Prediction:
# Actual:


shout = lambda message: message.upper()

print(shout('doors open at 7'))
# Prediction:
# Actual:


# Replace each None with a lambda, then uncomment the print lines and run.

# 1. last_letter('jazz') gives 'z'
last_letter = None
# print(last_letter('jazz'))

# 2. is_long('pottery') gives True, is_long('jazz') gives False
is_long = None
# print(is_long('pottery'))
# print(is_long('jazz'))
