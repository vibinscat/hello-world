#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:19:25 2020

@author: vibinscat
"""

from google.cloud import  bigquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "openaq" dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#List all tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

for table in tables:
    print(table.table_id)

# Construct a reference to the "global_air_quality" table
#table_ref = dataset_ref.table("global_air_quality")

# API request - fetch the table
#table = client.get_table(table_ref)

# Preview the first five lines of the "global_air_quality" table
#client.list_rows(table, max_results=5).to_dataframe()