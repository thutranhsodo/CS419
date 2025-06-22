import nltk
import json
import numpy as np
import pickle
import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens_lower = [word.lower() for word in tokens]
    cleaned_tokens = [re.sub(r'[^A-Za-z]+', '', word) for word in tokens_lower]
    cleaned_tokens = [word for word in cleaned_tokens if word]
    stop_words = set(stopwords.words('english'))
    tokens_no_stopwords = [word for word in cleaned_tokens if word not in stop_words]
    porter_stemmer = PorterStemmer()
    stemmed_tokens = [porter_stemmer.stem(word) for word in tokens_no_stopwords]
    return stemmed_tokens


def load_resources():
    tfidf_matrix = np.load("tfidf_matrix.npy")
    labels = np.load("labels.npy")
    with open("metadata.json", encoding="utf-8") as f:
        metadata = json.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("knn_model.pkl", "rb") as f:
        knn_model = pickle.load(f)
    return tfidf_matrix, metadata, vectorizer, knn_model, labels

def search(query, top_k=10):
    tfidf_matrix, metadata, vectorizer, knn_model, labels = load_resources()

    query_proc = preprocess_text(query)
    query_vec = vectorizer.transform([query_proc]).toarray()

    cate_pred = knn_model.predict(query_vec)[0]

    same_cate_indices = np.where(labels == cate_pred)[0]
    tfidf_same_cate = tfidf_matrix[same_cate_indices]
    similarities = cosine_similarity(query_vec, tfidf_same_cate)[0]

    top_indices_local = similarities.argsort()[-top_k:][::-1]
    top_indices_global = same_cate_indices[top_indices_local]

    results = []
    for idx in top_indices_global:
        result = metadata[idx].copy()
        result["score"] = round(cosine_similarity(query_vec, [tfidf_matrix[idx]])[0][0], 4)
        results.append(result)
    return results


# if __name__ == "__main__":
#     print("🔍 CNN News Search Engine")
#     query = input("Enter your search query: ")
#     results = search(query)
#     print(f"\nTop results for: {query}\n")
#     for r in results:
#         print(f"→ {r['title']}\n  Category: {r['cate']} | Score: {r['score']}\n  Link: {r['source_url']}\n")

