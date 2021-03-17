# import requests
# import shutil
# import wget

# # r = requests.get('https://api.nasa.gov/planetary/apod?api_key=HKX3fDXTgAIIQQz03Gi9YWIQe2Y3HN4j55tvnWA5',stream=True)
# # filename = wget.download(r.json()["hdurl"])

# API_KEY = "HKX3fDXTgAIIQQz03Gi9YWIQe2Y3HN4j55tvnWA5"
# START_DATE = "2021-03-08"
# END_DATE = "2021-04-01"
# x=(requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY").json())
# for i,j in x['near_earth_objects'].items():
#     print(i,end='\n')
# # print(x['near_earth_objects'][0]['name'])

sol_data = ["03-05",
"03-06",
"03-07",
"03-08",
"03-09",
"03-10",
"03-11"]

sol_final=[]
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in sol_data:
    sol_final.append(str(month[int(i[:2])-1])+'. '+i[3:])
print(sol_final)