loadData <- function(fileName,year){
	filePath <- paste('/Users/AdamCarter/Downloads/',fileName, sep='')
	

	daten <- read.csv(file=(as.character(filePath)))
	daten <- daten[2:26]
	name <- c('Team','G','TotPts','TotYds','TotPly','TotYP','TO','FL','X1stPy','X1stD','PCmp','PAtt','PYds','PTD','PInt','PNYA','P1stD','RAtt','RYds','RTD','RYA','R1stD','ScPer','TOPer','EXP','YR')
	YR <- rep (year,32)
	daten<-cbind(daten,YR)

	names(daten)<- name
	outputFileName <- paste('teamOffenseNfl',year, '.csv',sep='')

	write.table(daten, file=outputFileName,sep=',')
	return (daten)

}