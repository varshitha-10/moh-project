import React, { useState } from 'react';

export default function QueryInput({ onSubmit }) {
  const [query, setQuery] = useState('');
  return (
    <form className="flex gap-2" onSubmit={e => { e.preventDefault(); onSubmit(query); }}>
      <input
        className="flex-1 border rounded px-3 py-2 focus:outline-none"
        type="text"
        placeholder="Ask a question..."
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <button className="bg-blue-600 text-white px-4 py-2 rounded" type="submit">Ask</button>
    </form>
  );
}
