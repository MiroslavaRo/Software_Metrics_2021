import requests
import pprint
import unittest

LINK = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases2_v1/FeatureServer/2/query?where=1%3D1&outFields=*&outSR=4326&f=json"
Country_Region = "Ukraine"

def covid_by_country(cr):
    r = requests.get(LINK)
    print(r.status_code)
    res = r.json()
    found = False
    for curr in res['features']:
        print(curr['attributes'].keys())
        if curr['attributes']['Country_Region'] == cr:
            found = True
            print(pprint.pprint(curr['attributes']))
            return r.status_code, curr['attributes']
            raise ValueError(f"country{CR} not in json")

result = covid_by_country(Country_Region)
print('result', result)

class TestCovid(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(covid_by_country(Country_Region)[0],200)

    def test_wrong_country(self):
        with self.assertRaises(ValueError):
           covid_by_country("42")
   # def test_country_type(self):
       # with self.assertRaises(TypeError):
         #   covid_by_country(42)

if __name__=='__main__':
    unittest.main()