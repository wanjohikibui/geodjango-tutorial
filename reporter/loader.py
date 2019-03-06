
import os
from django.contrib.gis.utils import LayerMapping
from .models import County

county_mapping = {
    'counties' : 'Counties',
    'codes' : 'Codes',
    'cty_code' : 'Cty_CODE',
    'dis' : 'dis',
    'geom' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'counties.shp'),
)


def run(verbose=True):
	lm = LayerMapping(County, county_shp, county_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)