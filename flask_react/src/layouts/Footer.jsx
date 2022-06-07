import React from "react";
import { NavLink } from "react-router-dom";
import { Container, Divider, Grid, List, Icon } from "semantic-ui-react";

export default function Footer() {
  return (
    <Container className="footer">
      <Divider />
      <br />

      <Grid>
        <Grid.Row centered>
          <List link horizontal>
            <List.Item as={NavLink} to="/home" content="Ana Sayfa" />
            <List.Item as={NavLink} to="/jobPostings" content="İş İlanları" />
            <List.Item as={NavLink} to="/candidates" content="Adaylar" />
          </List>
        </Grid.Row>
        <Grid.Row centered>
          2022-Necibe Büşra Uylaş ve Elif İntizamoğlu
        </Grid.Row>
        <Grid.Row centered>
          <List link horizontal>
            <List.Item
              href="https://github.com/NecibeBusraUylas"
              target="blank"
            >
              <Icon name="github" size="large" />
            </List.Item>
            <List.Item href="https://github.com/elifintizamoglu" target="blank">
              <Icon name="github" size="large" />
            </List.Item>
            <List.Item
              href="https://www.linkedin.com/in/necibebusrauylas/"
              target="blank"
            >
              <Icon name="linkedin" size="large" />
            </List.Item>
            <List.Item
              href="http://www.linkedin.com/in/elif-intizamoglu"
              target="blank"
            >
              <Icon name="linkedin" size="large" />
            </List.Item>
          </List>
        </Grid.Row>
      </Grid>
      <br />
      <br />
      <br />
    </Container>
  );
}