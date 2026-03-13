import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || (
  window.location.hostname === 'saikumarreddyappidi.github.io'
    ? 'https://smartstudy-api-saikumarreddyappidi.onrender.com'
    : 'http://localhost:8000'
);

const API = axios.create({ baseURL: API_BASE_URL });

API.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default API;
