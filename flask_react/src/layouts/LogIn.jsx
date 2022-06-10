import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { Button, Grid, Header, Icon, Modal, Segment } from "semantic-ui-react";

export default function LogIn() {
  const [open, setOpen] = useState(false);
  const handleModal = (value) => {
    setOpen(value);
  };

  return (
    <span>
      <Button circular color="pink" content="Giriş Yap" onClick={() => handleModal(true)} />

      <Modal basic dimmer onClose={() => handleModal(false)} onOpen={() => handleModal(true)} open={open} size="small">
        <Header icon as="h2" className="orbitron">
          <Icon name="sign-in" />
             Aday olarak giriş yapmak için pembe butonu, iş ilanı eklemek için sarı butonu seçiniz.
        </Header>
        <Modal.Actions>
          <Grid>
            <Grid.Row>
              <Grid.Column width="7">
                <Button circular fluid color="pink" content="Aday Girişi" as={NavLink} to={"#"} onClick={() => setOpen(false)} ></Button>
              </Grid.Column>
              <Grid.Column width="2">
                <Segment basic className="or"> ya da</Segment>
              </Grid.Column>
              <Grid.Column width="7">
                <Button circula fluid color="yellow" content="İş İlanı Ekleme" as={NavLink} to={"#"} onClick={() => setOpen(false)}></Button>
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Modal.Actions>
      </Modal>
    </span>
  );
}