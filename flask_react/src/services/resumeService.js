import axios from "axios";

export default class ResumeService {
  add() {
    return axios.post("http://localhost:5000/resumes/add");
  }

  get() {
    return axios.get("http://localhost:5000/resumes/get");
  }

  update(id) {
    return axios.put(`http://localhost:5000/resumes/update?id=${id}`);
  }

  getById(id) {
    return axios.get(`http://localhost:5000/resumes/getById?id=${id}`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/resumes/delete?id=${id}`);
  }
}
