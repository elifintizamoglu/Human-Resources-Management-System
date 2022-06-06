import React from "react";
import {
  Grid,
  Divider,
  Segment,
  Header,
  Input,
} from "semantic-ui-react";

export default function HighlightedContent() {
  return (
    <Grid>
      <Grid.Row stretched columns="2">
        <Grid.Column>
          <Divider hidden />
          <Divider hidden />
          <Divider hidden />
          <Divider hidden />
          <Segment basic>
            <Header color="violet" textAlign="right">
              <span className="headline-1">Yeni bir işiniz olsun!</span>
            </Header>
          </Segment>
          <Segment raised circular>
            <Input
              transparent
              type="text"
              icon="search"
              size="big"
              placeholder="Search . . ."
            />
          </Segment>
          <Divider hidden />
          <Divider hidden />
          <Divider hidden />
        </Grid.Column>
      </Grid.Row>
    </Grid>
  );
}