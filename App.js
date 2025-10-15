import React, { useState } from 'react';
import Recorder from './components/Recorder';
import Results from './components/Results';

function App(){
  const [result, setResult] = useState(null);
  return (
    <div style={{padding:20}}>
      <h1>Interview Analysis System</h1>
      <Recorder onResult={setResult} />
      <Results data={result} />
    </div>
  );
}

export default App;
