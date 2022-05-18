from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:246135@localhost:5432/hrms_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Candidates(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer,  primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    identity_number = db.Column(db.String(11), unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)

    def __init__(self, first_name, last_name, identity_number, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.identity_number = identity_number
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

def format_cantidates(candidate):
    return{
        "id": candidate.id,
        "first_name": candidate.first_name,
        "last_name": candidate.last_name,
        "identity_number": candidate.identity_number,
        "date_of_birth": candidate.date_of_birth
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

    def __init__(self, company_name, web_address, phone_number):
        self.company_name = company_name
        self.web_address = web_address
        self.phone_number = phone_number

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

def format_employers(employer):
    return{
        "id": employer.id,
        "company_name": employer.company_name,
        "web_address": employer.web_address,
        "phone_number": employer.phone_number
    }
    
class Experinces(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey(
        'resumes.id'), nullable=False)
    job_title_id = db.Column(db.Integer, db.ForeignKey(
        'job_titles.id'), nullable=False)
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


def format_experinces(experince):
    return{
        "id": experince.id,
        "resume_id": experince.resume_id,
        "job_title__id": experince.job_title__id,
        "company_name": experince.company_name,
        "starting_date": experince.starting_date,
        "termination_date": experince.termination_date
    }

class Job_postings(db.Model):
    __tablename__ = 'job_postings'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey(
        'employers.user_id'), nullable=False)
    job_title_id = db.Column(db.Integer, db.ForeignKey(
        'job_titles.id'), nullable=False)
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


def format_job_postings(job_posting):
    return{
        "id": job_posting.id,
        "employer_id": job_posting.employer_id,
        "job_title__id": job_posting.job_title__id,
        "job_description": job_posting.job_description,
        "salary_min": job_posting.salary_min,
        "salary_max": job_posting.salary_max,
        "posting_date": job_posting.posting_date,
        "closing_date": job_posting.closing_date,
        "isActive" : job_posting.isActive
    }

class Job_titles(db.Model):
    __tablename__ = 'job_titles'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    title = db.Column(db.String(150), unique=True, nullable=False)

    def _init_(self, title):
        self.title = title

    def _repr_(self):
        return '<id %r>' % self.id


def format_job_titles(job_title):
    return{
        "id": job_title.id,
        "title": job_title.title
    }

class Languages(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    language = db.Column(db.String(50), unique=True, nullable=False)

    def _init_(self, language):
        self.language = language

    def _repr_(self):
        return '<id %r>' % self.id


def format_languages(language):
    return{
        "id": language.id,
        "language": language.language
    }

class Resumes(db.Model):
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey(
        'candidates.user_id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def _init_(self, candidate_id, creation_date):
        self.candidate_id = candidate_id
        self.creation_date = creation_date

    def _repr_(self):
        return '<id %r>' % self.id


def format_resumes(resume):
    return{
        "id": resume.id,
        "candidate_id": resume.resume_id,
        "creation_date": resume.creatiob_date
    }

class Skills(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey(
        'resumes.id'), nullable=False)
    skill = db.Column(db.String(150), nullable=False)

    def _init_(self, resume_id, skill):
        self.resume_id = resume_id
        self.skill = skill

    def _repr_(self):
        return '<id %r>' % self.id


def format_skills(skill):
    return{
        "id": skill.id,
        "resume_id": skill.resume_id,
        "skill" : skill.skill
    }

class Updated_employers(db.Model):
    __tablename__ = 'updated_employers'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey(
        'employers.user_id'), nullable=False)
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


def format_updated_employers(updated_employer):
    return{
        "employer_id": updated_employer.employer_id,
        "email": updated_employer.email,
        "password": updated_employer.password,
        "company_name": updated_employer.company_name,
        "web_address": updated_employer.web_address,
        "phone_number": updated_employer.phone_number
    }


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def _init_(self, email, password):
        self.email = email
        self.password = password

    def _repr_(self):
        return '<id %r>' % self.id


def format_users(user):
    return{
        "id": user.id,
        "email": user.email,
        "password": user.password
    }
    
@app.route('/candidates/add' , methods = ['POST'])
def crate_candidate():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    identity_number = request.json['identity_number']
    date_of_birth = request.json['date_of_birth']
    candidate = Candidates(first_name=first_name,last_name=last_name,identity_number=identity_number,date_of_birth=identity_number)
    db.session.add(candidate)
    db.session.commit()
    return format_cantidates(candidate)

@app.route('/job_titles/add', methods=['POST'])
def create_title():
        title=request.json['title']
        new_job_title= Job_titles(title=title)
        db.session.add(new_job_title)
        db.session.commit()
        return format_users(new_job_title)
    
@app.route('/users/add', methods=['POST'])
def create_user():
        email=request.json['email']
        password = request.json['password']
        new_user= Users(email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return format_users(new_user)
    
if __name__ == "__main__":
    app.run(host = 'localhost', port = 5000, debug=True)