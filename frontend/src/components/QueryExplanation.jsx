import React from 'react';

export default function QueryExplanation({ explanation }) {
  if (!explanation) return null;
  return (
    <div className="bg-yellow-50 border-l-4 border-yellow-400 p-3 my-4 text-yellow-800">
      <strong>Query Explanation:</strong>
      <div className="mt-1 whitespace-pre-wrap text-sm">{explanation}</div>
    </div>
  );
}
