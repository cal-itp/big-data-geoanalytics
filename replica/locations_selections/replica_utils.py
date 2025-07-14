import geopandas as gpd
import pandas as pd
from siuba import *
import numpy as np

from calitp_data_analysis.sql import to_snakecase
from calitp_data_analysis import utils
from calitp_data_analysis import get_fs
import gcsfs as fs
fs = get_fs()

import os
import shutil


gcs_path = "gs://calitp-analytics-data/data-analyses/big_data/lossan_stations/"


def import_stations(station_list):
     
    all_df = []
    
    for station in station_list:
        with get_fs().open(f"{gcs_path}saved-selection-geo-{station}_us-tract-2020.zip") as f:
            
            df = to_snakecase(gpd.read_file(f))
            
            df['station_name'] = station

            all_df.append(df)
            
    all_stations = pd.concat(all_df, ignore_index=True)
    
    return all_stations


def aggregate_destination_station_geometries(df_all_stations, origin_stations_list):
    
    for station in origin_stations_list:
        station_destinations = df_all_stations >> filter(_.station_name != station)
        station_destinations_deduplicated = station_destinations.drop_duplicates(subset=['geoname'], keep='first')

        utils.make_zipped_shapefile(station_destinations_deduplicated, f"station_destinations/origin_{station}_destinations_network_wide_2.zip")
        # station_destinations.to_file(f"{gcs_path}station_destinations_combined/{station}_destinations.shp", driver="ESRI Shapefile")

        print(f"Sucessfully exported {station} destinations to gcs")

    ### remove locations folder
    ### this function also puts a location in the root of the folder
    folder_to_delete = "./station_destinations"  # Replace with the actual path to your folder

    if os.path.isdir(folder_to_delete):
        try:
            shutil.rmtree(folder_to_delete)
            print(f"The folder '{folder_to_delete}' and its contents have been successfully removed.")
        except OSError as e:
            print(f"Error: {folder_to_delete} : {e.strerror}")
    else:
        print(f"The folder '{folder_to_delete}' does not exist.")