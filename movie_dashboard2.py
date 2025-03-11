import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("imdb_top_1000.csv")
df["Gross"] = df["Gross"].str.replace(",","").astype(float)
df["Released_Year"] = pd.to_numeric(df["Released_Year"],errors='coerce')

st.sidebar.header("Filters")
selected_genre = st.sidebar.selectbox("Select Genre",df["Genre"].unique())
min_rating = st.sidebar.slider("Minimum IMDB Rating",0.0,10.0,7.0,0.1)

filtered_df = df[(df["IMDB_Rating"]>=min_rating)&(df["Genre"].str.contains(selected_genre))]

tab1,tab2,tab3=st.tabs(["Top Movies","Visualizations","Raw Data"])

with tab1:
    st.header("Top Movies")
    st.dataframe(filtered_df[["Series_Title","IMDB_Rating","Gross"]].sort_values(by="IMDB_Rating",ascending=False).head(10))

with tab2:
    st.header("Visualizations")
    fig=px.scatter(filtered_df,x="IMDB_Rating",y="Gross",size="No_of_Votes",hover_name="Series_Title")
    st.plotly_chart(fig)

with tab3:
    st.header("Raw Data")
    st.dataframe(filtered_df)
