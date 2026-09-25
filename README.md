# 🎬 Movie Recommendation System

A full-stack, content-based movie recommendation web application built with **FastAPI**, **Scikit-learn**, **SQLAlchemy**, and modern vanilla **HTML5/CSS3/JavaScript**.

---

## 🌟 Features

- **Content-Based Filtering:** Computes TF-IDF vector representations across genres, directors, actors, and plot summaries, calculating similarity scores with Cosine Similarity.
- **RESTful API:** Powered by FastAPI with automatic interactive documentation (`/docs` and `/redoc`).
- **Database & Auto-Seeding:** SQLite database managed with SQLAlchemy ORM, automatically initialized and seeded with curated movie data on server start.
- **Modern Responsive UI:** Clean glassmorphism/dark-mode theme with dynamic cards, match percentage badges, and poster fallback support.
- **Single-Server Deployment:** FastAPI serves both the REST endpoints and the frontend static assets seamlessly.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn, SQLAlchemy, SQLite
- **Machine Learning / NLP:** Scikit-learn (`TfidfVectorizer`, `cosine_similarity`), Pandas, NumPy
- **Frontend:** HTML5, CSS3 (Flexbox/Grid, Glassmorphism, CSS Custom Properties), Modern Async JavaScript

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/VarunKuwar/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python run_server.py
```

### 5. Access the app
Open your web browser and navigate to:
- **Application:** [http://localhost:8000](http://localhost:8000)
- **Interactive Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure

```text
├── backend/
│   ├── database.py         # SQLAlchemy engine, session, and Movie model
│   ├── main.py             # FastAPI app, CORS, routes & static mounting
│   ├── recommendation.py   # TF-IDF & Cosine Similarity recommendation engine
│   └── seed_data.py        # Seed dataset with popular movies and metadata
├── frontend/
│   ├── index.html          # Main web application interface
│   ├── script.js           # Async API fetching and dynamic DOM rendering
│   └── style.css           # Modern dark-mode styling
├── .gitignore              # Ignored files (venv, sqlite db, cache)
├── README.md               # Project documentation
├── requirements.txt        # Python package dependencies
└── run_server.py           # Uvicorn entry point
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
