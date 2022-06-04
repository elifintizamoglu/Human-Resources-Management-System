import React from "react";
import { Route } from "react-router-dom";
import Navi from "./Navi";
import Footer from "./Footer";
import HomeLayout from "./HomeLayout";
import JobPostingLayout from "./JobPostingLayout";
import CandidateLayout from "./CandidateLayout";
import EmployerLayout from "./EmployerLayout";

export default function Dashboard() {
  return (
    <Container className="dashboard">
      <Navi />

      <Route exact path="/" component={HomeLayout} />
      <Route exact path="/home" component={HomeLayout} />
      <Route exact path="/jobPostings" component={JobPostingLayout} />

      <Route exact path="/candidates" component={CandidateLayout} />
     
      <Route exact path="/employers" component={EmployerLayout} />
    
      <Footer />
    </Container>
  );
}