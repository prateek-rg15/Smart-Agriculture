
#!flask/bin/python
import test2
from  tempsensor import TemperatureSensing 
from flask import Flask, jsonify
import testi2c

app = Flask(__name__)


tasks = [
    {
        'temp': 276,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])

def get_tasks():
    print("start")
    #test2.startProcess('3')
    app=TemperatureSensing()
    app.get_name()
    tempvalue=app.get_temperature()
    filemot = open("/home/pi/Desktop/test2",'r')
    motlines = filemot.readlines()
    print(motlines)
    filemot.close()
    filemoist=open("/home/pi/Desktop/test3",'r')
    moistlines=filemoist.readlines()
    filemoist.close()
    print(moistlines)
    
    return jsonify({'temp': tempvalue,
                    'motion': motlines,
                    'moisture':moistlines
                    })
@app.route('/todo/api/v1.0/test', methods=['GET'])

def get_test():
    print("hello")
    testi2c.startProcess('6')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    get_tasks();
    
