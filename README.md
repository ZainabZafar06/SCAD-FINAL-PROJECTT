**Spam Email Classifier
Project Description**

This project is a lightweight AI-based web application that detects whether an email/message is Spam or Not Spam.

The application is built using:

Flask (Backend)
HTML/CSS (Frontend)
Machine Learning with Scikit-learn

Users can enter a message on the webpage and get instant prediction results.

**Model Information**
What the Model Does

The model classifies text messages into:

Spam
Not Spam

**Model Used**
Multinomial Naive Bayes
CountVectorizer

This is a lightweight text classification model that works without GPU support.

**Input and Output**
Input
Email or message text
Output
Spam
Not Spam

**Features Added**

1. Flask web application
2. HTML/CSS frontend
3. Spam prediction system
4. API testing using Postman
5. Threading implementation
6. Unit testing using unittest
7. Error handling for empty input

**Technologies Used**
Python
Flask
HTML/CSS
Scikit-learn
Pandas
Numpy
Postman

**Project Structure**
Spam-Email-Classifier/
│
├── templates/
│   └── index.html
│
├── app.py
├── testing.py
├── model.ipynb
├── requirements.txt
├── spam.csv
└── README.md

**How to Run**
1. Install Requirements
pip install -r requirements.txt
2. Run the App
python app.py

3. Open in browser:

http://127.0.0.1:5000
4. API Testing
Endpoint
POST /api/predict
Example JSON
{
  "text": "Win a free iPhone now"
}

**Advantages**
Lightweight and fast
Easy to use
Works without GPU
Simple web interface

**Limitations**
Uses a basic dataset
Limited text understanding


**This project is based on the original GitHub repository by SrujanPR.**

Additional features such as threading, unit testing, API integration, and error handling were added for academic purposes.
