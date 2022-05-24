import datetime
from .models import Candidates,Educations,Employers,Experiences,Job_postings,Resumes
from .models import format_candidates,format_educations,format_employers,format_experiences,format_resumes,format_job_postings
from flask import Blueprint, request, session
#from __init__ import reqst
from . import db

reqst = Blueprint('reqst', __name__)


@reqst.route('/candidates/add', methods=['POST'])
def crate_candidate():
    name = request.json['name']
    identity_number = request.json['identity_number']
    date_of_birth = request.json['date_of_birth']
    email = request.json['email']
    password = request.json['password']
    new_candidate = Candidates(name=name,identity_number=identity_number, date_of_birth=date_of_birth,email=email,password=password)
    db.session.add(new_candidate)
    db.session.commit()
    return format_candidates(new_candidate)

@reqst.route('/candidates/get', methods=['GET'])
def get_candidates():
    candidates = Candidates.query.order_by(Candidates.id.asc()).all()
    candidate_lists=[]
    for candidate in candidates:
        candidate_lists.reqstend(format_candidates(candidate))
    return {'Candidates': candidate_lists}

@reqst.route('/candidates/get/<id>', methods=['GET'])
def get_candidate(id):
    candidate = Candidates.query.filter_by(id=id).one()
    formatted_candidate = format_candidates(candidate)
    return {'Candidate': formatted_candidate}

@reqst.route('/candidates/delete/<id>', methods=['DELETE'])
def delete_candidate(id):
    candidate = Candidates.query.filter_by(id=id).one()
    db.session.delete(candidate)
    db.session.commit()
    return f'Candidate (id: {id}) deleted'

@reqst.route('/candidates/update', methods=['PUT'])
def update_candidate():
    candidate = Candidates.query.filter_by(id=id)
    name = request.json['name']
    identity_number = request.json['identity_number']
    date_of_birth = request.json['date_of_birth']
    email = request.json['email']
    password = request.json['password']
    candidate.update(dict(name=name, identity_number=identity_number,
                          date_of_birth=date_of_birth, email=email, password=password))
    db.session.commit()
    return {'Candidate': format_candidates(candidate.one())}

@reqst.route('/educations/add', methods=['POST'])
def create_education():
    resume_id = request.json['resume_id']
    name_of_educational_institution = request.json['name_of_educational_institution']
    department = request.json['department']
    degree = request.json['degree']
    starting_date = request.json['starting_date']
    graduation_date = request.json['graduation_date']
    new_education = Educations(resume_id=resume_id, name_of_educational_institution=name_of_educational_institution,
                                   department=department, degree=degree, starting_date=starting_date, graduation_date=graduation_date)
    db.session.add(new_education)
    db.session.commit()
    return format_educations(new_education)

@reqst.route('/educations/get', methods=['GET'])
def get_educations():
    educations = Educations.query.order_by(Educations.id.asc()).all()
    education_lists = []
    for education in educations:
        education_lists.reqstend(format_educations(education))
    return {'Educations': education_lists}

@reqst.route('/educations/get/<id>', methods=['GET'])
def get_education(id):
    education = Educations.query.filter_by(id=id).one()
    formatted_education = format_educations(education)
    return {'Education': formatted_education}

@reqst.route('/educations/delete/<id>', methods=['DELETE'])
def delete_education(id):
    education = Educations.query.filter_by(id=id).one()
    db.session.delete(education)
    db.session.commit()
    return f'Education (id: {id}) deleted'

@reqst.route('/educations/update', methods=['PUT'])
def update_education():
    education = Educations.query.filter_by(id=id)
    resume_id = request.json['resume_id']
    name_of_educational_institution = request.json['name_of_educational_institution']
    department = request.json['department']
    degree = request.json['degree']
    starting_date = request.json['starting_date']
    graduation_date = request.json['graduation_date']
    education.update(dict(resume_id=resume_id, name_of_educational_institution=name_of_educational_institution,
                          department=department, degree=degree, starting_date=starting_date, graduation_date=graduation_date))
    db.session.commit()
    return {'Education': format_educations(education.one())}

