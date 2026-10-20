import axios from "axios";

export const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const TOKEN_KEY = "irgs_token";

export const api = axios.create({ baseURL: `${BACKEND_URL}/api`, withCredentials: true });

api.interceptors.request.use((config) => {
  const token = localStorage.getItem(TOKEN_KEY);
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export const fileUrl = (path) => (path ? `${BACKEND_URL}${path}` : null);

export const errMsg = (e, fallback = "Something went wrong") => {
  const d = e?.response?.data?.detail;
  if (typeof d === "string") return d;
  if (Array.isArray(d)) return d.map((x) => x.msg).join(", ");
  return fallback;
};
