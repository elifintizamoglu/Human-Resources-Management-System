import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import { useParams } from "react-router";
import Headline from "./../layouts/Headline";
import ResumeService from "./../services/resumeService";
import EducationService from "./../services/educationService";
import ExperienceService from "./../services/experienceService";
import GithubButton from "./../layouts/GithubButton";
import LinkedinButton from "./../layouts/LinkedinButton";
import DateLabel from "./../layouts/DateLabel";
import {
  Container,
  Grid,
  Header,
  Image,
  Segment,
  Divider,
  Icon,
  Button,
} from "semantic-ui-react";

export default function CandidateDetail() {
  let { id } = useParams();

  const [resumes, setResumes] = useState([]);

  let resumeService = new ResumeService();
  let educationService = new EducationService();
  let experienceService = new ExperienceService();

  useEffect(() => {
    resumeService.getAll().then((result) => setResumes(result.data.data));
    educationService.getAll().then((result) => setResumes(result.data.data));
    experienceService.getAll().then((result) => setResumes(result.data.data));
  }, []);

  return (
    <div>
      <Container className="content">
        <Headline content="Aday" />

        <Grid>
          <Grid.Row>
            <Grid.Column width="3" />
            <Grid.Column width="10">
              {resumes.map((resume) => (
                <Grid key={candidate.id}>
                  {resume.candidate_id?.id == id && (
                    <Grid.Row>
                      <Grid.Column>
                        <Button
                          circular
                          compact
                          floated="right"
                          color="yellow"
                          icon="pencil alternate"
                          as={NavLink}
                          to={`/candidates/update${candidate.id}`}
                        />
                        <Button
                          circular
                          compact
                          floated="right"
                          color="yellow"
                          icon="cog"
                          as={NavLink}
                          to={`/resumes/update/${resume.candidate_id?.id}`}
                        />
                        <Header>
                          <span className="detail-header">
                            {candidate?.name}
                          </span>
                        </Header>
                        {resume.experiences.length === 0 &&
                        resume.educations.length === 0 ? null : resume
                            .experiences.length === 0 ? (
                          <span>
                            {resume.educations[0].department}
                            <br />
                          </span>
                        ) : (
                          <span>
                            {resume.experiences[0].jobTitle?.title}
                            <br />
                          </span>
                        )}
                        <Icon name="envelope" />
                        {resume.candidate?.email}
                        <br />
                        {resume.links.length === 0 ? null : (
                          <span>
                            <br />
                            {resume.links.map((link) =>
                              link.linkName?.id === 1 ? (
                                <GithubButton url={link.url} />
                              ) : (
                                <LinkedinButton url={link.url} />
                              )
                            )}
                          </span>
                        )}
                        <Divider />

                        {resume.educations.length === 0 &&
                        resume.experiences.length === 0 &&
                        resume.skills.length === 0 ? null : (
                          <span>
                            <br />
                            <DateLabel
                              value={new Date(
                                resume.creationDate
                              ).toDateString()}
                            />
                            <br />
                            <br />
                          </span>
                        )}

                        {resume.educations.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Educations"
                              className="orbitron"
                            />
                            <br />
                            {resume.educations.map((education) => (
                              <span>
                                <strong>
                                  {education.nameOfEducationalInstitution}
                                </strong>
                                <br />
                                {education.degree} ・ {education.department}
                                <br />
                                <span className="extra">
                                  {new Date(
                                    education.startingDate
                                  ).getFullYear()}
                                  &nbsp;-&nbsp;
                                  {education.graduationDate === "Devam ediyor."
                                    ? "Continues"
                                    : new Date(
                                        education.graduationDate
                                      ).getFullYear()}
                                </span>
                                <br />
                                <br />
                              </span>
                            ))}
                          </Segment>
                        )}

                        {resume.experiences.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Experiences"
                              className="orbitron"
                            />
                            <br />
                            {resume.experiences.map((experience) => (
                              <span>
                                <strong>{experience.jobTitle?.title}</strong>
                                <br />
                                {experience.companyName}
                                <br />
                                <span className="extra">
                                  {new Date(experience.startingDate).getMonth()}
                                  .
                                  {new Date(
                                    experience.startingDate
                                  ).getFullYear()}
                                  &nbsp;-&nbsp;
                                  {experience.terminationDate ===
                                  "Devam ediyor."
                                    ? "Continues"
                                    : new Date(
                                        experience.terminationDate
                                      ).getMonth() +
                                      "." +
                                      new Date(
                                        experience.terminationDate
                                      ).getFullYear()}
                                </span>
                                <br />
                                <br />
                              </span>
                            ))}
                          </Segment>
                        )}

                        {resume.skills.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Skills"
                              className="orbitron"
                            />
                            <br />
                            {resume.skills.map((skill) => (
                              <span>・ {skill.skill}&nbsp;&nbsp;&nbsp;</span>
                            ))}
                            <br />
                            <br />
                          </Segment>
                        )}
                      </Grid.Column>
                    </Grid.Row>
                  )}
                </Grid>
              ))}
            </Grid.Column>
            <Grid.Column width="3" />
          </Grid.Row>
        </Grid>
      </Container>
    </div>
  );
}