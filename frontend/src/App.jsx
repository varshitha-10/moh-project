import React, { useState } from 'react';
import QueryInput from './components/QueryInput';
import ResultsTable from './components/ResultsTable';
import ResultsChart from './components/ResultsChart';
import QueryExplanation from './components/QueryExplanation';
import MonitoringDashboard from './components/MonitoringDashboard';
import AuthForm from './components/AuthForm';

export default function App() {
  const [user, setUser] = useState(null);
  const [results, setResults] = useState([]);
  const [explanation, setExplanation] = useState('');
  const [activeQueries, setActiveQueries] = useState([]);
  const [schemaChanges, setSchemaChanges] = useState([]);
  const [logs, setLogs] = useState([]);

  const handleLogin = (username, password) => {
    // TODO: Call backend for authentication
    setUser({ username, roles: ['admin'] });
  };

  const handleQuery = async (query) => {
    setActiveQueries(qs => [...qs, query]);
    // TODO: Call backend /ask endpoint
    setTimeout(() => {
      setResults([{ name: 'Sample', value: 42 }]);
      setExplanation('SELECT * FROM sample_table;');
      setActiveQueries(qs => qs.filter(q => q !== query));
      setLogs(ls => [...ls, `Query: ${query}`]);
    }, 1000);
  };

  if (!user) return <AuthForm onLogin={handleLogin} />;

  return (
    <div className="min-h-screen bg-gray-50 p-2 md:p-6">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-2xl font-bold mb-4 text-blue-700">Multi-DB NL Query Engine Dashboard</h1>
        <QueryInput onSubmit={handleQuery} />
        <QueryExplanation explanation={explanation} />
        <ResultsTable data={results} />
        <ResultsChart data={results} xKey="name" yKey="value" />
        <MonitoringDashboard activeQueries={activeQueries} schemaChanges={schemaChanges} logs={logs} />
      </div>
    </div>
  );
}
