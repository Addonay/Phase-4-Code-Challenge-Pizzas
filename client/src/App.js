import React from 'react';
import { Routes, Route } from 'react-router-dom';
import RestaurantList from './components/RestaurantList'
import PizzaList from './components/PizzaList';

function App() {
  return (
    <Routes>
      <Route exact path="/" element={<RestaurantList />} />
      <Route exact path="/restaurants/:restaurantId/pizzas" element={<PizzaList />} />
    </Routes>
  );
}

export default App;
