# ClickLearn

ClickLearn is an AI-powered interactive tutor app designed to explain topics at multiple levels of depth — from beginner to expert. Users can enter a topic or upload notes and get AI-generated explanations that become progressively deeper with each click. Keywords within explanations will be clickable, allowing users to dive even further into specific concepts.

---

## Project Goals

- Provide layered explanations for any topic using advanced language models.
- Enable recursive exploration of concepts via clickable keywords.
- Build a smooth and responsive user experience with React on the frontend.
- Develop a powerful backend using FastAPI that communicates with Google Gemini AI to generate explanations.
- Ensure scalability by integrating multiple languages: Python for AI logic, Go for API orchestration (planned), and React for the frontend UI.

---

## Tech Stack

- **Frontend:** React, TailwindCSS  
- **Backend:** FastAPI (Python), Google Gemini API for generative AI  
- **Future Plans:** Go for API gateway/microservices layer, MongoDB or Redis for session state  
- **Deployment:** Vercel (frontend), Render or Railway (backend)

---

## Current Progress

- Backend FastAPI server set up with Google Gemini API integration for multi-level explanations.
- React frontend scaffolded with input and output UI for basic interaction.
- Next steps include adding “Explain More” functionality and clickable keyword support.

---
## Weekly Development Plan

| Week | Goals & Deliverables |
|-------|---------------------|
| 1     | **Project Bootstrap:** Set up React frontend scaffold and FastAPI backend with Google Gemini integration. Test basic topic explanation API. |
| 2     | **Depth Control:** Implement “Explain More” button to request deeper explanation levels. |
| 3     | **Keyword Highlighting:** Extract keywords from explanations and make them clickable for recursive exploration. |
| 4     | **Conversation State:** Track user’s exploration path and display breadcrumb or navigation tree. |
| 5     | **UI/UX Enhancements:** Add animations, improve design, and optimize user interaction flow. |
| 6     | **Deployment & Documentation:** Deploy frontend and backend on hosting services, finalize README and docs, and polish project for portfolio showcase. |

---

## How to Run

1. Clone the repo
2. Install backend dependencies:  
   `pip install -r backend/requirements.txt`  
3. Add your Gemini API key to `backend/.env`  
4. Run backend server:  
   `uvicorn backend.main:app --reload`  
5. Run frontend server:  
   `cd frontend && npm install && npm run dev`  
6. Open the app in your browser at `http://localhost:5173`

---

Feel free to contribute or raise issues as the project evolves!
