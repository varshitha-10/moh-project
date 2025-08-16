import React, { useState } from 'react';

export default function AuthForm({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  return (
    <form className="max-w-xs mx-auto my-8 p-4 bg-white rounded shadow" onSubmit={e => { e.preventDefault(); onLogin(username, password); }}>
      <h2 className="text-xl font-bold mb-4">Login</h2>
      <input
        className="w-full mb-2 px-3 py-2 border rounded"
        type="text"
        placeholder="Username"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
      <input
        className="w-full mb-4 px-3 py-2 border rounded"
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      <button className="w-full bg-blue-600 text-white py-2 rounded" type="submit">Login</button>
    </form>
  );
}