@reqst.route('/employers/add', methods=['POST'])
def create_employer():
    company_name = request.json['company_name']
    web_address = request.json['web_address']
    phone_number = request.json['phone_number']
    email = request.json['email']
    password = request.json['password']
    new_employer = Employers(company_name=company_name,
                             web_address=web_address, phone_number=phone_number,email=email,password=password)
    db.session.add(new_employer)
    db.session.commit()
    return format_employers(new_employer)

@reqst.route('/employers/get', methods=['GET'])
def get_employers():
    employers = Employers.query.order_by(Employers.id.asc()).all()
    employer_lists = []
    for employer in employers:
        employer_lists.reqstend(format_employers(employers))
    return {'Employers': employer_lists}

@reqst.route('/employers/get/<id>', methods=['GET'])
def get_employer(id):
    employer = Employers.query.filter_by(id=id).one()
    formatted_employers = format_employers(employer)
    return {'Employer': formatted_employers}

@reqst.route('/employers/delete/<id>', methods=['DELETE'])
def delete_employer(id):
    employer = Employers.query.filter_by(id=id).one()
    db.session.delete(employer)
    db.session.commit()
    return f'Employer (id: {id}) deleted'

@reqst.route('/employers/update', methods=['PUT'])
def update_employer():
    employer = Employers.query.filter_by(id=id)
    company_name = request.json['company_name']
    web_address = request.json['web_address']
    phone_number = request.json['phone_number']
    email = request.json['email']
    password = request.json['password']
    employer.update(dict(company_name=company_name,
                         web_address=web_address, phone_number=phone_number, email=email, password=password))
    db.session.commit()
    return {'Employer': format_employers(employer.one())}

@reqst.route('/experiences/add', methods=['POST'])
def create_experience():
    resume_id = request.json['resume_id']
    job_title = request.json['job_title']
    company_name = request.json['company_name']
    starting_date = request.json['starting_date']
    termination_date = request.json['termination_date']
    new_experience = Experiences(resume_id=resume_id, job_title=job_title,
                                 company_name=company_name, starting_date=starting_date, termination_date=termination_date)
    db.session.add(new_experience)
    db.session.commit()
    return format_experiences(new_experience)

@reqst.route('/experiences/get', methods=['GET'])
def get_experiences():
    experiences = Experiences.query.order_by(Experiences.id.asc()).all()
    experience_lists = []
    for experience in experiences:
        experience_lists.reqstend(format_experiences(experience))
    return {'Experiences': experience_lists}

@reqst.route('/experiences/get/<id>', methods=['GET'])
def get_experience(id):
    experience = Experiences.query.filter_by(id=id).one()
    formatted_experience = format_experiences(experience)
    return {'Experience': formatted_experience}

@reqst.route('/experiences/delete/<id>', methods=['DELETE'])
def delete_experience(id):
    experience = Experiences.query.filter_by(id=id).one()
    db.session.delete(experience)
    db.session.commit()
    return f'Experience (id: {id}) deleted'

@reqst.route('/experiences/update', methods=['PUT'])
def update_experience():
    experience = Experiences.query.filter_by(id=id)
    resume_id = request.json['resume_id']
    job_title = request.json['job_title']
    company_name = request.json['company_name']
    starting_date = request.json['starting_date']
    termination_date = request.json['termination_date']
    experience.update(dict(resume_id=resume_id, job_title=job_title,
                           company_name=company_name, starting_date=starting_date, termination_date=termination_date))
    db.session.commit()
    return {'Experience': format_experiences(experience.one())}

