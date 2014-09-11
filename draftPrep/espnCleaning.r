ESPN <- read.table('ESPNPlayerRankings',sep=',',strip.white=T)

holder <- NULL

for (i in 1:length(playerRanking[,1])){
	name <- as.character(playerRanking$player[i])
	index <- grep(name,ESPN[,2],T)
	
	if (is.na(index[1])){index<-'not found'}

	if (is.null(holder)){
		holder <- c(ESPN$V1[index], name , ESPN$V2[index])
	} else { 
		holder <- rbind(holder, c(ESPN$V1[index], name, as.character(playerRanking$pos[i])))
	}
}

holder <- holder[order(as.numeric(holder[,1])),]

exportDataFrame(holder,'ESPN.txt')
