import requests 
import json
import pandas as pd

#cvs_all = pd.read_csv("/home/devuk/code/machine_learning/data/cvs_location_final.csv")
#real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")
subway = pd.read_csv("/home/devuk/code/machine_learning/data/subway.csv")

def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK 32786fab9fb7d042f070de15c98da6e2"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    try :
        address = api_json['documents'][0]['address']
    except :
        coordinate = ['0', '0']    
    else :
        if (address is None) :
            coordinate = ['0', '0']
        else :
            coordinate = [str(address['y']), str(address['x'])]        
    return coordinate

for i in range(len(subway)) :
    coordinate = get_location(subway.address1[i])
    subway.latitude[i] = coordinate[0]
    subway.longitude[i] = coordinate[1]
    print(subway.latitude[i], subway.longitude[i])
    
subway.to_csv("/home/devuk/code/machine_learning/data/subway.csv", index = False)

"""
j = 1
for i in range(len(cvs_all)) :
    coordinate = get_location(cvs_all.address[i])
    cvs_all.latitude[i] = coordinate[0]
    cvs_all.longitude[i] = coordinate[1]
    print(j, cvs_all.latitude[i], cvs_all.longitude[i])
    j += 1

cvs_all.to_csv("/home/devuk/code/machine_learning/data/cvs_location_final.csv")

duplication_address = 'temp'
duplication_coordinate = 'temp'


j = 1
for i in range(len(real_estate)) :
    if real_estate.address2[i] != real_estate.address2[i] :
        if real_estate.address3[i] != real_estate.address3[i] :
            address = ''
        else :
            address = real_estate.address1[i]+real_estate.address3[i]
            
            if address == duplication_address :
                coordinate = duplication_coordinate
                print('duplication address')
            else :
                coordinate = get_location(address)
                duplication_address = address
                duplication_coordinate = coordinate
                print('not duplication address')
        

            
    else :
        address = real_estate.address1[i]+real_estate.address2[i]
        
        if address == duplication_address :
            coordinate = duplication_coordinate
            print('duplication address')
        else :
            coordinate = get_location(address)
            duplication_address = address
            duplication_coordinate = coordinate
            print('not duplication address')
        
    real_estate.latitude[i] = coordinate[0]
    real_estate.longitude[i] = coordinate[1]
    print(j, real_estate.latitude[i], real_estate.longitude[i])
    j += 1
    
real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv")
"""