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
    return float(censusdata.download('acs5', year, \
        censusdata.censusgeo([('state', state_fip),('county', county_fip)]),\
            [var_code,],tabletype=type)[var_code])

#return data by state level
def cencus_state(state_fip,var_code,type,year):
    return float(censusdata.download('acs5', year, \
        censusdata.censusgeo([('state', state_fip)]),\
            [var_code,],tabletype=type)[var_code])

def get_cencus(state,county,catagory):
    result = []
    state_fip = state_dic[state][0][0]
    county_fip = county_dic[county][0][0]
    var_code = var_info[catagory][1]
    var_name = var_info[catagory][0]
    for i in range(len(var_code)):
        type = tabletypes[var_code[i][0]]
        for year in year_list:
            temp = []
            temp.append(catagory)
            temp.append(var_name[i])
            temp.append(year)
            temp.append(cencus_county(state_fip,county_fip,var_code[i],type,year))
            temp.append(cencus_state(state_fip,var_code[i],type,year))
            result.append(temp)
    print(result)
    return result

#test case
#get_cencus('Arizona','Cochise County','Educational Attainment')





