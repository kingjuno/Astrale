from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

API_KEY = "HKX3fDXTgAIIQQz03Gi9YWIQe2Y3HN4j55tvnWA5"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mars')
def mars():
    sol_data=[]
    sol_final=[]
    mars_weather=requests.get(f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0").json()
    # with open("api_2.json", "w") as outfile: 
    #     json.dump(mars_weather, outfile)
    # f=open('api_2.json')
    # mars_weather=json.load(f) 
    
    for i in mars_weather['sol_keys']:
        sol_data.append(mars_weather[str(i)]['First_UTC'][5:10])
    month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in sol_data:
        sol_final.append(str(month[int(i[:2])-1])+'. '+i[3:])

    return render_template('mars.html',content=mars_weather,dates=sol_final)

@app.route('/neows')
def neows():
    neows_data=requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={API_KEY}").json()
    # with open("api.json", "w") as outfile: 
    #     json.dump(neows_data, outfile)
    # f=open('api.json')
    # neows_data=json.load(f)    
    return render_template('neows.html',content=neows_data)

@app.route('/test')
def test():
    f=open('api_2.json')
    neows_data=json.load(f)    
    return render_template('test.html',content=neows_data)

if __name__ == '__main__':
    app.run(debug=True)