
from flask import Flask,jsonify,abort,make_response,request

app=Flask(__name__)


weatherList=[
    {'id':1,
    'city':'Bengaluru',
    'temperature':29,
    'description':'Cloudy'},
    {
        'id':2,
        'city':'Mangaluru',
        'temperature':35,
        'description':'Sunny'
    },

        'id':3,
        'city':'Mysore',
        'temperature':28,
        'description':'Thundertorm'
    },
    {
        'id':4,
        'city':'Kerala',
        'temperature':27,
        'description':'Foggy'
        -},
]

@app.route('/WeatherApp/api/v1.0/weatherList',methods=['GET'])
def get_weathers():
    return jsonify({'weather':weatherList})

@app.route('/WeatherApp/api/v1.0/weatherList/<int:weather_id>',methods=['GET'])
def get_weather(weather_id):
    weather=[weather for weather in weatherList if weather['id']==weather_id]
    if len(weather)==0:
        abort(404)
    return jsonify({'weather':weather[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

@app.route('/WeatherApp/api/v1.0/weatherList',methods=['POST'])
def create_weather():
    if not request.json or not 'city' or not 'temperature' or not 'description' in request.json:
        abort(400)
    weather={
        'id':weatherList[-1]['id'] + 1,
        'city':request.json['city'],
        'temperature':request.json['temperature'],
        'description':request.json['description'],    
    }
    weatherList.append(weather)
    return jsonify({'weather': weather}),201

if __name__=='__main__':
    app.run(debug=True)

