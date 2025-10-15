import React, { useState } from 'react';
import { analyzeAudio } from '../api';

export default function Recorder({ onResult }){
  const [file, setFile] = useState(null);
  const [name, setName] = useState('');

  function handleFile(e){
    setFile(e.target.files[0]);
  }

  async function submit(){
    if(!file) return alert('Select an audio file (wav preferred)');
    const res = await analyzeAudio(file, name);
    onResult(res.data);
  }

  return (
    <div>
      <input value={name} onChange={e=>setName(e.target.value)} placeholder="Candidate name" />
      <input type="file" accept="audio/*" onChange={handleFile} />
      <button onClick={submit}>Analyze</button>
    </div>
  );
}
