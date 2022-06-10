import "./App.css";
import "semantic-ui-css/semantic.min.css";
import React from "react";
import CandidateLayout from "./layouts/CandidateLayout";
import CandidateAdd from "./pages/CandidateAdd";
import CandidateDetail from "./pages/CandidateDetails";
import CandidateUpdate from "./pages/CandidateUpdate";
import JobPostingLayout from "./layouts/JobPostingLayout";
import JobPostingDetail from "./pages/JobPostingDetail";
import Footer from "./layouts/Footer";
import Navi from "./layouts/Navi";
import EducationAdd from "./pages/EducationAdd";
import ExperienceAdd from "./pages/ExperienceAdd";
import HomeLayout from "./layouts/HomeLayout";
import { Switch, Route } from "react-router-dom";


function App() {
  return (
    <div className="App">
      <Navi />
      <Switch>
        <Route exact path="/" component={HomeLayout} />
        <Route exact path="/home" component={HomeLayout} />
        <Route exact path="/candidate/add" component={CandidateAdd} />
        <Route exact path="/candidates" component={CandidateLayout} />
        <Route exact path="/candidates/candidate/:id" component={CandidateDetail}/>
        <Route exact path="/candidates/candidate/:id/update" component={CandidateUpdate} />
        <Route exact path="/jobPostings" component={JobPostingLayout} />
        <Route exact path="/jobPostings/jobPosting/:id" component={JobPostingDetail} />
        <Route exact path="/education/add" component={EducationAdd} />
        <Route exact path="/experience/add" component={ExperienceAdd} />
      </Switch>
      <Footer />
    </div>
  );
}

export default App;