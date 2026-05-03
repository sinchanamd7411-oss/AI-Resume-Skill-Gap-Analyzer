# AI Resume Skill Gap Analyzer

## Overview

AI Resume Skill Gap Analyzer is a machine learning and NLP-based web application that analyzes a candidate’s resume against job-required skills, calculates a match percentage, and identifies missing skills (skill gaps). The system helps users understand how well their resume aligns with a target role and suggests areas for improvement.

---

## Features

* Upload and analyze resume text
* Compare resume skills with job description or required skills
* Calculate skill match percentage
* Identify missing or weak skill areas
* Simple and interactive Streamlit-based frontend
* NLP-powered skill comparison using TF-IDF Vectorizer and Cosine Similarity

---

## Tech Stack

### Frontend

* Streamlit
* Python

### Backend / ML

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* NLP-based text processing

---

## Algorithm Used

### TF-IDF (Term Frequency–Inverse Document Frequency)

Converts resume content and job skills into weighted numerical vectors based on word importance.

### Cosine Similarity

Measures similarity between resume and job skill vectors to generate a matching score.

**Formula:**

```text
Cosine Similarity = (A · B) / (||A|| ||B||)
```

---

## Project Structure

```text
AI-Resume-SILL-GAP-ANALYZER/
│
├── backend/
│   ├── ml_model.py              # TF-IDF + Cosine Similarity model
│   └── skill_extractor.py       # Skill extraction logic
│
├── dataset/
│   └── job_dataset.csv          # Job skills dataset
│
├── frontend/
│   ├── app.py                   # Streamlit frontend
│   ├── resume_report.pdf        # Generated resume report
│   └── temp_resume.pdf          # Temporary uploaded resume
│
├── resumes/                     # Uploaded resumes folder
│
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
├── resume_analysis_report.pdf   # Analysis output report
├── resume_report.pdf            # Resume report
└── temp_resume.pdf              # Temporary resume file
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sinchanamd7411-oss/AI-Resume-Skill-Gap-Analyzer.git
cd AI-Resume-Skill-Gap-Analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run frontend/app.py
```

### 4. Open in Browser

```text
http://localhost:8501/
```

---

## Working Process

1. User uploads or enters resume text
2. Job-required skills are provided
3. TF-IDF converts both texts into vectors
4. Cosine Similarity calculates matching percentage
5. System displays:

   * Resume Match Score
   * Missing Skills
   * Skill Gap Analysis

---

## Example Output

### Input:

**Resume Skills:** Python, SQL, Machine Learning
**Job Skills:** Python, SQL, Tableau, Machine Learning

### Output:

* Match Score: 75%
* Missing Skill: Tableau

---

## Advantages

* Simple and fast
* Easy to use
* Helpful for students and job seekers
* Supports resume improvement
* Good academic ML project

---

## Limitations

* Keyword-based matching
* Limited semantic understanding
* Depends on resume text quality

---

## Future Enhancements

* Deep learning-based semantic matching
* PDF resume upload support
* Skill recommendation engine
* Job role prediction
* Dashboard analytics

---

## Use Cases

* Resume screening
* Placement preparation
* HR skill matching
* Career guidance

---


---

## License

This project is open-source and available for educational purposes.
