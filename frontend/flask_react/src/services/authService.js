import axios from "axios";

export default class AuthService {
  login(values) {
    return axios
      .all([axios.get(`http://localhost:5000/login`)])
      .then(axios.post(`http://localhost:5000/login`, values));
  }

  signUp(values) {
     return axios
       .all([axios.get(`http://localhost:5000/sign-up`)])
       .then(axios.post(`http://localhost:5000/sign-up`, values));
  }

  logout() {
    return axios(` http://localhost:5000/logout`);
  }
}