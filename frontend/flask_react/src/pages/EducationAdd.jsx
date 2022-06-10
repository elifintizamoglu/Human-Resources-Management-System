import React, { useState } from "react";
import { useParams } from "react-router";
import { Formik, useFormik } from "formik";
import * as Yup from "yup";
import Headline from "../layouts/Headline";
import DateLabel from "./../layouts/DateLabel";
import EducationService from "./../services/educationService";
import ResumeService from "./../services/resumeService";
import { Container, Grid, Form, Label, Button } from "semantic-ui-react";

export default function EducationAdd() {
  let { id } = useParams();

  const [setOpen] = useState(false);

  let educationService = new EducationService();
  let resumeService = new ResumeService();

  const initialValues = {
    resume_id: { id: id },
    nameOfEducationalInstitution: "",
    department: "",
    degree: "",
    startingDate: "",
    graduationDate: "",
  };

  const validationSchema = Yup.object({
    nameOfEducationalInstitution: Yup.string().required("Zorunlu Alan"),
    department: Yup.string().required("Zorunlu Alan"),
    degree: Yup.string().required("Zorunlu Alan"),
    startingDate: Yup.date().required("Zorunlu Alan"),
    graduationDate: Yup.date(),
  });

  const onSubmit = (values, { resetForm }) => {
    educationService.add(values);
    resumeService.update({ id: id });
    console.log(values);
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
        <Headline content="Eğitim Bilgisi Ekle" />
        <Grid>
          <Grid.Row>
            <Grid.Column width="3" />
            <Grid.Column width="10">
              <DateLabel value={new Date().toDateString()} />

              <Formik>
                <Form onSubmit={formik.handleSubmit}>
                  <Form.Input
                    name="nameOfEducationalInstitution"
                    label="Eğitim Kurumu"
                    onChange={(event, data) =>
                      handleChange("nameOfEducationalInstitution", data.value)
                    }
                    value={formik.values.nameOfEducationalInstitution}
                  />
                  {formik.errors.nameOfEducationalInstitution &&
                    formik.touched.nameOfEducationalInstitution && (
                      <span>
                        <Label
                          basic
                          pointing
                          color="pink"
                          className="orbitron"
                          content={formik.errors.nameOfEducationalInstitution}
                        />
                        <br />
                        <br />
                      </span>
                    )}
                  <Form.Input
                    name="department"
                    label="Departman"
                    onChange={(event, data) =>
                      handleChange("department", data.value)
                    }
                    value={formik.values.department}
                  />
                  {formik.errors.department && formik.touched.department && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.department}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <Form.Input
                    name="degree"
                    label="Derece"
                    onChange={(event, data) =>
                      handleChange("degree", data.value)
                    }
                    value={formik.values.degree}
                  />
                  {formik.errors.degree && formik.touched.degree && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.degree}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <Form.Group widths="equal">
                    <Form.Input
                      name="startingDate"
                      label="Başlangıç Tarihi"
                      placeholder="GG-AA-YYYY"
                      onChange={(event, data) =>
                        handleChange("startingDate", data.value)
                      }
                      value={formik.values.startingDate}
                    />
                    <Form.Input
                      name="graduationDate"
                      label="Mezuniyet Tarihi"
                      placeholder="GG-AA-YYYY"
                      onChange={(event, data) =>
                        handleChange("graduationDate", data.value)
                      }
                      value={formik.values.graduationDate}
                    />
                  </Form.Group>
                  <Grid>
                    <Grid.Row columns="equal">
                      <Grid.Column>
                        {formik.errors.startingDate &&
                          formik.touched.startingDate && (
                            <span>
                              <Label
                                basic
                                pointing
                                color="pink"
                                className="orbitron"
                                content={formik.errors.startingDate}
                              />
                              <br />
                            </span>
                          )}
                      </Grid.Column>
                      <Grid.Column>
                        {formik.errors.graduationDate &&
                          formik.touched.graduationDate && (
                            <span>
                              <Label
                                basic
                                pointing
                                color="pink"
                                className="orbitron"
                                content={formik.errors.graduationDate}
                              />
                              <br />
                            </span>
                          )}
                      </Grid.Column>
                    </Grid.Row>
                  </Grid>
                  <br />

                  <Button
                    circular
                    fluid
                    type="submit"
                    color="yellow"
                    content="Ekle"
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