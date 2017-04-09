import sys
import mysql.connector as mariadb
import logging

username = "web"
password = "web"
database = "weather"
mariadb_connection = mariadb.connect(user=username, password=password, database=database)

def insertreading(Reading):
    try:
        cursor = mariadb_connection.cursor()
        cursor.execute(
            "INSERT INTO reading (Temp1, Temp2, TempSensorAvg, Humidity, Pressure, SeaLevelPressure, TimeStamp)"
            "VALUES ({0}, {1}, {2}, {3}, {4}, {5}, NOW());".format(Reading.temp1, Reading.temp2, Reading.tempavg, Reading.pressure, Reading.sealevelpressure, Reading.humidity))
            
        mariadb_connection.commit()
    except mariadb.Error as error:
        logging.error("Error: {}".format(error))
        return False
        
    except IOError as e:
        logging.error("I/O error({0}): {1}".format(e.errno, e.strerror))
        return False
    except:
        logging.error("Unexpected error:", sys.exc_info()[0])
        return False
        
    return True
    
def getreadings(amount):
    cursor = mariadb_connection.cursor()
    query = ("SELECT * FROM weather.reading ORDER BY readingID desc LIMIT 0, " + str(amount))
    
    cursor.execute(query)
    
    output = []
    
    for (readingID, Temp1, Temp2, TempSensorAvg, Pressure, SeaLevelPressure, Humidity, TimeStamp) in cursor:
        output.append(str({
            "readingID": readingID,
            "Temp1": str(Temp1),
            "Temp2": str(Temp2),
            "TempSensorAvg": str(TempSensorAvg),
            "Pressure": str(Pressure),
            "SeaLevelPressure": str(SeaLevelPressure),
            "Humidity": str(Humidity),
            "TimeStamp": str(TimeStamp)
        }))
        
    cursor.close()
        
    return output

def getsinglereading(id):
    cursor = mariadb_connection.cursor()
    query = ("SELECT * FROM weather.reading where readingID=" + str(id))
    
    cursor.execute(query)
    
    output = []
    
    for (readingID, Temp1, Temp2, TempSensorAvg, Pressure, SeaLevelPressure, Humidity, TimeStamp) in cursor:
        output.append(str({
            "readingID": readingID,
            "Temp1": str(Temp1),
            "Temp2": str(Temp2),
            "TempSensorAvg": str(TempSensorAvg),
            "Pressure": str(Pressure),
            "SeaLevelPressure": str(SeaLevelPressure),
            "Humidity": str(Humidity),
            "TimeStamp": str(TimeStamp)
        }))
        
    cursor.close()
        
    return output
