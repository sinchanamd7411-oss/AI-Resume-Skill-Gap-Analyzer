from pdfminer.high_level import extract_text
import re

def extract_resume_text(file_path):
    text = extract_text(file_path)
    return text.lower()

def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    return text

skills_list = [
    "python","java","machine learning","deep learning",
    "sql","html","css","javascript","react","aws",
    "docker","kubernetes","linux","excel","powerbi",
    "pandas","numpy"
]

def extract_skills(text):

    detected_skills = []

    for skill in skills_list:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills