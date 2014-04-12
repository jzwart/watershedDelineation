## Automated Watershed Delineation
## JAZ & SEJ, 2014-04-11

import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy.gp 


# 1 merge DEM's, or clip DEM if we get CONUS DEM from Jordan 
#  use the mask of the HUC 6 to clip 

# 2 Fill DEM's

# 3 create flow direction

# loop for creating flow direction for each HUC 6 region

## grab all NHD HUC6 shapefiles and use the append tool to append all
##  files to one of the HUC6 shapefiles. This will include overlapping shapefiles
##  so you have to delete the identical polygons with the tool
##    arcpy.DeleteIdentical_management()
##  Use this to mask the DEM 


HUC6_ID = get unique row names from HUC6 master shapefile ## maybe use arcpy.GetParameterAsText()

for i in length(HUC6_ID):
    mask = arcpy.SelectLayerByAttribute_management()
    curDEM = arcpy.Clip_analysis(in_features=DEM,clip_features=mask)
    curFilled = arcpy.gp.Fill(curDEM)
    curFlowDir = arcpy.
    write flow direction give it HUC6 ID + flow Dir 
    # 





##**** iteration ******##
# for each NHD lake in huc region do the following: 
# 4 Flow accumulation
    # a) clip flow direction raster to extent of lake polygon+100m buffer
    # b) run flow accumulation on clipped flow direction
    # c) find highest flow accumlation cell and assign as pour point
    
# 5 Run watershed tool
    # inputs = pour point, flow direction raster
# 6 edit attribute table of output polygon to include a watershed column and
#     a permanent_ column for matching with lake permanent_

# 7 add polygon to watershed layer

