# app/utils/recommend.py

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
        place_categories = place['categories']
        place_activities = place['activities']

        place_category_embeddings = compute_embeddings(place_categories)
        place_activity_embeddings = compute_embeddings(place_activities)

        category_sim = max([semantic_similarity(t_emb, p_emb) for t_emb in user_category_embeddings for p_emb in place_category_embeddings], default=0)
        activity_sim = max([semantic_similarity(t_emb, p_emb) for t_emb in user_activity_embeddings for p_emb in place_activity_embeddings], default=0)

        total_similarity = (category_sim + activity_sim) / 2
        recommendations.append({
            'place': place,
            'similarity': total_similarity
        })

    recommendations.sort(key=lambda x: x['similarity'], reverse=True)
    return recommendations

# Define test data
users = [
    {
        'id': 1,
        'categories': ['rocks'],
        'activities': ['swimming']
    }
]

places = [
    {
        'name': 'Sigiriya',
        'categories': ['rocks', 'history'],
        'activities': ['climbing', 'sightseeing']
    },
    {
        'name': 'Hanthana Mountain',
        'categories': ['mountains', 'nature'],
        'activities': ['hiking', 'bird watching']
    },
    {
        'name': 'Yala National Park',
        'categories': ['wildlife', 'nature'],
        'activities': ['safari', 'bird watching']
    },
    {
        'name': 'Mirissa Beach',
        'categories': ['beach', 'water'],
        'activities': ['swimming', 'whale watching']
    },
    {
        'name': 'Galle Fort',
        'categories': ['history', 'architecture'],
        'activities': ['sightseeing', 'shopping']
    },
    {
        'name': 'Ella Rock',
        'categories': ['hiking', 'nature'],
        'activities': ['climbing', 'photography']
    },
    {
        'name': 'Kandy Lake',
        'categories': ['nature', 'water'],
        'activities': ['boating', 'relaxing']
    },
    {
        'name': 'Pidurangala Rock',
        'categories': ['rocks', 'hiking'],
        'activities': ['climbing', 'sightseeing']
    },
    {
        'name': 'Udawalawe National Park',
        'categories': ['wildlife', 'nature'],
        'activities': ['safari', 'photography']
    },
    {
        'name': 'Bentota Beach',
        'categories': ['beach', 'water'],
        'activities': ['swimming', 'water sports']
    },
    {
        'name': 'Horton Plains',
        'categories': ['nature', 'mountains'],
        'activities': ['hiking', 'bird watching']
    },
    {
        'name': 'Adam\'s Peak',
        'categories': ['mountains', 'pilgrimage'],
        'activities': ['hiking', 'climbing']
    },
    {
        'name': 'Dambulla Cave Temple',
        'categories': ['mountains', 'architecture'],
        'activities': ['sightseeing', 'pilgrimage']
    },
    {
        'name': 'Arugam Bay',
        'categories': ['beach', 'surfing'],
        'activities': ['surfing', 'relaxing']
    },
    {
        'name': 'Polonnaruwa',
        'categories': ['history', 'ruins'],
        'activities': ['sightseeing', 'photography']
    },
    {
        'name': 'Kitulgala',
        'categories': ['water', 'adventure'],
        'activities': ['white water rafting', 'hiking']
    },
    {
        'name': 'Nuwara Eliya',
        'categories': ['nature', 'tea plantations'],
        'activities': ['sightseeing', 'golf']
    },
    {
        'name': 'Wilpattu National Park',
        'categories': ['wildlife', 'nature'],
        'activities': ['safari', 'bird watching']
    },
    {
        'name': 'Trincomalee',
        'categories': ['beach', 'historical'],
        'activities': ['swimming', 'sightseeing']
    },
    {
        'name': 'Negombo Beach',
        'categories': ['beach', 'fishing'],
        'activities': ['swimming', 'fishing']
    },
]


# Test the recommendation system
def test_recommendation_system():
    user = users[0]
    recommendations = recommend_places(user['categories'], user['activities'], places)
    print("Recommendations for user with ID:", user['id'])
    for rec in recommendations:
        print(f"Place: {rec['place']['name']}, Similarity: {rec['similarity']}")

# Run the test
if __name__ == "__main__":
    test_recommendation_system()
