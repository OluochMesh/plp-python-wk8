# CORD-19 Data Explorer

A Python Frameworks Assignment for basic analysis and visualization of the CORD-19 research dataset, presented in a Streamlit web application.

---

## Assignment Overview

This assignment guides you through:

- Loading and exploring a real-world dataset
- Basic data cleaning
- Creating meaningful visualizations
- Building a simple interactive web app
- Presenting data insights

---

## Learning Objectives

By completing this assignment, you will:

- Practice loading and exploring a real-world dataset
- Learn basic data cleaning techniques
- Create meaningful visualizations
- Build a simple interactive web application
- Present data insights effectively

---

## Dataset Information

We use the `metadata.csv` file from the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), which contains:

- Paper titles and abstracts
- Publication dates
- Authors and journals
- Source information

> **Note:** The full dataset is large. Use only the metadata file or a sample.

---

## Required Tools

- Python 3.7+
- pandas (data manipulation)
- matplotlib / seaborn (visualization)
- Streamlit (web application)
- Jupyter Notebook (optional, for exploration)

Install required packages:

```bash
pip install pandas matplotlib seaborn streamlit
```

---

## Step-by-Step Tasks

### Part 1: Data Loading and Basic Exploration

- Download `metadata.csv` from CORD-19
- Load into a pandas DataFrame
- Examine first few rows and structure
- Check DataFrame dimensions, data types, missing values, and basic statistics

### Part 2: Data Cleaning and Preparation

- Identify and handle missing data
- Create a cleaned dataset
- Convert date columns to datetime
- Extract year from publication date
- Create new columns (e.g., abstract word count)

### Part 3: Data Analysis and Visualization

- Count papers by publication year
- Identify top journals
- Find frequent words in titles
- Visualize:
  - Publications over time
  - Top publishing journals
  - Word cloud of titles
  - Distribution by source

### Part 4: Streamlit Application

- Build a simple Streamlit app:
  - Title and description
  - Interactive widgets (sliders, dropdowns)
  - Display visualizations
  - Show sample data

**Example app structure:**

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Add interactive elements
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
# Add visualizations based on selection
```

### Part 5: Documentation and Reflection

- Write comments in your code
- Create a brief report of findings
- Reflect on challenges and learning

---

## Evaluation Criteria

- **Complete implementation** (40%): All tasks completed
- **Code quality** (30%): Readable, well-commented code
- **Visualizations** (20%): Clear, appropriate charts
- **Streamlit app** (10%): Functional application

---

## Tips for Success

- Start small: Use a data subset if needed
- Focus on basics
- Debug incrementally
- Use documentation
- Ask for help if stuck

---

## Example Code Snippets

```python
# Load the data
import pandas as pd
df = pd.read_csv('metadata.csv')

# Basic info
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Simple visualization
import matplotlib.pyplot as plt
df['year'] = pd.to_datetime(df['publish_time']).dt.year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.show()
```

---

## Expected Outcomes

- Jupyter notebook or Python script with analysis
- Several visualizations showing data patterns
- Simple Streamlit app displaying findings
- Experience with the data science workflow
Debug incrementally: Test each part of your code as you write it

Use resources: Consult pandas and Streamlit documentation when stuck

Ask for help: Reach out to instructors or peers if you get stuck

Example Code Snippets
python
# Load the data
import pandas as pd
df = pd.read_csv('metadata.csv')

# Basic info
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Simple visualization
import matplotlib.pyplot as plt
df['year'] = pd.to_datetime(df['publish_time']).dt.year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.show()
Expected Outcomes

By completing this assignment, you will have:

A Jupyter notebook or Python script with your analysis

Several visualizations showing patterns in the data

A simple Streamlit application that displays your findings

Basic experience with the data science workflow
