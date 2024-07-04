from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_location(ip):
    if ip == '127.0.0.1':
        return 'Localhost'
    
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('city', 'Unknown')
    else:
        return 'Unknown'
    

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', '')
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    location = get_location(client_ip)
    temperature = 11

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()