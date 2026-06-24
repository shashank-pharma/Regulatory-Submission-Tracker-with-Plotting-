# Regulatory-Submission-Tracker-with-Plotting-

A Python-based Regulatory Affairs dashboard that helps track and analyze drug submissions across regulatory agencies such as **CDSCO** and **FDA**.

The project processes submission data, identifies pending applications, calculates deadline urgency, and generates visual insights to support regulatory planning and submission management.

---

## Project Overview

Regulatory submissions often involve multiple products, agencies, deadlines, and approval statuses. Managing this information manually can be time-consuming and prone to errors.

This project demonstrates how Python can be used to:

* Track submission status.
* Monitor regulatory deadlines.
* Identify pending applications.
* Prioritize urgent submissions.
* Generate visual summaries for decision-making.

---

## Features

### Data Processing

* Import regulatory submission data from Excel.
* Clean and standardize datasets.
* Convert date fields into analyzable formats.

### Submission Analysis

* Count submissions by status.
* Identify pending submissions.
* Calculate days remaining until regulatory deadlines.
* Flag urgent submissions based on predefined criteria.

### Visualization

* Regulatory Submission Status Breakdown (Pie Chart)
* Submission Distribution by Agency (Bar Chart)

### Reporting

* Generate submission summaries.
* Highlight critical deadlines.
* Support regulatory planning activities.

---

## Technologies Used

* Python
* Pandas
* Seaborn
* Matplotlib
* OpenPyXL

---

## Workflow

### Step 1: Import Data

Load regulatory submission information from an Excel file.

### Step 2: Data Cleaning

* Remove unwanted spaces.
* Standardize column names.
* Format date fields.

### Step 3: Status Analysis

Track submission categories such as:

* Approved
* Pending
* Under Review
* Rejected

### Step 4: Deadline Monitoring

Calculate:

* Days remaining until submission deadlines.
* Urgency level for each submission.

### Step 5: Visualization

Generate charts to provide quick insights into submission progress and workload distribution.

---

## Sample Insights

The dashboard can answer questions such as:

* How many submissions are currently pending?
* Which applications require immediate attention?
* What percentage of submissions have been approved?
* Which regulatory agency has the highest workload?

---

## Example Output

### Regulatory Submission Status Breakdown

* Pending: 38%
* Approved: 25%
* Under Review: 25%
* Rejected: 12%

### Deadline Priority Tracking

Applications approaching their deadlines are automatically flagged to support timely regulatory action.

---

## Learning Outcomes

Through this project, I explored:

* Data cleaning using Pandas
* Date handling and calculations
* Filtering and sorting regulatory data
* Business-rule implementation using conditional logic
* Dashboard creation using Matplotlib and Seaborn
* Applying Python to Regulatory Affairs workflows

---

## Future Improvements

* Interactive dashboard using Streamlit
* Automated email alerts for urgent submissions
* Submission aging analysis
* CDSCO, FDA, EMA, and MHRA tracking in one dashboard
* KPI metrics for approval timelines
* Regulatory calendar integration

---

## Disclaimer

This project uses sample data for educational purposes and does not represent actual regulatory submissions.

---

## Author

**Shashank Limje**

Regulatory Affairs Student | Python for Pharma & Healthcare Analytics | Continuous Learner

---
