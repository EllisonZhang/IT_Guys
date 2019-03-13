import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_project.settings')
import django
django.setup()
from wegame.models import publisher

def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories. 
# This might seem a little bit confusing, but it allows us to iterate 
# through each data structure, and add the data to our models.

    # games = {"ARK: Sur":{},
    #         "Conan Exiles":{},
    # }
    
    publishers = {"Studio Wildcrd": {"name":Studio Wildcrd, "country": United States},
                "Funcom": {"name":Funcom, "country": United States},
    }
    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.
    
    for publisher, publisher_data in publishers.items():
        c = add_publisher(publisher,publisher_data)



def add_publisher(name,):

# Start execution here!
if __name__ == '__main__':
    print("Starting wegame population script...") 
    populate()