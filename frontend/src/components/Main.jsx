import React, {useState , useEffect} from "react";
import axios from "axios";
// import { useNavigate } from "react-router-dom";
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
            {animals.map(animal => (
                <div key={animal.id}>
                    <h3>{animal.title}</h3>
                    <p>{animal.description}</p>
                    {animal.imageFile && <img src={`http://localhost:8000${animal.imageFile}`} alt={animal.title} style={{ maxWidth: '200px' }} />}
                    <p>Price: {animal.price}</p>
                    <p>Category: {animal.category.categoryName}</p>
                    {/* يمكنك عرض المزيد من التفاصيل هنا */}
                </div>
            ))}
        </div>
    );
};
export default Main

