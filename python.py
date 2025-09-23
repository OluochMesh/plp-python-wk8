import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
from collections import Counter
import re
import streamlit as st
#loading data
df= pd.read_csv('netflix_titles.csv')

#displaying first 5 rows
print("First 5 rows of the dataset:")
print(df.head())
#dataset dimensions
print("\nDataset dimensions:")
print(f" The data has {df.shape[0]} rows and {df.shape[1]} columns.")
# data types of each column
print("\nData types of each column:")
print(df.info())
# data cleaning, checking for missing values
print("\nMissing values in each column:")

# filling missing values in 'director' column with 'Unknown'
df = df.fillna({
    'director': 'Unknown',
    'cast': 'Unknown', 
    'country': 'Unknown',
})
# Some columns like 'date_added' and 'rating' have very few missing values.
df=df.dropna(subset=['date_added', 'rating', 'duration'],)
print(df.isnull().sum())

        # let us prepare our data for analysis
df['date_added']= df['date_added'].str.strip() # removing leading spaces
df['date_added']= pd.to_datetime(df['date_added'], errors='coerce') # converting to datetime
df['year_added']= df['date_added'].dt.year  # extracting year for time series analysis

df['description_word_count']= df['description'].str.split().str.len()
print(df.isnull().sum())
print(df.info())


sns.set_style("darkgrid")
plt.figure(figsize=(12,6))

content_by_year= df['release_year'].value_counts().sort_index()
#ploting data from 2000 onwards
content_by_year= content_by_year[content_by_year.index >= 2000]
sns.lineplot(x=content_by_year.index, y=content_by_year.values)
plt.title('Content Added by Year (2000 onwards)')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()

# Creating a bar chart of top publishing journals (countries)
df['first_country'] = df['country'].apply(lambda x: x.split(',')[0])
top_countries = df['first_country'].value_counts().head(10)

plt.figure(figsize=(12, 8))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Content Producing Countries on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()



# Alternative: Create a bar chart of most common words
text = " ".join(desc for desc in df.description.dropna()).lower()
words = re.findall(r'\b[a-z]{3,}\b', text)  # Get words of 3+ letters
word_counts = Counter(words).most_common(20)

words, counts = zip(*word_counts)

plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.title('Top 20 Words in Netflix Descriptions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Then the pie chart (this part should work fine)
type_counts = df['type'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=['#b20710', '#221f1f'])
plt.title('Distribution of Content: Movie vs. TV Show')
plt.legend()
plt.tight_layout()
plt.show()

