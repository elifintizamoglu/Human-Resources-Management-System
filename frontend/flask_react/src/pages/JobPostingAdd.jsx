import React, { useEffect, useState } from "react";
import { useParams } from "react-router";
import { Formik, useFormik } from "formik";
import * as Yup from "yup";
import Headline from "./../layouts/Headline";
import JobPostingService from "../services/jobPostingService";
import JobTitleService from "../services/jobTitleService";
import CityService from "../services/cityService";
import WorkingTimeService from "../services/workingTimeService";
import WorkingTypeService from "../services/workingTypeService";
import DateLabel from "./../layouts/DateLabel";
import MessageModal from "./../layouts/MessageModal";
import { Container, Grid, Label, Form, Button } from "semantic-ui-react";

export default function JobPostingAdd() {
  let { id } = useParams();

  const [jobTitles, setJobTitles] = useState([]);
  const [cities, setCities] = useState([]);
  const [workingTimes, setWorkingTimes] = useState([]);
  const [workingTypes, setWorkingTypes] = useState([]);
  const [open, setOpen] = useState(false);

  let jobPostingService = new JobPostingService();
  let jobTitleService = new JobTitleService();
  let cityService = new CityService();
  let workingTimeService = new WorkingTimeService();
  let workingTypeService = new WorkingTypeService();

  useEffect(() => {
    jobTitleService.getAll().then((result) => setJobTitles(result.data.data));
    cityService.getAll().then((result) => setCities(result.data.data));
    workingTimeService
      .getAll()
      .then((result) => setWorkingTimes(result.data.data));
    workingTypeService
      .getAll()
      .then((result) => setWorkingTypes(result.data.data));
  }, []);

  const jobTitleOptions = jobTitles.map((jobTitle) => ({
    key: jobTitle.id,
    text: jobTitle.title,
    value: jobTitle,
  }));

  const cityOptions = cities.map((city) => ({
    key: city.id,
    text: city.city,
    value: city,
  }));

  const workingTimeOptions = workingTimes.map((workingTime) => ({
    key: workingTime.id,
    text: workingTime.time,
    value: workingTime,
  }));

  const workingTypeOptions = workingTypes.map((workingType) => ({
    key: workingType.id,
    text: workingType.type,
    value: workingType,
  }));

  const initialValues = {
    employer: { id: id },
    jobTitle: "",
    city: "",
    workingTime: "",
    workingType: "",
    jobDescription: "",
    numberOfOpenPositions: "",
    salaryMin: "",
    salaryMax: "",
    closingDate: "",
  };

  const validationSchema = Yup.object({
    jobTitle: Yup.object().required("Zorunlu Alan"),
    city: Yup.object().required("Zorunlu Alan"),
    workingTime: Yup.object().required("Zorunlu Alan"),
    workingType: Yup.object().required("Zorunlu Alan"),
    jobDescription: Yup.string()
      .max(2300, "150 karakterden fazla olamaz.")
      .required("Zorunlu Alan"),
    numberOfOpenPositions: Yup.number()
      .required("Zorunlu Alan"),
    salaryMin: Yup.string(),
    salaryMax: Yup.string(),
    closingDate: Yup.date().required("Zorunlu Alan"),
  });

  const onSubmit = (values, { resetForm }) => {
    console.log(values);
    jobPostingService.add(values);
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
        <Headline content="İş İlanı Yayınla" />

        <Grid>
          <Grid.Row>
            <Grid.Column width="3" />
            <Grid.Column width="10">
              <DateLabel value={new Date().toDateString()} />

              <Formik>
                <Form onSubmit={formik.handleSubmit}>
                  <Form.TextArea
                    name="companyName"
                    label="Firma Adı"
                    onChange={(event, data) =>
                      handleChange("companyName", data.value)
                    }
                    value={formik.values.companyName}
                  />
                  {formik.errors.companyName && formik.touched.companyName && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.companyName}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <Form.TextArea
                    name="jobTitle"
                    label="Ünvan"
                    onChange={(event, data) =>
                      handleChange("jobTitle", data.value)
                    }
                    value={formik.values.jobTitle}
                  />
                  {formik.errors.jobTitle && formik.touched.jobTitle && (
                    <span>
                      <Label
                        basic
                        pointing
                        color="pink"
                        className="orbitron"
                        content={formik.errors.jobTitle}
                      />
                      <br />
                      <br />
                    </span>
                  )}
                  <Form.TextArea
                    name="jobDescription"
                    label="İşin Tanımı"
                    onChange={(event, data) =>
                      handleChange("jobDescription", data.value)
                    }
                    value={formik.values.jobDescription}
                  />
                  {formik.errors.jobDescription &&
                    formik.touched.jobDescription && (
                      <span>
                        <Label
                          basic
                          pointing
                          color="pink"
                          className="orbitron"
                          content={formik.errors.jobDescription}
                        />
                        <br />
                        <br />
                      </span>
                    )}
                  <Form.Group widths="equal">
                    <Form.Input
                      name="closingDate"
                      label="Son Başvuru"
                      placeholder="GG-AA-YYYY"
                      onChange={(event, data) =>
                        handleChange("closingDate", data.value)
                      }
                      value={formik.values.closingDate}
                    />
                  </Form.Group>
                  <Grid>
                    <Grid.Row columns="equal">
                      <Grid.Column>
                        {formik.errors.closingDate &&
                          formik.touched.closingDate && (
                            <span>
                              <Label
                                basic
                                pointing
                                color="pink"
                                className="orbitron"
                                content={formik.errors.closingDate}
                              />
                              <br />
                              <br />
                            </span>
                          )}
                      </Grid.Column>
                    </Grid.Row>
                  </Grid>
                  <Form.Group widths="equal">
                    <Form.Input
                      name="salaryMin"
                      label="Minimum Ücret"
                      placeholder="5000 ₺"
                      onChange={(event, data) =>
                        handleChange("salaryMin", data.value)
                      }
                      value={formik.values.salaryMin}
                    />
                    <Form.Input
                      name="salaryMax"
                      label="Maksimum Ücret"
                      placeholder="10000 ₺"
                      onChange={(event, data) =>
                        handleChange("salaryMax", data.value)
                      }
                      value={formik.values.salaryMax}
                    />
                  </Form.Group>
                  <Grid>
                    <Grid.Row columns="equal">
                      <Grid.Column>
                        {formik.errors.salaryMin && formik.touched.salaryMin && (
                          <span>
                            <Label
                              basic
                              pointing
                              color="pink"
                              className="orbitron"
                              content={formik.errors.salaryMin}
                            />
                            <br />
                          </span>
                        )}
                      </Grid.Column>
                      <Grid.Column>
                        {formik.errors.salaryMax && formik.touched.salaryMax && (
                          <span>
                            <Label
                              basic
                              pointing
                              color="pink"
                              className="orbitron"
                              content={formik.errors.salaryMax}
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
                    content="Yayınla"
                  />
                </Form>
              </Formik>
            </Grid.Column>
            <Grid.Column width="3" />
          </Grid.Row>
        </Grid>

        <MessageModal
          onClose={() => handleModal(false)}
          onOpen={() => handleModal(true)}
          open={open}
          content="Waiting for posting confirmation !"
        />
      </Container>
    </div>
  );
}