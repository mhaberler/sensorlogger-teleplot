# teleplot relay for sensorlogger

## step 1: run https://teleplot.fr/
this will give you a UDP socket like `teleplot.fr:4711`

## step 2: run the this like so:

````
(penv) BigM1:sensorlogger-teleplot mah$ TELEPLOT=teleplot.fr:11646 flask run --host=0.0.0.0 --port=8000
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.16.0.104:8000
Press CTRL+C to quit
172.16.0.111 - - [22/Apr/2023 01:43:02] "POST /data HTTP/1.1" 200 -
172.16.0.111 - - [22/Apr/2023 01:43:02] "POST /data HTTP/1.1" 200 -
172.16.0.111 - - [22/Apr/2023 01:43:02] "POST /data HTTP/1.1" 200 -
172.16.0.111 - - [22/Apr/2023 01:43:03] "POST /data HTTP/1.1" 200 -
````

## step 3: run sensorlogger with http push

- configure URI as: `http://172.16.0.104:8000/data` 
- hit `Tap to Test Pushing`
- sensorlogger should display `Got status: 200`
- hit `start recording``

https://teleplot.fr should start displaying values:


<img src="doc/teleplot.png"/>

