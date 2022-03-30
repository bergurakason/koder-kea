import tempsensor
import ultrasonisksensor
import buzzer
import time
import sqlite3
temp = tempsensor
ultra = ultrasonisksensor
class data:
    temp = 0
    afstand = 0
    afstandmin = 5
    
def insert_data():
    try:
        sqliteConnection = sqlite3.connect('database/Sensor.db')
        cursor = sqliteConnection.cursor()


        sqlite_insert_query = """INSERT INTO sensordata
                            (Temperature, Afstand) 
                            VALUES 
                            (?,?)"""
        tuple1 = (int(data.temp),int(data.afstand))
        print("row værdi: ", tuple1)
        cursor.execute(sqlite_insert_query, tuple1)
        sqliteConnection.commit()
        print("Record inserted successfully into Batch, Productbatch table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into productbatch table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
while True:
    data.temp = temp.tempsensor()
    data.afstand = ultra.ultramåling()
    print("temp: ", data.temp, "afstand: ", data.afstand)
    print(data.afstand)
    if(data.afstand <= data.afstandmin):
        buzzer.buzzer()
    time.sleep(5)
    insert_data()