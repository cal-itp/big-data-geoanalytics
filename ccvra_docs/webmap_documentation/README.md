# Webmap Documentation

The following provides details on the [CCVRA Webmap](https://experience.arcgis.com/experience/8854a622e61849e5af86256b6f0c69a9), including background on the data structure, data fields, and setup of the webmap. 

### Data 
The data was originally received from the consultants as 20 individual layers, one layer for each hazard type and asset combination (5 hazard types, 4 asset types). From there, the data layers were combined based on hazard type to a total 5 hazard layers. 


### WebMap
The webmap showcases the different climate scenarios throughout the years, starting with an analysis for present-day. In the data, the risk ratings for the various scenarios are columns within the layer. To visualize the different scenarios, we created the WebMap to better see the risk ratings between scenarios.


#### Color Schemes
Colors are unique to the climate hazard and risk rating. The risk ratings, as stated previously, vary between the values of Negligible and Extremely High. Not every risk rating is present in each harzard layer, however each risk rating is assigned a color to keep consistency amongst the hazard types. Color Schemes were chosen using colorbrewer sequential colors for the nine classes and applied to the data using an arcpy script.

**Coastal Flood**
* Negligible: #f7fcf0
* Very-Low: #e0f3db
* Low: #ccebc5
* Low-Medium: #a8ddb5
* Medium: #k7bccc4
* Medium-High: #4eb3d3
* High: #2b8cbe
* Very High: #0868ac
* Extremely High: #084081
  
**Riverine Flood**
* Negligible: #ffffd9
* Very-Low: #edf8b1
* Low: #c7e9b4
* Low-Medium: #7fcdbb
* Medium: #41b6c4
* Medium-High: #1d91c0
* High: #225ea8
* Very High: #253494
* Extremely High: #081d58
  
**Coastal Erosion**
* Negligible: #f7fcfd
* Very-Low: #e5f5f9
* Low: #ccece6
* Low-Medium: #99d8c9
* Medium: #66c2a4
* Medium-High: #41ae76
* High: #006d2c
* Very High: #006d2c
* Extremely High: #00441b
  
**Wildfire**
* Negligible: #ffffcc
* Very-Low: #ffeda0
* Low: #fed976
* Low-Medium: #feb24c
* Medium: #fd8d3c
* Medium-High: #fc4e2a
* High: #e31a1c
* Very High: #bd0026
* Extremely High: #800026
  
**Landslide**
* Negligible: #ffffe5
* Very-Low: #f7fcb9
* Low: #d9f0a3
* Low-Medium: #addd8e
* Medium: #78c679
* Medium-High: #41ab5d
* High: #238443
* Very High: #006837
* Extremely High: #004529