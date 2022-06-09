import axios from "axios";

export default class ExperienceService {
  add() {
    return axios
      .all([axios.get(`http://localhost:5000/experiences/add`)])
      .then(axios.post(`http://localhost:5000/experiences/add`));
  }

  get() {
    return axios.get("http://localhost:5000/experiences/get");
  }

  update(id) {
    return axios.put(`http://localhost:5000/experiences/update?id=${id}`);
  }

  getById(id) {
    return axios.get(`http://localhost:5000/experiences/getById?id=${id}`);
  }

  delete(id) {
    return axios.delete(`http://localhost:5000/experiences/delete?id=${id}`);
  }
}
