import os
import glob
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vibe Extension Demo", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Candidate relative locations for the HTML file
candidate_paths = [
    os.path.join(BASE_DIR, "index.html"),
    os.path.join(BASE_DIR, "popup.html"),
    os.path.join(BASE_DIR, "vibe code4.html"),
    os.path.join(BASE_DIR, "extension", "index.html"),
    os.path.join(BASE_DIR, "extension", "popup.html"),
    os.path.join(BASE_DIR, "extension", "vibe code4.html"),
]

# Fallback search for any HTML file in the repository tree
found_files = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
candidate_paths.extend(found_files)

target_file = None
for path in candidate_paths:
    if os.path.exists(path) and os.path.isfile(path):
        target_file = path
        break

if target_file:
    with open(target_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=900, scrolling=True)
else:
    st.error("No HTML file was found in the GitHub repository.")
    st.write("Current repository structure detected by Streamlit:")
    
    file_list = []
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), BASE_DIR))
            
    st.code("\n".join(file_list) if file_list else "Directory is empty.")
