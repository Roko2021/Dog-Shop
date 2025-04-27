import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext({
    isAuthenticated: false,
    user: null,
    login: () => {},
    logout: () => {}
  });

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false); // حالة تسجيل الدخول
    const [user, setUser] = useState(null); // معلومات المستخدم (اختياري)

    useEffect(() => {
        // هنا يمكنك إضافة منطق للتحقق من وجود رمز مميز (token) محفوظ
        // في Local Storage أو Cookies عند تحميل التطبيق.
        const token = localStorage.getItem('authToken');
        if (token) {
            // قم بفك تشفير الرمز المميز أو استدعاء API للتحقق من صحته
            // وتعيين حالة تسجيل الدخول والمستخدم إذا كان صالحًا.
            setIsAuthenticated(true);
            // setUser({...});
        }
    }, []);

    const login = (userData) => {
        setIsAuthenticated(true);
        setUser(userData);
        // حفظ الرمز المميز (token) في Local Storage أو Cookies
        localStorage.setItem('authToken', 'your_auth_token'); // استبدل بآلية حفظ الرمز الحقيقية
    };

    const logout = () => {
        setIsAuthenticated(false);
        setUser(null);
        // إزالة الرمز المميز (token) من Local Storage أو Cookies
        localStorage.removeItem('authToken');
    };

    return (
        <AuthContext.Provider value={{ isAuthenticated, user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};