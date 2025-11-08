import os
import django
from django.conf import settings
from django.urls import path
from django.shortcuts import render, redirect
from django.core.management import execute_from_command_line
from django.db import models
from django.contrib import admin

from django.urls import path, include

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY="abc123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],

    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "shop",
    ],

    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],

    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },

    # ✅ Proper placement of CSRF Trusted Origins
    CSRF_TRUSTED_ORIGINS=[
        "https://anglespace.onrender.com",
        "http://localhost:8000",
    ],

    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }],

    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
    STATIC_URL="/static/",

    # ✅ Add login redirects to fix login/logout
    LOGIN_URL="/accounts/login/",
    LOGIN_REDIRECT_URL="/",
    LOGOUT_REDIRECT_URL="/",
)

django.setup()

from shop.models import Product, Order
from django.contrib.auth.models import User  # <-- Add this

# --- CREATE SUPERUSER HERE ---
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin123"
    )
    print("Superuser created: username='admin', password='admin123'")

from shop.models import Product, Order


# --- Views ---
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def about(request):
    return render(request, "about.html")

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def buy(request, product_id):
    product = Product.objects.get(id=product_id)
    Order.objects.create(product=product)
    return redirect("/orders/")

def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

# --- URLs ---
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),  # include shop app URLs
    path("accounts/", include("django.contrib.auth.urls"))
]

# --- Run Server ---
if __name__ == "__main__":
    from django.core.management import call_command

    call_command("makemigrations", "shop", interactive=False)
    call_command("migrate", interactive=False)

    # Seed products
   # Seed 20 products safely
products_to_add = [
    {"name": "Men's T-Shirt", "price": 19.99, "description": "Comfortable cotton T-shirt", "image": "https://images.pexels.com/photos/1043474/pexels-photo-1043474.jpeg"},
    {"name": "Women's Dress", "price": 39.99, "description": "Stylish summer dress", "image": "https://images.pexels.com/photos/1488463/pexels-photo-1488463.jpeg"},
    {"name": "Men's Jeans", "price": 49.99, "description": "Classic denim jeans", "image": "https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg"},
    {"name": "Women's Jeans", "price": 44.99, "description": "Skinny fit denim jeans", "image": "https://assets.ajio.com/medias/sys_master/root/20240307/aRVl/65e9b45405ac7d77bb9e0607/-473Wx593H-469574237-blue-MODEL.jpg"},
    {"name": "Men's Jacket", "price": 89.99, "description": "Casual winter jacket", "image": "https://images.pexels.com/photos/2897532/pexels-photo-2897532.jpeg"},
    {"name": "Women's Jacket", "price": 79.99, "description": "Trendy leather jacket", "image": "https://images.pexels.com/photos/842811/pexels-photo-842811.jpeg"},
    {"name": "Men's Shirt", "price": 29.99, "description": "Formal cotton shirt", "image": "https://images.pexels.com/photos/428338/pexels-photo-428338.jpeg"},
    {"name": "Women's Top", "price": 24.99, "description": "Floral printed top", "image": "https://images.pexels.com/photos/1578883/pexels-photo-1578883.jpeg"},
    {"name": "Men's Shorts", "price": 22.99, "description": "Casual summer shorts", "image": "https://contents.mediadecathlon.com/p2073161/fa5db4e274c467b2ef0d0acf402f13e9/p2073161.jpg"},
    {"name": "Women's Skirt", "price": 29.99, "description": "Elegant pleated skirt", "image": "https://images.pexels.com/photos/1488465/pexels-photo-1488465.jpeg"},
    {"name": "Men's Hoodie", "price": 34.99, "description": "Warm fleece hoodie", "image": "https://images-cdn.ubuy.co.in/654f2dc0e5fa023e6727b1d9-mens-hoodies-long-sleeves-with-pocket.jpg"},
    {"name": "Women's Sweater", "price": 39.99, "description": "Cozy knitted sweater", "image": "https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg"},
    {"name": "Men's Shoes", "price": 59.99, "description": "Casual lace-up sneakers", "image": "https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg"},
    {"name": "Women's Heels", "price": 69.99, "description": "Elegant high heels", "image": "https://m.media-amazon.com/images/I/61yQqiiZqhL._AC_UY1000_.jpg"},
    {"name": "Men's Watch", "price": 99.99, "description": "Classic analog wristwatch", "image": "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg"},
    {"name": "Women's Watch", "price": 89.99, "description": "Stylish wristwatch", "image": "https://m.media-amazon.com/images/I/71Fa85HR3dL._AC_UY1000_.jpg"},
    {"name": "Men's Sunglasses", "price": 24.99, "description": "UV-protected sunglasses", "image": "https://images.pexels.com/photos/46710/pexels-photo-46710.jpeg"},
    {"name": "Women's Handbag", "price": 79.99, "description": "Leather crossbody bag", "image": "https://images.pexels.com/photos/1488466/pexels-photo-1488466.jpeg"},
    {"name": "Men's Belt", "price": 19.99, "description": "Genuine leather belt", "image": "https://images.pexels.com/photos/298863/pexels-photo-298863.jpeg"},
    {"name": "Women's Scarf", "price": 14.99, "description": "Silky printed scarf", "image": "https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg"},
]



for p in products_to_add:
    Product.objects.get_or_create(name=p["name"], defaults=p)


execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])



