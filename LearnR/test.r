library(dplyr)

df <- data.frame(x = 1:3, y = c('a', 'b', 'c')) 
csv <- read.csv("ks-projects-201801.csv")



print(mean(select(csv,usd.pledged)))

