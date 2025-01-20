import pickle
import pandas as pd

new_df = pd.read_csv("data/new_df.csv")

# load model and vectorizer
with open("data/knn.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("data/vectorizer.pkl", "rb") as vect_file:
    vectorizer = pickle.load(vect_file)


# recommend the products
def recommend(item: str):
    item_vector = vectorizer.transform([item])
    distances, indices = model.kneighbors(item_vector, n_neighbors=5)

    lst = []
    for item in indices[0][:2]:
        lst.append(new_df.iloc[item]['product_name'])

    return lst
