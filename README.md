# Wardrobe Manager

AI-powered wardrobe management system that helps users organize their clothes and avoid buying duplicates using smart image recognition.

## 🏗️ Architecture

- **Frontend**: Next.js 14+ with TypeScript and TailwindCSS
- **Backend**: FastAPI (Python) with automatic API documentation
- **Database**: Supabase (PostgreSQL + Storage)
- **AI**: Google Gemini API for image analysis
- **Auth**: Supabase Auth with Google OAuth
- **Hosting**: Vercel (Frontend + Backend)

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- Supabase account
- Google Cloud API key

### Environment Setup
1. **Create Supabase Project:**
   - Go to [supabase.com](https://supabase.com) and create a new project
   - Enable Google OAuth in Authentication > Providers
   - Get your project URL, anon key, and JWT secret from Settings > API

2. **Configure Environment Variables:**
   - Copy `env.example` to `.env.local` (frontend)
   - Copy `env.example` to `.env` (backend)
   - Fill in your Supabase and Google API credentials

### Installation

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

#### Backend
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 📁 Project Structure

```
wardrobe-manager/
├── frontend/              # Next.js application
│   ├── src/
│   │   ├── app/          # Next.js App Router
│   │   ├── components/   # Reusable UI components
│   │   ├── lib/          # Utilities and API client
│   │   └── types/        # TypeScript type definitions
├── backend/               # FastAPI application
│   ├── main.py           # FastAPI app entry point
│   ├── config.py         # Configuration management
│   └── requirements.txt  # Python dependencies
└── env.example           # Environment variables template
```

## 🎯 Features

- ✅ User authentication via Google OAuth
- ✅ Image upload and storage
- 🔄 AI-powered image description (in progress)
- 🔄 Visual similarity matching (upcoming)
- 🔄 Outfit recommendations (planned)

## 🛠️ Development

The project follows a staged development approach:

1. **Stage 1**: Project Foundation ✅
2. **Stage 2**: Authentication System
3. **Stage 3**: Database & Storage Setup
4. **Stage 4**: Basic Image Upload
5. **Stage 5**: AI Integration
6. **Stage 6**: Wardrobe Dashboard
7. **Stage 7**: Similarity Matching
8. **Stage 8**: Enhanced UI/UX
9. **Stage 9**: Performance Optimization
10. **Stage 10**: Advanced Features

## 📚 API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

## 🤝 Contributing

This project is in active development. See the TODO list for upcoming features and improvements.
