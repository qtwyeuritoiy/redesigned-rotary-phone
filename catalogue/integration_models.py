# All are to be Copied & Pasted into Models.py after Migrations
# Because it throws you a major error, Or simply run this file

# Insert Categories
from oscar.apps.catalogue.categories import create_from_breadcrumbs

def pushCategories():
    categories = (
        'Processor > AMD',
        'Processor > Intel',
        'Graphics Card',
        'RAM',
        'Motherboard',
        'Storage',
        'Power Supply',
    )

    for breadcrumbs in categories:
        create_from_breadcrumbs(breadcrumbs)

pushCategories()