import numpy as np

def preprocess(word):
    # NOTE: Can improve this. Some ideas: lemmatization, removing spaces in the middle
    return word.strip().lower()


def levenshtein_distance(str1, str2):
    # Preprocess input strings
    word1 = preprocess(str1)
    word2 = preprocess(str2)

    # Set a matrix of zeros
    size1 = len(word1) + 1
    size2 = len(word2) + 1
    matrix = np.zeros((size1, size2))

    # Fill the initial row and column
    for i in range(size1):
        matrix[i, 0] = i

    for j in range(size2):
        matrix[0, j] = j

    # Fill the rest
    for i in range(1, size1):
        for j in range(1, size2):
            if word1[i-1] == word2[j-1]:
                matrix[i,j] = min(matrix[i-1,j-1], matrix[i-1,j]+1, matrix[i,j-1]+1)
            else:
                matrix[i,j] = min(matrix[i-1,j-1]+1, matrix[i-1,j]+1, matrix[i,j-1]+1)

    # matrix[size1-1,size2-1] should give the minimum number of edits needed from word1 to word2.
    return matrix[size1-1,size2-1], matrix


def top_n_similar_words(target, words, n):
    similarities = []
    for word in words:
        similarities.append((word, levenshtein_distance(target, word)))

    # Sort the words by their simiarities to the target
    similarities_sorted = sorted(similarities,
                                 key = lambda x: x[1],
                                 reverse=True)

    return similarities_sorted[:n]


if __name__ == "__main__":
    word1 = "woman"
    word2 = "man"
    print(levenshtein_distance(word1, word2))