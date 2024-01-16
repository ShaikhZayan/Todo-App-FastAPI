"use client"
import { useState, useEffect } from 'react';

const LogsPage = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    // Fetch logs from FastAPI
    fetch('http://localhost:8000/logs')
      .then((response) => response.json())
      .then((data) => {
        setLogs(data.logs.split('\n'));
      })
      .catch((error) => {
        console.error('Error fetching logs:', error);
      });
  }, []);

  return (
    <div>
      <h1>FastAPI Logs</h1>
      <ul>
        {logs.map((log, index) => (
          <li className="text-green-600" key={index}><b>{log}</b></li>
        ))}
      </ul>
    </div>
  );
};

export default LogsPage;
