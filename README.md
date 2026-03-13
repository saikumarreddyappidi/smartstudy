# 📚 Smart Study Habit Analyzer

A full-stack web application that helps students track, analyze, and optimize their study habits using AI/ML predictions.

## 🏗️ Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Frontend   | React.js + Recharts                 |
| Backend    | Python FastAPI                      |
| Database   | SQLite (via SQLAlchemy)             |
| ML Model   | scikit-learn Random Forest          |
| Auth       | JWT (python-jose + PBKDF2 hashing)  |

---

## 🚀 Quick Start

### Option 1: One-click Start (Windows)
```
Double-click start.bat
```

### Option 2: Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

Then open **http://localhost:3000**

---

## 📄 Pages

| Page               | Route              | Description                                |
|--------------------|--------------------|--------------------------------------------|
| Signup             | `/signup`          | Register with exam date & subjects         |
| Login              | `/login`           | JWT-based login                            |
| Dashboard          | `/`                | Summary, productivity score, countdown     |
| Log Session        | `/log`             | Record study sessions                      |
| Study Heatmap      | `/heatmap`         | GitHub-style activity calendar             |
| Analytics          | `/analytics`       | Bar, line, pie charts                      |
| AI Predictions     | `/predictions`     | ML readiness scores per subject            |
| Recommendations    | `/recommendations` | AI study plan & tips                       |
| Profile            | `/profile`         | Edit details, see badge                    |

---

## 🔌 API Endpoints

| Method | Endpoint                    | Description                     |
|--------|-----------------------------|---------------------------------|
| POST   | `/signup`                   | Register a new user             |
| POST   | `/login`                    | Login & get JWT token           |
| GET    | `/me`                       | Get current user info           |
| PUT    | `/me`                       | Update profile                  |
| POST   | `/log-session`              | Log a new study session         |
| GET    | `/sessions/{user_id}`       | Get all sessions                |
| GET    | `/heatmap/{user_id}`        | Heatmap data (last N days)      |
| GET    | `/analytics/{user_id}`      | Charts & summary analytics      |
| GET    | `/predict/{user_id}`        | ML readiness predictions        |
| GET    | `/recommendations/{user_id}`| AI study plan & tips            |

Swagger UI: **http://localhost:8000/docs**

---

## 🤖 ML Model

- **Algorithm:** Random Forest Regressor (scikit-learn)
- **Input Features:**
  - `total_hours` — Total study hours per subject
  - `sessions_per_week` — Frequency of study
  - `avg_focus_score` — Average focus rating (1–5)
  - `days_until_exam` — Days remaining to exam
  - `subject_difficulty` — Perceived difficulty (1–5)
- **Output:** Readiness Score (0–100)
- **Training:** 20000 synthetic student records

---

## ☁️ Deployment

### Frontend
- GitHub Pages: https://saikumarreddyappidi.github.io/smartstudy/

### Backend
- Render blueprint file: [render.yaml](render.yaml)
- Render start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Render setup
1. Open Render dashboard
2. Create a new Web Service from this GitHub repository
3. Render will detect [render.yaml](render.yaml)
4. Deploy the service named `smartstudy-api-saikumarreddyappidi`
5. After deploy, backend URL will be:
  - `https://smartstudy-api-saikumarreddyappidi.onrender.com`

### Important note
- Current backend storage uses SQLite. On hosted platforms, SQLite may be ephemeral unless a persistent disk or external database is configured.

---

## 📊 Analytics Features

- **Productive vs Unproductive:** Night sessions (after focus < 3) = unproductive
- **Productivity Score:** Based on average focus + total weekly hours
- **Exam Readiness Meter:** Per-subject progress bars on dashboard

---

## 🗂️ Project Structure

```
hackthon/
├── backend/
│   ├── main.py          # FastAPI app + all routes
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── auth.py          # JWT authentication
│   ├── database.py      # SQLite connection
│   ├── ml_model.py      # Random Forest ML model
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── api.js           # Axios instance
│   │   ├── AuthContext.js   # Global auth state
│   │   ├── components/
│   │   │   └── Sidebar.js
│   │   └── pages/
│   │       ├── Login.js
│   │       ├── Signup.js
│   │       ├── Dashboard.js
│   │       ├── LogSession.js
│   │       ├── Heatmap.js
│   │       ├── Analytics.js
│   │       ├── Predictions.js
│   │       ├── Recommendations.js
│   │       └── Profile.js
│   └── package.json
├── start.bat
└── README.md
```
