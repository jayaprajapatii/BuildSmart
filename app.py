from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/estimate", methods=["POST"])
def estimate():
    data = request.json
    budget = data.get("budget")
    rooms = data.get("rooms")
    location = data.get("location")
    construction_type = data.get("construction_type")
    plot_size = data.get("plot_size")
    language = data.get("language")
    build_type = data.get("build_type")
    features = data.get("features") or "none"
    floors = data.get("floors")

    prompt = f"""
You are an expert Indian construction advisor helping common Indian families.

Person's requirements:
- Budget: Rs {budget}
- Number of rooms: {rooms}
- Number of floors: {floors}
- Location: {location}
- Construction type: {construction_type}
- Plot size: {plot_size} sq ft
- Who will build: {build_type}
- Special requirements: {features}
- Response language: {language}

CRITICAL FORMATTING — FOLLOW EXACTLY:
- Use EXACTLY these section headers: 1. VERDICT: , 2. COST BREAKDOWN: , 3. FLOOR-WISE BREAKDOWN: , 4. SPECIAL REQUIREMENTS COST: , 5. SMART SAVINGS: , 6. MATERIALS: , 7. TIMELINE: , 8. WARNING: , 9. CONTRACTOR VS SELF:
- Skip section 3 if only 1 floor
- Skip section 4 if no special requirements
- NEVER use ## or ### headings
- NEVER number items inside sections
- Use • for ALL bullet points
- NEVER use - (hyphen) for any list item, ALWAYS use • (bullet)
- Even for sub-categories like Ground Floor, First Floor — use • not -
- No intro lines like "I will respond in English"
- LANGUAGE RULE:
- If language is hindi: Respond COMPLETELY in Hindi. Every word in Hindi.
- If language is english: Respond in English.
- No intro lines.

1. VERDICT: Budget realistic? (Yes/Tight/No) + explanation of why

2. COST BREAKDOWN:
- Material: Rs X (approx 50%)
  • Cement: Rs X
  • Steel: Rs X
  • Bricks: Rs X
  • Sand: Rs X
  • Other: Rs X
- Labour: Rs X (approx 30%)
  • Masonry: Rs X
  • Carpentry: Rs X
  • Plumbing: Rs X
  • Electrical: Rs X
- Finishing: Rs X (approx 20%)
  • Flooring: Rs X
  • Paint: Rs X
  • Doors & Windows: Rs X
- TOTAL: Rs {budget}

3. FLOOR-WISE BREAKDOWN: (only if more than 1 floor)
- Ground Floor: Rs X
  • Structure: Rs X
  • Material: Rs X
  • Labour: Rs X
- First Floor: Rs X
  • Additional structural cost: Rs X
  • Material: Rs X
  • Labour: Rs X
- Each additional floor add 15-20% extra cost
- Lift (if 3+ floors): Rs X
- Water tank & pumping: Rs X
- Fire safety (if required): Rs X

4. SPECIAL REQUIREMENTS COST: (only if user mentioned any)
- Each special requirement with separate cost:
  • Balcony: Rs X
  • Terrace: Rs X
  • Pooja Room: Rs X
  • Modular Kitchen: Rs X
  • Parking/Garage: Rs X
  • Garden/Lawn: Rs X
  • Solar Panels: Rs X
  • Any other mentioned: Rs X

5. SMART SAVINGS: 3 practical tips using •

6. MATERIALS: Best materials for {location} using • with prices

7. TIMELINE: Phase-wise breakdown using •
- Foundation: X weeks
- Structure: X weeks
- Finishing: X weeks
- Total: X months

8. WARNING: 3 critical mistakes using •

9. CONTRACTOR VS SELF:
 •  Contractor: Rs X total, pros and cons
 • Self-Construction: Rs X total, pros and cons
 • Recommendation: Which is better and why

Be very specific with Indian prices for {location}.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"result": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)