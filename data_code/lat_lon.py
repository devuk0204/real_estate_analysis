import requests 
import json
import pandas as pd

cvs_all = pd.read_csv("/home/devuk/code/machine_learning/data/cvs_location_final.csv")


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK 32786fab9fb7d042f070de15c98da6e2"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    try :
        address = api_json['documents'][0]['address']
    except :
        coordinate = ['0', '0']    
    else :
        coordinate = [str(address['y']), str(address['x'])]
    return coordinate


j = 1
for i in range(len(cvs_all)) :
    coordinate = get_location(cvs_all.address[i])
    cvs_all.latitude[i] = coordinate[0]
    cvs_all.longitude[i] = coordinate[1]
    print(j, cvs_all.latitude[i], cvs_all.longitude[i])
    j += 1
