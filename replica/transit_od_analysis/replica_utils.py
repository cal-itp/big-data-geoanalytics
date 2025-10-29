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


gcs_path = "gs://calitp-analytics-data/data-analyses/big_data/hta/"




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
        

        

def calc_auto_travel_info(df):
    df_auto = df[df.primary_mode=="private_auto"]
    
    auto_mean_min = df_auto.trip_duration_minutes.mean()
    auto_median_min = df_auto.trip_duration_minutes.median()
    
    auto_mean_miles = df_auto.trip_distance_miles.mean()
    auto_median_miles = df_auto.trip_distance_miles.median()
    
    auto_max_min = df_auto.trip_duration_minutes.max()
    auto_max_miles = df_auto.trip_distance_miles.max()
    
    return auto_mean_min, auto_median_min, auto_mean_miles, auto_median_miles, auto_max_min, auto_max_miles


def calc_transit_travel_info(df):
    df_auto = df[df.primary_mode=="public_transit"]
    
    transit_mean_min = df_auto.trip_duration_minutes.mean()
    transit_median_min = df_auto.trip_duration_minutes.median()
    
    transit_mean_miles = df_auto.trip_distance_miles.mean()
    transit_median_miles = df_auto.trip_distance_miles.median()
    
    transit_max_miles = df_auto.trip_distance_miles.max()
    transit_max_min = df_auto.trip_duration_minutes.max()
    
    return transit_mean_min, transit_median_min, transit_mean_miles, transit_median_miles, transit_max_miles, transit_max_min


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
    


#### NEED TO REFACTOR
### putting it all together
def return_score_summary(analyses_study_data_list, station_geom_list):
    
    #### read in the station geometries 
    #### this function also reads in the common names and transit lines
    gdf_stations_geom = read_in_stations(station_geom_list)
    
    results = []
    for analysis in analyses_study_data_list:

            auto_df = (df[df.primary_mode=="private_auto"])
            transit_df = (df[df.primary_mode=="public_transit"])

            all_trip_count = len(df)

            n_total_trips = len(df)
            n_private_auto_trips = len(auto_df)
            pct_private_auto_trips = ((len(auto_df)) / (len(df)))
            n_public_transit_trips = (len(transit_df))
            pct_public_transit_trips = ((len(transit_df)) / (len(df)))

            auto_mean_min, auto_median_min, auto_mean_miles, auto_median_miles, auto_max_min, auto_max_miles = calc_auto_travel_info(df)
            transit_mean_min, transit_median_min, transit_mean_miles, transit_median_miles, transit_max_miles, transit_max_min = calc_transit_travel_info(df)

            auto_top_name1, = get_top_and_bottom_tract_counts(auto_df, top_least = "top", all_trips=all_trip_count)
            auto_bottom_name1,  = get_top_and_bottom_tract_counts(auto_df, top_least = "least", all_trips=all_trip_count)
            # auto_top_name2, auto_top_name3,  auto_bottom_name2, auto_bottom_name3

            transit_top_name1,  = get_top_and_bottom_tract_counts(transit_df, top_least = "top", all_trips=all_trip_count)
            transit_bottom_name1, = get_top_and_bottom_tract_counts(transit_df, top_least = "least", all_trips=all_trip_count)
             # transit_top_name2, transit_top_name3
                 # transit_bottom_name2, transit_bottom_name3 

            ## set up the table for all the results
            results.append({
                    'station_name': station_name,
                    'station_name_full':station_name_full,
                    'metrolink_lines': line,
                    'total_trips_from_origin_station': n_total_trips,
                    'n_auto_trips_to_other_station_areas': n_private_auto_trips,
                    'pct_auto_trips_to_other_station_areas': pct_private_auto_trips,
                    'n_tranist_trips_to_other_station_areas': n_public_transit_trips,
                    'pct_transit_trips_to_other_station_areas': pct_public_transit_trips,
                    'auto_mean_minutes': auto_mean_min,
                    'auto_median_minutes': auto_median_min,
                    'auto_max_minutes': auto_max_min, 
                    'auto_mean_miles': auto_mean_miles,
                    'auto_median_miles': auto_median_miles,
                    'auto_max_miles': auto_max_miles,
                    'transit_mean_minutes': transit_mean_min,
                    'transit_median_minutes': transit_median_min,
                    'transit_max_minutes': transit_max_min,
                    'transit_mean_miles': transit_mean_miles,
                    'transit_median_miles': transit_median_miles,
                    'transit_max_miles':transit_max_miles,

                    'auto_top_tract_traveled_to': auto_top_name1,
                    # 'auto_top_tract_traveled_to_pct':auto_top_num1, 
                    # 'auto_second_top_tract_traveled_to':auto_top_name2, 
                    # 'auto_second_top_tract_traveled_to_pct':auto_top_num2, 
                    # 'auto_third_top_tract_traveled_to':auto_top_name3, 
                    # 'auto_third_top_tract_traveled_to_pct':auto_top_num3, 

                    'auto_least_tract_traveled_to': auto_bottom_name1,
                    # 'auto_second_least_tract_traveled_to':auto_bottom_name2, 
                    # 'auto_third_least_tract_traveled_to':auto_bottom_name3,  

                    'transit_top_tract_traveled_to': transit_top_name1,
                    # 'transit_top_tract_traveled_to_pct':transit_top_num1, 
                    # 'transit_second_top_tract_traveled_to':transit_top_name2, 
                    # 'transit_second_top_tract_traveled_to_pct':transit_top_num2, 
                    # 'transit_third_top_tract_traveled_to':transit_top_name3, 
                    # 'atransit_third_top_tract_traveled_to_pct':transit_top_num3, 

                    'transit_least_tract_traveled_to': transit_bottom_name1,
                    # 'transit_second_least_tract_traveled_to':transit_bottom_name2, 
                    # 'transit_third_least_tract_traveled_to':transit_bottom_name3
                    })

    result_summary = pd.DataFrame(results)   
    
    return result_summary
