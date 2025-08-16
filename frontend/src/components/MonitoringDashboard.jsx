import React from 'react';

export default function MonitoringDashboard({ activeQueries, schemaChanges, logs }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
      <div className="bg-white rounded shadow p-4">
        <h2 className="font-bold mb-2">Active Queries</h2>
        <ul className="text-xs">
          {activeQueries.map((q, i) => <li key={i}>{q}</li>)}
        </ul>
      </div>
      <div className="bg-white rounded shadow p-4">
        <h2 className="font-bold mb-2">Schema Changes</h2>
        <ul className="text-xs">
          {schemaChanges.map((s, i) => <li key={i}>{s}</li>)}
        </ul>
      </div>
      <div className="bg-white rounded shadow p-4">
        <h2 className="font-bold mb-2">Logs</h2>
        <ul className="text-xs max-h-32 overflow-y-auto">
          {logs.map((l, i) => <li key={i}>{l}</li>)}
        </ul>
      </div>
    </div>
  );
}
