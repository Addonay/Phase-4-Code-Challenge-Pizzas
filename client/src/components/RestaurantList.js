import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Fetch the list of restaurants from your API
    async function fetchRestaurants() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/restaurants');
        setRestaurants(response.data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    }

    fetchRestaurants();
  }, []);

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Restaurants</h1>
      <div className="row">
        {restaurants.map((restaurant) => (
          <div className="col-md-4 mb-4" key={restaurant.id}>
            <div className="card">
              <Link to={`/restaurants/${restaurant.id}/pizzas`} className="card-link">
                {/* Replace with actual restaurant image */}
                <img
                  src="data:image/jpeg;base64,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"
                  className="card-img-top"
                  alt="Restaurant Image"
                />
                <div className="card-body">
                  <h5 className="card-title">{restaurant.name}</h5>
                  <p className="card-text">Address: {restaurant.address}</p>
                </div>
              </Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RestaurantList;


