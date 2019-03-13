import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'IT_Project.settings')
import django
django.setup()
from WeGame.models import Publisher,Game,Picture

def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories. 
# This might seem a little bit confusing, but it allows us to iterate 
# through each data structure, and add the data to our models.

    # games = {"ARK: Sur":{},
    #         "Conan Exiles":{},
    # }
    

    publishers = {"Studio WildCard": "United States",
                "Funcom": "United States",
                "Nicalis, Inc.":"United States",
                "Klei Entertainment":"UK",
                "SCS Software":"Czech Republic",
                "Endnight Games Ltd":"China"}
    
    pictures = [
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic1.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic1.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic2.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic3.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic1.jpg"},
    ]

    games = [
        {"category":"Survival","name":"ARK:Survival Invovled","publisher_name":"Studio WildCard","year_released":"2017-08-27","game_content":"good game"},
        {"category":"Survival","name":"Conan Exiles","publisher_name":"Funcom","year_released":"2018-05-08","game_content":"good game"},
        {"category":"Indie","name":"The Binding of Isaac: Rebirth","publisher_name":"Nicals, Inc.","year_released":"2014-11-04","game_content":"good game"},
        {"category":"Survival","name":"Don't Starve Together","publisher_name":"Klei Entertainment","year_released":"2016-04-21","game_content":"good game"},
        {"category":"Simulation","name":"Euro Truck Simulator 2","publisher_name":"SCS Software","year_released":"2012-10-12","game_content":"good game"},
        {"category":"Survival","name":"The Forest","publisher_name":"Endnight Games Ltd","year_released":"2018-04-30","game_content":"good game"},
    ]
    
    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.
    
    for publisher,publisher_data in publishers.items():
        p = add_publisher(publisher,publisher_data)
        for game in games:
            if game["publisher_name"] == publisher:
                g = add_game(game["category"],game["name"],p,game["year_released"],game["game_content"])
            # for picture in pictures:
            #     if picture["game_name"]==game["name"]:
            #         pic = add_picture(g,picture["picture_path"])

   
    
    # for game in games:  
    for picture in pictures:
        for game in games: 
            if picture["game_name"] == game["name"]:
                g = Game.objects.get_or_create(name = picture["game_name"])
                add_picture(g,picture["picture_path"])
  

    # for game in games:
    #     g = add_game(game["category"],game["name"],
    #     game["publisher_name"],game["year_released"],game["game_content"])



def add_publisher(publisher,country):
    p = Publisher.objects.get_or_create(name=publisher,country=country)[0]
    p.save()
    return p

def add_game(category,name,publisher,year_released,game_content):
    g = Game.objects.get_or_create(category=category,name=name,
    publisher_name=publisher,year_released=year_released,game_content=game_content)[0]
    g.save()
    return g

def add_picture(game,path):
    pic = Picture.objects.get_or_create(game_name=game,picture_path=path)[0]
    pic.save()
    return pic


# Start execution here!
if __name__ == '__main__':
    print("Starting wegame population script...") 
    populate()
