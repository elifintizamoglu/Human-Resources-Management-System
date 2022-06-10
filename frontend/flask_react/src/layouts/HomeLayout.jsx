import React from "react";
import HighlightedContent from "./HighlightedContent";
import JobPostingList from "./../pages/JobPostingList";

export default function HomeLayout() {
  return (
    <div>
      <HighlightedContent />
      <br />
      <br />

      <JobPostingList type="recently" itemsPerRow="3" /> 
    </div>
  );
}