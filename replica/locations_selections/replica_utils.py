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


gcs_path = "gs://calitp-analytics-data/data-analyses/big_data/MetroLink_LinkUS/"


def import_stations(station_list):
     
    all_df = []
    
    for station in station_list:
        with get_fs().open(f"{gcs_path}station_locations/saved-selection-geo-{station}_us-tract-2020.zip") as f:
            
            df = to_snakecase(gpd.read_file(f))
            
            df['station_name'] = station

            all_df.append(df)
            
    all_stations = pd.concat(all_df, ignore_index=True)
    
    return all_stations


def read_in_stations(all_stations_list):
    
    gdf_stations = import_stations(all_stations_list)
    
    all_station_list = pd.read_csv(f"{gcs_path}Station_lists.csv",  nrows=72)
    
    column_names = all_station_list.columns[2:12]
    
    all_station_list['transit_lines'] = all_station_list[column_names].apply(lambda row: ', '.join([col for col in column_names if row[col] == 'x']), axis=1)
    all_station_list = all_station_list.rename(columns={'station_name':'station_name_full', 'downloaded_geo_name':'station_name'})
    
    gdf_stations = gdf_stations.merge((all_station_list[['station_name_full','station_name','transit_lines']]), on="station_name", how="left")
    
    
    return gdf_stations
    


def aggregate_destination_station_geometries(df_all_stations, origin_stations_list):
    
    for station in origin_stations_list:
        station_destinations = df_all_stations >> filter(_.station_name != station)
        station_destinations_deduplicated = station_destinations.drop_duplicates(subset=['geoname'], keep='first')

        utils.make_zipped_shapefile(station_destinations_deduplicated, f"station_destinations/origin_{station}_destinations_network_wide.zip")
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
        

        
def define_transit_line(line):
    if line == "sbline":
        line_name = "San Bernardino Line"
    elif line == "riversideline":
        line_name = "Riverside Line"
    else:
        line_name = "Both"
        
    return line_name
    

def calc_auto_travel_info(df):
    df_auto = df[df.primary_mode=="private_auto"]
    
    auto_mean_min = df_auto.trip_duration_minutes.mean()
    auto_median_min = df_auto.trip_duration_minutes.median()
    auto_mean_miles = df_auto.trip_distance_miles.mean()
    auto_median_miles = df_auto.trip_distance_miles.median()
    
    return auto_mean_min, auto_median_min, auto_mean_miles, auto_median_miles


def calc_transit_travel_info(df):
    df_auto = df[df.primary_mode=="public_transit"]
    
    transit_mean_min = df_auto.trip_duration_minutes.mean()
    transit_median_min = df_auto.trip_duration_minutes.median()
    transit_mean_miles = df_auto.trip_distance_miles.mean()
    transit_median_miles = df_auto.trip_distance_miles.median()
    
    return transit_mean_min, transit_median_min, transit_mean_miles, transit_median_miles


def get_top_and_bottom_tract_counts(df, top_least, all_trips):
    tract_counts = df['destination_tract_station_area'].value_counts().reset_index()
    tract_counts.columns = ['destination_tract_station_area', 'count']
    
    if (top_least == ("top")):
        top_name1 = tract_counts.iloc[0, 0]
        # top_num1 = (tract_counts.iloc[0, 1])/all_trips

        # top_name2 = tract_counts.iloc[1, 0]
#         top_num2 = (tract_counts.iloc[1, 1])/all_trips

        # top_name3 = tract_counts.iloc[2, 0]
#         top_num3 = (tract_counts.iloc[2, 1])/all_trips
        
        return top_name1, #top_name2, #top_name3
    
    if (top_least == ("least")):
        bottom_name1 = tract_counts.iloc[(len(tract_counts)-1), 0]
        # bottom_num1 = tract_counts.iloc[(len(tract_counts)-1), 1]

        # bottom_name2 = tract_counts.iloc[(len(tract_counts)-2), 0]
#         # bottom_num2 = tract_counts.iloc[(len(tract_counts)-2), 1]

#         bottom_name3 = tract_counts.iloc[(len(tract_counts)-3), 0]
#         # bottom_num3 = tract_counts.iloc[(len(tract_counts)-3), 1]
        
        return bottom_name1, #bottom_name2, #bottom_name3
    
