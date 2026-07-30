
# BuildSmart — AI Construction Advisor 
 [Live Demo → buildsmart-cnwz.onrender.com](https://buildsmart-cnwz.onrender.com)

### The Problem

Most families spend their life savings building a home, often without proper cost planning or expert guidance. Architects charge lakhs. Contractors mislead. Material prices vary by location. Most families end up overspending by 20–40% or getting cheated.

There was no free, intelligent tool that could give a common realistic construction estimate — BuildSmart fixes that now.

---

## What is BuildSmart ?

BuildSmart is an AI-powered construction advisor that acts as a virtual architect. Enter your budget, location, plot size, and requirements — and get a complete, detailed construction estimate in seconds for Free in both language Hindi or English.

---

## Why we built this ?

- sees this problem  — during construction families losing lakhs due to lack of information
- Tier 2 and tier 3 cities have zero access to affordable construction guidance
- Existing tools are too generic, too expensive, or too complicated for a common person
- AI can bridge this gap — making expert knowledge accessible to everyone

---

## Built with

- Python Flask — backend server
- Groq API with LLaMA 3.3 70B — AI engine
- HTML, CSS, JavaScript — frontend

---

## Project Structure

```
BuildSmart/
├── app.py              # Flask backend, AI prompt logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
└── .env                # API key 
```

## Run Locally

```bash
git clone <repository_url>
cd BuildSmart
pip install flask groq python-dotenv
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
```

```bash
python app.py
```

Open `http://localhost:5000`

---



