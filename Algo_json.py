import json


def Bild_Json(data):
    to_stg_json ={}
    for x in data:
        to_stg_json.update({str(x): data[x].to_string()})
    return to_stg_json

def Seve_Json(data,name):
    out_file = open(name+".json", "a")
    json.dump(data, out_file, indent=6)
    out_file.close()

def Read_Json(fil_name):
    file1 = open(fil_name+".json")
    data=file1.read()
    file1.close()
    return data

