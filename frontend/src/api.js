import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.PROD ? '' : 'http://localhost:8000',
});

export default api;