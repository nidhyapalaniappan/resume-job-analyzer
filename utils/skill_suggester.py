import spacy
import subprocess
import sys

# Load spaCy model with fallback to auto-download if not found
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")


def extract_skills(text):
    """Extract skill-like noun phrases from the given text using spaCy."""
    doc = nlp(text)
    return list(set([
        chunk.text.lower()
        for chunk in doc.noun_chunks
        if len(chunk.text.split()) <= 3
    ]))


def find_skill_gaps(resume_skills, jd_skills):
    """Compare extracted skills and return the missing ones."""
    return [skill for skill in jd_skills if skill not in resume_skills]

