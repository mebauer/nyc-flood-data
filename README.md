# Flood Data for New York City: A Comprehensive Inventory on NYC Open Data
Author: Mark Bauer

### Table of Contents
* [Introduction](#Introduction)
* [Dataset Summary Statistics](#Dataset-Summary-Statistics)
* [Dataset Descriptions](#Dataset-Descriptions)
    * [Flood Hazard Layers](#Flood-Hazard-Layers)
    * [Additional Datasets Related to Flooding](#Additional-Datasets-Related-to-Flooding)
    * [Unconventional Datasets](#Unconventional-Datasets)
* [Resources](#Resources)
* [Say Hello!](#Say-Hello)

# Introduction
This project compiles freely accessible flood data from NYC Open Data and conducts an analysis based on datasets with the highest downloads and page views. The methodology and outcomes are documented in the [analysis.ipynb](https://github.com/mebauer/nyc-flood-data/blob/main/analysis.ipynb) notebook, emphasizing the use of open-source and reproducible workflows. For specific flood-related information within datasets like 311 Service Requests from 2010 to Present, Emergency Response Incidents, NYCEM Emergency Notifications, Incidents Responded to by Fire Companies, and Street Construction Permits, refer to the [searchstring-flood.ipynb](https://github.com/mebauer/nyc-flood-data/blob/main/searchstring-flood.ipynb) notebook.

The flood datasets are categorized into two groups:

- **Flood Hazard Layers:** Typically provided as shapefiles, examples include stormwater flood maps, Sandy inundation zones, hurricane evacuation zones, etc.
- **Additional Data Related to Flooding:** These datasets are somewhat related to flooding and/or flood risk information, encompassing 311 street flooding complaints, green infrastructure projects, Hazard Mitigation Plan projects, etc.

Explore tables detailing download counts and page views per dataset below, followed by a comprehensive inventory of flood datasets available on NYC Open Data.

# Dataset Summary Statistics
Table xx: Top 10 flood datasets by total downloads on NYC Open Data.
|   rank | name                                                  | id        | created_date   |   download_count |   download_per_day |
|-------:|:------------------------------------------------------|:----------|:---------------|-----------------:|-------------------:|
|      1 | Hurricane Evacuation Centers (Map)                    | ayer-cga7 | 2022-08-01     |           230890 |             261.19 |
|      2 | Sea Level Rise Maps (2020s 100-year Floodplain)       | ezfn-5dsb | 2013-07-23     |           211663 |              50.64 |
|      3 | Hurricane Evacuation Zones                            | uihr-hn7s | 2015-07-14     |            41530 |              12.01 |
|      4 | DEP Green Infrastructure                              | spjh-pz7h | 2017-08-31     |            27796 |              10.37 |
|      5 | Sandy Inundation Zone                                 | uyj8-7rv5 | 2015-11-09     |            20293 |               6.08 |
|      6 | 1 foot Digital Elevation Model (DEM)                  | dpc8-z3jc | 2013-08-09     |             6524 |               1.57 |
|      7 | Land Cover Raster Data (2017) – 6in Resolution        | he6d-2qns | 2018-12-07     |             4674 |               2.11 |
|      8 | Sea Level Rise Maps (2050s 100-year Floodplain)       | hbw8-2bah | 2013-07-23     |             2546 |               0.61 |
|      9 | Sea Level Rise Maps (2050s 500-year Floodplain)       | qwca-zqw3 | 2013-07-23     |             2414 |               0.58 |
|     10 | DEP's Citywide Parcel-Based Impervious Area GIS Study | uex9-rfq8 | 2020-07-13     |             1970 |               1.21 |
  
<br />


Table xx: Top 10 flood datasets by total page views on NYC Open Data.
|   rank | name                                                  | id        | created_date   |   page_views_total |   page_views_per_day |   page_views_last_week |   page_views_last_month |
|-------:|:------------------------------------------------------|:----------|:---------------|-------------------:|---------------------:|-----------------------:|------------------------:|
|      1 | Sandy Inundation Zone                                 | uyj8-7rv5 | 2015-11-09     |              62224 |                18.63 |                     88 |                     543 |
|      2 | Sea Level Rise Maps (2050s 500-year Floodplain)       | qwca-zqw3 | 2013-07-23     |              53228 |                12.74 |                    130 |                     884 |
|      3 | 1 foot Digital Elevation Model (DEM)                  | dpc8-z3jc | 2013-08-09     |              38345 |                 9.21 |                     80 |                     680 |
|      4 | Sea Level Rise Maps (2020s 100-year Floodplain)       | ezfn-5dsb | 2013-07-23     |              31782 |                 7.6  |                     36 |                     450 |
|      5 | DEP Green Infrastructure                              | spjh-pz7h | 2017-08-31     |              19668 |                 7.34 |                     40 |                     432 |
|      6 | Land Cover Raster Data (2017) – 6in Resolution        | he6d-2qns | 2018-12-07     |              12934 |                 5.83 |                     23 |                     333 |
|      7 | Hurricane Evacuation Zones                            | uihr-hn7s | 2015-07-14     |              12346 |                 3.57 |                     24 |                     163 |
|      8 | Sea Level Rise Maps (2050s 100-year Floodplain)       | hbw8-2bah | 2013-07-23     |              12085 |                 2.89 |                      8 |                     142 |
|      9 | Hurricane Evacuation Centers (Map)                    | ayer-cga7 | 2022-08-01     |              10099 |                11.42 |                      4 |                     116 |
|     10 | DEP's Citywide Parcel-Based Impervious Area GIS Study | uex9-rfq8 | 2020-07-13     |               9260 |                 5.67 |                     36 |                     218 |
<br />

Table xx: Top 10 flood datasets by average of total downloads per day and page views per day on NYC Open Data.
|   rank | name                                                  | id        | created_date   |   downloads_and_views |   download_count |   page_views_total |
|-------:|:------------------------------------------------------|:----------|:---------------|----------------------:|-----------------:|-------------------:|
|      1 | Sea Level Rise Maps (2020s 100-year Floodplain)       | ezfn-5dsb | 2013-07-23     |                243462 |           211663 |              31799 |
|      2 | Hurricane Evacuation Centers (Map)                    | ayer-cga7 | 2022-08-01     |                240996 |           230890 |              10106 |
|      3 | Sandy Inundation Zone                                 | uyj8-7rv5 | 2015-11-09     |                 82549 |            20293 |              62256 |
|      4 | Sea Level Rise Maps (2050s 500-year Floodplain)       | qwca-zqw3 | 2013-07-23     |                 55698 |             2414 |              53284 |
|      5 | Hurricane Evacuation Zones                            | uihr-hn7s | 2015-07-14     |                 53886 |            41530 |              12356 |
|      6 | DEP Green Infrastructure                              | spjh-pz7h | 2017-08-31     |                 47479 |            27796 |              19683 |
|      7 | 1 foot Digital Elevation Model (DEM)                  | dpc8-z3jc | 2013-08-09     |                 44894 |             6524 |              38370 |
|      8 | Land Cover Raster Data (2017) – 6in Resolution        | he6d-2qns | 2018-12-07     |                 17626 |             4679 |              12947 |
|      9 | Sea Level Rise Maps (2050s 100-year Floodplain)       | hbw8-2bah | 2013-07-23     |                 14636 |             2546 |              12090 |
|     10 | DEP's Citywide Parcel-Based Impervious Area GIS Study | uex9-rfq8 | 2020-07-13     |                 11238 |             1971 |               9267 |

# Dataset Descriptions
## Flood Hazard Layers
| Dataset | Description |
| :-------- | :---------- |
| [Sandy Inundation Zone](https://data.cityofnewyork.us/Environment/Sandy-Inundation-Zone/uyj8-7rv5) | Areas of New York City that were flooded as a result of Hurricane Sandy. |
| [NYC Stormwater Flood Maps](https://data.cityofnewyork.us/Environment/NYC-Stormwater-Flood-Maps/9i7c-xyvv) | A collection of citywide Geographic Information System (GIS) layers that show areas of potential flooding scenarios under varying sea level rise conditions. Please see the New York City Stormwater Resiliency Plan for more information about the methodology applied to develop the maps. |
| [Hurricane Inundation by Evacuation Zone](https://data.cityofnewyork.us/Environment/Hurricane-Inundation-by-Evacuation-Zone/uk9f-6y9n) | These inundation areas are based on the National Hurricane Center’s 2020 SLOSH (Sea Lake and Overland Surge from Hurricanes) Model for the NE1 basin post-processed to a 10 meter resolution. The data used assumes that the storm surge will occur at high tide. The Storm surge inundation data then used to develop New York City’s Hurricane Evacuation Zones. |
| [Hurricane Inundation by Evacuation Zones (Map)](https://data.cityofnewyork.us/Environment/Hurricane-Inundation-by-Evacuation-Zone-Map-/2234-9r2y) | Hurricane Inundation by Evacuation Zones Map. See above. |
| [Sea Level Rise Maps (2020s 100-year Floodplain](https://data.cityofnewyork.us/Environment/Sea-Level-Rise-Maps-2020s-100-year-Floodplain-/ezfn-5dsb) | This is the 100-Year Floodplain for the 2020s based on FEMA's Preliminary Work Map data and the New York Panel on Climate Change's 90th Percentile Projects for Sea-Level Rise (11 inches). Please see the Disclaimer PDF for more information. Data Provided by the Mayor's Office of Long-Term Planning and Sustainability (OLTPS) on behalf of CUNY Institute for Sustainable Cities (CISC) and the New York Panel on Climate Change (NPCC). |
| [Sea Level Rise Maps (2020s 500-year Floodplain)](https://data.cityofnewyork.us/Environment/Sea-Level-Rise-Maps-2020s-500-year-Floodplain-/ajyu-7sgg) | This is the 500-Year Floodplain for the 2020s based on FEMA's Preliminary Work Map data and the New York Panel on Climate Change's 90th Percentile Projects for Sea-Level Rise (11 inches). Please see the Disclaimer PDF for more information. Data Provided by the Mayor's Office of Long-Term Planning and Sustainability (OLTPS) on behalf of CUNY Institute for Sustainable Cities (CISC) and the New York Panel on Climate Change (NPCC). |
| [Sea Level Rise Maps (2050s 100-year Floodplain](https://data.cityofnewyork.us/Environment/Sea-Level-Rise-Maps-2050s-100-year-Floodplain-/hbw8-2bah) | This is the 100-Year Floodplain for the 2050s based on FEMA's Preliminary Work Map data and the New York Panel on Climate Change's 90th Percentile Projects for Sea-Level Rise (31 inches). Please see the Disclaimer PDF for more information. Data Provided by the Mayor's Office of Long-Term Planning and Sustainability (OLTPS) on behalf of CUNY Institute for Sustainable Cities (CISC) and the New York Panel on Climate Change (NPCC). |
| [Sea Level Rise Maps (2050s 500-year Floodplain)](https://data.cityofnewyork.us/Environment/Sea-Level-Rise-Maps-2050s-500-year-Floodplain-/qwca-zqw3) | This is the 500-Year Floodplain for the 2050s based on FEMA's Preliminary Work Map data and the New York Panel on Climate Change's 90th Percentile Projects for Sea-Level Rise (31 inches). Please see the Disclaimer PDF for more information. Data Provided by the Mayor's Office of Long-Term Planning and Sustainability (OLTPS) on behalf of CUNY Institute for Sustainable Cities (CISC) and the New York Panel on Climate Change (NPCC). |
| [2050s Mean Sea Level](https://data.cityofnewyork.us/Environment/2050s-Mean-Sea-Level/3vjp-ybhy) | 2050s Future Mean Sea Level projections released by the NPCC March 2019. |
| [2080s Mean Sea Level](https://data.cityofnewyork.us/Environment/2080s-Mean-Sea-Level/cyvg-fsk8) | 2080s Future Mean Sea Level projections released by the NPCC March 2019. |
| [2100s Mean Sea Level](https://data.cityofnewyork.us/Environment/2100s-Mean-Sea-Level/q7rf-ks4h) | 2100s Future Mean Sea Level projections released by the NPCC March 2019. |
| [2020s Mean Monthly High Water](https://data.cityofnewyork.us/Environment/2020s-Mean-Monthly-High-Water/ebsy-4b6x) | 2020s Future Mean Monthly High Water (MMHW) projections released by the NPCC March 2019. |
| [2050s Mean Monthly High Water](https://data.cityofnewyork.us/Environment/2050s-Mean-Monthly-High-Water/p8e8-yh4m) | 2050s Future Mean Monthly High Water (MMHW) projections released by the NPCC March 2019. |
| [2080s Mean Monthly High Water](https://data.cityofnewyork.us/Environment/2080s-Mean-Monthly-High-Water/amfa-s2y8) | 2080s Future Mean Monthly High Water (MMHW) projections released by the NPCC March 2019. |
| [2100s Mean Monthly High Water](https://data.cityofnewyork.us/Environment/2100s-Mean-Monthly-High-Water/mzds-2cdc) | 2100s Future Mean Monthly High Water (MMHW) projections released by the NPCC March 2019. |

## Additional Data Related to Flooding
| Dataset | Description |
| :-------- | :---------- |
| [Hurricane Evacuation Zones](https://data.cityofnewyork.us/Public-Safety/Hurricane-Evacuation-Zones/uihr-hn7s) | Hurricane Evacuation Zones are determined by New York City Emergency Management and represent varying threat levels of coastal flooding resulting from storm surge. Hurricane evacuation zones should not be confused with flood insurance risk zones, which are designated by FEMA and available in the form of Flood Insurance Rate Maps (FIRMs). |
| [Hurricane Evacuation Centers](https://data.cityofnewyork.us/Public-Safety/Hurricane-Evacuation-Centers/p5md-weyf/about_data) | This dataset shows hurricane evacuation centers. Persons requiring shelter during a hurricane are processed at a hurricane evacuation center and then transported to a hurricane shelter. In the event of a hurricane, the status of these hurricane evacuation centers should be confirmed at www.nyc.gov or by calling 311. |
| [Hurricane Evacuation Centers (Map)](https://data.cityofnewyork.us/Public-Safety/Hurricane-Evacuation-Centers-Map-/ayer-cga7) | Hurricane Evacuation Centers Map. See above. |
| [New York City's Flood Vulnerability Index](https://data.cityofnewyork.us/Environment/New-York-City-s-Flood-Vulnerability-Index/mrjc-v9pm) | The Flood Vulnerability Index (FVI) assesses the distribution of vulnerability to flooding across NYC in order to guide flood resilience policies and programs. Vulnerability contains three components: exposure to a hazard, susceptibility to harm from the exposure, and capacity to recover (Cutter et al., 2009). There are six hazard-specific FVIs, one for each of the six different flood hazard scenarios, which include current and two future storm surge scenarios and current and two future tidal flooding scenarios. Exposures vary for different types of flooding and different scenarios within each flood type. |
| [New York City's Flood Vulnerability Index Map](https://data.cityofnewyork.us/Environment/New-York-City-s-Flood-Vulnerability-Index-Map/4vym-qrg3) | The Flood Vulnerability Index (FVI) Map. See above. |
| [DEP Green Infrastructure](https://data.cityofnewyork.us/Environment/DEP-Green-Infrastructure/spjh-pz7h) | NYC Green Infrastructure Program initiatives. Green infrastructure (GI) collects stormwater from streets, sidewalks, and other hard surfaces before it can enter the sewer system or cause local flooding. The GI practice data contained in this dataset includes the location, program area, status, and type of GI. |
| [Building Elevation and Subgrade (BES)](https://data.cityofnewyork.us/City-Government/Building-Elevation-and-Subgrade-BES-/bsin-59hv) | The Building Elevation and Subgrade data contains New York City building centroids derived from the Department of Building's (DOB) February 26th, 2022 building footprint dataset. Each record contains a grade and first floor measurement for each building (recorded as feet above sea-level in the NADV88 vertical datum) and indicates if subgrade space exists. DCP contracted with an external data vendor to generate a single point, or centroid, that represented the location of the center of every building recorded in the DOB dataset. The dataset excluded the footprints of small accessory buildings such as sheds. Each row within the dataset represents one building centroid, and records the X and Y coordinates of that centroid in the NAD 1983 coordinate system. |
| [Building Elevation and Subgrade (BES) - Map](https://data.cityofnewyork.us/City-Government/Building-Elevation-and-Subgrade-BES-Map/nmzg-6q5g) | The Building Elevation and Subgrade Map. See above. |
| [Hazard Mitigation Plan - Mitigation Actions Database](https://data.cityofnewyork.us/City-Government/Hazard-Mitigation-Plan-Mitigation-Actions-Database/veqt-eu3t) | New York City’s comprehensive effort to reduce or eliminate potential losses from the hazards described in the Hazard Specific section of the website. The map includes existing and completed mitigation actions that will minimize the effects of a hazard event on New York City’s population, economy, property, building stock, and infrastructure. It is the result of a coordinated effort by 46 New York City agencies and partners to develop and implement a broad range of inventive and effective ways to mitigate hazards. |
| [Hazard Mitigation Plan – Mitigation Actions Database (points)](https://data.cityofnewyork.us/City-Government/Hazard-Mitigation-Plan-Mitigation-Actions-Database/t7k8-wj6b) | New York City’s comprehensive effort to reduce or eliminate potential losses from the hazards described in the Hazard Specific section of the website. The map includes existing and completed mitigation actions that will minimize the effects of a hazard event on New York City’s population, economy, property, building stock, and infrastructure. It is the result of a coordinated effort by 46 New York City agencies and partners to develop and implement a broad range of inventive and effective ways to mitigate hazards. |
| [Hazard Mitigation Plan - Mitigation Actions Database (Lines)](https://data.cityofnewyork.us/City-Government/Hazard-Mitigation-Plan-Mitigation-Actions-Database/hqhh-iv7p) | New York City’s comprehensive effort to reduce or eliminate potential losses from the hazards described in the Hazard Specific section of the website. The map includes existing and completed mitigation actions that will minimize the effects of a hazard event on New York City’s population, economy, property, building stock, and infrastructure. It is the result of a coordinated effort by 46 New York City agencies and partners to develop and implement a broad range of inventive and effective ways to mitigate hazards. |
| [Hazard Mitigation Plan - Mitigation Actions Database (Polygons)](https://data.cityofnewyork.us/City-Government/Hazard-Mitigation-Plan-Mitigation-Actions-Database/cj2p-e3ej) | New York City’s comprehensive effort to reduce or eliminate potential losses from the hazards described in the Hazard Specific section of the website. The map includes existing and completed mitigation actions that will minimize the effects of a hazard event on New York City’s population, economy, property, building stock, and infrastructure. It is the result of a coordinated effort by 46 New York City agencies and partners to develop and implement a broad range of inventive and effective ways to mitigate hazards. |
| [1 foot Digital Elevation Model (DEM)](https://data.cityofnewyork.us/City-Government/1-foot-Digital-Elevation-Model-DEM-/dpc8-z3jc) | NYC 1foot Digital Elevation Model: A bare-earth, hydro-flattened, digital-elevation surface model derived from 2010 Light Detection and Ranging (LiDAR) data. Surface models are raster representations derived by interpolating the LiDAR point data to produce a seamless gridded elevation data set. A Digital Elevation Model (DEM) is a surface model generated from the LiDAR returns that correspond to the ground with all buildings, trees and other above ground features removed. The cell values represent the elevation of the ground relative to sea level. The DEM was generated by interpolating the LiDAR ground points to create a 1 foot resolution seamless surface. Cell values correspond to the ground elevation value (feet) above sea level. A proprietary approach to surface model generation was developed that reduced spurious elevation values in areas where there were no LiDAR returns, primarily beneath buildings and over water. This was combined with a detailed manual QA/QC process, with emphasis on accurate representation of docks and bare-earth within 2000ft of the water bodies surrounding each of the five boroughs. |
| [Land Cover Raster Data (2017) – 6in Resolution](https://data.cityofnewyork.us/Environment/Land-Cover-Raster-Data-2017-6in-Resolution/he6d-2qns) | A 6-in resolution 8-class land cover dataset derived from the 2017 Light Detection and Ranging (LiDAR) data capture. This dataset was developed as part of an updated urban tree canopy assessment and therefore represents a ''top-down" mapping perspective in which tree canopy overhanging features is assigned to the tree canopy class. The eight land cover classes mapped were: (1) Tree Canopy, (2) Grass\Shrubs, (3) Bare Soil, (4) Water, (5) Buildings, (6) Roads, (7) Other Impervious, and (8) Railroads. The primary sources used to derive this land cover layer were 2017 LiDAR (1-ft post spacing) and 2016 4-band orthoimagery (0.5-ft resolution). |
| [DEP's Citywide Parcel-Based Impervious Area GIS Study](https://data.cityofnewyork.us/City-Government/DEP-s-Citywide-Parcel-Based-Impervious-Area-GIS-St/uex9-rfq8) | NOTE: This file includes data for all 5 boroughs and has a size of 4.60 GB. Individual borough files are available for download from the metadata attachments section. Citywide Geographic Information System (GIS) land cover layer that displays land cover classification, plus pervious and impervious area and percentage at the parcel level, separated into 5 geodatabases, one per borough. DEP hosted a webinar on this study on June 23, 2020. A recording of the webinar, plus a PDF of the webinar presentation, accompany this dataset and are available for download. This citywide parcel-level impervious area GIS layer was developed by the City of New York to support stormwater-related planning, and is provided solely for informational purposes. The accuracy of the data should be independently verified for any other purpose. |

# Resources
I also created a [repository](https://github.com/mebauer/nyc-flood-layers) that demonstrates how to use flood hazard layers for New York City using the Python programming language.  

# Say Hello!
Contact information:  
Twitter: [markbauerwater](https://twitter.com/markbauerwater)   
LinkedIn: [markebauer](https://www.linkedin.com/in/markebauer/)  
GitHub: [mebauer](https://github.com/mebauer)

