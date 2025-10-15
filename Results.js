import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
ChartJS.register(ArcElement, Tooltip, Legend);

export default function Results({ data }){
  if(!data) return null;
  const sentimentVal = Math.round((data.sentiment + 1) * 50);
  const chartData = {
    labels: ['Positive','Neutral','Negative'],
    datasets: [{ data: [Math.max(0, sentimentVal-50), Math.max(0, 100-Math.abs(sentimentVal-50)*2), Math.max(0, 50-sentimentVal)] }]
  };

  return (
    <div>
      <h3>{data.candidate_name} - Score: {Math.round(data.final_score)}</h3>
      <Doughnut data={chartData} />
      <h4>Transcript</h4>
      <p>{data.transcript}</p>
      <p>Filler words: {data.filler_count}</p>
      <p>Keyword count: {data.keyword_count}</p>
      <p>Sentiment: {data.sentiment.toFixed(2)}</p>
    </div>
  );
}
