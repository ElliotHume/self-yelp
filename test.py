from vocabulary import Vocabulary
from collections import Counter
review = ["The", "pizza", "is", "excellent", ".", "The", "wine", "is", "not", "."]
count = Counter(review)
print(count)
vocabulary = Vocabulary(count)
print(vocabulary)
print(vocabulary.encode(review))
print(vocabulary.decode(vocabulary.encode(review)))