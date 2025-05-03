import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
// import { AuthContext } from "./AuthContext.jsx"; // يمكنك إزالة هذا الاستيراد إذا لم تعد تستخدم الحالة هنا

const Main = () => {
  // const { isAuthenticated, user, login, logout } = useContext(AuthContext); // قم بإزالة هذا السطر

  const [animals, setAnimals] = useState([]);
  const [loadingAnimals, setLoadingAnimals] = useState(true);
  const [errorAnimals, setErrorAnimals] = useState('');
  const [categories, setCategories] = useState([]);
  const [loadingCategories, setLoadingCategories] = useState(true);
  const [errorCategories, setErrorCategories] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [filteredAnimals, setFilteredAnimals] = useState([]);

  useEffect(() => {
    console.log("Categories state:", categories); // أضف هذا لمشاهدة البيانات
    const fetchAnimals = async () => {
      setLoadingAnimals(true);
      try {
        const response = await axios.get("http://127.0.0.1:8000/animal/main/");
        console.log("Categories response:", response); // أضف هذا السطر

        setAnimals(response.data);
        
        setLoadingAnimals(false);
      } catch (error) {
        console.error("Error details:", error.response); // أضف هذا السطر

        console.error("Error fetching animals:", error);
        setErrorAnimals("Failed to load animals.");
        setLoadingAnimals(false);
      }
    };

    const fetchCategories = async () => {
      setLoadingCategories(true);
      try {
        const response = await axios.get("http://127.0.0.1:8000/animal/categories/");
        setCategories(response.data);
        setLoadingCategories(false);
      } catch (error) {
        console.error("Error fetching categories:", error);
        setErrorCategories("Failed to load categories.");
        setLoadingCategories(false);
      }
    };

    fetchAnimals();
    fetchCategories();
  }, []);

  useEffect(() => {
    if (selectedCategory === '') {
      setFilteredAnimals(animals);
    } else {
      const filtered = animals.filter(animal => animal.category.id.toString() === selectedCategory);
      setFilteredAnimals(filtered);
    }
  }, [animals, selectedCategory]);

  const handleCategoryChange = (event) => {
    setSelectedCategory(event.target.value);
  };

  if (loadingAnimals || loadingCategories) {
    return <p>Loading data...</p>;
  }

  if (errorAnimals || errorCategories) {
    return <p>{errorAnimals || errorCategories}</p>;
  }

  return (
    <div>
      <h2>List of Animals</h2>


      {/* يمكنك إزالة هذا الجزء */}
      {/* {isAuthenticated ? (
        <div>
          <p>Welcome, {user ? user.username : 'User'}!</p>
          <button onClick={logout}>Logout</button>
        </div>
      ) : (
        <div>
          <Link to="/signup">Sign Up</Link>
          <Link to="/signin">Sign In</Link>
        </div>
      )} */}

      <div>
        <label htmlFor="categoryFilter">Filter by Category: </label>
        <select id="categoryFilter" value={selectedCategory} onChange={handleCategoryChange}>
          <option value="">All Categories</option>
          {categories.map(category => (
            <option key={category.id} value={category.id}>{category.categoryName}</option>
          ))}
        </select>
      </div>

      <div className="container" style={{ display: 'flex', flexDirection: "row", flexWrap: 'wrap', gap: '20px' }}>
        {filteredAnimals.map(animal => (
          <div key={animal.id} className="card" style={{ width: "20%" }}>
            {animal.imageFile && <img className="card-img-top" src={`${animal.imageFile}`} alt={animal.title} style={{ maxWidth: '200px' }} />}
            <div className="card-body">
              <h4 className="card-title">{animal.title}</h4>
              <p className="card-text">
                {animal.description.length > 50 ? `${animal.description.substring(0, 150)}...` : animal.description}
              </p>
              <p>Price: {animal.price} $</p>
              <p>Category: {animal.category.categoryName}</p>
              <Link to={`/animal/${animal.id}`} className="btn btn-primary stretched-link">See Details</Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Main;