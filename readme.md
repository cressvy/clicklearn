# ClickLearn - AI-Powered Interactive Learning Platform

ClickLearn is an AI-powered interactive tutor app designed to explain topics at multiple levels of depth — from beginner to expert. Users can enter a topic or upload notes and get AI-generated explanations that become progressively deeper with each click.

## 🚀 Features

- **Multi-Level Explanations**: Get explanations at 4 different depth levels (Beginner → Expert)
- **Interactive Learning**: Clickable keywords for deeper exploration (coming soon)
- **Modern UI/UX**: Beautiful, responsive interface built with React and Tailwind CSS
- **Smart AI Integration**: Powered by Google Gemini AI for high-quality explanations
- **Learning History**: Track your exploration journey
- **Real-time Feedback**: Instant explanations with loading states

## 🏗️ Project Structure

```
clicklearn/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API service layer
│   │   ├── utils/           # Utility functions
│   │   └── styles/          # CSS and styling
│   ├── package.json
│   └── vite.config.js
├── backend/                  # FastAPI backend application
│   ├── app/
│   │   ├── models/          # Pydantic models
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic
│   │   └── utils/           # Utility functions
│   ├── tests/               # Test files
│   ├── requirements.txt
│   └── main.py
└── README.md
```

## 🛠️ Tech Stack

### Frontend
- **React 19** - Modern React with latest features
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide React** - Beautiful icons
- **Axios** - HTTP client for API calls

### Backend
- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation and settings
- **Google Gemini AI** - Advanced language model
- **Uvicorn** - ASGI server
- **Python-dotenv** - Environment variable management

## 📦 Installation & Setup

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Google Gemini API key

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd clicklearn
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

4. **Run the backend server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Configure environment variables**
   ```bash
   cp env.example .env
   # Edit .env if needed (defaults should work)
   ```

3. **Run the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:5173`

## 🚀 Usage

1. **Enter a topic** in the search box (e.g., "Machine Learning", "Quantum Physics")
2. **Select depth level**:
   - 🧠 **Beginner**: Simple explanations with analogies
   - ⚡ **Intermediate**: Detailed explanations with examples
   - 🚀 **Advanced**: Technical explanations with deep insights
   - 👑 **Expert**: Academic-level explanations with research
3. **Click "Start Learning"** to get your explanation
4. **Use "Explain Deeper"** to get more detailed explanations
5. **View your learning history** to revisit previous topics

## 🔧 Development

### Frontend Development
```bash
cd frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run ESLint
npm run test         # Run tests
```

### Backend Development
```bash
cd backend
uvicorn app.main:app --reload  # Start development server
pytest tests/                   # Run tests
black .                        # Format code
flake8 .                       # Lint code
```

### API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🧪 Testing

### Frontend Tests
```bash
cd frontend
npm run test
```

### Backend Tests
```bash
cd backend
pytest tests/
```

## 📝 API Endpoints

### Core Endpoints
- `POST /api/v1/explain` - Generate topic explanation
- `POST /api/v1/extract-keywords` - Extract keywords from text
- `POST /api/v1/conversation` - Generate conversational response
- `GET /api/v1/health` - Health check

### Example Request
```bash
curl -X POST "http://localhost:8000/api/v1/explain" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Machine Learning", "depth": 2}'
```

## 🚀 Deployment

### Frontend (Vercel)
1. Connect your GitHub repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

### Backend (Railway/Render)
1. Connect your GitHub repository
2. Set environment variables (GEMINI_API_KEY)
3. Deploy automatically

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] **Clickable Keywords**: Make keywords in explanations clickable for deeper exploration
- [ ] **Conversation Mode**: Multi-turn conversations with context
- [ ] **File Upload**: Upload notes/documents for explanation
- [ ] **User Accounts**: Save learning progress and preferences
- [ ] **Mobile App**: React Native mobile application
- [ ] **Offline Mode**: Cache explanations for offline access
- [ ] **Multi-language Support**: Support for multiple languages
- [ ] **Voice Input**: Speech-to-text for topic input

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for providing the language model
- FastAPI team for the excellent web framework
- React team for the amazing frontend library
- Tailwind CSS for the utility-first CSS framework

---

**Happy Learning! 🎓** 