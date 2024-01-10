# Make recommendations based on contents-.

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('db/csv/processed/cocktails.csv')

vectorizer = CountVectorizer(tokenizer=lambda x: x.split(', '))

ingredient_matrix = vectorizer.fit_transform(df['ingredients'].apply(', '.join))

cosine_sim = cosine_similarity(ingredient_matrix, ingredient_matrix)

def recommend_cocktails(cocktail_name: str, cosine_sim=cosine_sim):
    cocktail_index = df[df['cocktail_name'] == cocktail_name].index[0]
    sim_scores = list(enumerate(cosine_sim[cocktail_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get the top 5 similar cocktails

    cocktail_indices = [i[0] for i in sim_scores]
    return df['cocktail_name'].iloc[cocktail_indices]

# def recommend_cocktails(ingredients: list[str], cosine_sim=cosine_sim):
#     pass

recommendations = recommend_cocktails('White Russian')
print(recommendations)

