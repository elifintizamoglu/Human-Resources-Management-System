import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import CandidateService from "./../services/candidateService";
import { Card} from "semantic-ui-react";

export default function CandidateList() {
    const [candidates, setCandidates] = useState([]);

    let candidateService = new CandidateService();

    useEffect(() => {
        candidateService.getAllInfo().then((result) => setCandidates(result.data.data));
    }, []);

    return (
      <Card.Group itemsPerRow="4">
        {candidates.map((candidate) => (
          <Card raised key={candidate.id}>
            <Card.Content
              textAlign="center"
              as={NavLink}
              to={`/candidates/candidate/${candidate?.id}`}
            >
              <Card.Header className="montserrat">
                {candidate?.name}
              </Card.Header>
              <Card.Meta>
                {candidates.experiences.length === 0 &&
                candidates.educations.length === 0 ? (
                  <br />
                ) : candidates.experiences.length === 0 ? (
                  candidates.educations[0].department
                ) : (
                  candidates.experiences[0].jobTitle?.title
                )}
              </Card.Meta>
            </Card.Content>
          </Card>
        ))}
      </Card.Group>
    );
}