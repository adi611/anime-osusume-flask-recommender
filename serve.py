import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import bz2
from urllib.request import urlopen


def anime_recommend_api(user_input, rec_type):
    with open("similarity.pkl", "rb") as file:
        similarity = pickle.load(file)
    with open("data.pkl", "rb") as file:
        data = pickle.load(file)

    print('from serve.py')
    
    # data = bz2.BZ2File('data.pbz2', 'rb')
    # data = pickle.load(data)
    
    # similarity = bz2.BZ2File('similarity.pbz2', 'rb')
    # similarity = pickle.load(similarity)

    print(user_input)
    print(data[data["Name"] == user_input])
    Index_of_anime = data[data["Name"] == user_input].index[0]
    Similarity_score = similarity[Index_of_anime]
    Sorted_scores = sorted(list(enumerate(Similarity_score)),
                           reverse=True, key=lambda x: x[1])[1:]
    Recommended_Anime = []
    for i in Sorted_scores:
        if data.iloc[i[0]].Rank > 2000:
            continue
        if len(Recommended_Anime) > 5:
            break
        if rec_type is None:
            Recommended_Anime.append(data.iloc[i[0]].Name)
        elif data.iloc[i[0]].Type == rec_type:
            Recommended_Anime.append(data.iloc[i[0]].Name)
    return Recommended_Anime

    # print(Recommender("Jujutsu Kaisen", "Movie"))


# anime_recommend_api()
