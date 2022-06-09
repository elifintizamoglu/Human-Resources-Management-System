import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import JobPostingService from "./../services/jobPostingService";
import ButtonsOfPagination from "../layouts/ButtonsOfPagination";
import { Card, Label, Button, Icon, Grid, Form } from "semantic-ui-react";

export default function JobPostingList({ type, itemsPerRow, id }) {
  const [jobPostings, setJobPostings] = useState([]);

  const [pageNo, setPageNo] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [numberOfData, setNumberOfData] = useState(0);

  let jobPostingService = new JobPostingService();

  let totalNumberOfPages = Math.ceil(
    numberOfData === 0 ? 1 : numberOfData / pageSize
  );

  useEffect(() => {
    
  }, [pageNo, pageSize, numberOfData]);

  const handlePreviousPage = () => {
    if (pageNo != 1) {
      setPageNo(pageNo - 1);
    }
  };

  const handleNextPage = () => {
    if (pageNo != totalNumberOfPages) {
      setPageNo(pageNo + 1);
    }
  };

  const handlePageSize = (size) => {
    setPageNo(1);
    setPageSize(size);
  };
  const handleFilter = () => {
    setPageNo(1);
    setPageSize(10);
    jobPostingService
      .getAll()
      .then((result) => setNumberOfData(result.data.data.length));
    jobPostingService
      .getAll()
      .then((result) => setJobPostings(result.data.data));
  };

  const handleClearFilter = () => {
    window.location.reload();
  };

  return (
    <Grid>
      {type === "filtered" && (
        <Grid.Row>
          <Grid.Column width="12" textAlign="center">
            <ButtonsOfPagination
              previous={() => handlePreviousPage()}
              next={() => handleNextPage()}
              pageContent={pageNo + " / " + totalNumberOfPages}
              pageSizeOne={() => handlePageSize(10)}
              pageSizeTwo={() => handlePageSize(20)}
              pageSizeThree={() => handlePageSize(50)}
              pageSizeFour={() => handlePageSize(100)}
              pageSizeContent={"Sayfa Boyutu: " + pageSize}
            />
          </Grid.Column>
          <Grid.Column width="4" />
        </Grid.Row>
      )}

      <Grid.Row>
        <Grid.Column width={type === "filtered" ? "12" : "16"}>
          <Card.Group itemsPerRow={itemsPerRow}>
            {jobPostings.map((jobPosting) => (
              <Card raised key={jobPosting.id}>
                <Card.Content>
                  <Card.Header className="montserrat">
                    {jobPosting.jobTitle?.title}
                  </Card.Header>
                  <Card.Meta>
                    {jobPosting.companyName}
    
                  </Card.Meta>
                  <Card.Description className="orbitron">
                    <strong>Yayınlanma Tarihi</strong>
                    &nbsp;&nbsp;
                    {new Date(jobPosting.postingDate).toDateString()}
                    <br />
                    <strong>Son Başvuru</strong>
                    &nbsp;&nbsp;
                    {new Date(jobPosting.closingDate).toDateString()}
                  </Card.Description>
                </Card.Content>
                <Card.Content>
                  {type === "recently" && (
                    <Icon name="fire" size="big" color="yellow" />
                  )}
                  <Button
                    circular
                    compact
                    floated="right"
                    color="violet"
                    content="Detayları Görüntüle"
                    as={NavLink}
                    to={`/jobPostings/jobPosting/${jobPosting.id}`}
                  />
                </Card.Content>
              </Card>
            ))}
          </Card.Group>
        </Grid.Column>

        {type === "filtered" && (
          <Grid.Column width="4">
            <Form>
              <Form.TextArea
                name="jobTitle"
                placeholder="Ünvan"
              />
              <br />

              <Button
                circular
                fluid
                color="yellow"
                content="Filtrele"
                onClick={() => handleFilter()}
              />
              <br />
              <Button
                circular
                fluid
                color="pink"
                content="Filtreyi Temizle"
                onClick={() => handleClearFilter()}
              />
            </Form>
          </Grid.Column>
        )}
      </Grid.Row>
    </Grid>
  );
}
