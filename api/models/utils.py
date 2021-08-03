from math import isnan
import json
from numpy import nan


def isNaN(string):
    return string != string

def deleteNone(d):

    #Delete keys with the value ``None`` in a dictionary, recursively.
    
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            deleteNone(value)
    return d 


def traverseLocation(x,loc):
    if(x in loc):
        return(loc[x])
    

def axisDetailedAddress(location,latitude,longitude):
    address={
        
        'area'             : location['display_name'],
        'city'              :   (traverseLocation('city',location['address'])),
        'district'     : (traverseLocation('city_district',location['address'])),
        'flag_pincode'      : False,
        'latitude'          : latitude,
        'longitude'         : longitude,
        'pincode'           : (traverseLocation('postcode',location['address'])),
        #'state_district'    : (traverseLocation('county_name',location['address'])),
        'state'             : (traverseLocation('state',location['address'])),
        'tehsil'            : (traverseLocation('county',location['address'])),
       
    }
    if(address['district']==None):
        address['district']=(traverseLocation('state_district',location['address']))
    if(address['area']==None):
        address['area']=(traverseLocation('place_name',location['address']))
    if(address['pincode']==None):
        address['pincode'] = (traverseLocation('postal_code',location['address']))
    if(address['tehsil']==None):
        address['tehsil']= (traverseLocation('suburb',location['address']))
    
    return (json.loads((json.dumps(address).replace("NaN" ,  "0",))))

def pincodeDetailedAddress(location,pin):
  

    address = {
        
        'area': location['place_name'],
        'district':location['county_name'],
        'flag_pincode':True,
        'latitude':location['latitude'],
        'longitude':location['longitude'],
        'pincode':pin,
        'state':location['state_name'], 
        'tehsil': location['community_name'],


    }
    
    return (json.loads((json.dumps(address).replace("NaN" ,  "0",))))