
import spacy
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    return list(set([chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]))

def find_skill_gaps(resume_skills, jd_skills):
    return [skill for skill in jd_skills if skill not in resume_skills]
