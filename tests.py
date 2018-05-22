from unittest import TestCase
from pytest import fixture
import warnings
from main import getCensusMetadata

class UnsupportedYearException(Exception):
    pass
year = 2012
df =getCensusMetadata('acs5', year)
# class APINameTest(TestCase):
@fixture
def acs_keys():
    return ['label', 'concept', 'required', 'limit', 'predicateType', 'group', 'validValues']

def test_df_non_zero_and_valid(acs_keys):
    '''
    getCensusMetadata() should return a non-empty dataframe of metadata for acs5
    '''

    # for year in range(2009,2017,1):

    assert df.shape[0] >0
    assert df.shape[1]> 0
    assert set(acs_keys).issubset(list(df.columns.values))
# def test_df_valid_entries(self):
    assert df.loc['COUSUB','label']=='County Subdivision (FIPS)'

    # def test_acs5(self):
    #     client = self.client('acs5')
    #     self.assertRaises(UnsupportedYearException,
    #                       client.state, ('NAME', '06'))
    #     self.assertRaises()

# years =
# for x in range(2009,2017,1):
    # getCensusMetadata('acs5',x).shape[0]
