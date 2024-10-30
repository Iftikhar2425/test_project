from django.contrib import admin
from .models import Category, Product, Role, User, Testimonial,Setup

# Register your models here
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image')  # Display image
    list_filter = ('category',)
    search_fields = ('name', 'description')
      # Search functionality
class RoleAdmin(admin.ModelAdmin):
     list_display = ('name','decription')
     search_fields = ('name','decription')
     list_filter = ('name','decription')



# Customizing User Admin View
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')  # Display username, email, and role in the admin list view   list_filter = ('role',)                       # Filters by user role


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'content', 'created_at')   # # Fields to display in admin list view
    search_fields = ('name', 'destination')  # Searchable fields
    
class SetupAdmin(admin.ModelAdmin):
    list_display = ('footer_text', 'primary_color', 'secondary_color')  # Adjust fields as needed
    search_fields = ('footer_text',)    
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)  # Registers the Product model
admin.site.register(Role)      # Registers the Role model
admin.site.register(User,UserAdmin)      # Registers the Custom User model
admin.site.register(Testimonial,TestimonialAdmin)  # Registers the Testimonial model
admin.site.register(Setup, SetupAdmin)


