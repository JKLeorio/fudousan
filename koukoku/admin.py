from django.contrib import admin

from koukoku.models import (
    Region,
    City,
    District,
    Communication,
    Document,
    TargetPurpose,
    Infrastructure,
    PaymentTerm,
    Estate, Location)


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


class PaymentTermAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class EstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'plot_area', 'house_area', 'deal_type', 'price', 'currency', 'phone', 'location',
                    'target', 'communications', 'documents', 'infrastructure', 'payment_term'
                    )


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(TargetPurpose, TargetPurposeAdmin)
admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(PaymentTerm, PaymentTermAdmin)
admin.site.register(Estate, EstateAdmin)
