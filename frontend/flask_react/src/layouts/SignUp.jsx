import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { Button, Header, Icon, Modal } from "semantic-ui-react";

export default function SignUp() {
  const [open, setOpen] = useState(false);

  const handleModal = (value) => {
    setOpen(value);
  };

  return (
    <span>
      <Button
        circular
        color="yellow"
        content="Kayıt Ol"
        onClick={() => handleModal(true)}
      />

      <Modal
        basic
        dimmer
        onClose={() => handleModal(false)}
        onOpen={() => handleModal(true)}
        open={open}
        size="small"
      >
        <Header icon as="h2" className="orbitron">
          <Icon name="paper plane" />
              Yeni Hesap Oluşturma
        </Header>

        <Modal.Actions>
                <Button
                  circular
                  fluid
                  color="pink"
                  content="Aday"
                  as={NavLink}
                  to={"/sign-up"}
                  onClick={() => setOpen(false)}
                />      
        </Modal.Actions>
      </Modal>
    </span>
  );
}