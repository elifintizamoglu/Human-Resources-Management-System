import axios from "axios";

export default class CandidateService {
  update(id) {
    return axios.put(`http://localhost:5000/candidates/update?id=${id}`);
  }

  get() {
    return axios.get("http://localhost:5000/candidates/get");
  }

  getById(id) {
    return axios.get(`http://localhost:5000/candidates/getById?id=${id}`);
  }

  getAllInfo() {
    return axios.get(`http://localhost:5000//candidates/get/<id>/all/info`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/candidates/delete?id=${id}`);
  }
}