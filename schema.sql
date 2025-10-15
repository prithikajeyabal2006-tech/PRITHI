CREATE DATABASE IF NOT EXISTS interview_analysis;
USE interview_analysis;

CREATE TABLE IF NOT EXISTS interview_results (
  id INT AUTO_INCREMENT PRIMARY KEY,
  candidate_name VARCHAR(100),
  transcript TEXT,
  sentiment FLOAT,
  filler_count INT,
  keyword_count INT,
  final_score FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
