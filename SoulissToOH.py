 # This Python file uses the following encoding: utf-8
import os, sys, requests

ipaddress = '192.168.1.17'  # IP ADDRESS OF ZOZZARIELLO SERVER

url = 'http://' + ipaddress + ':8080/structure?all'
print (url)
r = requests.get(url)
r.encoding = "utf-8-sig"

tfs = 'souliss.sitemap'
f1 = open(tfs, 'w+')

tf = 'souliss.items'
f2 = open(tf, 'w+') #f2 = open(tf, 'a+')

import json
#data = {"id":[{"hlt":255,"slot":[{"val":0,"ddesc":"Luz Regulable","slo":0,"typ":"19"}],"ndesc":"Nodo O"},{"hlt":255,"slot":[{"val":26,"ddesc":"Sensor de Temperatura","slo":0,"typ":"52"},{"val":20,"ddesc":"Sensor de Humedad","slo":2,"typ":"53"},{"val":19,"ddesc":"Sensor de Temperatura","slo":4,"typ":"52"},{"val":50,"ddesc":"Sensor de Humedad","slo":6,"typ":"53"},{"val":179,"ddesc":"Sensor de luz","slo":8,"typ":"54"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":10,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":11,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":12,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":13,"typ":"11"},{"val":0,"ddesc":"Tira de LED RGB","slo":16,"typ":"16"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":20,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":21,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":22,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":23,"typ":"11"}],"ndesc":"Nodo I"},{"hlt":25,"slot":[{"val":18,"ddesc":"Sensor de Temperatura","slo":0,"typ":"52"},{"val":47,"ddesc":"Sensor de Humedad","slo":2,"typ":"53"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":4,"typ":"11"},{"val":0,"ddesc":"ON\/OFF Salida digital con timer","slo":5,"typ":"11"},{"val":0,"ddesc":"Luz Regulable","slo":6,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":8,"typ":"19"},{"val":154,"ddesc":"Sensor de luz","slo":10,"typ":"54"},{"val":240,"ddesc":"ON\/OFF Salida con modo AUT","slo":12,"typ":"12"},{"val":1.4296875,"ddesc":"Sensor de Corriente","slo":13,"typ":"56"},{"val":329,"ddesc":"Sensor de Potencia","slo":15,"typ":"57"}],"ndesc":"Nodo II"},{"hlt":25,"slot":[],"ndesc":"Nodo III"},{"hlt":255,"slot":[{"val":20,"ddesc":"Sensor de Temperatura","slo":0,"typ":"52"},{"val":37,"ddesc":"Sensor de Humedad","slo":2,"typ":"53"},{"val":0,"ddesc":"Luz Regulable","slo":4,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":6,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":8,"typ":"19"},{"val":0,"ddesc":"Sensor de luz","slo":10,"typ":"54"}],"ndesc":"Nodo IV"},{"hlt":1,"slot":[{"val":16.203125,"ddesc":"Sensor de Temperatura","slo":0,"typ":"52"},{"val":60.3125,"ddesc":"Sensor de Humedad","slo":2,"typ":"53"},{"val":0,"ddesc":"Luz Regulable","slo":4,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":6,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":8,"typ":"19"},{"val":0,"ddesc":"Sensor de luz","slo":10,"typ":"54"},{"val":15.75,"ddesc":"Sensor de Temperatura","slo":12,"typ":"52"}],"ndesc":"Nodo V"},{"hlt":255,"slot":[{"val":22,"ddesc":"Sensor de Temperatura","slo":0,"typ":"52"},{"val":37,"ddesc":"Sensor de Humedad","slo":2,"typ":"53"},{"val":0,"ddesc":"Luz Regulable","slo":4,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":6,"typ":"19"},{"val":0,"ddesc":"Luz Regulable","slo":8,"typ":"19"},{"val":40,"ddesc":"Sensor de Temperatura","slo":10,"typ":"52"},{"val":124,"ddesc":"Entrada analógica","slo":12,"typ":"51"},{"val":0,"ddesc":"Entrada analógica","slo":14,"typ":"51"},{"val":0,"ddesc":"Entrada analógica","slo":16,"typ":"51"},{"val":0,"ddesc":"Entrada analógica","slo":18,"typ":"51"}],"ndesc":"Nodo VI"}]} 
data = r.json()
#encoded
data_string = json.dumps(data)
 
#Decoded
decoded = json.loads(data_string)

nod = 0
slot = 0
line = ""

#SITEMAP HEADER
header = 'sitemap souliss label="Souliss"' + '\n' + '{' + '\n' + 'Frame label="Nodes" {' + '\n'
f1.write(header)

#ITEM GROUPS
f2.write('Group all' + '\n')
f2.write('Group nodes "Nodos" <house> (all)' + '\n')

f2.write('Group diagnostic "Diagnostico" <keyring> (all)'  + '\n')
f2.write('Group health "Salud" <keyring> (diagnostic)'  + '\n')
f2.write('Group timestamp "Timestamp" <clock> (diagnostic)'  + '\n')

f2.write('Group weather "Metereologia" <weather> (all)'  + '\n')
f2.write('Group temperature "Temperatura" <temperature> (weather)'  + '\n')
f2.write('Group humidity "Humedad" <humidity> (weather)'  + '\n')
f2.write('Group lux "Luz Ambiental" <lux> (weather)'  + '\n')
f2.write('Group:Number:AVG() avg_temperatures "Temperaturas Medias [%.1f C]" <temperature> (weather)'  + '\n')
f2.write('Group light "Luces" <light> (all)'  + '\n')
#QUEDAN MAS GRUPOS POR PONER

