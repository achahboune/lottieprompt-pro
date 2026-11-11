# LottiePrompt Pro

## Description
LottiePrompt Pro turns text into ready‑to‑use Lottie animations with instant timing and color tweaks.

## Features
- Convert a textual description into a vector animation.
- One‑click timing and color adjustments.
- Live demo on the landing page.
- FastAPI backend with health check.

## Setup
```bash
git clone <repo-url>
cd <repo-dir>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```
Open `index.html` in a browser.

## Limitations
- Demo returns a static placeholder animation.
- No AI model integration yet.

## Next Steps
- Integrate a text‑to‑animation model.
- Add export to .json and .svg.
- Authentication and user storage.
