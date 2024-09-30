import spacy
from flask import Flask, request, render_template, flash, redirect, url_for
from objective import ObjectiveTest  # Custom logic for objective questions
from subjective import SubjectiveTest  # Custom logic for subjective questions
import google.generativeai as genai  # Import Gemini API library
import config  # Import the configuration file for API keys
import logging

# Load the SpaCypip install google-generativeai
#  English model
nlp = spacy.load("en_core_web_sm")

# Configure Gemini API using your API key
genai.configure(api_key=config.GEMINI_API_KEY)

# Switch to a simpler Gemini model (if available)
gemini_model = genai.GenerativeModel('gemini-pro')  # Use 'gemini-lite' or 'gemini-pro'

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'aica2'

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')  # Render the form to input data

# Tokenize text using SpaCy
def tokenize_sentences(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

# Route to handle requests for test generation
@app.route('/test_generate', methods=["POST"])
def test_generate():
    if request.method == "POST":
        inputText = request.form["itext"]
        testType = request.form["test_type"]
        noOfQues = request.form["noq"]

        # Validate input
        if not inputText or not noOfQues:
            flash("Please provide input text and number of questions.")
            return redirect(url_for('index'))

        # Use Gemini API for subjective question generation
        if testType == "subjective":
            try:
                chat = gemini_model.start_chat(history=[])
                logging.debug(f"Sending request to Gemini: Generate {noOfQues} questions based on the text.")
                response = chat.send_message(f"Generate {noOfQues} questions and answers based on the following text. Format as 'Question: <question_text>', 'Answer: <answer_text>':\n{inputText}")

                # Split the response text by line and extract questions and answers
                lines = response.text.strip().split("\n")

                questions = []
                answers = []
                for line in lines:
                    if line.startswith("Question:"):
                        questions.append(line)
                    elif line.startswith("Answer:"):
                        answers.append(line)

                # Ensure questions and answers are paired correctly
                results = zip(questions, answers)

                return render_template('generatedtestdata.html', cresults=results)
            except Exception as e:
                logging.error(f"Error with Gemini API: {str(e)}")
                flash(f"Error with Gemini API: {str(e)}")
                return redirect(url_for('index'))

        # Use existing logic for objective question generation
        elif testType == "objective":
            try:
                chat = gemini_model.start_chat(history=[])
                logging.debug(f"Sending request to Gemini: Generate {noOfQues} questions based on the text.")
        
        # Request AI to generate questions and answers
                response = chat.send_message(f"Generate {noOfQues} multiple-choice questions and answers based on the following text. /n {inputText}""")

        # Log the raw response to check its structure
                logging.debug(f"Raw response from Gemini: {response.text}")
                
                # Split the response text into lines
                lines = response.text.strip().split("\n")
                
                # Store and structure each line in a list for display
                structured_output = []
                question_block = []
                
                for line in lines:
                    # Detect start of a new question (assuming "Question:" prefix is provided in the response)
                    if line.startswith("Question:"):
                        if question_block:
                            structured_output.append("\n".join(question_block))  # Store the previous question block
                            question_block = []  # Reset for the new question
                        question_block.append(line)  # Add new question to the block
                    else:
                        question_block.append(line)  # Add options/answers to the current question block

                # Add the last question block
                if question_block:
                    structured_output.append("\n".join(question_block))

                # Pass the structured output to the template for display
                return render_template("objective_type.html", cresults=structured_output)
            except Exception as e:
                logging.error(f"Error with Gemini API: {str(e)}")
                flash(f"Error with Gemini API: {str(e)}")
                return redirect(url_for("index"))

        # Use existing logic for subjective question generation using local method
        elif testType == "gemini":
            try:
                response = generate_questions_with_ai(inputText, noOfQues, "subjective")
                return render_template('generatedtestdata.html', cresults=response)
            except Exception as e:
                logging.error(f"Error generating subjective questions: {str(e)}")
                flash(f"Error generating subjective questions: {str(e)}")
                return redirect(url_for('index'))

        else:
            flash('Error: Invalid test type!')
            return redirect(url_for('index'))
# Function to generate questions based on existing local logic (objective/subjective)
def generate_questions_with_ai(input_text, num_questions, question_type):
    if question_type == "objective":
        # Tokenize the input text using SpaCy
        sentences = tokenize_sentences(input_text)

        # Create an instance of ObjectiveTest with the tokenized sentences and number of questions
        objective_test = ObjectiveTest(input_text, num_questions)
        questions, answers = objective_test.generate_test()
        return zip(questions, answers)

    elif question_type == "subjective":
        # Create an instance of SubjectiveTest with the input text and number of questions
        subjective_test = SubjectiveTest(input_text, num_questions)
        questions, answers = subjective_test.generate_test()
        return zip(questions, answers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
