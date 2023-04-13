
from django.contrib import admin
from .models import Category,Building

admin.site.register(Category)
# admin.site.register(Building)

@admin.register(Building)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'ochered','sdacha_sekcii', 'number', 'ploshad','total_price','photo')  # для отображения в одмин панеле по каиегориям
    # fields = ('name', ('price', 'ploshad'), 'image')
    # search_fields = ('name',)   # добавить строку поиска по имени
    # ordering = ('name',)   # добавить сортировку не по айди которая по стандарту а по имени поалфавиту