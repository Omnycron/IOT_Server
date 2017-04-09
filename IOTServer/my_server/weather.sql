CREATE TABLE `weather`.`reading` (
	`readingID` INT NOT NULL AUTO_INCREMENT,
	`Temp1` DECIMAL(20,10) NULL,
	`Temp2` DECIMAL(20,10) NULL,
	`TempSensorAvg` DECIMAL(20,10),
	`Humidity` DECIMAL(20,10) NULL,
	`Pressure` DECIMAL(20,10) NULL,
	`SeaLevelPressure` DECIMAL(20,10) NULL,
	`TimeStamp` VARCHAR(45) NULL,
	PRIMARY KEY (`readingId`));