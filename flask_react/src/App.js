import "./App.css";
import "semantic-ui-css/semantic.min.css";
import React from "react";
import Navi from "./layouts/Navi";
import Footer from "./layouts/Footer";
import CandidateLayout from "./layouts/CandidateLayout";
import JobPostingLayout from "./layouts/JobPostingLayout";
import HomeLayout from "./layouts/HomeLayout";
import CandidateAdd from "./pages/CandidateAdd";
import CandidateDetail from "./pages/CandidateDetails";
import CandidateUpdate from "./pages/CandidateUpdate";
import JobPostingDetail from "./pages/JobPostingDetail";
import EducationAdd from "./pages/EducationAdd";
import ExperienceAdd from "./pages/ExperienceAdd";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Navi />
      <Routes>
        <Route exact path="/" element={<HomeLayout/>} />
        <Route exact path="/home" element={<HomeLayout/>} />
        <Route exact path="/candidate/add" element={<CandidateAdd/>} />
        <Route exact path="/candidates" element={<CandidateLayout/>} />
        <Route
          exact
          path="/candidates/candidate/:id"
          element={<CandidateDetail/>}
        />
        <Route
          exact
          path="/candidates/candidate/:id/update"
          element={<CandidateUpdate/>}
        />
        <Route exact path="/jobPostings" element={<JobPostingLayout/>} />
        <Route
          exact
          path="/jobPostings/jobPosting/:id"
          element={<JobPostingDetail/>}
        />
        <Route exact path="/education/add" element={<EducationAdd/>} />
        <Route exact path="/experience/add" element={<ExperienceAdd/>} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
