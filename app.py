import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vibe Extension Demo", layout="wide")

# Read the HTML file directly from the root directory
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the application interface
components.html(html_content, height=900, scrolling=True)