def match_skills(candidate_skills, job_skills):

    score = 0

    for skill in job_skills:
        if skill in candidate_skills:
            score += 1

    percentage = (score / len(job_skills)) * 100

    return percentage