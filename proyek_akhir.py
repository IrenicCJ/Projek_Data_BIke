import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Analisis Data Bike Sharing")
df1=pd.read_csv("https://raw.githubusercontent.com/IrenicCJ/Projek_Data_BIke/main/Bike-sharing-dataset/day.csv")
df2=pd.read_csv("https://raw.githubusercontent.com/IrenicCJ/Projek_Data_BIke/main/Bike-sharing-dataset/hour.csv")
tab1, tab2, tab3, tab4 = st.tabs(["Perbedaan Pengguna", "Jam Paling Ramai", "Perbandingan Season", "Total Sewa PerBulan"])
with tab1:
    st.header("Persentase pengguna casual dan registered")
    user = ('Casual', 'Registered')
    votes = (df1['casual'].sum(), df1['registered'].sum())  
    colors = ('#8B4513', '#FFF8DC')
    explode = (0.2, 0)

    fig, ax = plt.subplots()  
    ax.pie(x=votes, labels=user, autopct='%1.1f%%', colors=colors, explode=explode)  
    st.pyplot(fig)

with tab2:
    st.header("Jam dengan total penyewaan paling banyak")
    
    grouped_data = df2.groupby(by="hr")['cnt'].sum().sort_values(ascending=False)  
    
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped_data.plot(kind='bar', color='skyblue', ax=ax)
    plt.title('Total Rental by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Total Rental')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

with tab3:
    st.header("Perbandingan Season")
    Season = ('Spring', 'Summer', 'Winter', 'Fall')
    votes = df1.groupby(by="season").cnt.sum()
    colors = ('#8B4513', '#FFF8DC', '#FF0000', '#0000FF')
    explode = (0 , 0, 0.2, 0)
    fig, ax = plt.subplots()  
    ax.pie(x=votes, labels=Season, autopct='%1.1f%%', colors=colors, explode=explode)  
    st.pyplot(fig)

with tab4:
    st.header("Bulan dengan penyewa sepeda terbanyak")
    
    grouped_data = df1.groupby(by="mnth")['cnt'].sum().sort_values(ascending=False)  
    
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped_data.plot(kind='bar', color='skyblue', ax=ax)
    plt.title('Total Rental by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Rental')
    plt.xticks(rotation=0) 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
