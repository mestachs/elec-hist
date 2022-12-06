# https://docstore.entsoe.eu/Documents/Publications/Statistics/Factsheet/entsoe_sfs2018_web.pdf

import os

countries = ["be","fr","de","ch","at","ba","bg","es","gr","nl"]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
years = ["2015","2016","2017","2018","2019","2020","2021","2022"]

for country in countries:
    for year in years:
        for month in months:
            country_dir = f"./data/{country}"
            if not os.path.exists(country_dir):
                os.mkdir(country_dir)
            output_file = f"{country_dir}/month_{year}_{month}.json"
            if not os.path.exists(output_file):
                os.system(f"wget https://www.energy-charts.info/charts/power/data/{country}/month_{year}_{month}.json -O {output_file}")