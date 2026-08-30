// Fixture: TS file with axios calls — string literal + template literal
import axios from "axios";

export async function getAdminStats() {
  const response = await axios.get("/api/admin/stats");
  return response.data;
}

export async function updateSettings(settings: any) {
  const response = await axios.post("/api/admin/settings", settings);
  return response.data;
}

export async function getItemDetails(itemId: string) {
  const response = await axios.get(`/api/items/${itemId}`);
  return response.data;
}

export async function bulkUpdate(data: any) {
  const response = await axios({
    url: "/api/admin/bulk",
    method: "PUT",
    data: data,
  });
  return response.data;
}
