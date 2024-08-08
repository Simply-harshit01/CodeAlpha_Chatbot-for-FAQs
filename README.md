# CodeAlpha_Chatbot-for-FAQs

Overview
The Mental Health FAQ Chatbot is a simple command-line interface (CLI) application designed to answer frequently asked questions (FAQs) related to mental health among young people. The chatbot uses Natural Language Processing (NLP) techniques to understand user queries and provides appropriate responses from a predefined set of FAQs.

Features-

FAQ Responses:  Answers questions related to mental health issues commonly faced by youth.
  Natural Language Processing: Utilizes NLP libraries to process and analyze text inputs.
Text-Based Interaction: Simple CLI-based interface for easy interaction.
Scalable: Easily expandable to include more questions and answers.

Technologies Used-

Python: Core programming language for developing the chatbot.

NLTK (Natural Language Toolkit): Used for tokenization and stopword removal.

SpaCy: Used for entity recognition and dependency parsing.

Scikit-Learn: Used for text vectorization and similarity calculations.

Virtual Environment: To manage project dependencies and isolate the environment.

Getting Started-

Prerequisites:

Python 3.x installed on your system.

Access to the command line or terminal.

Visual Studio Code (VS Code) or any other code editor of your choice.

Setup Instructions-

Clone the Repository:


git clone https://github.com/your-username/mental-health-chatbot.git

cd mental-health-chatbot

Create a Virtual Environment:

python -m venv chatbot-env
Activate the Virtual Environment:

Windows:
chatbot-env\Scripts\activate

macOS/Linux:
source chatbot-env/bin/activate
Install Dependencies:

Install the required Python packages using pip:


pip install -r requirements.txt
python -m spacy download en_core_web_sm
Ensure requirements.txt contains:


nltk
spacy
scikit-learn
Download NLTK Data:


Run the chatbot.py script to download necessary NLTK data:


python chatbot.py
Run the Chatbot:


Start the chatbot by executing the chatbot.py script:



python chatbot.py

The chatbot will greet you and wait for your questions.


Using the Chatbot-

Ask Questions: Type a question about mental health, and the chatbot will respond with the most relevant answer.

Exit the Chatbot: Type exit or quit to end the session.

Contribution-

Contributions are welcome! Please fork the repository and submit a pull request with any improvements or new features.

Acknowledgments-

NLTK Documentation

SpaCy Documentation

Scikit-Learn Documentation
