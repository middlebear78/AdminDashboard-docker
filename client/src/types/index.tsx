export interface User {
    user_id: string;
    first_name: string;
    last_name: string;
    email: string;
    role: "Admin" | "User";
    token: string;
}
