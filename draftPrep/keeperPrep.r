comb <- function(vector){
	#make round vector

	round <- NULL
	offset <- 0
	for (i in 1:15){
		round <- c(round, rep(i,10))
	}

	#FIND DRAFT RESULTS
	drafted <- NULL
	team <- NULL
	position <- NULL
	fanTeam <- NULL


	for (i in 1:length(vector[,])){
		#Grab our target
		target <- as.character(vector[i,])
		#Check to see if this is a round marker
		if (nchar(target) <= 8){
		} else {
			if (i%%11 == 0){
				offset <- 1
			}
			minusIndex <- regexpr('-',target)[1]
			drafted <- c(drafted,(substr(target,(3 + offset),minusIndex - 6)))
			team <- c(team,(substr(target,minusIndex-5,minusIndex-1)))
			position <- c(position,(substr(target,minusIndex+1,minusIndex+5)))
			fanTeam <- c(fanTeam,(substr(target,minusIndex+6,100)))
			offset <- 0
		}
	}

	'print (length(round))
	print (length(drafted))
	print (length(team))
	print (length(position))
	print (length(fanTeam))'
	return(data.frame(round,drafted,team, position,fanTeam))
}

first100 <- function(dataframe){
	return(dataframe[dataframe$round<=4,])
}


myPlot <- function(){
	plot(years,complete[,1],type='l',col=pal(6)[1], xaxt='n',ylim=c(0,50))
	axis(1, at=2011:2013,labels=c('2011','2012','2013'))
	lines(years, y=complete[,2],col=pal(6)[2])
	lines(years, y=complete[,3],col=pal(6)[3])
	lines(years, y=complete[,4],col=pal(6)[4])
	lines(years, y=complete[,5],col=pal(6)[5])
	lines(years, y=complete[,6],col=pal(6)[6])
	legend('topright',pch=1,col=pal(6),legend=positons)
}

## Import our files  ### NOW WE HAVE THREE YEARS OF DATA, EACH DRAFT YEAR IS CAPTURES IN A FILE NAMED FOR THAT YEAR
results2011 <- read.table('2011',sep='\n')
results2012 <- read.table('2012',sep='\n')
results2013 <- read.table('2013',sep='\n')

# apply our comb function to said files, this will create three data frames with the draft results for each respective year.
results2011 <- comb(results2011)
results2012 <- comb(results2012)
results2013 <- comb(results2013)

# Gather the first 100 players selected 

best2011 <- first100(results2011)
best2012 <- first100(results2012)
best2013 <- first100(results2013)

# get breakdown by year

breakdown2011 <- table(best2011$position)
breakdown2012 <- table(best2012$position)
breakdown2013 <- table(best2013$position)

# Combine breakdowns

complete <- rbind(breakdown2011, breakdown2012, breakdown2013)

# Find mean of all three years
name <- names(complete[1,])
means <- NULL
for (i in 1:length(complete[1,])){
	means <- c(means, round(mean(complete[,i]),0))
}
names(means)<- name

############          MEAN OUTPUT           ###############
###												   		###
###	  1. DEF  2. K  3. QB   4. RB   5. TE    6. WR   	###
###    	  0     0     11       16      2       11 		###	
###														###
########################################################### 

# import player stats data from 2013 **REFER TO yahooScrape.py FOR NEW SEASON DATA (WAS A BITCH LAST YEAR)

data <- read.table('data',sep=',')

# split by position

############ SPLIT DATA INDEX CHART ###############
###												###
###					1 --- QB 					###
### 				2 --- RB 					###
### 				3 --- TE 					###
### 				4 --- WR					###	
###												###
################################################### 
splitData <- split(data,data$V3)

splitNames <- c ('player','team','pos','points')

qbData <- data.frame(splitData[1])
colnames(qbData) <- splitNames

rbData <- data.frame(splitData[2])
colnames(rbData) <- splitNames

teData <- data.frame(splitData[3])
colnames(teData) <- splitNames

wrData <- data.frame(splitData[4])
colnames(wrData) <- splitNames

prototypeQB <- qbData[11,]
prototypeRB <- rbData[16,]
prototypeTE <- teData[2,]
prototypeWR <- wrData[11,]

prototypeQBPoints <- prototypeQB$points
prototypeRBPoints <- prototypeRB$points
prototypeTEPoints <- prototypeTE$points
prototypeWRPoints <- prototypeWR$points

qbData$points <- qbData$points - prototypeQBPoints
rbData$points <- rbData$points - prototypeRBPoints
teData$points <- teData$points - prototypeTEPoints
wrData$points <- wrData$points - prototypeWRPoints

prototypedData <- rbind(qbData,rbData,teData,wrData)

playerRanking <- prototypedData[order(-prototypedData$points),]

top48Players <- playerRanking[1:48,]
