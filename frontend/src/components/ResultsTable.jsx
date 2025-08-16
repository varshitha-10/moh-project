import React from 'react';

export default function ResultsTable({ data }) {
  if (!data || data.length === 0) return <div className="text-gray-500">No results</div>;
  const columns = Object.keys(data[0]);
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full border mt-4">
        <thead>
          <tr>
            {columns.map(col => <th key={col} className="px-2 py-1 border-b bg-gray-100">{col}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              {columns.map(col => <td key={col} className="px-2 py-1 border-b">{row[col]}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
