# 🌱 CropAdvisor

AI-powered crop disease detection for smallholder farmers.

LIVE HERE: https://crop-advisor-0g6x.onrender.com/

Upload a photo of your plant and get simple, actionable advice in plain English — no agronomist needed.

## What it does

- Detects crop diseases, pests, and nutrient problems from photos
- Gives location-aware advice tailored to your region
- Speaks like a trusted farm advisor, not a textbook
- Built for low-literacy farmers on slow networks

## Built With

- Python + Streamlit
- OpenAI GPT-4o-mini (vision)
- Pillow for image compression

## Run Locally

1. Clone the repo
```bash
   git clone https://github.com/yourusername/crop-advisor.git
   cd crop-advisor
```

2. Create a virtual environment
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Add your OpenAI API key
```bash
   echo "OPENAI_API_KEY=your-key-here" > .env
```

5. Run the app
```bash
   streamlit run app.py
```

## Project Structure
```
crop-advisor/
├── app.py                  # Streamlit UI
├── agent/
│   └── crop_agent.py       # AI prompt and analysis logic
├── utils/
│   └── image_utils.py      # Image compression and validation
├── config/
│   └── settings.py         # App constants
├── requirements.txt
└── render.yaml             # Render deployment config
```

## Deployment

Deployed on Render. Set `OPENAI_API_KEY` as an environment variable in your Render dashboard.

## Target Users

Smallholder farmers across Nigeria and beyond — using borrowed phones, slow networks, and local knowledge.

---

Built by Devair
