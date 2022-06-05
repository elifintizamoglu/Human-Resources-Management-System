import React from "react";


import HomeLayout from "./HomeLayout";

//import JobPostingLayout from "./JobPostingLayout";
//import CandidateLayout from "./CandidateLayout";
//import EmployerLayout from "./EmployerLayout";
import { Container } from "semantic-ui-react";

export default function Dashboard() {
  return (
    <Container className="dashboard">
      
      <Route exact path="/" component={HomeLayout} />
      <Route exact path="/home" component={HomeLayout} />

      
    </Container>
  );
}