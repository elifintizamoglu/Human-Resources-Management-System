import axios from "axios";

export default class AuthService {
  loginCandidate(values) {
    return axios
      .all([axios.get(`http://localhost:5000/login/candidate`)])
      .then(axios.post(`http://localhost:5000/login/candidate`, values));
  }

  loginEmployer(values) {
     return axios
       .all([axios.get(`http://localhost:5000/login/employer`)])
       .then(axios.post(`http://localhost:5000/login/employer`, values));
  }

  signUpCandidate(values) {
     return axios
       .all([axios.get(`http://localhost:5000/sign-up/candidate`)])
       .then(axios.post(`http://localhost:5000/sign-up/candidate`, values));
  }

  signUpEmployer(values) {
     return axios
       .all([axios.get(`http://localhost:5000/sign-up/employer`)])
       .then(axios.post(`http://localhost:5000/sign-up/employer`, values));
  }

  logout() {
    return axios(` http://localhost:5000/logout`);
  }
}