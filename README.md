# Lecture-to-Notes System (PRJ-019)

## Project Overview

The Lecture-to-Notes System is an AI-powered tool that converts lecture text into concise and meaningful summaries. It helps students quickly understand and revise key concepts from long lecture content.

---

## Features

* Text input for lecture content
* AI-based summarization (HuggingFace Transformers)
* FastAPI backend for processing
* Streamlit frontend for user interaction
* Clean and simple UI

---

##  Tech Stack

* Backend: FastAPI
* Frontend: Streamlit
* AI/NLP: HuggingFace Transformers
* Language: Python

---

## 📂 Project Structure

```
lecture-to-notes-system/
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── routes/
│       └── services/
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
├── tests/
├── README.md
```

---

## Installation & Setup

### 1.Clone the repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

### 2.Install dependencies

```
pip install -r backend/requirements.txt
```

---

### 3.Run Backend (FastAPI)

```
uvicorn backend.app.main:app --reload
```

---

### 4.Run Frontend (Streamlit)

```
python -m streamlit run frontend/streamlit_app.py
```

---

## Usage

1. Open Streamlit app in browser
2. Enter lecture text
3. Click **Summarize**
4. View generated summary

---

## Example Output

**Input:**
Machine learning is a subset of artificial intelligence...

**Output:**
Machine learning enables systems to learn from data and is widely used in real-world applications.

---

## Development Plan

* **Week 1:** Setup project structure, API, UI
* **Week 2:** Implement summarization model
* **Week 3:** Improve UI, add features, testing

---

## Future Improvements

* Key points extraction
* Quiz/question generation
* Audio-to-text transcription
* Downloadable notes (PDF)

---

## Author

* ADELINE NISIA.P

---

## Notes

This project is developed as part of an academic assignment under the domain of **GenAI + NLP in Education**.
