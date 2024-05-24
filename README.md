# YOUTUBETTRANSCRIPT

YouTube Transcript Analyzer

Overview
Welcome to the YouTube Transcript Analyzer! This application utilizes Flask, spaCy, and NLP packages to provide summaries of YouTube videos in English, Kannada, and Hindi languages.

Features

1. Input YouTube Video URL
Paste the URL of the YouTube video you want to analyze.
Supports videos in various languages.
2. Multi-Language Support
Generate summaries in English, Kannada, or Hindi languages.
Utilizes spaCy for natural language processing.
3. Real-Time Summary Generation
Quickly generate summaries of YouTube video transcripts.
Accessible through a user-friendly web interface.
4. Easy-to-Use Interface
Simple and intuitive interface for seamless user experience.
Get summaries with just a few clicks.

Usage

To use the YouTube Transcript Analyzer, follow these steps:

Input YouTube Video URL: Paste the URL of the YouTube video you want to analyze into the provided input field.

Select Language: Choose the language in which you want to view the summary (English, Kannada, or Hindi).

Get Summary: Click on the "Get Summary" button to generate a summary of the video's transcript in the selected language.

View Summary: Once the summary is generated, it will be displayed on the screen for your review.


Setup Instructions

Clone the Repository

Install Dependencies:

cd youtube-transcript-analyzer
pip install -r requirements.txt

Download spaCy Language Models:

python -m spacy download en
python -m spacy download kn
python -m spacy download hi

Run the Application:
python app.py

Access the Application:
Open your web browser and go to http://localhost:3000 to access the YouTube Transcript Analyzer.

Contributors

Poornachandra (poornachandrapc777@gmail.com)
Rohan Shetty (shettyrohan253@gmail.com)
