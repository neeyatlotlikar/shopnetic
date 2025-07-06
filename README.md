# Shopnetic: Online Marketplace Built with Django

Welcome to Shopnetic, a simple online marketplace built using Python's Django framework! This project is inspired by a hands-on YouTube tutorial and is perfect for anyone looking to learn Django by building a real-world application.

## 🚀 Features

- User Authentication: Sign up, log in, and manage your account.
- Item Listings: Create, browse, edit, and delete items for sale.
- Categories: Organize items by categories and display item counts.
- Search & Filter: Search items by title or description, filter by category.
- User Dashboard: Manage your own items from a personalized dashboard.
- Discourse: Contact sellers and chat with other users via an inbox system.
- Responsive UI: Styled with Tailwind CSS for a modern, mobile-friendly design.

## 🛠️ Getting Started

Prerequisites

- Python 3.8+
- pip
- Virtualenv
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/neeyatlotlikar/shopnetic.git
cd shopnetic
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up the Django project:

```bash
django-admin startproject shopnetic .
```

Run migrations:

```bash
python manage.py migrate
```

Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🧩 Project Structure

```test
shopnetic/
│
├── shopnetic/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── core/                 # Main app: homepage, contact, navigation, etc.
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── contact.html
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── items/                # App for item listings (create, edit, delete)
├── discourse/            # App for messaging between users
├── env/                  # Virtual environment (not tracked)
├── manage.py
├── requirements.txt
└── README.md
```

## 📝 Usage

- Browse Items: Search and filter items on the browse page.
- Create Item: Click "New Item" in the navigation bar to add a new listing.
- Contact Seller: Use the "Contact Seller" button on an item's page to start a conversation.
- Dashboard: Manage your listings, edit or mark as sold.
- Inbox: View and reply to conversations with other users.

## 🎨 Customization

- Styling: Uses [Tailwind CSS](https://tailwindcss.com/) via CDN for rapid UI development.
- Templates: Extend base.html for consistent layout and navigation.
- Apps: Modular Django apps for scalability (core, items, conversations, etc.).

## 📚 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Python Official Docs](https://docs.python.org/3/)

## 🙏 Acknowledgements

- Inspired by [Stein's Django Marketplace Tutorial on YouTube.](https://youtu.be/ZxMB6Njs3ck?si=aXqG7gRX2j1SPhpZ)
- Thanks to the Django and Tailwind CSS communities!

## Happy coding! 🚀

If you found this project useful, please ⭐️ the repo and share it with others!
