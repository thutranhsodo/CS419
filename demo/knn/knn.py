import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

X = np.load("tfidf_matrix.npy")
y = np.load("labels.npy")

# Train KNN
model = KNeighborsClassifier(n_neighbors=6)
model.fit(X, y)

# Save model
with open("knn_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("KNN model saved to knn_model.pkl")
