import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import React from 'react'
import ReactDOM from 'react-dom/client'
import { PayPalScriptProvider } from '@paypal/react-paypal-js';
import { AuthProvider } from './AuthContext.jsx'; // استيراد AuthProvider



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider> {/* تغليف App بـ AuthProvider */}
        <PayPalScriptProvider
        options={{
            "client-id": "AVkAV_89lXJ7o21oN3kaN7ZS0KhHcOvVyi3hKqD9Fr1ktFKiYBT6Steg37ZREgHOa7WL00YgDJHWvDjq", // استبدل هذا بمعرف عميل PayPal الخاص بك
            currency: "USD", // تحديد العملة بالدولار الأمريكي
        }}
        >
        <App />
        </PayPalScriptProvider>
    </AuthProvider>
  </React.StrictMode>
);