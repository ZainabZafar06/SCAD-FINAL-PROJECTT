_**Spam Email Classifier**_

**Project Description**

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

**Technologies Used**<br>
Python<br>
Flask<br>
HTML/CSS<br>
Scikit-learn<br>
Pandas<br>
Numpy<br>
Postman<br>

**Project Structure**<br>
Spam-Email-Classifier/<br>
│<br>
├── templates/<br>
│   └── index.html<br>
│<br>
├── app.py<br>
├── testing.py<br>
├── model.ipynb<br>
├── requirements.txt<br>
├── spam.csv<br>
└── README.md<br>

**How to Run**<br>
1. Install Requirements<br>
pip install -r requirements.txt<br>
2. Run the App<br>
python app.py<br>

3. Open in browser:<br>

http://127.0.0.1:5000<br>

4. API Testing<br>
Endpoint<br>
POST /api/predict<br>
Example<br>
JSON<br>
{<br>
  "text": "Win a free iPhone now"<br>
}

**Advantages**<br>
Lightweight and fast<br>
Easy to use<br>
Works without GPU<br>
Simple web interface<br>

**Limitations**<br>
Uses a basic dataset<br>
Limited text understanding<br>


**This project is based on the original GitHub repository by SrujanPR.**<br>

Additional features such as threading, unit testing, API integration, and error handling were added for academic purposes.
