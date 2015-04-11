from flask import render_template
from . import hacks
import googlemaps
from googleplaces import GooglePlaces
import collections
@hacks.route('/')
def index():
    data=[]
	#import pdb; pdb.set_trace()
    position="mahipalpur, new delhi"
    gmaps = googlemaps.Client(key='Add your own api key')
    google_places = GooglePlaces('Add your own api key')
    query_result = google_places.nearby_search(location=position, keyword='public toilets',radius=20000)
    for data1 in query_result.places:
            matrix=gmaps.distance_matrix("%s, %s " %(str(data1.geo_location['lat']),str(data1.geo_location['lng'])),position)
            matrix['rows'][0]['elements'][0]['distance']['lat']=data1.geo_location['lat']
            matrix['rows'][0]['elements'][0]['distance']['lng']=data1.geo_location['lng']
            data.append(matrix)
    #import pdb;pdb.set_trace()
    x={}
    x=collections.defaultdict(lambda:5000000, x)

    
    for place in data:
            for rows in place['rows']:
                    for elements in rows['elements']:
                            distance=elements['distance']
                            if int(distance['value'])<int(x['value']):
                                            x=distance
    return render_template('hacks/index.html',data=x, location=position)






