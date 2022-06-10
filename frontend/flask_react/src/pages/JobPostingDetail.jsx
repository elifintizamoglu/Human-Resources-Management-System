import React, { useState, useEffect } from "react";
import { useParams } from "react-router";
import JobPostingService from "./../services/jobPostingService";
import Headline from "../layouts/Headline";
import DateLabel from "./../layouts/DateLabel";
import {
  Container,
  Header,
  Grid,
  Divider,
  Icon,
  Label,
} from "semantic-ui-react";

export default function JobPostingDetail() {
  let { id } = useParams();

  const [jobPosting, setJobPosting] = useState({});

  let jobPostingService = new JobPostingService();

  useEffect(() => {
    jobPostingService
      .getById(id)
      .then((result) => setJobPosting(result.data.data));
  }, []);

  return (
    <div>
      <Container className="content">
        <Headline content="İş İlanı" />

        <Grid>
          <Grid.Row>
            <Grid.Column width="3" />
            <Grid.Column width="10">
              <Grid.Row>
                <DateLabel
                  value={new Date(jobPosting.postingDate).toDateString()}
                />
                <br />
                <br />
                <br />
          
              </Grid.Row>
              <Grid.Row>
                <Header>
                  <span className="detail-header">
                    <strong>{jobPosting.job_title}</strong>
                  </span>
                </Header>
                {jobPosting.companyName}
                <br />
                <Divider />
                <br />

                {jobPosting.jobDescription}
                <br />
                <br />
                <ul>
                  <li>
                    <strong>Minimum Maaş</strong>
                    &nbsp;&nbsp;
                    {jobPosting.salaryMin}
                  </li>
                  <li>
                    <strong>Maksimum Maaş</strong>
                    &nbsp;&nbsp;
                    {jobPosting.salaryMax}
                  </li>
                  <br />
                </ul>

                <Label circular basic color="yellow" size="large">
                  <Grid>
                    <Grid.Row>
                      <Grid.Column width="2" />
                      <Grid.Column width="2">
                        <Icon name="calendar alternate outline" size="big" />
                      </Grid.Column>
                      <Grid.Column width="10">
                        <span className="orbitron">
                          Son Başvuru
                          <br />
                          {new Date(jobPosting.closingDate).toDateString()}
                        </span>
                      </Grid.Column>
                      <Grid.Column width="2" />
                    </Grid.Row>
                  </Grid>
                </Label>
              </Grid.Row>
            </Grid.Column>
            <Grid.Column width="3" />
          </Grid.Row>
        </Grid>
      </Container>
    </div>
  );
}