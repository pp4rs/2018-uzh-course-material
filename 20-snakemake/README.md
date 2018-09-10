# Overview and Purpose

The following repo contains an example project which illustrates how to use `Snakemake` to execute a full research project.

We will reproduce a term-paper, which I and a colleague handed in for Ernst Fehr's Experimental Economics course in the Spring term 2017.

The project features data from a single experimental session with 24 subjects. For illustrative purposes the dataset has been copied several times to show how `Snakemake` can be helpful when a single task has to be repeated many times without specifying all the input files through hardcoding.

## Usage
The workflow can be activated via two commands:

To start the workflow use the shell command `snakemake makePDF` in the project main directory.

To clean the directory use the shell command `snakemake clean` in the project main directory.

The `snakemake makePDF` workflow is illustrated in the following flow chart:

![The snakemake all workflow](./documentation/flowchart.png)

## Dependencies

* **Snakemake:** The current version of this project has been created using `Snakemake 5.2.2`.
* **R:** All data-analysis is performed using `R 3.5.1` and requires the following packages
    * readr
    * purrr
    * dplyr
    * stargazer
    * tibble
    * zTree
    * ggplot2
* **pandoc:** The final PDF is built using `pandoc 2.2.1`

## PS: The paper is shit :D
