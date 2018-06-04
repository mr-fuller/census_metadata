import requests, pandas
# get a pandas dataframe of Census Metadata
def getCensusMetadata(name,vintage=2016, type="variables"):
    if name not in ['acs5','acs1','sf1','sf3']:
        print("Error: API not yet supported.")
        quit()
    elif (vintage is None):
        print("Invalid ACS year.")
        quit()
    elif name == 'acs1' and vintage < 2012:
        print("Invalid ACS year.")
        quit()
    elif name in ['sf1','sf3'] and vintage not in [2010,2000,1990]:
        print("Invalid Census year.")
        quit()
    else:
        def buildURL():

            if vintage in[1990,2000,2009,2010,2012,2013,2014]:
                api_url = "https://api.census.gov/data/" + str(vintage) +  '/' + name
            else:
                api_url = "https://api.census.gov/data/" + str(vintage) + "/" + name[:3] + '/' + name
            return api_url

        # Handle messy URLs?

        apiurl = buildURL()
        if type in ['variables','v']:
            u = apiurl + '/' + 'variables.json'
        # print(u)
        df = pandas.DataFrame(requests.get(u).json()['variables']).transpose()
        return df
# These are tests

# print(getCensusMetadata('acs1',2009).shape)
print(getCensusMetadata('acs1',2012).shape)
# print(getCensusMetadata('acs5',vintage=None).shape)
# print(getCensusMetadata('acs5',vintage='2015').shape)
