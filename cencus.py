import censusdata
from datetime import date
import preload_data


#get year
year = int(date.today().strftime("%Y"))
year_list = list(range(year-6,year-1))

#get table types: defined by the first letter of var_code
tabletypes = {'B':"detail",'S':"subject",'D':"profile",'C':"cprofile" }

state_dic,county_dic = preload_data.preload_county_data()
#dictionary, key = var catagory, value = [[name],[code],[description]]
var_info,var_data = preload_data.preload_var()

#list of varible infos

#return data by county level
def cencus_county(state_fip,county_fip,var_code,type,year):
    try:
        return float(censusdata.download('acs5', year, \
        censusdata.censusgeo([('state', state_fip),('county', county_fip)]),\
            [var_code,],key = 'e12de88e1f23dcdd9a802fbbb92b362a1e67c3c4',\
                tabletype=type)[var_code])
    except:
        return None

#return data by state level
def cencus_state(state_fip,var_code,type,year):
    try:
        return float(censusdata.download('acs5', year, \
        censusdata.censusgeo([('state', state_fip)]),\
            [var_code,],key = "'e12de88e1f23dcdd9a802fbbb92b362a1e67c3c4'",\
                tabletype=type)[var_code])
    except:
        return None
    

def get_cencus(state,county,catagory):
    print(state,county,catagory)
    result = []
    state_fip = state_dic[state][0][0]
    county_fip = county_dic[county][0][0]
    var_code = var_info[catagory][1]
    var_name = var_info[catagory][0]
    # print(state_fip)
    # print(county_fip)
    # print(var_code)
    # print(var_name)

    for i in range(len(var_code)):
        type = tabletypes[var_code[i][0]]
        for year in year_list:
            temp = []
            temp.append(catagory)
            temp.append(var_name[i])
            temp.append(year)
            temp.append(cencus_county(state_fip,county_fip,var_code[i],type,year))
            # print('here')
            temp.append(cencus_state(state_fip,var_code[i],type,year))
            result.append(temp)
    return result

#test case
# get_cencus('Alaska','Aleutians East Borough','Children in Foster Care')
# get_cencus('Alaska','Aleutians East Borough','Educational Attainment')





