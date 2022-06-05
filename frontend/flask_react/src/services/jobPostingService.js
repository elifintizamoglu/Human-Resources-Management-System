import axios from "axios";

export default class JobPostingService {
  add() {
    return axios.post("http://localhost:5000/jobPostings/add");
  }

  get() {
    return axios.get("http://localhost:5000/jobPostings/get");
  }

  update(id) {
    return axios.put(`http://localhost:5000/jobPostings/update?id=${id}`);
  }

  getById(id) {
    return axios.get(`http://localhost:5000/jobPostings/getById?id=${id}`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/jobPostings/delete?id=${id}`);
  }
}
