import React, { useEffect, useState } from 'react';
import AiList from '../components/AiList';

const Home = () => {
  const [aiData, setAiData] = useState([]);

  useEffect(() => {
    fetch("/api/ai")
      .then(response => response.json())
      .then(data => setAiData(data));
  }, []);

  return (
    <div>
      <h1>AI Civilization Simulation</h1>
      <AiList aiData={aiData} />
    </div>
  );
};

export default Home;
