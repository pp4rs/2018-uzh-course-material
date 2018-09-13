####################################################
# this file creates graphs for the latex file from the cleaned data
####################################################

#-- tabula rasa --- #
rm(list = ls())


#-- load packages --- #
library(readr) # to load csv's
library(dplyr) # for better df's
library(ggplot2) # for output plots


#-- parse CLI --- #
args <- commandArgs(trailingOnly = TRUE)
in_csv = args[1]
out_path = args[2]


# -- check files meet requirements -- #
 checkCLI = function(in_cli, file_ending) {

   print(paste("Checking argument:", in_cli))

   if ( !endsWith(in_cli, file_ending)  && !dir.exists(in_cli) ){
     stop("Command Line Input fails type check.")
   }
 }

checkCLI(in_csv, ".csv")

print("All Command Line Inputs passed file ending check.")


# -- load bundled data -- #
df = as_data_frame(read_csv(in_csv))

# plot of first stage contribution frequencies
first_stage = ggplot(data = df) +
  coord_cartesian(xlim = c(0, 20)) +
  geom_bar(mapping = aes(x=Contribution, y = ..prop..)) +
  labs(x = "Contribution in First Stage", y = "Frequency") +
  scale_x_continuous(breaks = seq(0, 20, 1))

# plot of second stage dice throw frequencies
second_stage = ggplot(data = df) +
  geom_bar(mapping = aes(x=Dice, y=..prop..)) +
  labs(x = "Reported Dice Roll in Second Stage", y = "Frequency") +
  scale_x_continuous(breaks = seq(1, 6, 1))

# plot of second stage dice throw frequencies filled by treatment variable
second_stage_grouped = ggplot(data = df) +
  geom_bar(mapping = aes(x=Dice, y=..prop.., fill = Above_Average_Contribution)) +
  labs(x = "Reported Dice Roll in Second Stage", y = "Frequency") +
  scale_x_continuous(breaks = seq(1, 6, 1)) +
 # scale_y_continuous(breaks = seq(0, 1, 0.167)) +
  scale_fill_discrete(name = "First Stage Contribution", labels = c("Below Group Average", "Above Group Average"))

# boxplot of second stage dice thrown by endogeneous treatment group
boxplot = ggplot(data = df, aes(x=Above_Average_Contribution, y=Dice)) +
  geom_boxplot() +
  labs(x="First Stage Contribution", y = "Reported Dice Roll in Second Stage") +
  scale_y_continuous(breaks = seq(1, 6, 1)) +
  scale_x_discrete(labels = c("Below Group Average", "Above Group Average"))



# save the plots
ggsave("output\\graphs\\first-stage.png", first_stage)
ggsave("output\\graphs\\second-stage.png", second_stage)
ggsave("output\\graphs\\second-stage-grouped.png", second_stage_grouped)
ggsave("output\\graphs\\boxplot.png", boxplot)
