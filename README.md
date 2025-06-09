# 🎤 AI Interview Coach

Practice behavioral interview questions and get instant feedback using AI. This tool helps job seekers sharpen their answers using the STAR method.

## 🚀 Features

- 🎲 Random or category-based question selection
- 📝 Instant AI-generated feedback (Clarity, STAR use, Impact)
- 📜 Answer archive
- 💾 Export all your answers and feedback as a .txt file
- 🗂️ Filter archive by category
- ✍️ Add custom questions
- 🎛️ Choose feedback style (Detailed, Concise, Friendly)

## 🧠 Powered by

- [Streamlit](https://streamlit.io/)
- [Google Gemini Pro (Generative AI)](https://ai.google.dev/)
- `google-generativeai` Python SDK

## 🌐 Deployed App

Check out the live version here: **(WILL PUT LINK LATER)**

> ⚠️ You may encounter errors if token or request quotas are exceeded. The AI model runs on a free-tier API key.

## 🧰 Tech Stack & Tools

**Frontend / App Framework**
- ![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?logo=streamlit&logoColor=white) Interactive UI using Streamlit: used to manage questions, answers, and feedback flow
- Session state management with `st.session_state`

**AI / Backend**
- ![Google Generative AI](https://img.shields.io/badge/Google%20Generative%20AI-Gemini-blueviolet?logo=google) - Google Gemini via `google-generativeai`: for evaluating interview answers
- ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) - Core language used

**Data & Logic**
- ![JSON](https://img.shields.io/badge/JSON-data-lightgrey?logo=json) Categorized questions via `questions.json`

**Deployment**
- ![Streamlit Cloud](https://img.shields.io/badge/Deployed%20on-Streamlit%20Cloud-FF4B4B?logo=streamlit) used for online deployment, via GitHub
- ![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github) - for source code hosting and CI/CD

## 📦 Setup Instructions

### 1. Clone the repo
bash:
```bash
git clone https://github.com/your-username/ai-interview-coach.git
cd ai-interview-coach
```

### 2. Install Dependences
bash:
```bash
pip install -r requirements.txt
```
### 3. Add your API key
**For local use, create a .env file:**
.env:
```env
GEMINI_API_KEY=your-gemini-api-key
```
**For Streamlit Cloud, use the Secrets tab to securely store the key:**
toml:
```toml
GEMINI_API_KEY = "your-api-key"
```

### 4. Set AI Model (Optional)
**The app uses gemini-2.0-flash by default, which is free-tier friendly.**
**To change it, go to interview_logic.py:**
```python
model = genai.GenerativeModel("gemini-2.0-flash")
# Change to "gemini-pro" or other model if your key supports it
```

### 5. Run the App
```bash
streamlit run app.py
```

### 📁 File Structure

```
├── app.py
├── interview_logic.py
├── questions.json
├── requirements.txt
├── .env (optional, not committed)
└── .gitignore
```

## 📬 Contact
Built with ❤️ by Hari Vemulapalli
