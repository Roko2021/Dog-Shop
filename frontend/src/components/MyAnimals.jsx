import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../AuthContext'; // استيراد الـ context الخاص بالمصادقة
import { Link } from 'react-router-dom';

const MyAnimals = () => {
  const { isAuthenticated, loading, user } = useContext(AuthContext);
  const [animals, setAnimals] = useState([]);
  const [loadingAnimals, setLoadingAnimals] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!isAuthenticated || loading) return; // انتظر حتى يتم تحميل بيانات المستخدم

    const fetchMyAnimals = async () => {
      setLoadingAnimals(true);
      try {
        // افترض أن لديك توكن في localStorage
        const token = localStorage.getItem('access');

        const response = await axios.get('http://localhost:8000/animal/my-animals/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });

        setAnimals(response.data);
        setLoadingAnimals(false);
      } catch (err) {
        console.error('Error fetching user animals:', err);
        setError('Failed to load your animals.');
        setLoadingAnimals(false);
      }
    };

    fetchMyAnimals();
  }, [isAuthenticated, loading]);

  if (!isAuthenticated) {
    return <p>Please login to see your animals.</p>;
  }

  if (loadingAnimals) {
    return <p>Loading your animals...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  if (animals.length === 0) {
    return <p>You have no animals listed.</p>;
  }

  return (
    <div>
      <h2>My Animals</h2>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {animals.map(animal => (
          <li key={animal.id} style={{ marginBottom: '20px', borderBottom: '1px solid #ccc', paddingBottom: '10px' }}>
            <Link to={`/animal/${animal.id}`} style={{ fontSize: '18px', fontWeight: 'bold', color: '#333', textDecoration: 'none' }}>
              {animal.title}
            </Link>
            {animal.imageFile && (
              <div>
                <img src={animal.imageFile} alt={animal.title} style={{ maxWidth: '200px', marginTop: '5px' }} />
              </div>
            )}
            <p>{animal.description}</p>
            <p>Price: {animal.price}</p>
            <p>Category: {animal.category?.categoryName}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MyAnimals;
