# Orbit — Portfolio API

Shaxsiy portfolio/CV sayti uchun Django REST Framework asosida qurilgan backend API.

---

## Loyiha tuzilmasi

```
project/
├── orbit/                  # Asosiy ilova
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── config/                 # Loyiha sozlamalari
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## Texnologiyalar

- **Python**
- **Django** — web framework
- **Django REST Framework** — API yaratish uchun
- **django-allauth** — autentifikatsiya
- **dj-rest-auth** — REST orqali login/registratsiya
- **drf-yasg** — Swagger/OpenAPI dokumentatsiya

---

## O'rnatish

```bash
# 1. Reponi klonlash
git clone https://github.com/username/orbit.git
cd orbit

# 2. Virtual muhit yaratish
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 4. Migratsiyalarni bajarish
python manage.py migrate

# 5. Serverni ishga tushirish
python manage.py runserver
```

---

## API Endpointlari

| Method | URL | Tavsif |
|--------|-----|--------|
| GET | `/api/about/` | Shaxsiy ma'lumotlar (About) ro'yxati |
| GET | `/api/about-skill/` | Ko'nikmalar (Skills) ro'yxati |
| GET | `/api/category/` | Portfolio kategoriyalari |
| GET | `/api/portfolio/` | Portfolio loyihalari ro'yxati |
| GET | `/api/workex/` | Ish tajribasi ro'yxati |
| GET | `/api/education/` | Ta'lim ma'lumotlari |
| GET | `/api/hapclients/` | Mamnun mijozlar (fikr-mulohazalar) |
| GET | `/api/services/` | Xizmatlar ro'yxati |
| GET | `/api/blogpost/` | Blog postlar ro'yxati |
| POST | `/api/contact/` | Aloqa formasi orqali xabar yuborish |

---

## Modellar haqida qisqacha

- **About** — shaxsiy ma'lumotlar (sarlavha, tavsif, rasm)
- **About_skill** — ko'nikmalar va ularning foiz darajasi
- **Category** — portfolio loyihalari kategoriyasi
- **Portfolio** — bajarilgan loyihalar
- **Workex** — ish tajribasi (to'liq/yarim stavka)
- **Education** — ta'lim tarixi
- **Hapclients** — mijozlar fikri
- **Services** — taklif qilinadigan xizmatlar
- **BlogPost** — blog postlari (o'qilganlar soni bilan)
- **Contact** — saytdan yuborilgan xabarlar

---

## Admin panel

Barcha modellarni boshqarish uchun Django admin paneldan foydalaning:

```
http://127.0.0.1:8000/admin/
```

---

## Muhit o'zgaruvchilari

`.env` fayl yaratib quyidagilarni sozlang:

```env
SECRET_KEY=
DEBUG=True
```

---

## Litsenziya

MIT License