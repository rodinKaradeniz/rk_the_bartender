import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity

# Sample DataFrame
data = {'CocktailName': ['Margarita', 'Martini', 'Cosmopolitan'],
        'Ingredients': [['Tequila', 'Triple Sec', 'Lime Juice'],
                        ['Gin', 'Vermouth'],
                        ['Vodka', 'Triple Sec', 'Cranberry Juice']]}

cocktail_df = pd.read_csv('db/csv/processed/cocktails.csv')

# Using MultiLabelBinarizer to create a binary matrix
mlb = MultiLabelBinarizer()
X = pd.DataFrame(mlb.fit_transform(cocktail_df['ingredients']), columns=mlb.classes_, index=cocktail_df.index)

# Autoencoder architecture
input_dim = X.shape[1]  # Number of ingredients
encoding_dim = 32  # You can adjust this dimension based on experimentation

input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Training the autoencoder
autoencoder.fit(X, X, epochs=50, batch_size=64, shuffle=True)

# Extracting the encoded representations for cocktails
encoder = Model(inputs=input_layer, outputs=encoded)
encoded_cocktails = encoder.predict(X)

# Calculate cosine similarity between a specific cocktail and all others
cocktail_name = "White Russian"
cocktail_index = cocktail_df[cocktail_df['cocktail_name'] == cocktail_name].index[0]
similarities = cosine_similarity(encoded_cocktails, encoded_cocktails[cocktail_index].reshape(1, -1))

# Get indices of top N most similar cocktails
N = 10 # Number of recommendations
top_n_indices = np.argsort(similarities.flatten())[::-1][:N]

# Displaying the top N recommended cocktails
recommended_cocktails = cocktail_df['cocktail_name'].iloc[top_n_indices].tolist()[1:]
print(f"Top {N} recommended cocktails for {cocktail_df['cocktail_name'].iloc[cocktail_index]}: {recommended_cocktails}")
