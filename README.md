# WE Guide

This workspace contains a Streamlit manual site for `WarEra Ireland`.

## Overview

This is a beginner manual for new players explaining core WarEra concepts and giving tips with:

- Ireland branding
- dark themed UI with emerald green accents
- sidebar and top navigation
- quick-start checklist screenshot popovers
- translated English content
- screenshot placeholders for files you want to add later

## Project files

- `app.py` - main Streamlit application
- `requirements.txt` - Python dependencies
- `assets/screenshots` - Screenshot assets

## Run locally

1. Create and activate a Python environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Start the app:
   - `streamlit run app.py`

## App sections

The app includes these sections:

- Quick Start
- Basics
- Economy
- Fighting & War
- Strategies
- Did You Know?
- FAQ

## Navigation

Navigation works inside the same Streamlit window through:

- the modern sidebar navigation panel
- the horizontal section navigation bar

The active section is also reflected in the query string through `?section=...`.

## Screenshots

Place screenshots in `assets/screenshots/` 
