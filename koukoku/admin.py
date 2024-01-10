from django.contrib import admin

from koukoku.models import (
    Region,
    City,
    District,
    Communication,
    Document,
    TargetPurpose,
    Infrastructure,
    Estate,
    Location,
    Image)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'district', 'region')


class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TargetPurposeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'estate')


class EstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'plot_area', 'house_area', 'deal_type', 'price', 'currency', 'phone', 'location',
                    'target', 'documents'#, 'communications',  'infrastructure'
                    )


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(TargetPurpose, TargetPurposeAdmin)
admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(Estate, EstateAdmin)
admin.site.register(Image)
