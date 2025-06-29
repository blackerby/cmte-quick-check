import polars as pl
import streamlit as st
import httpx

from constants import TITLE, URL


st.set_page_config(TITLE, layout="wide")

st.title(TITLE)

response = httpx.get(URL)
data = response.json()
meetings = data["meetings"]

df = pl.DataFrame(meetings).filter(pl.col("cdg_json_status") != 200)

st.subheader("House Events with Error Codes in CDG")

st.dataframe(
    df,
    use_container_width=True,
    column_config={
        "cdg_api_url_json": st.column_config.LinkColumn(),
        "cdg_api_url_xml": st.column_config.LinkColumn(),
        "cdg_url": st.column_config.LinkColumn(),
        "house_repo_url": st.column_config.LinkColumn(),
    },
)
