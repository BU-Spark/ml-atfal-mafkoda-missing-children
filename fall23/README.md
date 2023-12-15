
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
