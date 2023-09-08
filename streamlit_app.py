import datetime
import pandas as pd
import numpy as np
import os
import streamlit as st
from src.stobjects import KpiComponent
from src.settings import SHOPIFY_TABLE_PATH
from src.html import html_code
import base64

st.set_page_config(layout="wide")

logo_image = os.path.abspath("/home/appuser/app/static/keboola.png")
logo_html = f'<div style="display: flex; justify-content: flex-end;"><img src="data:image/png;base64,{base64.b64encode(open(logo_image, "rb").read()).decode()}" style="width: 100px; margin-left: -10px;"></div>'
st.markdown(f"{logo_html}", unsafe_allow_html=True)
st.title("Interactive KPI Reporting")

@st.cache_data()
def read_df(table_path, index_col=None, date_col=None):
    return pd.read_csv(table_path,  index_col=index_col, parse_dates=date_col)

# 1 mock a dataframe
message = "from inside2 false"
rec = [{'channel':'tmp_streamlit_slack', 'text':message}]

# LINK TO THE CUSTOM CSS FILE
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

date_from_c, date_to_c = st.columns(2)

df_shopify = read_df(SHOPIFY_TABLE_PATH, date_col=["date"])
df_shopify.sort_values(by="date", inplace=True)

with date_from_c:
    DFROM = st.date_input(
        "From",
        min(df.date.min(),df_shopify.date.min()) 
    )

with date_to_c:
    DTO = st.date_input(
        "To",
        datetime.date.today()
    )

DFROM = DFROM.isoformat()
DTO = DTO.isoformat()

c_sales, c_orders, c_new_customers = st.columns(3)
with c_sales:
    salesc = KpiComponent(df_shopify, "sales", np.sum, dto=DTO, dfrom=DFROM)
with c_orders:
    ordersc = KpiComponent(df_shopify, "orders", np.mean, dto=DTO, dfrom=DFROM)
with c_new_customers:
    customersc = KpiComponent(df_shopify, "new customers", np.sum, dto=DTO, dfrom=DFROM)

c_margin, c_avg_order, c_conv_rate = st.columns(3)
with c_margin:
    customersc = KpiComponent(df_shopify, "total customers", np.sum, dto=DTO, dfrom=DFROM)
with c_avg_order:
    customersc = KpiComponent(df_shopify, "average order value", np.sum, dto=DTO, dfrom=DFROM)
#with c_conv_rate:
#    customersc = KpiComponent(df, "conversion_rate", np.sum, dto=DTO, dfrom=DFROM)
