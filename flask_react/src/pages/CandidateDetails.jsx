import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import { useParams } from "react-router";
import Headline from "./../layouts/Headline";
import CandidateService from "./../services/candidateService";
import DateLabel from "./../layouts/DateLabel";
import {
  Container,
  Grid,
  Header,
  Segment,
  Divider,
  Icon,
  Button,
} from "semantic-ui-react";

export default function CandidateDetail() {
  let { id } = useParams();
  const [candidates, setCandidates] = useState([]);

  let candidateService = new CandidateService();

  useEffect(() => {
    candidateService
      .getAllInfo()
      .then((result) => setCandidates(result.data.data));
  }, []);

  return (
    <div>
      <Container className="content">
        <Headline content="Aday" />

        <Grid>
          <Grid.Row>
            <Grid.Column width="3" />
            <Grid.Column width="10">
              {candidates.map((candidate) => (
                <Grid key={candidate.id}>
                  {candidates.candidate.id === id && (
                    <Grid.Row>
                      <Grid.Column>
                        <Button
                          circular
                          compact
                          floated="right"
                          color="yellow"
                          icon="cog"
                          as={NavLink}
                          to={`/candidates/candidate/${candidate.id}/update`}
                        />
                        <Header>
                          <span className="detail-header">
                            {candidate.name}
                          </span>
                        </Header>
                        {candidates.experiences.length === 0 &&
                        candidates.educations.length === 0 ? null : candidates
                            .experiences.length === 0 ? (
                          <span>
                            {candidates.educations[0].department}
                            <br />
                          </span>
                        ) : (
                          <span>
                            {candidates.experiences[0].job_title}
                            <br />
                          </span>
                        )}
                        <Icon name="envelope" />
                        {candidate.email}
                        <br />
                        <Divider />

                        {candidates.educations.length === 0 &&
                        candidates.experiences.length === 0 &&
                        candidates.resume.skills.length === 0 ? null : (
                          <span>
                            <br />
                            <DateLabel
                              value={new Date(
                                candidates.resume.creationDate
                              ).toDateString()}
                            />
                            <br />
                            <br />
                          </span>
                        )}

                        {candidates.educations.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Eğitim Geçmişi"
                              className="orbitron"
                            />
                            <br />
                            {candidates.educations.map((education) => (
                              <span>
                                <strong>
                                  {education.nameOfEducationalInstitution}
                                </strong>
                                <br />
                                {education.degree} ・ {education.department}
                                <br />
                                {candidates.experiences.map((experience) => (
                                  <span className="extra">
                                    {new Date(
                                      experience.startingDate
                                    ).getMonth() +
                                      "." +
                                      new Date(
                                        experience.startingDate
                                      ).getFullYear()}
                                    &nbsp;-&nbsp;
                                    {new Date(
                                      experience.graduationDate
                                    ).getMonth() +
                                      "." +
                                      new Date(
                                        experience.gradiationDate
                                      ).getFullYear()}
                                  </span>
                                ))}
                                <br />
                                <br />
                              </span>
                            ))}
                          </Segment>
                        )}

                        {candidates.experiences.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Deneyimleri"
                              className="orbitron"
                            />
                            <br />
                            {candidates.experiences.map((experience) => (
                              <span>
                                <strong>{experience.job_title}</strong>
                                <br />
                                {experience.companyName}
                                <br />
                                <span className="extra">
                                  {new Date(experience.startingDate).getMonth()}
                                  .
                                  {new Date(
                                    experience.startingDate
                                  ).getMonth() +
                                    "." +
                                    new Date(
                                      experience.startingDate
                                    ).getFullYear()}
                                  &nbsp;-&nbsp;
                                  {new Date(
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
                        {candidates.resume.skills.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Yetenekleri"
                              className="orbitron"
                            />
                            <br />
                            {candidates.resume.skills.map((skill) => (
                              <span>・ {skill}&nbsp;&nbsp;&nbsp;</span>
                            ))}
                            <br />
                            <br />
                          </Segment>
                        )}
                        {candidates.resume.languages.length === 0 ? null : (
                          <Segment raised>
                            <Header
                              as="h5"
                              content="Diller"
                              className="orbitron"
                            />
                            <br />
                            {candidates.resume.languages.map((language) => (
                              <span>・ {language}&nbsp;&nbsp;&nbsp;</span>
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
