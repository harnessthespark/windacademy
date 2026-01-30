import { cookies } from "next/headers";
import { decodeJwt } from "./tokens";

export async function getSession() {
  const cookieStore = await cookies();
  const accessToken = cookieStore.get("access_token")?.value;

  if (!accessToken) {
    return null;
  }

  const payload = decodeJwt(accessToken);
  if (!payload) {
    return null;
  }

  return {
    userId: payload.user_id,
    accessToken,
  };
}
