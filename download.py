# https://docstore.entsoe.eu/Documents/Publications/Statistics/Factsheet/entsoe_sfs2018_web.pdf

import os

countries = ["be","fr"]

months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
years = ["2015","2016","2017","2018","2019","2020","2021","2022"]

for country in countries:
    for year in years:
        for month in months:
            os.system(f"wget https://www.energy-charts.info/charts/power/data/{country}/month_{year}_{month}.json -O ./data/{country}/month_{year}_{month}.json")