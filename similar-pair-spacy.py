import spacy
import warnings
warnings.filterwarnings('ignore')

#nlp = spacy.load('en')
nlp = spacy.load('en_core_web_lg')

print("Enter space-separated words")
words = input()

tokens = nlp(words)

for token in tokens:
    # Printing the following attributes of each token.
    # text: the word string, has_vector: if it contains
    # a vector representation in the model,
    # vector_norm: the algebraic norm of the vector,
    # is_oov: if the word is out of vocabulary.
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)

#token1, token2, token3 = tokens[0], tokens[1], tokens[2], tokens[3]

#print("Similarity:", token1.similarity(token2))
sim = 0

for i in range(len(tokens)):
    for j in range(i+1, len(tokens)):
        temp = tokens[i].similarity(tokens[j])
        if temp > sim:
            sim = temp
            pair = [tokens[i], tokens[j]]

print('The pair is:', pair)
