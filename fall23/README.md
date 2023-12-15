
# Flow Documentation
This document provides an overview of the key components in our ML Pipeline. Please refer to each file for in depth explanation.

## Key Components

**JSON Data File**
- Description : This is a JSON file that contains all relevant Facebook data. It serves as the primary dataset.

**Data Downloader**
- Function : Downloads all images associated with a specific `CaseId`.
- Output : Images are stored in a structured directory named `case_status/case_id`.

**Data Organizer**
- Function : Aggregates enhanced images from each `CaseId`.
- Organization Method : Images are sorted into folders based on their `case_status`.

**Face Detector**
- Function : Identifies any faces that are not detectable and Removes non-detectable faces from the processing queue.
- Output : Non-detectable faces are listed in a CSV file.

**Face Matcher**
- Function : Compares each individual's face against a directory of 'John Does'.
- Output : Generates a CSV file listing individuals who resemble 'John Does' along with their respective similarity scores.


<img src="flow_chart.png" alt="Flow Chart" width="750"/>

## Euclidean l2 Vs Cosine

| Criteria | Euclidean_l2 | Cosine |
|---|---|---|
| Total Case IDs Evaluated | 249 | 249 |
| Case IDs with No Matches | 26 | 18 |
| Case IDs with At Least One Match | 223 | 231 |
| Avg Pool Size | Small (221) | Large (336) |
| Probability of Finding Exact Match | Good | Slightly Higher |
| Matches in Top 50 Pool | 85.7% (191/223) | 86.6% (200/231) |
