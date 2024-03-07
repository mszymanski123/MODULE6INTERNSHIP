import requests
import json

ACCESS_TOKEN = 'f472sdfD823489gJ45l9032'
SURVEY_MONKEY_API_URL = 'https://api.surveymonkey.com/intershipwro/surveys'
HEADERS = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

def create_survey(survey_name):
    """Creates a new survey and returns its ID."""
    data = {"title": survey_name}
    response = requests.post(SURVEY_MONKEY_API_URL, headers=HEADERS, json=data)
    return response.json().get('id')

def add_page_to_survey(survey_id, page_title):
    """Adds a new page to a survey and returns its ID."""
    url = f'{SURVEY_MONKEY_API_URL}/{survey_id}/pages'
    data = {"title": page_title}
    response = requests.post(url, headers=HEADERS, json=data)
    return response.json().get('id')

def add_question_to_page(survey_id, page_id, question):
    """Adds a new question to a survey page."""
    url = f'{SURVEY_MONKEY_API_URL}/{survey_id}/pages/{page_id}/questions'
    data = {
        "headings": [{"heading": question["Description"]}],
        "answers": {"choices": [{"text": ans} for ans in question["Answers"]]},
        "family": "single_choice",
        "subtype": "vertical"
    }
    response = requests.post(url, headers=HEADERS, json=data)
    return response.json()

def main(survey_questions_file, recipients_file):
    with open(survey_questions_file, 'r') as file:
        survey_data = json.load(file)

    for survey_name, pages in survey_data.items():
        survey_id = create_survey(survey_name)
        for page_name, questions in pages.items():
            page_id = add_page_to_survey(survey_id, page_name)
            for question_name, question in questions.items():
                add_question_to_page(survey_id, page_id, question)

    with open(recipients_file, 'r') as file:
        recipients = [email.strip() for email in file.readlines()]

    print(f'Survey "{survey_name}" created and questions added successfully.')

if __name__ == '__main__':
    survey_questions_file = 'path_to_your_survey_questions.json'
    recipients_file = 'path_to_your_recipients.txt'
    main(survey_questions_file, recipients_file)

