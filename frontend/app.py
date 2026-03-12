import streamlit as st
import pandas as pd
import sys
import os
import plotly.graph_objects as go
from reportlab.pdfgen import canvas

# backend path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
from skill_extractor import extract_resume_text, clean_text, extract_skills

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ---------- SIMPLE DARK STYLE ----------
st.markdown("""
<style>

.stApp {
    background-color: #F0FFFF;
    color: black;
}

/* card container */
.card {
    background-color: #F0FFFF;
    padding:20px;
    border-radius:12px;
}

/* skills found */
.skill {
    background-color: green;
    padding:8px;
    border-radius:6px;
    margin:4px;
    text-align:center;
    color:white;
}

/* missing skills */
.missing {
    background-color: red;
    padding:8px;
    border-radius:6px;
    margin:4px;
    text-align:center;
    color:white;
}

/* buttons */
button {
    background-color: navy;
    color: transparent;
}

/* remove white background from widgets */
div[data-testid="stFileUploader"]{
    background-color: transparent;
}

section.main > div{
    background-color: transparent;
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("AI Resume Analyzer")
menu = st.sidebar.radio("Navigation", ["Home","Resume Analyzer","About"])

# ---------- HOME ----------
if menu == "Home":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("AI Resume Skill Gap Analyzer")

    st.write("""
This AI tool analyzes resumes and compares them with job skill requirements.

Features:
• Skill extraction from resume  
• Skill gap detection  
• Resume ATS score  
• Radar skill chart  
• Learning recommendations  
• Resume improvement suggestions  
• Job role prediction  
• PDF report download
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ANALYZER ----------
elif menu == "Resume Analyzer":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset", "job_dataset.csv"))
    df = pd.read_csv(dataset_path)

    job_role = st.selectbox("Select Job Role", df["Job Role"])

    if uploaded_file:

        with open("temp_resume.pdf","wb") as f:
            f.write(uploaded_file.getbuffer())

        resume_text = extract_resume_text("temp_resume.pdf")
        resume_text = clean_text(resume_text)

        resume_skills = extract_skills(resume_text)

        job_skills = df[df["Job Role"]==job_role]["Skills"].values[0]
        job_skill_list = job_skills.split(",")

        matched_skills = list(set(job_skill_list) & set(resume_skills))
        missing_skills = list(set(job_skill_list) - set(resume_skills))

        score = (len(matched_skills)/len(job_skill_list))*100

        # ---------- ATS SCORE ----------
        st.subheader("Resume ATS Score")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Resume Score"},
            gauge={
                'axis': {'range':[0,100]},
                'bar':{'color': "blue"},
                'steps':[
                    {'range':[0,40],'color': "red"},
                    {'range':[40,70],'color': "orange"},
                    {'range':[70,100],'color': "green"}
                ]
            }
        ))

        st.plotly_chart(fig,use_container_width=True)

        col1,col2 = st.columns(2)

        # ---------- SKILLS FOUND ----------
        with col1:
            st.subheader("Skills Found")
            for skill in matched_skills:
                st.markdown(f'<div class="skill">{skill}</div>', unsafe_allow_html=True)

        # ---------- MISSING SKILLS ----------
        with col2:
            st.subheader("Missing Skills")
            for skill in missing_skills:
                st.markdown(f'<div class="missing">{skill}</div>', unsafe_allow_html=True)

        # ---------- RADAR CHART ----------
        st.subheader("Skill Radar Chart")

        values=[]
        for skill in job_skill_list:
            if skill in matched_skills:
                values.append(1)
            else:
                values.append(0)

        radar=go.Figure()

        radar.add_trace(go.Scatterpolar(
            r=values,
            theta=job_skill_list,
            fill='toself'
        ))

        radar.update_layout(
            polar=dict(radialaxis=dict(visible=True,range=[0,1])),
            showlegend=False
        )

        st.plotly_chart(radar,use_container_width=True)

        # ---------- JOB ROLE PREDICTION ----------
        st.subheader("Predicted Job Role")

        role_scores={}
        for index,row in df.iterrows():
            skills=row["Skills"].split(",")
            match=len(set(skills) & set(resume_skills))
            role_scores[row["Job Role"]]=match

        predicted_role=max(role_scores,key=role_scores.get)
        st.success(f"Predicted Role: {predicted_role}")

        # ---------- SUGGESTIONS ----------
        st.subheader("Resume Improvement Suggestions")

        if missing_skills:
            for skill in missing_skills:
                st.warning(f"Add {skill} to improve your resume score.")
        else:
            st.success("Your resume already matches the job role.")

        # ---------- LEARNING LINKS ----------
        st.subheader("Learning Resources")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"Learn {skill}: https://www.coursera.org/courses?query={skill}")

        # ---------- PDF REPORT ----------
        if st.button("Generate PDF Report"):

            pdf="resume_report.pdf"
            c=canvas.Canvas(pdf)

            c.drawString(100,800,"Resume Analysis Report")
            c.drawString(100,760,f"Resume Score: {round(score,2)}%")

            y=720
            c.drawString(100,y,"Skills Found:")
            y-=20

            for s in matched_skills:
                c.drawString(120,y,s)
                y-=20

            y-=20
            c.drawString(100,y,"Missing Skills:")
            y-=20

            for s in missing_skills:
                c.drawString(120,y,s)
                y-=20

            c.save()

            with open(pdf,"rb") as f:
                st.download_button("Download Report",data=f,file_name="resume_analysis.pdf")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ABOUT ----------
elif menu == "About":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
AI Resume Skill Gap Analyzer

Technologies Used:
Python, NLP, Machine Learning, Streamlit, Plotly

This system analyzes resumes and identifies missing skills for job roles.
""")

    st.markdown('</div>', unsafe_allow_html=True)