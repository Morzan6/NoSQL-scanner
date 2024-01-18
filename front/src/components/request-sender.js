import axios from "axios";

export default async function requestSender(method, address, data={}, token='') {
  return await axios({
    method: method,
    url: address,
    data: data,
    responseType: "json",
    headers: { ContextType: "application/jsom", Authorization: `Bearer ${token}`},
  });
}
