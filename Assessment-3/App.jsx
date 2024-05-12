import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Import CSS file for styling

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleLogin = () => {
    // Here you can implement your login logic, such as making an API call to authenticate the user
    if (username === 'admin' && password === 'password') {
      // Successful login
      alert('Login successful!');
    } else {
      // Failed login
      setErrorMessage('Invalid username or password');
    }
  };

  return (
    <div>
      <h2>Login Page</h2>
      <div>
        <label>Username:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div>
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button onClick={handleLogin}>Login</button>
      {errorMessage && <div style={{ color: 'red' }}>{errorMessage}</div>}
    </div>
  );
};

export default LoginPage;
