import streamlit as st
import pandas as pd


today = st.date_input('Date', pd.to_datetime('today'))
yesterday = today - pd.Timedelta(days=1)
prior_year = yesterday - pd.Timedelta(weeks=52)

file = st.file_uploader('Calls Report','csv')

if file:
    df = pd.read_csv(file, index_col=False)
    df = df[df['Call Type'] == 'inbound']
    df['Start Time'] = pd.to_datetime(df['Start Time']).dt.date

    yesterday
    prior_year


    ydf = df[df['Start Time'] == yesterday]

    st.metric(str(yesterday), ydf.shape[0])

    pdf = df[df['Start Time'] == prior_year]

    st.metric(str(prior_year), pdf.shape[0])