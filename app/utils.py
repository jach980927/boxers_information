'''
def get_world_percentages(data):
    percentages_dict = {item["Country"]: item["World Population Percentage"] for item in data}

    labels = percentages_dict.keys()
    values = percentages_dict.values()

    return labels, values
    '''

def get_boxer_data(data,name_boxer):

    result =  list(filter(lambda item: item['name'] == name_boxer, data ))
    return result


def get_ko_rate(boxer_dict):
        KO_dict = { 
              
              'wins ' + boxer_dict['name']: int(boxer_dict['wins']),
              'looses ' +  boxer_dict['name']: int(boxer_dict['looses']),
               'draws ' +  boxer_dict['name']: int(boxer_dict['draws'])


              }
        labels = KO_dict.keys()
        value = KO_dict.values()
        return labels, value