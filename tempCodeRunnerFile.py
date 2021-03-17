for i in mars_weather['sol_keys']:
        sol_data.append(mars_weather[str(i)]['First_UTC'][5:10])
    month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in sol_data:
        sol_final.append(str(month[int(i[:2])-1])+'. '+i[3:])
