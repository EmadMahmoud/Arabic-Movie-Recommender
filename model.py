# importing the libraries
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib


def model_func(movie_n):
    # importing the dataset
    data = pd.read_csv("Movies.csv")
    data = data.loc[:, ["اسم الفيلم", "تصنيف الفيلم", "ملخص", "تأليف", "تمثيل", "إخراج"]]

    # data cleaning
    data.isnull().values.any()  # Trying to find null values of the dataframe = True
    naValuesCount = data.isnull().values.any().sum()  # Count the null values =1
    data.dropna(inplace=True)  # Drop all null values

    features = data["إخراج"] + ' ' + data["تمثيل"] + ' ' + data["تأليف"] + ' ' + data["ملخص"] + ' ' + data[
        "تصنيف الفيلم"] + ' ' + data["اسم الفيلم"]

    # Converting the features to features vector
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(features)

    # Finding cosing similarity
    similarity = cosine_similarity(feature_vectors)

    # Getting movie name from the user

    movie_name = movie_n

    movie_desc = data.loc[data["اسم الفيلم"] == movie_name, "ملخص"].tolist()
    list_desc = data["ملخص"].tolist()
    try:
        find_close_match = difflib.get_close_matches(movie_desc[0], list_desc)

        close_match = find_close_match[0]

        index_of_the_movie = data[data["ملخص"] == close_match].index[0]

        # Getting similarity between best match and another rows
        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        # Sorting based on similarity from big sim to small sim
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    except:
        sorted_similar_movies = []

    x = 0
    recommended_movies = []
    for i in sorted_similar_movies:
        index = i[0]
        moviename = data.loc[data.index == index, "اسم الفيلم"].tolist()
        if x < 10:
            try:
                recommended_movies.append(moviename[0])
            except:
                continue
            x += 1

    return recommended_movies





