from Utility import dot
from Utility import norm

def cosine_similarity(query_vector, vector):
    similarity = dot(query_vector, vector) / (norm(query_vector) * norm(vector))
    return similarity