from flask import Flask, request, send_from_directory, jsonify
import json


DATA_FILE = 'data.json'

app = Flask(__name__)


@app.route('/')
def index():

    return send_from_directory('.', 'index.html')

@app.route('/markers')
def get_markers():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    
    return jsonify(data)
    
@app.route('/markers/update', methods=['GET','POST'])
def update_markers():
    
    return "Success"    
    marker = request.json
    
    label = marker['label']

    with open(DATA_FILE, 'r+') as f:
        data = json.load(f)
        
        updated = False
        
        for index,marker_db in enumerate(data['markers']):
            if(marker_db['label'] == label):
                data['markers'][index]['position'] = marker['position']
                print("FOUND")
                updated = True
        
        if(not updated):
            data['markers'].append(marker)
            print("NOT FOUND")

        
        f.seek(0)
        
        json.dump(data, f, indent=4)
        
        f.truncate()
        
    return "Success"
	
if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=3454)
