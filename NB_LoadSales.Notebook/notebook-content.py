# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f7362275-828d-416e-a2fb-d721e70e16ca",
# META       "default_lakehouse_name": "LC_Lakehouse",
# META       "default_lakehouse_workspace_id": "b511efa0-df7e-4f7d-805d-26ad45058abb",
# META       "known_lakehouses": [
# META         {
# META           "id": "f7362275-828d-416e-a2fb-d721e70e16ca"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
import pandas as pd

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# NB_LoadSales: demo notebook
# Change this comment to create a visible change.
df = spark.sql("SELECT 1 AS order_id, 'Laptop' AS product, 55000 AS amount")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# NB_LoadSales: demo notebook
# Change this comment to create a visible change.
df = spark.sql("SELECT 1 AS order_id, 'Laptop' AS product, 55000 AS amount")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
