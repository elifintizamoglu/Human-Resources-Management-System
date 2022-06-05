import axios from "axios";

export default class CandidateService {
  get() {
    return axios.get("http://localhost:5000/candidates/get");
  }

  update(id) {
    return axios.put(`http://localhost:5000/candidates/update?id=${id}`);
  }

  getById(id) {
    return axios.get(`http://localhost:5000/candidates/getById?id=${id}`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/candidates/delete?id=${id}`);
  }
}