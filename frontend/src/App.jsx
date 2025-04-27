import { useState } from 'react';
import { ToastContainer } from 'react-toastify';
import "react-toastify/dist/ReactToastify.css";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Signup, Login, Profile, VerifyEmail, ForgetPassword, ResetPassword
    , Main, AddAnimls, AnimalDetails, PaymentPage } from './components';
import './App.css';
import Layout from './utils/Layout';
import { AuthProvider } from './AuthContext'; // استيراد AuthProvider

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <AuthProvider> {/* تغليف التطبيق كله بـ AuthProvider */}
                <Router>
                    <ToastContainer />
                    <Routes>
                        <Route element={<Layout />}>
                            <Route path='/' element={<Main />} />
                            <Route path='/register' element={<Signup />} />
                            <Route path='/login' element={<Login />} />
                            <Route path='/dashboard' element={<Profile />} />
                            <Route path='/otp/verify' element={<VerifyEmail />} />
                            <Route path='/forget_password' element={<ForgetPassword />} />
                            <Route path='/password-reset/confirm/:uid/:token' element={<ResetPassword />} />
                            <Route path='/AddAnimls' element={<AddAnimls />} />
                            <Route path="/animal/:id" element={<AnimalDetails />} />
                            <Route path="/PaymentPage" element={<PaymentPage />} />
                        </Route>
                    </Routes>
                </Router>
            </AuthProvider>
        </>
    );
}

export default App;