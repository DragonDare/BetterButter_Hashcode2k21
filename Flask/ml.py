# code
import numpy as np
import pandas as pd
import requests
import bs4
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

import warnings


def generate_model():
    warnings.simplefilter(action='ignore', category=FutureWarning)

    ratings = pd.read_csv("C:\\Users\\Chairman APGB\\Downloads\\ratings.csv")
    ratings.head()

    topics = pd.read_csv("C:\\Users\\Chairman APGB\\Downloads\\topics.csv")
    topics.head()

    n_ratings = len(ratings)
    n_topics = len(ratings['topicId'].unique())
    n_users = len(ratings['userId'].unique())

    # print(f"Number of ratings: {n_ratings}")
    # print(f"Number of unique topicId's: {n_topics}")
    # print(f"Number of unique users: {n_users}")
    # print(f"Average ratings per user: {round(n_ratings / n_users, 2)}")
    # print(f"Average ratings per topic: {round(n_ratings / n_topics, 2)}")

    user_freq = ratings[['userId', 'topicId']].groupby('userId').count().reset_index()
    user_freq.columns = ['userId', 'n_ratings']
    user_freq.head()

    # Find Lowest and Highest rated topics:
    mean_rating = ratings.groupby('topicId')[['rating']].mean()
    # Lowest rated topics
    lowest_rated = mean_rating['rating'].idxmin()
    topics.loc[topics['topicId'] == lowest_rated]
    # Highest rated topics
    highest_rated = mean_rating['rating'].idxmax()
    topics.loc[topics['topicId'] == highest_rated]
    # show number of people who rated topics rated topic highest
    ratings[ratings['topicId'] == highest_rated]
    # show number of people who rated topics rated topic lowest
    ratings[ratings['topicId'] == lowest_rated]

    ## the above topics has very low dataset. We will use bayesian average
    topic_stats = ratings.groupby('topicId')[['rating']].agg(['count', 'mean'])
    topic_stats.columns = topic_stats.columns.droplevel()

    # Now, we create user-item matrix using scipy csr matrix
    from scipy.sparse import csr_matrix

    def create_matrix(df):
        N = len(df['userId'].unique())
        M = len(df['topicId'].unique())

        # Map Ids to indices
        user_mapper = dict(zip(np.unique(df["userId"]), list(range(N))))
        topic_mapper = dict(zip(np.unique(df["topicId"]), list(range(M))))

        # Map indices to IDs
        user_inv_mapper = dict(zip(list(range(N)), np.unique(df["userId"])))
        topic_inv_mapper = dict(zip(list(range(M)), np.unique(df["topicId"])))

        user_index = [user_mapper[i] for i in df['userId']]
        topic_index = [topic_mapper[i] for i in df['topicId']]

        X = csr_matrix((df["rating"], (topic_index, user_index)), shape=(M, N))

        return X, user_mapper, topic_mapper, user_inv_mapper, topic_inv_mapper

    X, user_mapper, topic_mapper, user_inv_mapper, topic_inv_mapper = create_matrix(ratings)

    from sklearn.neighbors import NearestNeighbors

    """
    Find similar topics using KNN
    """

    def find_similar_topics(topic_id, X, k, metric='cosine', show_distance=False):
        neighbour_ids = []

        topic_ind = topic_mapper[topic_id]
        topic_vec = X[topic_ind]
        k += 1
        kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
        kNN.fit(X)
        topic_vec = topic_vec.reshape(1, -1)
        neighbour = kNN.kneighbors(topic_vec, return_distance=show_distance)
        for i in range(0, k):
            n = neighbour.item(i)
            neighbour_ids.append(topic_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids

    topic_titles = dict(zip(topics['topicId'], topics['title']))

    topic_id = 7

    similar_ids = find_similar_topics(topic_id, X, k=10)
    topic_title = topic_titles[topic_id]

    print(f"Since you followed {topic_title}")
    ALL_TOPICS = list()
    ALL_RATINGS = list()
    for i in similar_ids:
        ALL_TOPICS.append(str(topic_titles[i]))
        ALL_RATINGS.append(str(i))
        # print(topic_titles[i], i)
    return ALL_TOPICS, ALL_RATINGS


def web_scrape(query, limit):
    # text = "geeksforgeeks"
    url = 'https://google.com/search?q=' + query
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    heading_object = soup.find_all('a')
    TAGS = list()
    for info in heading_object:
        href = info["href"]
        if href.startswith('/url?q='):
            TAGS.append(href.lstrip('/url?q='))
    return TAGS[0:limit]
