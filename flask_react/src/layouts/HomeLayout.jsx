import React from "react";
import HighlightedContent from "./HighlightedContent";
import JobPostingList from "./../pages/JobPostingList";
import { Divider, Icon } from "semantic-ui-react";

export default function HomeLayout() {
  return (
    <div>
      <HighlightedContent />

      <Divider horizontal>
        <Icon name="bell outline" /> Recently Posted
      </Divider>
      <br />
      <br />

      <JobPostingList type="recently" itemsPerRow="3" /> 
    </div>
  );
}