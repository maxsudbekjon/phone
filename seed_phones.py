import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
django.setup()

from phones.models import Phone, PhoneVariant, Category, Color  # noqa: E402


def seed():
    brands = [
        'Apple', 'Samsung', 'Xiaomi', 'Realme', 'Oppo', 'Vivo', 'Huawei', 'OnePlus', 'Google', 'Honor'
    ]
    models = {
        'Apple': ['iPhone 12', 'iPhone 13', 'iPhone 14', 'iPhone 15 Pro', 'iPhone 11'],
        'Samsung': ['Galaxy S21', 'Galaxy S22 Ultra', 'Galaxy S23', 'Galaxy A54', 'Galaxy Note 20'],
        'Xiaomi': ['Mi 10', 'Mi 11', '13 Pro', 'Redmi Note 12', 'Redmi Note 13'],
        'Realme': ['GT 2', 'GT 3', '11 Pro', 'C55', 'Narzo 60'],
        'Oppo': ['Reno 8', 'Reno 9', 'Reno 10', 'Find X5', 'Find X7'],
        'Vivo': ['V23', 'V25', 'V27', 'X90', 'Y100'],
        'Huawei': ['P40', 'P50', 'Mate 40', 'Mate 50', 'Nova 10'],
        'OnePlus': ['9 Pro', '10 Pro', '11', 'Nord 2', 'Nord 3'],
        'Google': ['Pixel 6', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 8', 'Pixel 8 Pro'],
        'Honor': ['Honor 50', 'Honor 70', 'Honor 90', 'Magic 4', 'Magic 5']
    }
    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    rams = ['4GB', '6GB', '8GB', '12GB', '16GB']
    storages = ['64GB', '128GB', '256GB', '512GB']
    colors = ['Black', 'White', 'Blue', 'Red', 'Green', 'Gold', 'Silver', 'Titanium']

    category_names = ['new', 'old-good', 'used']
    categories = {name: Category.objects.get_or_create(name=name)[0] for name in category_names}
    color_objs = {name: Color.objects.get_or_create(name=name)[0] for name in colors}

    PhoneVariant.objects.all().delete()
    Phone.objects.all().delete()

    phones = []
    for i in range(50):
        brand = random.choice(brands)
        model = random.choice(models[brand])
        year = random.choice(years)
        category = categories[random.choice(category_names)]
        battery = random.choice([None, 78, 85, 90, 95])
        cycles = None if battery is None else random.randint(20, 600)
        issues = [] if category.name != 'used' else random.sample(
            ['Ekran chizilgan', 'Batareya tez tugaydi', 'Korpusda chizishlar', 'Kamera ishlamaydi'],
            k=random.randint(1, 2),
        )
        verified = random.choice([True, False])
        hot = random.choice([True, False])

        phone = Phone.objects.create(
            brand=brand,
            model=model,
            year=year,
            category=category,
            battery=battery,
            cycles=cycles,
            issues=issues,
            verified=verified,
            hot=hot,
        )
        phones.append(phone)

        variant_count = random.randint(2, 4)
        used_pairs = set()
        for _ in range(variant_count):
            ram = random.choice(rams)
            storage = random.choice(storages)
            color = random.choice(colors)
            key = (ram, storage, color)
            if key in used_pairs:
                continue
            used_pairs.add(key)
            price_base = random.randint(2000000, 18000000)
            price = price_base + (storages.index(storage) * 400000) + (rams.index(ram) * 300000)
            PhoneVariant.objects.create(
                phone=phone,
                ram=ram,
                storage=storage,
                color=color_objs[color],
                price=price,
            )

    print(f"Seeded {len(phones)} phones with variants.")


if __name__ == '__main__':
    seed()
