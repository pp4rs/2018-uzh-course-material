####################################################
# this file performs the main analysis
####################################################


#-- tabula rasa --- #
rm(list = ls())

#-- load packages --- #
library(readr) # reading csv's
library(lfe) # for regressions
library(purrr) # for the export magic
library(dplyr) # for better df's
library(stargazer) # to make fancy tales

#-- parse CLI --- #
args <- commandArgs(trailingOnly = TRUE)
in_csv = args[1]
# in_data = "output/data/bundled.csv"
out_results = args[2]
# out_file = "output/results/results.rda"
out_table = args[3]
# out_tex = "output/tables/ols-regression.tex"


# -- check files meet requirements -- #
 checkCLI = function(in_cli, file_ending) {

   print(paste("Checking argument:", in_cli))
   
   if ( !endsWith(in_cli, file_ending)  && !dir.exists(in_cli) ){
     stop("Command Line Input fails type check.")
   }
 }

checkCLI(in_csv, ".csv")
checkCLI(out_results, ".rda")
checkCLI(out_table, ".tex")

print("All Command Line Inputs passed file ending check.")


# -- load bundled data -- #
df = as_data_frame(read_csv(in_csv))

# -- create exogeneous treatment variables -- #

# x: group with above average group contribution
x = filter(df, Above_Average_Contribution == TRUE)[["Dice"]]

# x_dropped: additionally drops the outlier
x_dropped = filter(df, Above_Average_Contribution == TRUE, Dice >1 )[["Dice"]]

# y: group with below average group contribution
y = filter(df, Above_Average_Contribution == FALSE)[["Dice"]]

# -- main analysis -- #

# rank-sum test to see if treated lie more in the dice task
wilcox_full = wilcox.test(x,y, alternative = 'greater')
wilcox_dropped = wilcox.test(x_dropped,y, alternative = 'greater')

# difference in mean test to see if treated lie more in dice task
kruskal.test(list(x,y))
kruskal.test(list(x_dropped,y))

# regressions to see if endogeneous treatment variable has significant influence
# note:
# 1. dependend variable 'Dice' \in {1,2,3,4,5,6} and hence ordered and discrete
# 2. differences in 'Dice' are cardinal and hence a OLS is more appropriate than an ordered probit model

filtered_df = filter(df, Dice > 1)
ols_1 = felm(Dice ~ Contribution | 0 | 0 |0, data = df)

ols_2 = felm(Dice ~ Above_Average_Contribution | 0 | 0 |0, data = df)

ols_3 = felm(Dice ~ Contribution | 0 | 0 |0, data = filtered_df)

ols_4 = felm(Dice ~ Above_Average_Contribution | 0 | 0 |0, data = filtered_df)

ols_5 = felm(Dice ~ Above_Average_Contribution + 
                    Contribution + 
                    Above_Average_Contribution * Contribution | 0 | 0 |0, data = filtered_df)

ols_6 = felm(Dice ~ Above_Average_Contribution + 
                    Profit1 | 0 | 0 |0, data = filtered_df)

ols_7 = felm(Dice ~ Above_Average_Contribution + 
                    Feedback_Time | 0 | 0 | 0, data = filtered_df)

ols_8 = felm(Dice ~ Above_Average_Contribution + 
                    Feedback_Time + 
                    Above_Feedback | 0 | 0 | 0, data = filtered_df)

# -- save results -- #

# statistical tests
save(list = ls(pattern = "ols*|wilcox*"), file = out_results)

# table
stargazer(ols_1, ols_2, ols_3, ols_4, ols_5, ols_6, ols_7, ols_8,
      out = out_table,
      covariate.labels = c("CONTRIBUTION", "CONTRIBUTION $\\times$ ABOVE", "ABOVE AVERAGE", "STAGE 1 PROFIT", "DISPLAY TIME FEEDBACK", "ABOVE AVERAGE $\\times$ FEEDBACK", "CONST"),
      dep.var.labels = c("Dependent Variable: Reported DICE Roll in Second Stage"),
      dep.var.labels.include = FALSE,
      no.space = TRUE,
      float = FALSE,
      omit.stat= c("adj.rsq", "ser"),
      omit.table.layout = "nl"
      )
