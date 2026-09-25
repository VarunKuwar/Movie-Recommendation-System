import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from .database import Movie

def get_recommendations(session: Session, movie_id: int, top_n: int = 5):
    # Fetch all movies from database
    movies = session.query(Movie).all()
    if not movies:
        return []

    # Convert to pandas DataFrame
    movies_data = [
        {
            "id": m.id,
            "title": m.title,
            "genre": m.genre or "",
            "director": m.director or "",
            "actors": m.actors or "",
            "description": m.description or "",
            "poster_url": m.poster_url or ""
        }
        for m in movies
    ]
    df = pd.DataFrame(movies_data)

    # Check if movie_id exists in our dataset
    if movie_id not in df['id'].values:
        return []

    # Create a combined features column
    # Weighting: Description is important, but Genre, Director, and Actors define the style.
    df['combined_features'] = df['genre'] + " " + df['director'] + " " + df['actors'] + " " + df['description']
    df['combined_features'] = df['combined_features'].fillna('')

    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])

    # Compute Cosine Similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Find the index of the requested movie
    idx = df.index[df['id'] == movie_id].tolist()
    if not idx:
        return []
    idx = idx[0]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top n most similar movies (excluding itself)
    sim_scores = sim_scores[1:top_n + 1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    similarity_values = [i[1] for i in sim_scores]

    # Return top N similar movies with their similarity score
    recommended_movies = []
    for count, i in enumerate(movie_indices):
        movie_dict = df.iloc[i].to_dict()
        movie_dict['similarity_score'] = similarity_values[count]
        recommended_movies.append(movie_dict)

    return recommended_movies
