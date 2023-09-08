#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:05:14 2023

@author: ondrejsvoboda
"""
import streamlit as st
from kbcstorage.client import Client

DECIMALS = 1


# credentials
KEBOOLA_STACK = st.secrets["kbc_url"]
KEBOOLA_TOKEN = st.secrets["kbc_token"]
keboola_client = Client(KEBOOLA_STACK, KEBOOLA_TOKEN)

# keboola settings
SHOPIFY_TABLE_PATH = '/data/in/tables/shopify_metrics.csv'