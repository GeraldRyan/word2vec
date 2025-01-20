import numpy as np
import random
from collections import defaultdict
import itertools

# Example corpus
corpus = [["the", "cat", "sat", "on", "the", "mat"],
          ["the", "dog", "barked", "at", "the", "cat"]]

# Build vocabulary and word-to-index mapping
def build_vocab(corpus):
    word_freq = defaultdict(int)
    for sentence in corpus:
        for word in sentence:
            word_freq[word] += 1
    vocab = {word: i for i, (word, _) in enumerate(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))}
    return vocab, {i: word for word, i in vocab.items()}

vocab, idx_to_word = build_vocab(corpus)
vocab_size = len(vocab)
print(vocab)
print(idx_to_word)

