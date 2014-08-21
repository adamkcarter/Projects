loadPlayerData <- function(fileName,year){
	filePath <- paste('/Users/AdamCarter/Downloads/',fileName, sep='')

	daten <- read.csv(file = (as.character(filePath)))
	daten <- daten[2:ncol(daten)]
	name <- c('Player','Tm','Age','G','GS','QBrec','Cmp','Att','CmpPer','Yds','TD','TDPer','Int','IntPer','Lng','YA','AYA','YC','YG','Rate','QBR','Sk','Yds','NYA','ANYA','SkPer','4QC','GWD')
	YR <- rep (year,nrow(daten))
	daten<-cbind(daten,YR)

	names(daten)<- name
	outputFileName <- paste('playerOffenseNfl',year, '.csv',sep='')

	write.table(daten, file=outputFileName,sep=',')
	return (daten)


}