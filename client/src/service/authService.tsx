import axios from "axios";

export const createOrUpdateUser = async (authtoken: string) => {
    try {
        const response = await axios.post(
            "http://localhost:8000/verify_firebase_token/",
            { token: authtoken },
            {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${authtoken}`,
                },
            }
        );

        return response.data;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.error("Error response:", error.response?.data);
            throw new Error(error.response?.data?.message || "An error occurred");
        } else {
            console.error("Unexpected error:", error);
            throw new Error("An unexpected error occurred");
        }
    }
};

export default createOrUpdateUser;

export const currentAdmin = async (authtoken: string) => {
    try {
        const response = await axios.post(
            "http://localhost:8000/check_admin/",
            { token: authtoken }, // Send token in the body
            {
                headers: {
                    Authorization: `Bearer ${authtoken}`, // Optional: Still include this if your middleware needs it
                },
            }
        );

        return response.data;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.error("Error response:", error.response?.data);
            throw new Error(error.response?.data?.message || "An error occurred");
        } else {
            console.error("Unexpected error:", error);
            throw new Error("An unexpected error occurred");
        }
    }
};