for i in decoded["id"]:
    if (nod > 0):
        f1.write('}' + '\n')
    #EXTRAE NOMBRE DE NODO
    #print nod
    ndesc = decoded["id"][nod]["ndesc"]
    print ndesc
    nodehead = 'Group item=node' + str(nod) + '{' + '\n' 
    f1.write(nodehead)
    line = 'Group node' + str(nod) + ' "' + ndesc + '" <firstfloor> (all,nodes)' 
    f2.write(line.encode('latin1') + '\n')

    #SALUD Y TIMESTAMP DE NODO
    site = 'Text item=health_node' + str(nod)
    f1.write(site.encode('latin1') + '\n')
    line = 'Number health_node' + str(nod) + ' "Salud ' + ndesc + ' [%1d]" <keyring> (node' + str(nod) + ', diagnostic) {souliss="D98' + ':' + str(nod) + ':998"}' 
    f2.write(line.encode('latin1') + '\n')

    site = 'Text item=timestamp_node' + str(nod)
    f1.write(site.encode('latin1') + '\n')
    line = 'String timestamp_node' + str(nod) + ' "Timestamp ' + ndesc + ' [%1$td.%1$tm.%1$tY %1$tk:%1$tM:%1$tS]" <clock> (node' + str(nod) + ', diagnostic) {souliss="D99' + ':' + str(nod) + ':999"}' 
    f2.write(line.encode('latin1') + '\n')

    for j in decoded["id"][nod]["slot"]:
        print slot
        ddesc = decoded["id"][nod]["slot"][slot]["ddesc"]
        typ = int(decoded["id"][nod]["slot"][slot]["typ"])
        slo = str(decoded["id"][nod]["slot"][slot]["slo"])

        #T1X TYPICALS
        if (typ == 11):  # NECESITO CAMBIAR EL \/ POR - EN DDESC
            site = 'Switch item=node' + str(nod) + '_slot' + slo
            line = 'Switch node' + str(nod) + '_slot' + slo + ' "' + ddesc + '" <light> (node' + str(nod) + ', lights) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '", autoupdate="false"}' 
        elif (typ == 12):
            site = 'Switch item=node' + str(nod) + '_slot' + slo
            site = site + '\n' + 'Switch item=node' + str(nod) + '_slot' + slo + '_auto'
            line = 'Switch node' + str(nod) + '_slot' + slo + ' "' + ddesc + '" <light> (node' + str(nod) + ', lights) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + ':switch", autoupdate="false"}' 
            line = line + '\n' + 'Switch node' + str(nod) + '_slot' + slo + '_auto "' + ddesc + '_Auto" <light> (node' + str(nod) + ', lights) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + ':automode", autoupdate="false"}' 
        elif (typ == 13):
            site = 'Switch item=node' + str(nod) + '_slot' + slo
            line = 'Contact node' + str(nod) + '_slot' + slo + ' "' + ddesc + '" <contact> (node' + str(nod) + ', lights) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '", autoupdate="true"}' 
        elif (typ == 16):
            site = 'Colorpicker item=node' + str(nod) + '_slot' + slo
            line = 'Color node' + str(nod) + '_slot' + slo + ' "' + ddesc + '" <pie> (node' + str(nod) + ', lights) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '", autoupdate="false"}' 
        elif (typ == 19):
            site = 'Slider item=node' + str(nod) + '_slot' + slo + ' switchSupport'
            line = 'Dimmer node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f %%]" <slider> (node' + str(nod) + ', lights) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        #T2X TYPICALS 
        elif (typ == 21):
            #SITE MISSING!
            line = 'Rollershutter node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' " <garage> (node' + str(nod) + ', garage) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 22):
            #SITE MISSING!
            line = 'Rollershutter node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' " <rollershutter> (node' + str(nod) + ', rollershutter) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        #T5X TYPICALS
        elif (typ == 51):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f %%]" <analog> (node' + str(nod) + ', analog) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 52):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f C]" <temperature> (node' + str(nod) + ', temperature) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 53):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f %%]" <humidity> (node' + str(nod) + ', humidity) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 54):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f lux]" <lux> (node' + str(nod) + ', lux) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 56):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f A]" <energy> (node' + str(nod) + ', current) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 57):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f W]" <energy> (node' + str(nod) + ', watt) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        elif (typ == 58):
            site = 'Text item=node' + str(nod) + '_slot' + slo
            line = 'Number node' + str(nod) + '_slot' + slo + ' "' + ddesc + ' [%.1f mb]" <pressure> (node' + str(nod) + ', pressure) {souliss="T' + str(typ) + ':' + str(nod) + ':' + slo + '"}' 
        
        f1.write(site.encode('latin1') + '\n')
        print line
        #if (len(line) > 0):
        #    f2.write(line.encode('latin1') + '\n')
        f2.write(line.encode('latin1') + '\n')
        slot = slot + 1
        site = ""
        line = ""
    nod = nod + 1
    slot = 0
nod = 0 
f1.write('}' + '\n')  #END OF LAST NODE
f1.write('Text item=avg_temperatures' + '\n')
footer = '}' + '\n' + '}'
f1.write(footer)
f1.close()  
f2.close()

