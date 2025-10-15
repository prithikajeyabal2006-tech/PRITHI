import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:8000' });

export const analyzeAudio = (file, candidateName) => {
  const form = new FormData();
  form.append('audio', file);
  form.append('candidate_name', candidateName);
  return API.post('/analyze', form, { headers: { 'Content-Type': 'multipart/form-data' } });
};
