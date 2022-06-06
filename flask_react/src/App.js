import "./App.css";
import "semantic-ui-css/semantic.min.css";
import React from "react";
import CandidateAdd from "./pages/CandidateAdd";
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
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
