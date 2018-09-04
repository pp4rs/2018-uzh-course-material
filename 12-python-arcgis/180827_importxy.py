#"C:/Program Files/ArcGIS/Pro/bin/Python/Scripts/propy.bat" "C:/Users/uschaede/Dropbox/teaching/pp4rs_2018/gis/180827_importxy.py"
# Import two modules we need: one for running arc with python and os.
import arcpy
import os

print("hello hello, python is working")
# Run the file to see if it works.

# Set up shop and define directories

maindir = os.path.normpath('C:/Users/uschaede/Dropbox/teaching/pp4rs_2018/gis')
#os.path.normapath takes care of the backlashes if you are on different machines.

# link to the data folder that contains the raw files
indir = maindir + os.path.normpath('/data_raw')

# Make an output directory
folder_name = maindir + os.path.normpath('/data/180818')
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
#Set the output directory.
outdir = folder_name
print(outdir)
# Test again and run in terminal



# Set arc workspace and check out license
arcpy.env.workspace = outdir
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("spatial")


#Set local input file path from raw data
table = indir + os.path.normpath("/crimes/crimes.csv")
in_x_field = "Longitude"
in_y_field = "Latitude"
out_layer = "crimes_layer"
saved_layer = outdir + os.path.normpath("/crimes.lyrx")
print("i am here", table)
print("i am here", saved_layer)
arcpy.MakeXYEventLayer_management (table, in_x_field, in_y_field, out_layer, "4326", "")
# Save to a layer file
arcpy.SaveToLayerFile_management(out_layer, saved_layer)
# Convert the layer to a shapefile

out_path = outdir
out_name = 'crimes.shp'
arcpy.FeatureClassToFeatureClass_conversion(saved_layer, out_path, out_name)
# need to save this as a new shapefile


# Exercise: do the same with the police file

table = indir + os.path.normpath("/police_stations/stations.csv")
in_x_field = "Longitude"
in_y_field = "Latitude"
out_layer = "station_layer"
saved_layer = outdir + os.path.normpath("/station.lyrx")
arcpy.MakeXYEventLayer_management (table, in_x_field, in_y_field, out_layer, "4326", "")
# Save to a layer file
arcpy.SaveToLayerFile_management(out_layer, saved_layer)
# Convert the layer to a shapefile

out_path = outdir
out_name = 'stations.shp'
arcpy.FeatureClassToFeatureClass_conversion (saved_layer, out_path, out_name)



# Want to select only assault cases
crimes = outdir + os.path.normpath('/crimes.shp')
# Make a layer
arcpy.MakeFeatureLayer_management (crimes, "projlyr")
# Want to select assault cases


sql_clause = "Primary_Ty = 'ASSAULT'"
out_path = outdir
out_name = 's_crimes.shp'
# Select by map features
arcpy.FeatureClassToFeatureClass_conversion ('projlyr', out_path, out_name, sql_clause)
arcpy.Delete_management(crimes)
# We should project this properly. Give them the projected file and the police station file

# Set folder path:
police_stations = outdir + os.path.normpath('/stations.shp')
assaults = outdir + os.path.normpath('/s_crimes.shp')


to_project = [police_stations, assaults]

# open empty list
projected_files = []

# set coordinate system, here we use US ALbers contiguous with ref: 102039
out_coordinate_system = arcpy.SpatialReference(102039)

for file in to_project:
    input_file = file
    proj_file = file.replace('.shp', '_proj' + '.shp')
    arcpy.Project_management(input_file, proj_file, out_coordinate_system)
    # add the file to the list of projected files
    projected_files.append(proj_file)
    # Clean up and delete the copied file since we ll be working with the projection
    arcpy.Delete_management(file)

print("projected successfully")



# Then do a near analysis.

in_features = outdir + os.path.normpath('/s_crimes_proj.shp')
near_features = outdir + os.path.normpath('/stations_proj.shp')
out_table = 'n' +  near_features.rsplit('\\',1)[1].replace("_proj.shp", "")
arcpy.GenerateNearTable_analysis(in_features, near_features, out_table, '', '', '', 'CLOSEST', '', 'GEODESIC')

#IN_FID in the output table is for the PLSS identifier
outdir = folder_name
arcpy.TableToTable_conversion (out_table, outdir, out_table + '.dbf')
