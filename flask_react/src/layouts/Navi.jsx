import React from "react";
import { NavLink } from "react-router-dom";
import LogIn from "./LogIn";
import SignUp from "./SignUp";
import { Menu, Container, Header } from "semantic-ui-react";

export default function Navi() {
  return (
    <Menu borderless fixed="top">
      <Container>
        <Menu.Item color="violet" position="left">
          <Header as="h4" color="violet" className="orbitron" icon="cube" content="İnsan Kaynakları Yönetim Sistemi"/>
        </Menu.Item>
        <Menu.Item
          as={NavLink}
          to="/home"
          icon="circle notched"
          content="Ana Sayfa"
        />
        <Menu.Item as={NavLink} to="/jobPostings" icon="list alternate outline" content="İş İlanları" />
        <Menu.Item as={NavLink} to="/candidates" icon="user outline" content="Adaylar"/>
        <Menu.Menu position="right">
          <Menu.Item position="right">
            <LogIn />
          </Menu.Item>
          <Menu.Item position="right">
            <SignUp />
          </Menu.Item>
        </Menu.Menu>
      </Container>
    </Menu>
  );
}

