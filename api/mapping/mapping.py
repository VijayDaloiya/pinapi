import folium
import pandas as pd
from databaseFiles.connectDatabase import *

#connecting database
cursor,dbConnection = DatabaseConnection()
#cursor=dbConnection.cursor(buffered=True)

#setting up layers name


def mappingdata():
    map = folium.Map(location=[23.2599,77.4126], tiles="OpenStreetMap", zoom_start=5)
    layers=pd.read_sql("select * from projects",dbConnection)
    data = pd.read_sql("select * from pincodedata", dbConnection)
    
    for i in layers.index:
       print(i)
       code=layers['code'][i]
       code= folium.FeatureGroup(layers['name'][i])
       for i in range(0,len(data)):
         print("u r here")
         if(data['product'][i]==code):
            code.add_child(folium.Marker(
          location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']],
          popup=data.iloc[i]['area'],icon=folium.Icon(color='green'),
         )).add_to(map)
       
   
    
    #initializing the map (opening points)
    
    


    #locating longitude n latitudes
    #for i in range(0,len(data)):
       #if(data['product'][i]=='goapptiv'):
       #   goapptiv.add_child(folium.Marker(
       #   location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']],
       #   popup=data.iloc[i]['area'],icon=folium.Icon(color='green'),
       #)).add_to(map)

       #if(data['product'][i]=='channelpay'):
       #   icon=folium.features.CustomIcon('http://goapptiv.com/images/goapptiv_data_new.png', icon_size=(50,50))
       #   channelpay.add_child(folium.Marker(
       #   location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']],
       #   popup=data.iloc[i]['area'],icon=icon),
       #  ).add_to(map)

    # adding layers
    #map.add_child(goapptiv)
    #map.add_child(channelpay)
    map.add_child(folium.LayerControl())   
    map.save('templates/mapped.html')