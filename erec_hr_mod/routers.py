from hr.viewsets import CountryViewsets, CityViewsets, OrganizationViewsets
from addtional_conn.viewsets import SongsViewsets

from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'country', CountryViewsets,  basename='Country' )
router.register(r'city', CityViewsets,  basename='City' )
router.register(r'organization', OrganizationViewsets,  basename='organization' )

router.register(r'songs', SongsViewsets,  basename='songs' )

