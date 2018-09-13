####################################################
# this file does the following:
# 1. it converts a zTree file into a csv
# 2. it creates date and session_ids from the file name
####################################################

# tabula rasa
rm(list = ls())
# loading packages
library(zTree) # to read in those ugly zTree tables
library(dplyr) # to mutate data frames
library(readr) # to write csvs

#-- parse CLI --- #
args <- commandArgs(trailingOnly = TRUE)
in_zTree <- args[1]
out_csv <- args[2]

# in_zTree = "input/raw-data/170531_01.xls"
# out_csv = "output/data/experiment.csv"

# -- Check Files meet requirements -- #
 checkCLI = function(in_cli, file_ending, type) {

   print(paste("Checking argument:", in_cli))
   
   if ( (endsWith(in_cli, file_ending) == FALSE) ){
     stop("Command Line Input fails type check.")
   }
 }

checkCLI(in_zTree, "xls", input)
checkCLI(out_csv, "csv", output)

print("All Command Line Inputs passed file ending check.")

# -- Read in data -- #

session_df = zTreeTables(in_zTree)

# structure into session and subjects tibbles
session_session = as_data_frame(session_df[[1]])
session_subjects = as_data_frame(session_df[[2]])

# create session_ID and date_ID from filename
split_1 = unlist(strsplit(in_zTree, split = "[/_.]"))
date_ID = split_1[[length(split_1)-2]] %>% as.Date(format="%y%m%d") # take date part of file name and make it a date object
session_ID = split_1[[length(split_1)-1]] %>% as.integer # take session part of file name and make it an integer

# extract relevant data & generate variables for analysis
cleaned_df = select(session_subjects, Date, Subject, Group, Contribution, Profit1, Dice, Profit, SumC, TimeOK23ProfitDisplay2OK) %>%
  mutate(Date = date_ID,
         Session = session_ID,
         Above_Average_Contribution = if_else(Contribution > SumC/4, TRUE, FALSE)) %>%
  dplyr::rename(Feedback_Time = TimeOK23ProfitDisplay2OK) %>%
  mutate(Above_Feedback = Above_Average_Contribution * Feedback_Time,
         ontribution_Above = Contribution*Above_Average_Contribution)

# re-order columns to have Date, Session, Subject, rest
cleaned_df = select(cleaned_df, Date, Session, Subject, everything())

# save outputs
write_csv(cleaned_df, out_csv)
