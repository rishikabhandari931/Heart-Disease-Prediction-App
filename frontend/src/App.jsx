import React, { useState } from "react";

function App() {
  const [form, setForm] = useState({
    Age: "",
    Sex: "",
    ChestPainType: "",
    RestingBP: "",
    Cholesterol: "",
    FastingBS: "",
    RestingECG: "",
    MaxHR: "",
    ExerciseAngina: "",
    Oldpeak: "",
    ST_Slope: ""
  });

  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handlePredict = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });
      const data = await response.json();
      setResult(data.prediction);
    } catch {
      setResult("Backend connection error");
    }
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(135deg, #0f172a, #1e293b)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      padding: "30px",
      fontFamily: "Arial"
    }}>
      <div style={{
        width: "900px",
        background: "white",
        borderRadius: "20px",
        padding: "40px",
        boxShadow: "0 20px 50px rgba(0,0,0,0.25)"
      }}>
        <h1 style={{ textAlign: "center", fontSize: "34px", marginBottom: "10px" }}>
          Heart Disease Prediction System
        </h1>
        <p style={{ textAlign: "center", color: "gray", marginBottom: "35px" }}>
          AI-powered clinical risk assessment platform
        </p>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "18px" }}>
          {Object.keys(form).map((field) => {
            const dropdowns = {
              Sex: ["M", "F"],
              ChestPainType: ["ATA", "NAP", "ASY", "TA"],
              FastingBS: ["0", "1"],
              RestingECG: ["Normal", "ST", "LVH"],
              ExerciseAngina: ["Y", "N"],
              ST_Slope: ["Up", "Flat", "Down"]
            };

            return dropdowns[field] ? (
              <select
                key={field}
                name={field}
                value={form[field]}
                onChange={handleChange}
                style={{
                  padding: "14px",
                  borderRadius: "12px",
                  border: "1px solid #d1d5db",
                  fontSize: "15px"
                }}
              >
                <option value="">Select {field}</option>
                {dropdowns[field].map((option) => (
                  <option key={option} value={option}>{option}</option>
                ))}
              </select>
            ) : (
              <input
                key={field}
                type="text"
                name={field}
                placeholder={field}
                value={form[field]}
                onChange={handleChange}
                style={{
                  padding: "14px",
                  borderRadius: "12px",
                  border: "1px solid #d1d5db",
                  fontSize: "15px",
                  outline: "none"
                }}
              />
            );
          })}
        </div>

        <button
          onClick={handlePredict}
          style={{
            width: "100%",
            marginTop: "28px",
            padding: "16px",
            background: "#0f172a",
            color: "white",
            border: "none",
            borderRadius: "14px",
            fontSize: "18px",
            cursor: "pointer"
          }}
        >
          Predict Risk
        </button>

        {result && (
          <div style={{
            marginTop: "30px",
            padding: "18px",
            background: "#f8fafc",
            borderRadius: "14px",
            textAlign: "center",
            fontSize: "20px",
            fontWeight: "bold"
          }}>
            {result}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
