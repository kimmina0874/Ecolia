import React from 'react';

const AiList = ({ aiData }) => {
  return (
    <div>
      <h2>AI List</h2>
      {aiData.map((ai) => (
        <div key={ai.id}>
          <p>Name: {ai.name}</p>
          <p>Age: {ai.age}</p>
        </div>
      ))}
    </div>
  );
};

export default AiList;
