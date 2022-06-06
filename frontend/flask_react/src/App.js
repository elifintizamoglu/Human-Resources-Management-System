import "./App.css";
import "semantic-ui-css/semantic.min.css";
import React from "react";
import CandidateAdd from "./pages/CandidateAdd";
import Footer from "./layouts/Footer";
import Navi from "./layouts/Navi";
import {Route} from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";


function App() {
  return (
    <div className="App">
      <Navi/>
      
        <Route exact path="/" component={HomeLayout} />
        <Route exact path="/home" component={HomeLayout} />
        <Route exact path="/candidate/add" component={CandidateAdd} />
      
      <Footer/>
    </div>
  );
}

export default App;