# Working with Replica Locations 

Currently, Replica's plaform does not allow for us to combine multiple predefined geographies. These geographies are the ones that we can save and define in `Saved Selections`. These can be either network links or census tracts or even counties. 

An issue arises when we want to combine multiple of the `Saved Selections`. The current dashboard only allows you to filter to one of the selections and cannot add additional predefined ones.

An example of this issue happening is if we predefine the census tracts around train stations, we cannot select more than one train stations' census tracts. 

So, with census tracts already defined around each station, and saved for each locations separately, we need a way to connect those locations so we dont need to create new locations and reselect all the census tracts. 

This notebook does that by taking the already defined census tracts around each train station, downloading as shapefiles, and combining the census tracts for all stations except the one we want to define as the origin to create a new selection. Then save it out and upload to Replica in the `Custom Geographies`. 