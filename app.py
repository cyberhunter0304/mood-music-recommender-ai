from fastembed import TextEmbedding
import json
import numpy as np

# Load song dataset
with open("songs.json", "r") as f:
    songs = json.load(f)

# Load embedding model
model = TextEmbedding()

# Precompute song embeddings
song_texts = [s["tags"] for s in songs]
song_embeddings = list(model.embed(song_texts))  # list of vectors

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def recommend_music(mood):
    mood_vector = list(model.embed([mood]))[0]

    # Compute similarity with each song
    similarities = [
        cosine_similarity(mood_vector, song_embeddings[i])
        for i in range(len(songs))
    ]

    # Get top 5 results
    top_indices = np.argsort(similarities)[::-1][:5]

    print("\n🎧 Recommended Songs:\n")
    for idx in top_indices:
        song = songs[idx]
        print(f"- {song['title']} by {song['artist']} (Score: {similarities[idx]:.3f})")

if __name__ == "__main__":
    mood = input("Enter your current mood: ")
    recommend_music(mood)
