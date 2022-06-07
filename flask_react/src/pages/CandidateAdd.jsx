import React, { useState } from "react";
import { Formik, useFormik } from "formik";
import * as Yup from "yup";
import Headline from "../layouts/Headline";
import DateLabel from "./../layouts/DateLabel";
import { Container, Grid, Label, Form, Button } from "semantic-ui-react";
import AuthService from "../services/authService";

export default function CandidateAdd() {
  const [setOpen] = useState(false);

  let authService = new AuthService();

  const initialValues = {
    name: "",
    identityNumber: "",
    dateOfBirth: "",
    email: "",
    password: "",
  };

  const validationSchema = Yup.object({
    name: Yup.string().required("Zorunlu Alan"),
    identityNumber: Yup.string()
      .length(11, "11 karakter gereklidir.")
      .required("Zorunlu Alan"),
    dateOfBirth: Yup.date().required("Zorunlu Alan"),
    email: Yup.string()
      .email("Geçersiz Email")
      .required("Zorunlu Alan"),
    password: Yup.string().required("Zorunlu Alan"),
  });

  const onSubmit = (values, { resetForm }) => {
    console.log(values);
    authService.loginCandidate(values);
    handleModal(true);
    setTimeout(() => {
      resetForm();
    }, 100);
  };

  const formik = useFormik({
    initialValues: initialValues,
    validationSchema: validationSchema,
    onSubmit: onSubmit,
  });

  const handleModal = (value) => {
    setOpen(value);
  };

  const handleChange = (fieldName, value) => {
    formik.setFieldValue(fieldName, value);
  };

  return (
    <div>
      <Container className="content">
        <Headline content="Aday Girişi" />

        <Grid>
          <Grid.Row>
            <Grid.Column width="3" />
            <Grid.Column width="10">
              <DateLabel value={new Date().toDateString()} />

              <Formik>
                <Form onSubmit={formik.handleSubmit}>
                  <Form.Input
                    name="name"
                    label="Ad Soyad"
                    onChange={(event, data) => handleChange("name", data.value)}
                    value={formik.values.name}
                  />
                  {formik.errors.name && formik.touched.name && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.name}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <Form.Group widths="equal">
                    <Form.Input
                      name="identityNumber"
                      label="TC Kimlik Numarası"
                      placeholder="XXXXXXXXXXX"
                      onChange={(event, data) =>
                        handleChange("identityNumber", data.value)
                      }
                      value={formik.values.identityNumber}
                    />
                    <Form.Input
                      name="dateOfBirth"
                      label="Doğum Tarihi"
                      placeholder="GG-AA-YYYY"
                      onChange={(event, data) =>
                        handleChange("dateOfBirth", data.value)
                      }
                      value={formik.values.dateOfBirth}
                    />
                  </Form.Group>
                  <Grid>
                    <Grid.Row columns="equal">
                      <Grid.Column>
                        {formik.errors.identityNumber &&
                          formik.touched.identityNumber && (
                            <span>
                              <Label
                                basic
                                pointing
                                color="pink"
                                className="orbitron"
                                content={formik.errors.identityNumber}
                              />
                              <br />
                              <br />
                            </span>
                          )}
                      </Grid.Column>
                      <Grid.Column>
                        {formik.errors.dateOfBirth &&
                          formik.touched.dateOfBirth && (
                            <span>
                              <Label
                                basic
                                pointing
                                color="pink"
                                className="orbitron"
                                content={formik.errors.dateOfBirth}
                              />
                              <br />
                              <br />
                            </span>
                          )}
                      </Grid.Column>
                    </Grid.Row>
                  </Grid>
                  <Form.Input
                    name="email"
                    label="E-mail"
                    placeholder="ornek@ornek.com"
                    onChange={(event, data) =>
                      handleChange("email", data.value)
                    }
                    value={formik.values.email}
                  />
                  {formik.errors.email && formik.touched.email && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.email}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <Form.Input
                    name="password"
                    label="Şifre"
                    onChange={(event, data) =>
                      handleChange("password", data.value)
                    }
                    value={formik.values.password}
                  />
                  {formik.errors.password && formik.touched.password && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.password}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <br />

                  <Button
                    circular
                    fluid
                    type="submit"
                    color="yellow"
                    content="Kayıt Ol"
                  />
                </Form>
              </Formik>
            </Grid.Column>
            <Grid.Column width="3" />
          </Grid.Row>
        </Grid>
      </Container>
    </div>
  );
}
