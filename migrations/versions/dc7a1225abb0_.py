"""empty message

Revision ID: dc7a1225abb0
Revises: 
Create Date: 2022-05-18 00:07:38.886467

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dc7a1225abb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('candidates', 'user_id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('uk_candidates_identity_number', 'candidates', type_='unique')
    op.drop_constraint('fk_candidates_users', 'candidates', type_='foreignkey')
    op.alter_column('educations', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('fk_educations_resumes', 'educations', type_='foreignkey')
    op.drop_constraint('fk_employers_users', 'employers', type_='foreignkey')
    op.alter_column('experiences', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False)
    op.drop_constraint('fk_experiences_resumes', 'experiences', type_='foreignkey')
    op.drop_constraint('fk_experiences_job_titles', 'experiences', type_='foreignkey')
    op.add_column('job_postings', sa.Column('isActive', sa.Boolean(), nullable=False))
    op.alter_column('job_postings', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('job_postings', 'closing_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.drop_constraint('fk_job_postings_job_titles', 'job_postings', type_='foreignkey')
    op.drop_constraint('fk_job_postings_employers', 'job_postings', type_='foreignkey')
    op.drop_column('job_postings', 'is_active')
    op.alter_column('job_titles', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('uk_job_titles_title', 'job_titles', type_='unique')
    op.alter_column('languages', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('uk_languages_language', 'languages', type_='unique')
    op.alter_column('resumes', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('fk_resumes_candidates', 'resumes', type_='foreignkey')
    op.alter_column('skills', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('fk_skills_resumes', 'skills', type_='foreignkey')
    op.alter_column('updated_employers', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('fk_updated_employers_employers', 'updated_employers', type_='foreignkey')
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint('uk_users_email', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uk_users_email', 'users', ['email'])
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_foreign_key('fk_updated_employers_employers', 'updated_employers', 'employers', ['employer_id'], ['user_id'])
    op.alter_column('updated_employers', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_foreign_key('fk_skills_resumes', 'skills', 'resumes', ['resume_id'], ['id'])
    op.alter_column('skills', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_foreign_key('fk_resumes_candidates', 'resumes', 'candidates', ['candidate_id'], ['user_id'])
    op.alter_column('resumes', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_unique_constraint('uk_languages_language', 'languages', ['language'])
    op.alter_column('languages', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_unique_constraint('uk_job_titles_title', 'job_titles', ['title'])
    op.alter_column('job_titles', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.add_column('job_postings', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_job_postings_employers', 'job_postings', 'employers', ['employer_id'], ['user_id'])
    op.create_foreign_key('fk_job_postings_job_titles', 'job_postings', 'job_titles', ['job_title_id'], ['id'])
    op.alter_column('job_postings', 'closing_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('job_postings', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.drop_column('job_postings', 'isActive')
    op.create_foreign_key('fk_experiences_job_titles', 'experiences', 'job_titles', ['job_title_id'], ['id'])
    op.create_foreign_key('fk_experiences_resumes', 'experiences', 'resumes', ['resume_id'], ['id'])
    op.alter_column('experiences', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False)
    op.create_foreign_key('fk_employers_users', 'employers', 'users', ['user_id'], ['id'])
    op.create_foreign_key('fk_educations_resumes', 'educations', 'resumes', ['resume_id'], ['id'])
    op.alter_column('educations', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_foreign_key('fk_candidates_users', 'candidates', 'users', ['user_id'], ['id'])
    op.create_unique_constraint('uk_candidates_identity_number', 'candidates', ['identity_number'])
    op.alter_column('candidates', 'user_id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
