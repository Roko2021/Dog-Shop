import React, {useState , useEffect} from "react";
import axios from "axios";
import { Link } from "react-router-dom";
// import { toast } from "react-toastify";
// import React from "react"

const Main= () =>{
    const [animals, setAnimals] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchAnimals = async () => {
            setLoading(true);
            try {
                const response = await axios.get("http://127.0.0.1:8000/animal/main/"); // إزالة رأس Authorization
                setAnimals(response.data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching animals:", error);
                setError("Failed to load animals.");
                setLoading(false);
            }
        };

        fetchAnimals();
    }, []); // إزالة jwt_access من قائمة الاعتماديات

    if (loading) {
        return <p>Loading animals...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <div>
            <h2>List of Animals</h2>
            <div className="container" style={{ display: 'flex', flexDirection:"row", flexWrap: 'wrap', gap: '20px' }}>
                {animals.map(animal => (
                    <div key={animal.id} className="card" style={{ width: "20%" }}>
                        {animal.imageFile && <img className="card-img-top" src={`http://localhost:8000${animal.imageFile}`} alt={animal.title} style={{ maxWidth: '200px' }} />}
                        <div className="card-body">
                            <h4 className="card-title">{animal.title}</h4>
                            <p className="card-text">
                                {animal.description.length > 50 ? `${animal.description.substring(0, 150)}...` : animal.description}
                            </p>
                            <p>Price: {animal.price}</p>
                            <p>Category: {animal.category.categoryName}</p>
                            <Link to={`/animal/${animal.id}`} className="btn btn-primary stretched-link">See Details</Link> {/* استخدام Link للانتقال */}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};
export default Main

