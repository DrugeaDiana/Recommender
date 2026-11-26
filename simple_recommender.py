import pandas as pd

# Importing database
metadata = pd.read_csv('../movies_metadata.csv', low_memory=False)

def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']
    # Using the IMDB formula
    return (v / (v+m) * R) + (m/(m+v) * C)

# quick check to see if it's there
#print(metadata.head(3))

# Mean of vote average collumn
C = metadata['vote_average'].mean()
print(C)

# Minimum number of votes required to be in the chart, m
m = metadata['vote_count'].quantile(0.90)
print(m)

# All Qualified movies in a new DataFrame
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
print(q_movies.shape)

q_movies['score'] = q_movies.apply(weighted_rating, axis = 1)
q_movies = q_movies.sort_values('score', ascending = False)

# Print top 15
print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(15))
