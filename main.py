import requests, pandas
# get a pandas dataframe of Census Metadata
def getCensusMetadata(name,vintage=2016, type="variables"):
    def buildURL(name, vintage):
        if name != 'acs5':
            print("Error: API not yet supported.")
            quit()
        elif (vintage is None):
            print("Invalid ACS year.")
            quit()
        elif vintage in[2009,2010,2012,2013,2014]:
            api_url = "https://api.census.gov/data/" + str(vintage) +  '/' + name
        else:
            api_url = "https://api.census.gov/data/" + str(vintage) + "/" + name[:3] + '/' + name
        return api_url

        # Handle messy URLs?

    apiurl = buildURL(name,vintage)
    if type in ['variables','v']:
        u = apiurl + '/' + 'variables.json'
    print(u)
    df = pandas.DataFrame(requests.get(u).json()['variables']).transpose()
    return df
# These are tests
# print(getCensusMetadata('acs5',2016).shape)
# print(getCensusMetadata('acs5',2015).shape)
# print(getCensusMetadata('acs5',2014).shape)
# print(getCensusMetadata('acs5',2013).shape)
# print(getCensusMetadata('acs5',2012).shape)
# print(getCensusMetadata('acs5',2011).shape)
# print(getCensusMetadata('acs5',2010).shape)
# print(getCensusMetadata('acs5',2009).shape)
# print(getCensusMetadata('acs1',2009).shape)
# print(getCensusMetadata('acs5').shape)
# print(getCensusMetadata('acs5',vintage=None).shape)
# print(getCensusMetadata('acs5',vintage='2015').shape)