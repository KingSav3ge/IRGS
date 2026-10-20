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

export const fmtDate = (date, calendar) => {
  if (!date) return "";
  if (calendar === "roman") return `${date.replace(/^0+/, "")} BCE`;
  if (calendar === "eldoria") return `Day ${parseInt(date.split("-").pop(), 10)} of the vigil`;
  const m = date.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  if (!m) return date;
  const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  return `${parseInt(m[3], 10)} ${months[parseInt(m[2], 10) - 1] || ""} ${parseInt(m[1], 10)}`;
};

export const errMsg = (e, fallback = "Something went wrong") => {
  const d = e?.response?.data?.detail;
  if (typeof d === "string") return d;
  if (Array.isArray(d)) return d.map((x) => x.msg).join(", ");
  return fallback;
};
