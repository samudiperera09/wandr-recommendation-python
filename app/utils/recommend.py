from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cosine_sim

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def compute_embeddings(items):
    embeddings = model.encode(items)
    return embeddings

def semantic_similarity(vec1, vec2):
    return cosine_sim([vec1], [vec2])[0][0]

def recommend_places(user_categories, user_activities, places):
    user_category_embeddings = compute_embeddings(user_categories)
    user_activity_embeddings = compute_embeddings(user_activities)

    recommendations = []
    for place in places:
        place_categories = place.categories
        place_activities = place.activities

        place_category_embeddings = compute_embeddings(place_categories)
        place_activity_embeddings = compute_embeddings(place_activities)

        category_sim = max([semantic_similarity(t_emb, p_emb) for t_emb in user_category_embeddings for p_emb in place_category_embeddings], default=0)
        activity_sim = max([semantic_similarity(t_emb, p_emb) for t_emb in user_activity_embeddings for p_emb in place_activity_embeddings], default=0)

        total_similarity = (category_sim + activity_sim) / 2
        recommendations.append({
            'place_id': place.id,
            'place_name': place.name,
            'similarity': total_similarity
        })

    recommendations.sort(key=lambda x: x['similarity'], reverse=True)
    return recommendations
