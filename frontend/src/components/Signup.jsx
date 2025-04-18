import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
// import axiosInstance from "../utils/axiosinstance";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
// import { jwtDecode } from 'jwt-decode';

const Signup = () => {
    const navigate = useNavigate();
    // const [searchParams] = useSearchParams();

    const [formData, setFormData] = useState({
        email: "",
        first_name: "",
        last_name: "",
        password: "",
        password2: "",
    });

    const [error, setError] = useState("");

    // 🔐 تسجيل الدخول باستخدام Google
    const handleSignInWithGoogle = useCallback(async (response) => {
        console.log("Google Credential Response:", response);

        if (!response.credential) {
            console.error("لم يتم العثور على الرمز المميز");
            toast.error("فشل في الحصول على الرمز المميز");
            return;
        }

        const payload = response.credential;

        try {
            const decodedToken = JSON.parse(atob(payload.split(".")[1]));
            console.log("decodedToken:", decodedToken);

            if (!decodedToken?.email || !decodedToken?.given_name || !decodedToken?.family_name) {
                console.error("البيانات غير مكتملة");
                toast.error("البيانات غير مكتملة");
                return;
            }

            // أرسل الـ access token إلى السيرفر
            const serverRes = await axios.post("http://localhost:8000/api/v1/auth/google/", {
                access_token: payload,
            });

            if (serverRes.status === 200) {
                console.log("تم تسجيل الدخول بنجاح");
                toast.success("تم تسجيل الدخول بنجاح");

                const user = {
                    email: serverRes.data.email,
                    names: serverRes.data.full_name,
                };

                localStorage.setItem("user", JSON.stringify(user));
                localStorage.setItem("access", serverRes.data.access_token);
                localStorage.setItem("refresh", serverRes.data.refresh_token);

                navigate("/dashboard");
            } else {
                toast.error("حدث خطأ أثناء تسجيل الدخول");
            }
        } catch (err) {
            console.error("خطأ في تسجيل الدخول باستخدام Google:", err);
            toast.error("فشل التسجيل باستخدام جوجل");
        }
    }, [navigate]);

    // 🌐 تهيئة زر Google
    useEffect(() => {
        /* global google */
        if (window.google) {
            google.accounts.id.initialize({
                client_id: import.meta.env.VITE_CLIENT_ID,
                callback: handleSignInWithGoogle,
            });

            google.accounts.id.renderButton(document.getElementById("signInDiv"), {
                theme: "outline",
                size: "large",
                text: "continue-with",
                shape: "circle",
                width: "280",
            });
        }
    }, [handleSignInWithGoogle]);

    const handleOnChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const { email, first_name, last_name, password, password2 } = formData;

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!email || !first_name || !last_name || !password || !password2) {
            setError("جميع الحقول مطلوبة");
            return;
        }
        if (password !== password2) {
            setError("كلمتا المرور غير متطابقتين");
            return;
        }

        try {
            const res = await axios.post("http://localhost:8000/api/v1/auth/register/", formData);

            if (res.status === 201) {
                toast.success(res.data.message || "تم إنشاء الحساب بنجاح");
                navigate("/otp/verify");
            }
        } catch (err) {
            console.error("خطأ في التسجيل:", err);
            if (err.response?.data?.message) {
                toast.error(err.response.data.message);
            } else {
                toast.error("فشل في إنشاء الحساب");
            }
        }
    };

    // const handleSignInWithGithub = () => {
    //     window.location.assign(`https://github.com/login/oauth/authorize?client_id=Ov23libKLQO4Vlu13eJp`);
    // };

    // const sendCodeToBackend = useCallback(async () => {
    //     const code = searchParams.get('code');
    //     if (code) {
    //         try {
    //             const response = await axiosInstance.post("/auth/github/", { 'code': code });
    //             const result = response.data;
    //             console.log("Response from server:", result);

    //             if (response.status === 200) {
    //                 if (result.access_token && result.refresh_token) {
    //                     // Check if the token is a valid JWT before decoding
    //                     const tokenFormatRegex = /^([a-zA-Z0-9_-]+\.){2}[a-zA-Z0-9_-]+$/;
    //                     if (tokenFormatRegex.test(result.access_token)) {
    //                         try {
    //                             const decoded = jwtDecode(result.access_token);
    //                             const user = {
    //                                 'email': decoded.email,
    //                                 'names': decoded.name
    //                             };
    //                             localStorage.setItem('access', result.access_token);
    //                             localStorage.setItem('refresh', result.refresh_token);
    //                             localStorage.setItem('user', JSON.stringify(user));
    //                             navigate('/dashboard');
    //                             toast.success('Login Successful');
    //                         } catch (decodeError) {
    //                             console.error("Error decoding JWT:", decodeError);
    //                             toast.error('Failed to login: Invalid token format');
    //                         }

    //                     }
    //                     else {
    //                         console.error("Invalid access token format from server", result.access_token);
    //                         toast.error('Failed to login: Invalid token format from server');
    //                     }
    //                 } else {
    //                     console.error("Access token or refresh token is missing in the response");
    //                     toast.error('Failed to login with GitHub: Missing tokens');
    //                 }
    //             } else {
    //                 console.error("Unexpected response status:", response.status);
    //                 toast.error(`Failed to login with GitHub: Unexpected status ${response.status}`);
    //             }
    //         } catch (error) {
    //             console.error("Error during GitHub login:", error);
    //             toast.error('Failed to login with GitHub');
    //         }
    //     }
    // }, [navigate, searchParams]);

    // useEffect(() => {
    //     sendCodeToBackend();
    // }, [sendCodeToBackend]);

    return (
        <div className="form-container">
            <div className="wrapper" style={{ width: "100%" }}>
                <h2>Create Account</h2>
                <form onSubmit={handleSubmit}>
                    <p style={{ color: "red", padding: "1px" }}>{error && error}</p>
                    <div className="form-group">
                        <label>Email Address:</label>
                        <input
                            type="text"
                            className="email-form"
                            name="email"
                            value={email}
                            onChange={handleOnChange}
                        />
                    </div>
                    <div className="form-group">
                        <label>First Name:</label>
                        <input
                            type="text"
                            className="email-form"
                            name="first_name"
                            value={first_name}
                            onChange={handleOnChange}
                        />
                    </div>
                    <div className="form-group">
                        <label>Last Name:</label>
                        <input
                            type="text"
                            className="email-form"
                            name="last_name"
                            value={last_name}
                            onChange={handleOnChange}
                        />
                    </div>
                    <div className="form-group">
                        <label>Password:</label>
                        <input
                            type="password"
                            className="email-form"
                            name="password"
                            value={password}
                            onChange={handleOnChange}
                        />
                    </div>
                    <div className="form-group">
                        <label>Confirm Password:</label>
                        <input
                            type="password"
                            className="email-form"
                            name="password2"
                            value={password2}
                            onChange={handleOnChange}
                        />
                    </div>
                    <input type="submit" value="Submit" className="submitButton" />
                </form>

                {/* <h3 className="text-option">Or</h3> */}

                {/* <div className="githubContainer">
                    <button onClick={handleSignInWithGithub}>Sign up with GitHub</button>
                </div> */}

                <div className="googleContainer" id="signInDiv"></div>
            </div>
        </div>
    );
};

export default Signup;
