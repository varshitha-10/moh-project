import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function ResultsChart({ data, xKey, yKey }) {
  if (!data || data.length === 0) return null;
  return (
    <div className="w-full h-64">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <XAxis dataKey={xKey} />
          <YAxis />
          <Tooltip />
          <Bar dataKey={yKey} fill="#2563eb" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
