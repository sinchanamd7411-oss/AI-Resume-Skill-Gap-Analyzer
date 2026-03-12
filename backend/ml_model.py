from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_skills):

    documents = [resume_text, job_skills]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity_score = cosine_similarity(matrix[0:1], matrix[1:2])

    return similarity_score[0][0] * 100