@reqst.route('/job_postings/add', methods=['POST'])
def create_job_posting():
    company_name = request.json['company_name']
    job_title = request.json['job_title_id']
    job_description = request.json['job_description']
    salary_min = request.json['salary_min']
    salary_max = request.json['salary_max']
    posting_date = request.json['posting_date']
    closing_date = request.json['closing_date']
    isActive = request.json['isActive']
    new_job_posting = Job_postings(company_name=company_name, job_title=job_title, job_description=job_description,
                                   salary_min=salary_min, salary_max=salary_max, posting_date=posting_date, closing_date=closing_date, isActive=isActive)
    db.session.add(new_job_posting)
    db.session.commit()
    return format_job_postings(new_job_posting)

@reqst.route('/job_postings/get', methods=['GET'])
def get_job_postings():
    job_postings = Job_postings.query.order_by(Job_postings.id.asc()).all()
    job_posting_lists = []
    for job_posting in job_postings:
        job_posting_lists.reqstend(format_job_postings(job_posting))
    return {'Job_postings': job_posting_lists}

@reqst.route('/job_postings/get/<id>', methods=['GET'])
def get_job_posting(id):
    job_posting = Job_postings.query.filter_by(id=id).one()
    formatted_job_posting = format_job_postings(job_posting)
    return {'Job_posting': formatted_job_posting}

@reqst.route('/job_postings/delete/<id>', methods=['DELETE'])
def delete_job_posting(id):
    job_posting = Job_postings.query.filter_by(id=id).one()
    db.session.delete(job_posting)
    db.session.commit()
    return f'Job_posting (id: {id}) deleted'

@reqst.route('/job_postings/update', methods=['PUT'])
def update_job_posting():
    job_posting = Job_postings.query.filter_by(id=id)
    company_name = request.json['company_name']
    job_title = request.json['job_title_id']
    job_description = request.json['job_description']
    salary_min = request.json['salary_min']
    salary_max = request.json['salary_max']
    posting_date = request.json['posting_date']
    closing_date = request.json['closing_date']
    isActive = request.json['isActive']
    job_posting.update(dict(company_name=company_name, job_title=job_title, job_description=job_description,
                            salary_min=salary_min, salary_max=salary_max, posting_date=posting_date, closing_date=closing_date, isActive=isActive))
    db.session.commit()
    return {'Job_posting': format_job_postings(job_posting.one())}

@reqst.route('/resumes/add', methods=['POST'])
def create_resume():
    candidate_id = session["id"]
    skills = request.json['skills']
    languages = request.json['languages']
    new_resume = Resumes(candidate_id=candidate_id, creation_date=datetime.now, skills=skills, languages=languages)
    db.session.add(new_resume)
    db.session.commit()
    return format_resumes(new_resume)

@reqst.route('/resumes/get', methods=['GET'])
def get_resumes():
    resumes = Resumes.query.order_by(Resumes.id.asc()).all()
    resume_lists = []
    for resume in resumes:
        resume_lists.reqstend(format_resumes(resume))
    return {'Resumes': resume_lists}

@reqst.route('/resumes/get/<id>', methods=['GET'])
def get_resume(id):
    resume = Resumes.query.filter_by(id=id).one()
    formatted_resume = format_resumes(resume)
    return {'Resume': formatted_resume}

@reqst.route('/resumes/delete/<id>', methods=['DELETE'])
def delete_resume(id):
    resume = Resumes.query.filter_by(id=id).one()
    db.session.delete(resume)
    db.session.commit()
    return f'Resume (id: {id}) deleted'

@reqst.route('/resumes/update', methods=['PUT'])
def update_resume():
    resume = Resumes.query.filter_by(id=id)
    candidate_id = request.json['candidate_id']
    creation_date = request.json['creation_date']
    skills = request.json['skills']
    languages = request.json['languages']
    resume.update(dict(candidate_id=candidate_id,
                  creation_date=creation_date, skills=skills, languages=languages))
    db.session.commit()
    return {'Resume': format_resumes(resume.one())}