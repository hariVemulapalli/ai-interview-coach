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
- `google-generativeai` SDK

## 🌐 Deployed App

Check out the live version here: WILL PUT LINK LATER

**NOTE:** Please keep in mind that you may encounter errors if the tokens or requests quota has been reached. The AI model runs on a free tier API key.

## 🧰 Tech Stack & Tools

**Frontend / App Framework**
- ![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?logo=streamlit&logoColor=white) for the interactive UI, used to manage questions, answers, and feedback flow

**AI / Backend**
- ![Google Generative AI](https://img.shields.io/badge/Google%20Generative%20AI-Gemini-blueviolet?logo=google) - for evaluating interview answers, via ```google-generativeai``` Python SDK
- ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) - primary programming language

**Data & Logic**
- ![JSON](https://img.shields.io/badge/JSON-data-lightgrey?logo=json) ```questions.json``` for question categories
- `st.session_state` for session management

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
Create an ```.env``` file:
```env
GEMINI_API_KEY=your-gemini-api-key # You can take the free tier (may have to use gemini-2.0-flash or others where requests and tokens have good amount of quota for a free tier.
```

#### Set the AI Model by given API Key
The default model set for the app is ```gemini-2.0-flash```. This model is available on a free tier API key for Gemini and doesn't need to be modified. 

Please read the following if you want to use a different model:

You can change the model to use in the ```interview_logic.py``` file.

The following line that sets the model is shown here:
```model = genai.GenerativeModel("gemini-2.0-flash") # Can change the argument inside the GenerativeModel argument to any Gemini model that you plan to use. Can also use pro version.```

I have set the ```gemini-2.0-flash``` model by default on this repository and the deployed version since it is free. You can change to a pro version if your API key allows, this will help
with the requests and tokens quota. It is up to you.

### 4. Run the App
```basb
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
Built by Hari Vemulapalli
