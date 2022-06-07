import "./App.css";
import "semantic-ui-css/semantic.min.css";
import React from "react";
import CandidateLayout from "./layouts/CandidateLayout";
import CandidateAdd from "./pages/CandidateAdd";
import CandidateDetail from "./pages/CandidateDetails";
import CandidateUpdate from "./pages/CandidateUpdate";
import Footer from "./layouts/Footer";
import Navi from "./layouts/Navi";
import { Routes, Route } from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";

function App() {
  return (
    <div className="App">
      <Navi />
      <Routes>
        <Route exact path="/" component={HomeLayout} />
        <Route exact path="/home" component={HomeLayout} />
        <Route exact path="/candidate/add" component={CandidateAdd} />
        <Route exact path="/candidates" component={CandidateLayout} />
        <Route exact path="/candidates/candidate/:id" component={CandidateDetail}/>
        <Route exact path="/candidates/candidate/:id/update" component={CandidateUpdate} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
