from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
#from flask import Blueprint

class Candidates(db.Model, UserMixin):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    identity_number = db.Column(db.String(11), unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    resumes = db.relationship('Resumes')

    def __init__(self, name, identity_number, date_of_birth, email, password):
        self.name = name
        self.identity_number = identity_number
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Educations(db.Model):
    __tablename__ = 'educations'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey(
        'resumes.id'), nullable=False)
    name_of_educational_institution = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(150), nullable=False)
    degree = db.Column(db.String(50), nullable=False)
    starting_date = db.Column(db.DateTime, nullable=False)
    graduation_date = db.Column(db.DateTime)

    def __init__(self, resume_id, name_of_educational_institution, department, degree, starting_date, graduation_date):
        self.resume_id = resume_id
        self.name_of_educational_institution = name_of_educational_institution
        self.department = department
        self.degree = degree
        self.starting_date = starting_date
        self.graduation_date = graduation_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Employers(db.Model):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    web_address = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __init__(self, company_name, web_address, phone_number, email, password):
        self.company_name = company_name
        self.web_address = web_address
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    
class Experiences(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey(
        'resumes.id'), nullable=False)
    job_title = db.Column(db.String(50),  nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    starting_date = db.Column(db.DateTime, nullable=False)
    termination_date = db.Column(db.DateTime)

    def __init__(self, resume_id, job_title, company_name, starting_date, termination_date):
        self.resume_id = resume_id
        self.job_title = job_title
        self.company_name = company_name
        self.starting_date = starting_date
        self.termination_date = termination_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Job_postings(db.Model):
    __tablename__ = 'job_postings'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    job_title = db.Column(db.String(50), nullable=False)
    job_description = db.Column(db.String(2300), nullable=False)
    salary_min = db.Column(db.String(50))
    salary_max = db.Column(db.String(50))
    posting_date = db.Column(db.DateTime, nullable=False)
    closing_date = db.Column(db.DateTime)
    isActive = db.Column(db.Boolean, nullable=False,default=1)

    def __init__(self,  company_name, job_title, job_description, salary_min, salary_max, posting_date, closing_date, isActive):
        self.company_name = company_name
        self.job_title = job_title
        self.job_description = job_description
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.posting_date = posting_date
        self.closing_date = closing_date
        self.isActive = isActive

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Resumes(db.Model):
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey(
        'candidates.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False,default=datetime.now)
    educations = db.relationship('Educations', backref='resume')
    experiences = db.relationship('Experiences', backref='resume')
    skills = db.Column(db.String(300), nullable=False)
    languages = db.Column(db.String(300), nullable=False)

    def _init_(self, candidate_id, creation_date,skills,languages):
        self.candidate_id = candidate_id
        self.creation_date = creation_date
        self.skills = skills
        self.languages= languages

    def _repr_(self):
        return '<id %r>' % self.id

def format_candidates(candidate):
    return{
        "id": candidate.id,
        "name": candidate.name,
        "identity_number": candidate.identity_number,
        "date_of_birth": candidate.date_of_birth,
        "email": candidate.email,
        "password": candidate.password
    }

def format_educations(education):
    return{
        "id": education.id,
        "resume_id": education.resume_id,
        "name_of_educational_institution": education.name_of_educational_institution,
        "department": education.department,
        "degree": education.degree,
        "starting_date": education.starting_date,
        "graduation_date": education.graduation_date
    }

def format_employers(employer):
    return{
        "id": employer.id,
        "company_name": employer.company_name,
        "web_address": employer.web_address,
        "phone_number": employer.phone_number,
        "email": employer.email,
        "password": employer.password
    }

def format_experiences(experience):
    return{
        "id": experience.id,
        "resume_id": experience.resume_id,
        "job_title": experience.job_title,
        "company_name": experience.company_name,
        "starting_date": experience.starting_date,
        "termination_date": experience.termination_date
    }

def format_job_postings(job_posting):
    return{
        "id": job_posting.id,
        "company_name": job_posting.company_name,
        "job_title": job_posting.job_title,
        "job_description": job_posting.job_description,
        "salary_min": job_posting.salary_min,
        "salary_max": job_posting.salary_max,
        "posting_date": job_posting.posting_date,
        "closing_date": job_posting.closing_date,
        "isActive": job_posting.isActive
    }

def format_resumes(resume):
    return{
        "id": resume.id,
        "candidate_id": resume.resume_id,
        "creation_date": resume.creatiob_date,
        "skills":resume.skills,
        "languages":resume.languages
    }




