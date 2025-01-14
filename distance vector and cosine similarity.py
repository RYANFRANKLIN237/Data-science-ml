import numpy as np
from scipy.spatial.distance import cosine

#data
text1_words = ['when', 'was', 'the', 'a', 'of', 'dead', 'in', 'at', 'torn', 'fields', 'you', 'fell', 'things', 'rest', 'and', 'either', 'file', 'dreams', 'soft', 'say']
text1_frequencies = [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1]

text2_words = ['when', 'was', 'the', 'a', 'of', 'dead', 'in', 'at', 'torn', 'fields', 'you', 'fell', 'things', 'rest', 'and', 'either', 'file', 'dreams', 'soft', 'say']
text2_frequencies = [0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]

text3_words = ['when', 'was', 'the', 'a', 'of', 'dead', 'in', 'at', 'torn', 'fields', 'you', 'fell', 'things', 'rest', 'and', 'either', 'file', 'dreams', 'soft', 'say']
text3_frequencies = [0, 0, 2, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]

# dictionaries to store word frequencies for each text file
text1_freq_dict = {word: freq for word, freq in zip(text1_words, text1_frequencies)}
text2_freq_dict = {word: freq for word, freq in zip(text2_words, text2_frequencies)}
text3_freq_dict = {word: freq for word, freq in zip(text3_words, text3_frequencies)}

#list of unique words from all documents
all_words = set(text1_freq_dict.keys()) | set(text2_freq_dict.keys()) | set(text3_freq_dict.keys())

#vectors for each document
vectors = []
for document in [text1_freq_dict, text2_freq_dict, text3_freq_dict]:
    vector = []
    for word in all_words:
        vector.append(document.get(word, 0))  # Get frequency or 0 if not present
    vectors.append(vector)

# Converting vectors to NumPy arrays
vectors = np.array(vectors)

# Calculating cosine similarities
similarity_matrix = np.zeros((len(vectors), len(vectors)))

for i in range(len(vectors)):
    for j in range(len(vectors)):
        if i == j:
            similarity_matrix[i, j] = 1.0  # Cosine similarity of a vector with itself is 1
        else:
            similarity_matrix[i, j] = 1 - cosine(vectors[i], vectors[j])


#specific similarities:
similarity_1_2 = similarity_matrix[0, 1]
similarity_1_3 = similarity_matrix[0, 2]
similarity_2_3 = similarity_matrix[1, 2]

print("Similarity between text1 and text2:", similarity_1_2)
print("Similarity between text1 and text3:", similarity_1_3)
print("Similarity between text2 and text3:", similarity_2_3)



