
# BuildSmart — AI Construction Advisor 
 [Live Demo → buildsmart-cnwz.onrender.com](https://buildsmart-cnwz.onrender.com)

### The Problem

Most families spend their life savings building a home, often without proper cost planning or expert guidance. Architects charge lakhs. Contractors mislead. Material prices vary by location. Most families end up overspending by 20–40% or getting cheated.

There was no free, intelligent tool that could give a common realistic construction estimate — BuildSmart fixes that now.

---

## What is BuildSmart?

BuildSmart is an AI-powered construction advisor that acts as a virtual architect. Enter your budget, location, plot size, and requirements — and get a complete, detailed construction estimate in seconds for Free in both language Hindi or English.

---

## Why we built this

- sees this problem  — during construction families losing lakhs due to lack of information
- Tier 2 and tier 3 cities have zero access to affordable construction guidance
- Existing tools are too generic, too expensive, or too complicated for a common person
- AI can bridge this gap — making expert knowledge accessible to everyone

---

## What it does

**Smart Cost Estimation:**
Gives a detailed breakdown of material, labour, and finishing costs — specific to your city and budget. Not a generic calculator, but an intelligent estimate that understands context.

**Multi-Storey Support:**
Planning a 2 or 3 floor building? BuildSmart gives a floor-wise cost breakdown including additional structural costs, water tank, and lift requirements.

**Custom Requirements:**
Tell it exactly what you want — balcony, terrace, pooja room, modular kitchen, parking, garden, solar panels etc. It includes the cost of each requirement separately.

**Contractor vs Self-Construction:**
Confused whether to hire a contractor or manage construction yourself? BuildSmart compares both options with cost difference, pros, cons, and a recommendation based on your specific situation.

**Smart Savings Tips:**
Get practical, location-specific tips to reduce costs without compromising quality.

**Material Recommendations:**
Know exactly which cement brand, steel grade, tiles, and finishing materials to use — with current Indian market prices.

**Bilingual Support:**
Works in Hindi and English — because India's construction decisions happen in both languages.

**WhatsApp Sharing:**
Share your complete estimate with family members instantly with one click.

---

## Built with

- Python Flask — backend server
- Groq API with LLaMA 3.3 70B — AI engine
- HTML, CSS, JavaScript — frontend

---

## Run Locally

```bash
git clone https://github.com/jayaprajapatii/BuildSmart.git
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



