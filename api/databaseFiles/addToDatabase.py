import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='oreo0008',
                             db='practice')
cursor=connection.cursor()

def addingToDatabase(address,product):
   
    
    
    #check if pincode exist or not
    row = cursor.execute("SELECT * FROM practice.pincodedata WHERE pincode = (%s) and flag_pincode =(%s) and product=(%s)",(address["pincode"],True,product,))
    col = cursor.execute("SELECT * FROM practice.pincodedata WHERE latitude =(%s) and longitude=(%s) and product=(%s)",(address["latitude"],address["longitude"],product,))
    if(row==0 and col==0) :
        cursor.execute("INSERT INTO practice.pincodedata (pincode,area,tehsil,district,state,flag_pincode,latitude,longitude,product) VALUES (%s ,%s,%s,%s,%s,%s,%s,%s,%s)" ,(address['pincode'],address['area'],address['tehsil'],address['district'],address['state'],address['flag_pincode'],address['latitude'],address['longitude'],product,))
    
    #Saving the Actions performed on the DB
    connection.commit()

    #Closing the cursor
    