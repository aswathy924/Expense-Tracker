import React, { useState, useEffect } from "react";
import axios from "axios";
import AddExpenseForm from "./AddExpenseForm";

function App() {
  const [expenses, setExpenses] = useState([]);

  const fetchExpenses = async () => {
    const response = await axios.get("http://localhost:8000/expenses/");
    setExpenses(response.data);
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Expense Tracker</h1>
      <AddExpenseForm onAdd={fetchExpenses} />
      <ul>
        {expenses.map((exp) => (
          <li key={exp.id}>
            {exp.title} - ₹{exp.amount} - {exp.category} - {exp.date}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
