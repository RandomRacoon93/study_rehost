import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import folium
from streamlit_folium import st_folium
import json
from geopandas.tools import geocode
with st.echo(code_location='below'):
    df_1 = pd.read_csv("Height.csv")
    df_2 = pd.read_csv("500.csv")
    df_3 = pd.read_csv("mass.csv")

    st.header("Select the country for which you want to receive data on height, weight and body mass index")
    country = st.selectbox(
        "Country", df_1["Country Name"].value_counts().index)
    df_selection = df_1[lambda x: x["Country Name"] == country]
    df_selection
    df_sel = df_3[lambda y: y["Country"] == country]
    df_sel

    st.header("You can see which countries have the highest and lowest heights for men and women")
    the_most = st.selectbox(
        'The highest or the lowest',
        ('the highest', 'the lowest'))
    gen = st.selectbox(
        'Gender',
        ('men', 'women'))

    if (the_most == 'the lowest' and gen == 'men'):
        df_11 = df_1.sort_values(by=['Male Height in Cm'])[:10]
        fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
        ax.vlines(x=df_11['Country Name'], ymin=155, ymax=df_11['Male Height in Cm'], color='blue', alpha=0.7, linewidth=2)
        ax.scatter(x=df_11['Country Name'], y=df_11['Male Height in Cm'], s=75, color='blue', alpha=0.7)
        st.pyplot(fig)
    if (the_most == 'the highest' and gen == 'men'):
        df_11 = df_1.sort_values(by=['Male Height in Cm'])[-10:]
        fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
        ax.vlines(x=df_11['Country Name'], ymin=180, ymax=df_11['Male Height in Cm'], color='blue', alpha=0.7, linewidth=2)
        ax.scatter(x=df_11['Country Name'], y=df_11['Male Height in Cm'], s=75, color='blue', alpha=0.7)
        st.pyplot(fig)
    if (the_most == 'the lowest' and gen == 'women'):
        df_11 = df_1.sort_values(by=['Female Height in Cm'])[:10]
        fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
        ax.vlines(x=df_11['Country Name'], ymin=150, ymax=df_11['Female Height in Cm'], color='blue', alpha=0.7,
                  linewidth=2)
        ax.scatter(x=df_11['Country Name'], y=df_11['Female Height in Cm'], s=75, color='blue', alpha=0.7)
        st.pyplot(fig)
    if (the_most == 'the highest' and gen == 'women'):
        df_11 = df_1.sort_values(by=['Female Height in Cm'])[-10:]
        fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
        ax.vlines(x=df_11['Country Name'], ymin=165, ymax=df_11['Female Height in Cm'], color='blue', alpha=0.7,
                  linewidth=2)
        ax.scatter(x=df_11['Country Name'], y=df_11['Female Height in Cm'], s=75, color='blue', alpha=0.7)
        st.pyplot(fig)

    ###in the process of creating maps this link was used: https://pythonim.ru/libraries/geopandas-v-python .
    st.header("The country with the largest growth of men and women on the map (Netherlands)")
    loc = 'Netherlands'
    location = geocode(loc, provider="nominatim", user_agent='my_request')
    point = location.geometry.iloc[0]
    df = pd.DataFrame({"longitude": [point.x], "latitude": [point.y]})
    mapit = folium.Map(location=[0, 0], zoom_start=1)
    for lat, lon in zip(df.latitude, df.longitude):
        folium.Marker(location=[lat, lon], fill_color='#43d9de', radius=8).add_to(mapit)
    ans = st_folium(mapit, width=725)
    ans

    st.header("The country with the lowest growth of men on the map (Timor-Lest)")
    loc = 'Timor-Leste'
    location = geocode(loc, provider="nominatim", user_agent='my_request')
    point = location.geometry.iloc[0]
    df = pd.DataFrame({"longitude": [point.x], "latitude": [point.y]})
    mapit = folium.Map(location=[0, 0], zoom_start=1)
    for lat, lon in zip(df.latitude, df.longitude):
        folium.Marker(location=[lat, lon], fill_color='#43d9de', radius=8).add_to(mapit)
    ans = st_folium(mapit, width=725)
    ans

    st.header("The country with the lowest growth of women on the map (Guatemala)")
    loc = 'Guatemala'
    location = geocode(loc, provider="nominatim", user_agent='my_request')
    point = location.geometry.iloc[0]
    df = pd.DataFrame({"longitude": [point.x], "latitude": [point.y]})
    mapit = folium.Map(location=[0, 0], zoom_start=1)
    for lat, lon in zip(df.latitude, df.longitude):
        folium.Marker(location=[lat, lon], fill_color='#43d9de', radius=8).add_to(mapit)
    ans = st_folium(mapit, width=725)
    ans

    st.markdown("Now let's take the height, weight and body mass index data of 500 random people from the US.")
    fig, ax = plt.subplots(figsize=(30, 50), dpi=80)
    sns.stripplot(df_2.Height, df_2.Weight, jitter=0.25, size=8, ax=ax, linewidth=.7, orient='h')
    plt.title('Height and weight of people from a sample size of 500 people', fontsize=50)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=20)
    ax.set_xlabel("Height", fontsize=40)
    ax.set_ylabel("Weight", fontsize=40)
    st.pyplot(fig)
    st.markdown(
        "The only conclusion that can be drawn from this graph is that the people in the sample were chosen randomly. The points are approximately evenly spaced. Only tall, short, slender or fat were not included in the sample.")
    st.markdown("")

    fig = plt.figure(figsize=(15, 12), dpi=80)
    sns.boxplot(x='Gender', y='Height', data=df_2, notch=False)
    plt.title('Height', fontsize=30)
    st.pyplot(fig)

    fig = plt.figure(figsize=(15, 12), dpi=80)
    sns.boxplot(x='Gender', y='Weight', data=df_2, notch=False)
    plt.title('Weight', fontsize=30)
    st.pyplot(fig)

    fig = plt.figure(figsize=(15, 12), dpi=80)
    sns.boxplot(x='Gender', y='Index', data=df_2, notch=False)
    plt.title('Mass index', fontsize=30)
    st.pyplot(fig)

    df_counts = df_2.groupby(['Index']).size().reset_index(name='counts')
    ###in the process of writing this code was used https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#35.-Time-Series-Plot .
    categories = df_counts.shape[0]
    colors = [plt.cm.inferno_r(i / float(categories)) for i in range(categories)]
    fig = plt.figure(
        FigureClass=Waffle,
        plots={
            111: {
                'values': df_counts['counts'],
                'labels': ["{0}".format(n[0], n[1]) for n in df_counts[['Index', 'counts']].itertuples()],
                'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1.2), 'fontsize': 22},
            },
        },
        rows=10,
        colors=colors,
        figsize=(20, 15)
    )
    plt.title('Distribution of body mass index', fontsize=40)
    st.pyplot(fig)
    st.markdown(
        "We see that the higher the body mass index, the more people who have it. Hence the conclusion that many Americans have a high body mass index, which corresponds to obesity.")
