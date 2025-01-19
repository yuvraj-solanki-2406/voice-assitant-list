import pickle

# load model and vectorizer
with open("notebooks/random_forest.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("notebooks/vectorizer.pkl", "rb") as vect_file:
    vectorizer = pickle.load(vect_file)


# function to find category
def put_in_category(item: str):
    item_vect = vectorizer.transform([item])
    response = model.predict(item_vect)
    return list(response)[0]


if __name__ == "__main__":
    txt = "bananas"
    print(put_in_category(txt))