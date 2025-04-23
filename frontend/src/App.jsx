import { useState } from 'react';
import { ToastContainer } from 'react-toastify';
import "react-toastify/dist/ReactToastify.css";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Signup, Login, Profile, VerifyEmail, ForgetPassword, ResetPassword
    , Main, AddAnimls } from './components';
import './App.css';
import Layout from './utils/Layout'; // بدون curly braces {}

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <Router>
                <ToastContainer />
                <Routes>
                    {/* جميع الصفحات ستظهر داخل Layout (سيظهر الشريط العلوي في كل الصفحات) */}
                    <Route element={<Layout />}>
                        <Route path='/' element={<Main />} />
                        <Route path='/register' element={<Signup />} />
                        <Route path='/login' element={<Login />} />
                        <Route path='/dashboard' element={<Profile />} />
                        <Route path='/otp/verify' element={<VerifyEmail />} />
                        <Route path='/forget_password' element={<ForgetPassword />} />
                        <Route path='/password-reset/confirm/:uid/:token' element={<ResetPassword />} />
                        <Route path='/AddAnimls' element={<AddAnimls />} />
                    </Route>
                </Routes>
            </Router>
        </>
    );
}

export default App;