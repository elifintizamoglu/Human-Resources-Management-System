from calendar import c
from email.policy import default
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:246135@localhost:5432/HRMS_DB'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Candidates(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    identity_number = db.Column(db.String(11), unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    resumes = db.relationship('Resumes', backref='candidate')

    def __init__(self, name, identity_number, date_of_birth, email, password):
        self.name = name
        self.identity_number = identity_number
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

def format_cantidates(candidate):
    return{
        "id": candidate.id,
        "name": candidate.name,
        "identity_number": candidate.identity_number,
        "date_of_birth": candidate.date_of_birth,
        "email": candidate.email,
        "password": candidate.password
    }

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

class Employers(db.Model):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    web_address = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __init__(self, company_name, web_address, phone_number, email, password):
        self.company_name = company_name
        self.web_address = web_address
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

def format_employers(employer):
    return{
        "id": employer.id,
        "company_name": employer.company_name,
        "web_address": employer.web_address,
        "phone_number": employer.phone_number,
        "email": employer.email,
        "password": employer.password
    }
    
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

def format_experiences(experience):
    return{
        "id": experience.id,
        "resume_id": experience.resume_id,
        "job_title": experience.job_title,
        "company_name": experience.company_name,
        "starting_date": experience.starting_date,
        "termination_date": experience.termination_date
    }

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
    isActive = db.Column(db.Boolean, nullable=False)

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


def format_resumes(resume):
    return{
        "id": resume.id,
        "candidate_id": resume.resume_id,
        "creation_date": resume.creatiob_date,
        "skills":resume.skills,
        "languages":resume.languages
    }

@app.route('/candidates/add', methods=['POST'])
def crate_candidate():
    name = request.json['name']
    identity_number = request.json['identity_number']
    date_of_birth = request.json['date_of_birth']
    email = request.json['email']
    password = request.json['password']
    new_candidate = Candidates(name=name,identity_number=identity_number, date_of_birth=date_of_birth,email=email,password=password)
    db.session.add(new_candidate)
    db.session.commit()
    return format_cantidates(new_candidate)

@app.route('/educations/add', methods=['POST'])
def create_education():
    resume_id = request.json['resume_id']
    name_of_educational_institution = request.json['name_of_educational_institution']
    department = request.json['department']
    degree = request.json['degree']
    starting_date = request.json['starting_date']
    graduation_date = request.json['graduation_date']
    new_job_posting = Job_postings(resume_id=resume_id, name_of_educational_institution=name_of_educational_institution,
                                   department=department, degree=degree, starting_date=starting_date, graduation_date=graduation_date)
    db.session.add(new_job_posting)
    db.session.commit()
    return format_job_postings(new_job_posting)

@app.route('/employers/add', methods=['POST'])
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

@app.route('/experiences/add', methods=['POST'])
def create_experience():
    resume_id = request.json['resume_id']
    job_title_id = request.json['job_title_id']
    company_name = request.json['company_name']
    starting_date = request.json['starting_date']
    termination_date = request.json['termination_date']
    new_experience = Experiences(resume_id=resume_id, job_title_id=job_title_id,
                                 company_name=company_name, starting_date=starting_date, termination_date=termination_date)
    db.session.add(new_experience)
    db.session.commit()
    return format_job_postings(new_experience)

@app.route('/job_postings/add', methods=['POST'])
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

@app.route('/resumes/add', methods=['POST'])
def create_resume():
    candidate_id = request.json['candidate_id']
    creation_date = request.json['creation_date']
    skills = request.json['skills']
    languages = request.json['languages']
    new_resume = Resumes(candidate_id=candidate_id, creation_date=creation_date, skills=skills, languages=languages)
    db.session.add(new_resume)
    db.session.commit()
    return format_resumes(new_resume)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
