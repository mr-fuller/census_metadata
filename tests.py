from unittest import TestCase
import warnings
from main import getCensusMetadata

class UnsupportedYearException(Exception):
    pass
year = 2012
df =getCensusMetadata('acs5', year)
class APINameTest(TestCase):
    def test_df_non_zero(self):
        '''
        getCensusMetadata() should return a non-empty dataframe of metadata for acs5
        '''

        # for year in range(2009,2017,1):

        self.assertGreater(df.shape[0],0)
        self.assertGreater(df.shape[1],0)
    def test_df_valid_entries(self):
        self.assertEqual(df.loc['COUSUB','label'],'County Subdivision (FIPS)')

    # def test_acs5(self):
    #     client = self.client('acs5')
    #     self.assertRaises(UnsupportedYearException,
    #                       client.state, ('NAME', '06'))
    #     self.assertRaises()

# years =
# for x in range(2009,2017,1):
    # getCensusMetadata('acs5',x).shape[0]
