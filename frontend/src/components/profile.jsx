import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Profile() {
    const navigate = useNavigate();

    const jwt_access = localStorage.getItem('access');
    const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;

    useEffect(() => {
        if (!jwt_access || !user) {
            navigate('/login');
        }
    }, [jwt_access, user, navigate]);

    return (
        <div className="text-center mt-12">
            <h2 className="text-xl font-bold">Hi {user?.names}</h2>
            <p className="text-gray-600">{user?.email}</p>
            {/* <img src={user?.picture} alt="profile" className="w-24 h-24 rounded-full mx-auto mt-4" /> */}
        </div>
    );
}
