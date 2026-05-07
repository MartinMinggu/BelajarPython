jalankan 
python manage.py shell

# 1. Import dengan nama app langsung (asumsi nama app kamu adalah 'book')
from book.models import Book  

# 2. Sisanya sama seperti tadi
import random
from datetime import date, timedelta
from decimal import Decimal

titles = ["The Secrets of", "Journey to", "Mastering", "The Chronicles of", "Guide to"]
subjects = ["Python", "Django", "Database", "Universe", "Cooking", "Self-Care", "History"]

books_to_create = []

for i in range(100):
    random_title = f"{random.choice(titles)} {random.choice(subjects)} Vol. {random.randint(1, 99)}"
    random_author = f"Author {random.choice(['Alpha', 'Bravo', 'Charlie', 'Delta'])} {i}"
    random_pages = random.randint(150, 1200)
    random_date = date.today() - timedelta(days=random.randint(0, 1825))
    random_price = Decimal(random.uniform(50000, 500000)).quantize(Decimal('0.00'))
    random_desc = f"Deskripsi untuk {random_title}."
    
    books_to_create.append(
        Book(
            title=random_title,
            author=random_author,
            total_page=random_pages,
            published_date=random_date,
            description=random_desc,
            price=random_price,
            available=random.choice([True, True, False])
        )
    )

# 3. Eksekusi
Book.objects.bulk_create(books_to_create)

print(f"Mantap! Sekarang ada {Book.objects.count()} buku di database.")