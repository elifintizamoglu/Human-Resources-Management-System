import axios from "axios";

export default class EmployerService {
  get() {
    return axios.get("http://localhost:5000/employers/get");
  }

  update(id) {
    return axios.put(`http://localhost:5000/employers/update?id=${id}`);
  }

  getById(id) {
    return axios.get(`http://localhost:5000/employers/getById?id=${id}`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/employers/delete?id=${id}`);
  }
}