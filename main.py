from database import create_connection
from resume_parser import extract_email, extract_skills
from matcher import match_skills


text = """
Name: Rahul
Email: rahul@gmail.com
Skills: Python, SQL, Django
"""

email = extract_email(text)
skills = extract_skills(text)

conn = create_connection()
cursor = conn.cursor()

cursor.execute(
"INSERT INTO candidates(name,email,skills) VALUES(%s,%s,%s)",
("Rahul",email,str(skills))
)

conn.commit()

job_skills = ["python","sql","machine learning"]

match = match_skills(skills, job_skills)

print("Candidate Match:", match,"%")