from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:246135@localhost/HRMS_DB'

db = SQLAlchemy(app)

class Candidates(db.Model):
    __tablename__ = 'candidates'

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    identity_number = db.Column(db.String(11), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)

    def __init__(self, first_name, last_name, identity_number, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.identity_number = identity_number
        self.date_of_birth = date_of_birth 

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

class Educations(db.Model):
    __tablename__ = 'educations'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    resume_id = db.Column(db.Integer, nullable=False)
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

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    web_address = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)

    def __init__(self, user_id, company_name, web_address, phone_number):
        self.user_id = user_id
        self.company_name = company_name
        self.web_address = web_address
        self.phone_number = phone_number

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)
    

class Experinces(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    resume_id = db.Column(db.Integer, nullable=False)
    job_title_id = db.Column(db.Integer, primary_key=True, nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    starting_date = db.Column(db.DateTime, nullable=False)
    termination_date = db.Column(db.DateTime)

    def __init__(self, resume_id, job_title_id, company_name, starting_date, termination_date):
        self.resume_id = resume_id
        self.job_title_id = job_title_id
        self.company_name = company_name
        self.starting_date = starting_date
        self.termination_date = termination_date

    def __repr__(self):
        return '<id {}>'.format(self.id)
 

class Job_postings(db.Model):
    __tablename__ = 'job_postings'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    employer_id = db.Column(db.Integer, nullable=False)
    job_title_id = db.Column(db.Integer, nullable=False)
    job_description = db.Column(db.String(2300), nullable=False)
    salary_min = db.Column(db.String(50))
    salary_max = db.Column(db.String(50))
    posting_date = db.Column(db.DateTime, nullable=False)
    closing_date = db.Column(db.DateTime)
    isActive = db.Column(db.Boolean, nullable=False)

    def __init__(self, employer_id, job_title_id, job_description, salary_min, salary_max, posting_date, closing_date, isActive):
        self.employer_id = employer_id
        self.job_title_id = job_title_id
        self.job_description = job_description
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.posting_date = posting_date
        self.closing_date = closing_date
        self.isActive = isActive

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Job_titles(db.Model):
    __tablename__ = 'job_titles'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)

    def _init_(self, title):
        self.title = title

    def _repr_(self):
        return '<id %r>' % self.id


class Languages(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    language = db.Column(db.String(50), nullable=False)

    def _init_(self, language):
        self.language = language

    def _repr_(self):
        return '<id %r>' % self.id


class Resumes(db.Model):
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    candidate_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def _init_(self, candidate_id, creation_date):
        self.candidate_id = candidate_id
        self.creation_date = creation_date

    def _repr_(self):
        return '<id %r>' % self.id


class Skills(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    resume_id = db.Column(db.Integer, nullable=False)
    skill = db.Column(db.String(150), nullable=False)

    def _init_(self, resume_id, skill):
        self.resume_id = resume_id
        self.skill = skill

    def _repr_(self):
        return '<id %r>' % self.id


class Updated_employers(db.Model):
    __tablename__ = 'updated_employers'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    employer_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    web_address = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)

    def _init_(self, employer_id, email, password, company_name, web_address, phone_number):
        self.employer_id = employer_id
        self.email = email
        self.password = password
        self.company_name = company_name
        self.web_address = web_address
        self.phone_number = phone_number

    def _repr_(self):
        return '<id %r>' % self.id


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def _init_(self, email, password):
        self.email = email
        self.password = password

    def _repr_(self):
        return '<id %r>' % self.id
    
@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)