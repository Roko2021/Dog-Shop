import React from 'react';
import { Outlet } from 'react-router-dom';

const Layout = () => {
  return (
    <div style={{ 
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column'
    }}>
      {/* Header */}
      <header style={{
        background: '#333',
        color: 'white',
        padding: '1rem',
        position: 'sticky',
        top: 0,
        zIndex: 100
      }}>
        <nav style={{
            alignItems: 'center',      // camelCase
            justifyContent: 'space-between', // camelCase
            display: 'flex',
            flexWrap: 'wrap'           // camelCase
            }}>
          <div>
            <a href="/" style={{ color: 'white', marginRight: '1rem' }}>Main</a>
          </div>
          <div style={{
                display: 'flex',
                flexWrap: 'nowrap',
                flexDirection: 'row',
                alignContent: 'space-around',
                justifyContent: 'flex-end',
                alignItems: 'center',
          }}>
            <a href="/" ><img src="/images/IconPets.jpg" alt="icon" style={{height:"40px" ,width:"35px",margin: '10px'}}/></a>
            <a href="/FoodDogs" ><img src="/images/FoodDog.jpg" alt="icon" style={{height:"40px" ,width:"35px" ,margin: '10px'}} /></a>
            <a href="/login" style={{ color: 'white' ,margin: '0 10px' }}>Login</a>
            <a href="/register" style={{ color: 'white' ,margin: '10px' }}>Register</a>
          </div>
        </nav>
      </header>

      {/* Main Content - سيظهر هنا محتوى Login أو أي صفحة أخرى */}
      <main style={{ 
        flex: 1,
        padding: '2rem'
      }}>
        <Outlet />
      </main>

      {/* Footer */}
      <footer style={{
        background: '#333',
        color: 'white',
        padding: '1rem',
        textAlign: 'center'
      }}>
        <p>© 2025 Your Company. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Layout;