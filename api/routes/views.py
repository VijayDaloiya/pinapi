from flask import Flask , redirect , url_for ,render_template , request, jsonify
import pgeocode
import json as simplejson
from models.utils import *
from mapping.mapping import *
from databaseFiles.addToDatabase import *
from geopy.geocoders import Nominatim
import math
from __main__ import app
# free api key for geocoder
geocoder = Nominatim(user_agent = 'geoapiExercise')
data = pgeocode.Nominatim('In')



@app.route("/map")
def map():
    mappingdata()
    return render_template('mapped.html')


@app.route("/")
def home():
    return render_template('datainput.html')


@app.route("/axis/<latitude>-<longitude>")
def getAddressByAxis(latitude,longitude):
    productId=request.args.get('product')
    location = geocoder.reverse((latitude, longitude))
    addingToDatabase(axisDetailedAddress(location.raw,latitude,longitude),product)
    return jsonify((axisDetailedAddress(location.raw,latitude,longitude)))

@app.route("/pincode/<pin>")
def getAddressByPinCode(pin):
    product=(request.args.get('product'))
    location=(data.query_postal_code(str(pin)))
    if(isNaN(location['place_name'])):
        return jsonify("Invalid Pincode")
    elif(request.args.get('map',type=bool)==True):
        addingToDatabase(pincodeDetailedAddress(location,pin),product)
    return jsonify(deleteNone(pincodeDetailedAddress(location,pin)))
  


