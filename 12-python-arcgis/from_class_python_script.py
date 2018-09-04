

print("Hello World")
# Set up
import arcpy
import os

# Set up folder paths
maindir = os.path.normpath("C:/Users/econspare/Dropbox/teaching/pp4rs_2018/2018-uzh-course-material/12-python-arcgis")

print(maindir)


# Path to raw data
indir = maindir + os.path.normpath("/data_raw")

# Create an ouptput folder
output_folder = maindir + os.path.normpath("/output_data")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Path to output directory
outdir = output_folder
print(outdir)


# Set up arcpy work environment:
arcpy.env.workspace = outdir
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("spatial")

# Set up path to input files
communities = indir + os.path.normpath("/communities/comm.shp")
police_districts = indir + os.path.normpath("/police_districts/distr.shp")

# List of files:
file_list = [communities, police_districts]
print("This is my file list", file_list)


# Copy my input files:
copied_files = []

for file in file_list:
    # Define output folder:
    output_name = file.rsplit("\\",1)[1].replace(".shp", "")
    print(output_name)

    # Create output folder for copied files
    folder_name = outdir + os.path.normpath("/" + output_name)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Give the copied file a name
    copied_file = folder_name + os.path.normpath("/" + output_name + "_c.shp")
    print(copied_file)

    arcpy.Copy_management(file, copied_file)

    copied_files.append(copied_file)

    print("Successfully copied", copied_file)


proj_files = []

for file in copied_files:
    input_file = file
    proj_file = file.replace("_c.shp", "_proj.shp")

    out_coord_system = "102039"
    arcpy.Project_management(input_file, proj_file, out_coord_system)
    # Delete the copied file:
    arcpy.Delete_management(file)
    proj_files.append(proj_file)

    print("Projected successfully", proj_file)

print("This is my list of projected files", proj_files)

# Define the variables for SJ
#police districts:
target_features = proj_files[1]
# communities:
join_features = proj_files[0]
# Give a name to the output file:
out_feature_class = outdir + os.path.normpath("/sj.shp")

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class, "JOIN_ONE_TO_MANY", "KEEP_ALL", "INTERSECT")

print("Spatial join worked", out_feature_class)

# create folder to store output tables
folder_name = outdir + os.path.normpath("/dbf_output")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define list of files i want to export as a table:
to_export = [proj_files, out_feature_class]
# Proj_files contains the projected communities and police police_districts
# Out feature class is the spatial join output file.

for file in to_export:
    arcpy.TableToDBASE_conversion(file, folder_name)



"C:/Program Files/ArcGIS/Pro/bin/Python/Scripts/propy.bat"
"C:/Users/econspare/Dropbox/teaching/pp4rs_2018/2018-uzh-course-material/12-python-arcgis/
python_script.py"

"C:/Program Files/ArcGIS/Pro/bin/Python/Scripts/propy.bat" "C:/Users/econspare/Dropbox/teaching/pp4rs_2018/2018-uzh-course-material/12-python-arcgis/python_script.py"














#"C:/Program Files/ArcGIS/Pro/bin/Python/Scripts/propy.bat" "C:/Users/econspare/Dropbox/teaching/pp4rs_2018/2018-uzh-course-material/12-python-arcgis/python_script.py"
