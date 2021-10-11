# MLB jet lag analysis

## PowerPoint Presentation
To view the presentation where I present my full methodolgy and results/analysis, please view MLB_jet_lag.pdf.

## Overview
The purpose of this project was to analyze a large data set of Major League Baseball game, seeking to find (if any) a relationship between jet lag due to teams' travel schedules and their performances in games.

## Methodology and Design
Using the MySportsFeeds API, I gathered data from ~19,000 games between the 2016-2019 regular seasons. I created an (from scratch) equation to numerically represent jet lag, and jet lag's extent, and ran Python scripts to apply this equation to these games and associated travel schedules. Using statistics, I then determined, when applicable, statstically significant differences in data points. 

## Results
I discovered a statistically significant decrease in a team's winning percentage when experiencing jet lag, with a p-value of 0.018.

I discovered a statistically significant increase in runs allowed per game when a team experienced jet lag, with a p-value of 0.0025.

I discovered a statistically significant decrease in runs scored per game when a team experienced WESTWARD jet lag as opposed to EASTWARD jet lag, with a p value of 0.0006.

