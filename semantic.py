import spacy

nlp = spacy.load('en_core_web_md')

# Creating a vector for each word.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Creating a vector for each word.
word4 = nlp("frog")
word5 = nlp("toad")
word6 = nlp("dog")


# Comparing the similarity of the words.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Comparing the similarity of the words.
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# Creating a vector for each word.
tokens = nlp('cat apple monkey banana fruit kitten')
# Iterating through the tokens.
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana",
             "Hey, my cat is on top of the car"]

# Creating a vector for the sentence.
model_sentence = nlp(sentence_to_compare)

# Comparing the similarity of the sentences.
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)



'''
What I found interesting about the monkey and banana example is that Spacy allows grouping by categories 
and associations. Then when I tasted frogs, toads and dogs, he found that frogs and toads are almost the same.
'''

'''
I noticed that en_core_web_md has a lot more details and information than web_sm which is more 
on similarities at the surface level.
'''
