import re

def extract_email(text):
    email = re.findall(r'\S+@\S+', text)
    return email[0] if email else None


def extract_skills(text):

    skills_list = ["python","sql","django","machine learning","java"]

    found_skills = []

    for skill in skills_list:
        if skill in text.lower():
            found_skills.append(skill)

    return found_skills