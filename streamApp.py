import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from collections import Counter
import re

# Page configuration
st.set_page_config(page_title="Netflix Data Explorer", layout="wide")

# Caching Data Loading and Cleaning
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv('netflix_titles.csv')
    df = df.fillna({
        'director': 'Unknown',
        'cast': 'Unknown', 
        'country': 'Unknown',
    })
    df = df.dropna(subset=['date_added', 'rating', 'duration'])
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['first_country'] = df['country'].apply(lambda x: x.split(',')[0])
    return df

# Load the data
df = load_and_clean_data()

# Application Layout
st.title("🎬 Netflix Content Explorer")
st.write("An interactive dashboard to explore movies and TV shows on Netflix.")

# Sidebar for Filters
st.sidebar.header("Filter Options")

year_range = st.sidebar.slider(
    "Select a Release Year Range",
    min_value=int(df['release_year'].min()),
    max_value=int(df['release_year'].max()),
    value=(2010, 2022)
)

type_filter = st.sidebar.multiselect(
    "Select Content Type",
    options=df['type'].unique(),
    default=df['type'].unique()
)

# Filtering Data
filtered_df = df[
    (df['release_year'] >= year_range[0]) &
    (df['release_year'] <= year_range[1]) &
    (df['type'].isin(type_filter))
]

# Main Page Content
st.header(f"Showing {len(filtered_df)} Titles")
st.dataframe(filtered_df.head())

# Visualizations
st.header("Visualizations")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Content Producing Countries")
    top_countries = filtered_df['first_country'].value_counts().head(10)
    fig1, ax1 = plt.subplots()
    sns.barplot(y=top_countries.index, x=top_countries.values, ax=ax1, palette="viridis")
    ax1.set_title("Top 10 Countries")
    ax1.set_xlabel("Number of Titles")
    st.pyplot(fig1)

with col2:
    st.subheader("Content Type Distribution")
    type_counts = filtered_df['type'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=['#b20710', '#221f1f'])
    ax2.axis('equal')
    st.pyplot(fig2)

# Word frequency bar chart instead of word cloud
st.subheader("Common Words in Descriptions")
if not filtered_df.empty:
    text = " ".join(desc for desc in filtered_df.description.dropna()).lower()
    words = re.findall(r'\b[a-z]{3,}\b', text)
    word_counts = Counter(words).most_common(20)
    
    words, counts = zip(*word_counts)
    
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.bar(words, counts)
    ax3.set_title("Top 20 Words in Descriptions")
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)
else:
    st.write("No data to generate word cloud for the selected filters.")