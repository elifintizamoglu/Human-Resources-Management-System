import React from "react";
import Headline from "./Headline";
import JobPostingList from "../pages/JobPostingList";
import { Container } from "semantic-ui-react";

export default function JobPostingLayout() {
  return (
    <div>
      <Container className="content">
        <Headline content="İş İlanları" />

        <JobPostingList type="filtered" itemsPerRow="2" />
      </Container>
    </div>
  );
}