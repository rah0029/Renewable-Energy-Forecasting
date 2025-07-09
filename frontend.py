// EnergyPredictor.jsx
import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import axios from "axios";
import { Line } from "react-chartjs-2";

const EnergyPredictor = () => {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState([]);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:5000/predict", formData);
    setPrediction(res.data.predictions);
  };

  const chartData = {
    labels: prediction.map((_, i) => `Day ${i + 1}`),
    datasets: [
      
      {
        label: "Predicted Energy Requirement",
        data: prediction,
        borderColor: "#10B981",
        fill: false,
      },
    ],
  };

  return (
    <div className="max-w-xl mx-auto p-4">
      <h2 className="text-xl font-bold mb-4">Energy Requirement Predictor</h2>
      <Input type="file" onChange={handleFileChange} className="mb-4" />
      <Button onClick={handleUpload}>Upload & Predict</Button>
      {prediction.length > 0 && (
        <div className="mt-6">
          <Line data={chartData} />
        </div>
      )}
    </div>
  );
};

export default EnergyPredictor;
