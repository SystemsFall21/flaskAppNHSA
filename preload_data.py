import pandas as pd

def preload_county_data():

    print('State data is loading...')

    #dictionary, key = state name, value = [[fip],[coynty list]]
    state_dic = {}
    # #dictionary, key = county name, value = [[fip],[location]]
    county_dic = {}
    #read the data
    state_county_fips = pd.read_csv('state_county_data.csv', dtype=str).values.tolist()
    temp = []
   
    for line in state_county_fips:
    #if the state haven't be added in dic
        if line[0] not in state_dic:
            temp.append(line[0])
            #initialate the key and value, added fit first
            state_dic[line[0]] = [[line[2]],[]]
        #add county to the list
        state_dic[line[0]][1].append(line[1].split(',')[0])
        #add fips and position to key county
        county_dic[line[1].split(',')[0]] = [[line[3]],line[4:]]

    # print(state_dic['Alaska'])
    
    return state_dic, county_dic


def preload_var():
    print('Variable data is loading...')
    #dictionary, key = var catagory, value = [[name],[code],[description]]
    var_info = {}
    #read csv file
    var_data = pd.read_csv('census_vars.csv').values.tolist()

    for line in var_data:
        #check whether catagory in dic:
        if not line[0] in var_info:
            var_info[line[0]] = [[],[],[],[]]
        #add name
        var_info[line[0]][0].append(line[1])
        #add code
        var_info[line[0]][1].append(line[2])
        #add description
        var_info[line[0]][2].append(line[3])
        #add another code
        var_info[line[0]][3].append(line[4])
    
    return var_info,var_data

a,b = preload_county_data()