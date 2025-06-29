# Name:     run_get_bls_data.py
# Date:     2025-06-20
# Author:   STEVEN M. GURIDI
#
# Description:
# Use the c_bls_data class to obtain series of data
# from the US Bureau of Labor Statistics (BLS) API.
import csv
import numpy as np
import pandas as pd
from CPI_Puller import CPI_Puller
from Power_Delivery import Power_Delivery
from US_Labor_Force import US_Labor_Force
from Lumber import US_Lumber


# @params API Key, Export_File, Series ID, start year, and year
# CUSR0000SA0 - All items in U.S. city average, all urban consumers, seasonally adjusted
# CUSR0000SETB01 - Gasoline (all types) in U.S. city average, all urban consumers, seasonally adjusted
# CUSR0000SAF1 - Food in U.S. city average, all urban consumers, seasonally adjusted
# CUSR0000SETA02 - Used cars and trucks in U.S. city average, all urban consumers, seasonally adjusted
df_ky = pd.read_csv('API_KEY.csv')
BLS_API_KEY = df_ky['BLS_API'][0]
#OUTPUT DEFLATOR ID: IPUCN2211__T051000000, REAL SECTOR OUTPUT ID: IPUCN2211__T011000000
#bls_dt = labor_US(BLS_API_KEY, 'POWER DELIVER SG.CSV' , ['IPUCN2211__T051000000', 'IPUCN2211__T011000000'], 2000, 2022 )
#CPI for Gas, Groceries, necessities. 
#CPI-->CUSR0000SA0 ALL URBAN AREAS
bls_dt = CPI_Puller(BLS_API_KEY, 'CPI_1990_MTD.csv',
                        ['CUSR0000SA0', 'CUSR0000SETB01', 'CUSR0000SAF1', 'CUSR0000SETA02']
                        , 2006, 2025)
Power_Delivery = Power_Delivery(BLS_API_KEY, 'POWER_SECTOR_OUTPUT.csv'
                                ,['IPUCN2211__T051000000', 'IPUCN2211__T011000000']
                                , 2006, 2023 )
# Labor Civilian Workforce code: LNS11000000, Employment code: LNS12000000
# 16 years and older and under 65 years old all civilians
#Pay and Benefits NBU20530000000000033030
Labor = US_Labor_Force(BLS_API_KEY, 'Labor_Force.csv'
                                ,['LNS11000000']
                                , 2006, 2025 )
#PCU321991321991  Manufactured home, mobile home, manufacturing
Lumber = US_Lumber(BLS_API_KEY, 'LUMBER_HOUSES.CSV',
                ['PCU321991321991'], 2006, 2025)
