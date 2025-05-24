
import streamlit as st
from utils.resume_parser import extract_resume_text
from utils.similarity import compute_similarity
from utils.skill_suggester import extract_skills, find_skill_gaps

st.title("📄 Resume vs 🧾 Job Description Analyzer")

resume_file = st.file_uploader("Upload Your Resume (PDF only)", type=["pdf"])
jd_text = st.text_area("Paste the Job Description")

if resume_file and jd_text:
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())

    resume_text = extract_resume_text("temp_resume.pdf")

    similarity_score = compute_similarity(resume_text, jd_text)
    st.metric("Similarity Score", f"{similarity_score:.2f}")

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    missing_skills = find_skill_gaps(resume_skills, jd_skills)

    st.subheader("🔍 Skill Gap Suggestions")
    if missing_skills:
        st.write("You might want to improve or add these skills:")
        st.write(missing_skills)
    else:
        st.success("✅ Your resume matches most required skills!")
