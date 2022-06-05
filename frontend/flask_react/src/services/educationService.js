import axios from "axios";

export default class EducationService {
  add() {
    return axios.post("http://localhost:5000/educations/add");
  }

  get() {
    return axios.get("http://localhost:5000/educations/get");
  }

  update(id) {
    return axios.put(`http://localhost:5000/educations/update?id=${id}`);
  }

  getById(id) {
    return axios.get(`http://localhost:5000/educations/getById?id=${id}`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/educations/delete?id=${id}`);
  }
}
