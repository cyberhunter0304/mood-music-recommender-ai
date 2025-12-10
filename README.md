# 🎵 Mood-Based Music Recommender (AI + NLP)

A simple but powerful AI project that analyzes your mood through natural language and recommends the best matching song using **sentence embeddings**.

## 🚀 How It Works

1. User enters a mood description (e.g., “I feel energetic”, “I’m sad today”)
2. AI model (`all-MiniLM-L6-v2`) converts the input into a semantic vector
3. We compare the meaning with vectors of predefined songs
4. The closest match is recommended instantly

This project demonstrates:
- **Semantic Embeddings**
- **Vector Similarity Search (Cosine Similarity)**
- **Lightweight NLP Pipeline**
- **Practical AI Application without heavy LLMs**

---

## 🧠 Tech Stack

- Python 3.10+
- Sentence Transformers (`all-MiniLM-L6-v2`)
- PyTorch (CPU)
- NumPy
- Flask (optional for API version)

---

## 🗂 Project Structure

