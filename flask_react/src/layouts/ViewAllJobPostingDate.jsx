import React from "react";
import { NavLink } from "react-router-dom";
import { Container, Grid, Button } from "semantic-ui-react";

export default function ViewAllJobPostingsByPostingDate() {
  return (
    <Container className="view-all-job-postings-by-posting-date">
      <Grid>
        <Grid.Row centered>
          <Button
            circular
            color="yellow"
            as={NavLink}
            to={"/jobPostings"}
            content="View All Job Postings by Posting Date"
          />
        </Grid.Row>
      </Grid>
    </Container>
  );
}