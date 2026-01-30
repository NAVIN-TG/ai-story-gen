# AI Story Generator

A Streamlit web app that generates creative stories based on user input.

## Features

- **Genre Selection:** Fantasy, Sci-Fi, Mystery, Horror, Romance, Historical, and more
- **Tone Control:** Serious, Humorous, Dark, Inspirational
- **Length Options:** Short, Medium, Long
- **OpenAI Integration (Optional):** Use real AI with your OpenAI API key
- **Fallback Generator:** Works without API key using deterministic narrative templates

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ai-story-generator.git
cd ai-story-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file with your OpenAI key:
```
OPENAI_API_KEY=sk-your-key-here
```

5. Run the app:
```bash
streamlit run app.py
```

Access at http://localhost:8501

## Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub → New app
4. Select repo, branch, and `app.py`
5. Deploy

To add your OpenAI key:
- Streamlit Cloud dashboard → Manage secrets
- Add `OPENAI_API_KEY = sk-...`

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku config:set OPENAI_API_KEY=sk-...
```

## Architecture

```
.
├── app.py                 # Streamlit main app
├── src/
│   ├── __init__.py
│   ├── generator.py       # Story generator (AI + fallback)
│   └── utils.py           # Utilities
├── requirements.txt
├── .gitignore
├── Procfile               # Heroku config
└── README.md
```

## License

MIT
