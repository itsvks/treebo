from import_export import resources

from hotel.models import Deals


class DealsResource(resources.ModelResource):

    class Meta:
        model = Deals
