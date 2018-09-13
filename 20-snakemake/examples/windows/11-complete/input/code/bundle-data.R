####################################################
# this file does the following:
# 1. it creates a list of all csv files in the input folder (CLI arg #1)
# 2. it appends all the data into a single data frame
# 3. it saves the bundled data into a csv file (CLI arg #2)
####################################################

#-- tabula rasa --- #
rm(list = ls())

#-- loading packages --- #
library(readr)    # read-in csv
library(tibble)   # nicer dataframes
library(dplyr)    # data transformations
library(purrr)    # to use map_df()

#-- parse CLI --- #
args = commandArgs(trailingOnly = TRUE)
in_folder = args[1]
out_csv = args[2]

# -- Check Files meet requirements -- #
 checkCLI = function(in_cli, file_ending) {

   print(paste("Checking argument:", in_cli))
   
   if ( !endsWith(in_cli, file_ending)  && !dir.exists(in_cli) ){
     stop("Command Line Input fails type check.")
   }
 }

checkCLI(out_csv, ".csv")
checkCLI(in_folder, ".csv")

print("All Command Line Inputs passed file ending check.")


#-- reading in csv's --- #
data_format = "*.csv"

data_file_list = list.files(path=in_folder,pattern=data_format, full.names=TRUE)

df = map_df(data_file_list, 
                read_csv)

                
#-- save output --- #
write_csv(df, out_csv)