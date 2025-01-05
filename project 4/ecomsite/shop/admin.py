from django.contrib import admin
from .models import Products,Order
# Register your models here.

admin.site.site_header = 'E-commerce site'
admin.site.site_title ="shopmate shopping cart"
admin.site.index_title="Manage your shopping cart"

class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
        
        
    change_category_to_default.short_description = "default category"
    list_display =('title',"price","discount","category","image",)
    search_fields = ('title',"discount")
    actions = ('change_category_to_default',)
# hiddin only ceratian fields in the adminn panel
    fields =('title','price',)# check out the admin panel databaes of the products
    list_editable=("price","discount")
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
