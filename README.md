# 🎬 CineMatch AI - Movie Recommender System

A sleek, AI-powered movie recommendation engine built with **Python**, **Machine Learning**, and **Streamlit**. It suggests movies based on content similarity and fetches real-time metadata (posters, ratings, years) using the OMDb API.

## ✨ Features
- **Top 10 Recommendations**: Provides highly relevant movie suggestions using Cosine Similarity.
- **Live Metadata**: Fetches movie posters, IMDb ratings, and release years dynamically.
- **Netflix-Style UI**: A clean, dark-themed interface for a premium user experience.
- **Optimized Performance**: Integrated Streamlit caching for lightning-fast results.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Machine Learning**: Scikit-learn (Cosine Similarity)
- **Data Handling**: Pandas, NumPy
- **API**: OMDb API (for real-time movie posters)
- **Language**: Python

## 📂 Project Structure
```text
CineMatch-AI/
├── dataset/                # Original TMDB CSV files
├── models/                 # Pre-trained Pickle (.pkl) files
├── notebooks/              # Jupyter Notebook (Data Processing & ML)
├── app.py                  # Main Streamlit application
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation