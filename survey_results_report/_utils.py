'''
Utils for preparing a summary report of the results we got from our surveys. 


'''
import pandas as pd 
import altair as alt

from calitp_data_analysis.sql import to_snakecase
from calitp_data_analysis import calitp_color_palette as cp


from IPython.display import Markdown, HTML, display_html, display
from IPython.core.display import display

from siuba import *

import ast
import numpy as np

import _utils


def read_in_data(sheetname):
    ## read in the data from google docs where the survey is being collected
    sheet_id = "1KwmAzwrl7sKupS8ZX33HzG-SpUSL65sSrW_Ns5a6h3w"
    sheet_name = sheetname
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = to_snakecase(pd.read_csv(url))
    
    ## convert timestamp column in datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    ## filter the survey responses to when the survey went live
    ## this removes the test responses the team sent in
    df = df[(df['timestamp'] > '2024-07-10 17:30:00')]
    
    ## remove the email attached to the response. 
    df = df.drop('caltrans_email', axis=1)
    
    ## rename some of the columns: 
    df = df.rename(columns={"what_are_you_typically_using_the_platforms_for?_what_types_of_analyses_are_you_running?_\n_ex__to_gather_speed_data,_downloading_segment_analysis_data_for_additional_analysis_outside_the_platform_":"what_types_of_analyses_are_you_running?",
                            "do_you_have_any_success_stories_that_you_would_like_to_share?_or_stories_on_how_you_applied_the_data_to_projects?":"do_you_have_any_success_stories_that_you_would_like_to_share?",
                            "what_district_division_of_caltrans_are_you_in?_":"what_district_division_of_caltrans_are_you_in?",
                           "what_sorts_of_challenges_are_you_facing?_":"what_sorts_of_challenges_are_you_facing?",
                        "what_are_the_common_modes_of_transportation_you_are_running_analyses_for?":"what_are_the_common_modes_of_transportation_you_are_running?",
                           "have_you_utilized_the_resources_training_streetlight_and_replica_provide?":"have_you_utilized_the_resources_training?"})
    
    if sheetname==("Streetlight_and_Replica"):
        df = df.rename(columns={'how_often_do_you_use_the_streetlight_and_or_replica_platforms?':'how_often_do_you_use_the_platforms?',
                                'would_you_like_to_be_part_of_the_caltrans_big_data_user_group_for_replica_and_streetlight?\nthis_user_group_would_be_internal_just_for_caltrans_and_would_meet_quarterly__':'would_you_like_to_be_part_of_the_user_groups?',
                                'what_sorts_of_challenges_are_you_facing?_\n_can_be_for_just_one_or_both_platforms_':'what_sorts_of_challenges_are_you_facing?'})

    elif sheetname==("Streetlight"):
        df = df.rename(columns={'how_often_do_you_use_streetlight?':'how_often_do_you_use_the_platforms?',
                                'would_you_like_to_be_part_of_the_caltrans_big_data_user_group_for_streetlight?\nthis_user_group_would_be_internal_just_for_caltrans_and_would_meet_quarterly__':'would_you_like_to_be_part_of_the_user_groups?',
                               "what_are_you_typically_using_the_platforms_data_for?\n_ex__to_gather_speed_data,_downloading_segment_analysis_data_for_additional_analysis_outside_the_platform_":"what_types_of_analyses_are_you_running?",
                               "have_you_utilized_the_resources_training_streetlight_provides?":"have_you_utilized_the_resources_training?",
                               "if_yes,_is_there_a_particular_reason_why_you_gravitated_towards_streetlight?":"if_you_do_gravitate_towards_one_platform_more,_could_you_briefly_explain_why?"})
   
    elif sheetname==("Replica"):
        df = df.rename(columns={'how_often_do_you_use_replica?':'how_often_do_you_use_the_platforms?', 
                                'what_types_of_analyses_are_you_running?':'which_types_of_analyses_that_you_typically_use?',
                                'would_you_like_to_be_part_of_the_caltrans_big_data_user_group_for_replica?\nthis_user_group_would_be_internal_just_for_caltrans_and_would_meet_quarterly__':'would_you_like_to_be_part_of_the_user_groups?',
                               'have_you_utilized_the_training_resources_replica_provides?':'have_you_utilized_the_resources_training?',
                               'what_are_you_typically_using_the_platforms_data_for?_\n__ex__to_gather_speed_data,_downloading_study_data_for_additional_analysis_outside_the_platform_':'what_types_of_analyses_are_you_running?'})
    
    
    return df


def title_column_names(df):
    df.columns = df.columns.map(str.title) 
    df.columns = df.columns.map(lambda x : x.replace("_", " "))
    
    return df


def chart_results(df, column_list):
    for col in column_list:
        chart = (
            alt.Chart(df>>filter(_[col].notnull()))
            .mark_bar()
            .encode(
                x=alt.X(col),
                 y='count()',
                color=alt.Color(col, scale=alt.Scale(range = cp.CALITP_DIVERGING_COLORS,)
                ))
          .properties(title=col,
        width=800,
        height=300))
        
        display(chart)
        
        
##https://github.com/cal-itp/data-analyses/blob/corridor_study_sb125/sb125_analyses/corridor_study/_utils.py
def get_list_of_responses(df, response):
    
    ## Get just one columns
    column = df[[response]]
    #remove single-dimensional entries from the shape of an array
    col_text = column.squeeze()
    # get list of words
    text_list = col_text.tolist()
    # #join list of words 
    text_list = ', '.join(text_list).title()
    
    text_list = text_list.replace(", ", "', '")
    text_list = "['" + text_list + "']"
    
    response_list = ast.literal_eval(text_list)
    response_list = set(response_list)
    
    return response_list

