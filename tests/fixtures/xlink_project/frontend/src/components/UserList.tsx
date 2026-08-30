// Fixture: TS file with fetch() calls — string literal + template literal

export async function fetchUsers() {
  const response = await fetch("/api/users");
  return response.json();
}

export async function fetchUserById(userId: string) {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
}

export async function createUser(data: any) {
  const response = await fetch("/api/users", {
    method: "POST",
    body: JSON.stringify(data),
  });
  return response.json();
}

export async function deleteUser(userId: string) {
  const response = await fetch(`/api/users/${userId}`, {
    method: "DELETE",
  });
  return response.json();
}
