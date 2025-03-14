// Import these 

import React, { useState } from "react";
import axios from "axios";

function App() {
  const [amount, setAmount] = useState("");
  const [result, setResult] = useState("");

  const checkClaim = async () => {
    const response = await axios.post("https://your-api-url/predict", { amount: Number(amount) });
    setResult(response.data.prediction);
  };

  return (
    <div>
      <h1>Medical Claim Processing</h1>
      <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
      <button onClick={checkClaim}>Check Claim</button>
      {result && <h2>Prediction: {result}</h2>}
    </div>
  );
}

export default App;
