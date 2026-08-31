import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vibe Extension Demo", layout="wide")

# Locate index.html dynamically relative to app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "index.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=True)
