import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'IT_Project.settings')
import django
django.setup()
from WeGame.models import Publisher,Game,Picture,Review,Video,News

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
                "Endnight Games Ltd":"China",
                "ConcernedApe":"United States",
                "Blizzard Entertainment":"United States",
                }
    
    pictures = [
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic1.jpg"},
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic2.jpg"},
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic3.jpg"},
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic4.jpg"},
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic5.jpg"},
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic6.jpg"},
        {"game_name":"ARK:Survival Invovled","picture_path":"/media/game-pic/Ark-pic/pic7.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic1.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic2.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic3.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic4.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic5.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic6.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","picture_path":"/media/game-pic/Binding-Of-Isaac-pic/pic7.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic1.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic2.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic3.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic4.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic5.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic6.jpg"},
        {"game_name":"Don't Starve Together","picture_path":"/media/game-pic/Dont-Starve-pic/pic7.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic1.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic2.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic3.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic4.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic5.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic6.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic7.jpg"},
        {"game_name":"Euro Truck Simulator 2","picture_path":"/media/game-pic/EU-Truck-pic/pic7.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic1.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic2.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic3.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic4.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic5.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic6.jpg"},
        {"game_name":"The Forest","picture_path":"/media/game-pic/Forest-pic/pic7.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic1.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic2.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic3.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic4.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic5.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic6.jpg"},
        {"game_name":"Hearthstone","picture_path":"/media/game-pic/Hearthstone-pic/pic7.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic1.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic2.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic3.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic4.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic5.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic6.jpg"},
        {"game_name":"OVERWATCH","picture_path":"/media/game-pic/Overwatch-pic/pic7.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic1.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic2.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic3.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic4.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic5.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic6.jpg"},
        {"game_name":"Stardew Valley","picture_path":"/media/game-pic/Stardewvalley-pic/pic7.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic1.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic2.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic3.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic4.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic5.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic6.jpg"},
        {"game_name":"WORLD OF WARCRFT","picture_path":"/media/game-pic/WOW-pic/pic7.jpg"},
    ]

    games = [
        {"category":"Survival","name":"ARK:Survival Invovled","publisher_name":"Studio WildCard","year_released":"2017-08-27","game_content":"good game"},
        {"category":"Cosplay","name":"Stardew Valley","publisher_name":"ConcernedApe","year_released":"2016-02-16","game_content":"good game"},
        {"category":"Indie","name":"The Binding of Isaac: Rebirth","publisher_name":"Nicals, Inc.","year_released":"2014-11-04","game_content":"good game"},
        {"category":"Survival","name":"Don't Starve Together","publisher_name":"Klei Entertainment","year_released":"2016-04-21","game_content":"good game"},
        {"category":"Simulation","name":"Euro Truck Simulator 2","publisher_name":"SCS Software","year_released":"2012-10-12","game_content":"good game"},
        {"category":"Survival","name":"The Forest","publisher_name":"Endnight Games Ltd","year_released":"2018-04-30","game_content":"good game"},
        {"category":"Cosplay","name":"OVERWATCH","publisher_name":"Blizzard Entertainment","year_released":"1991-02-22","game_content":"good game"},
        {"category":"Cospaly","name":"WORLD OF WARCRFT","publisher_name":"Blizzard Entertainment","year_released":"1991-02-19","game_content":"good game"},
        {"category":"Card","name":"Hearthstone","publisher_name":"Blizzard Entertainment","year_released":"1991-02-05","game_content":"good game"},
    ]
    
    videos = [
        {"game_name":"ARK:Survival Invovled","video_path":"https://www.youtube.com/watch?v=E9Wb_zRnJek"},
        {"game_name":"ARK:Survival Invovled","video_path":"https://www.youtube.com/embed/E9Wb_zRnJek"},
        {"game_name":"The Binding of Isaac: Rebirth","video_path":"https://www.youtube.com/watch?v=DALFKiVsoDk"},
        {"game_name":"Don't Starve Together","video_path":"https://www.youtube.com/watch?v=_k3fUJpDXxs"},
        {"game_name":"Euro Truck Simulator 2","video_path":"https://www.youtube.com/watch?v=2bfVnhxFvfQ"},
        {"game_name":"Euro Truck Simulator 2","video_path":"https://www.youtube.com/embed/2bfVnhxFvfQ"},
        {"game_name":"The Forest","video_path":"https://www.youtube.com/watch?v=FM28K6ABbQs"},
        {"game_name":"Hearthstone","video_path":"https://www.youtube.com/watch?v=HaZH57Q9B18"},
        {"game_name":"Hearthstone","video_path":"https://www.youtube.com/embed/HaZH57Q9B18"},
        {"game_name":"Hearthstone","video_path":"https://www.youtube.com/watch?v=HaZH57Q9B18"},
        {"game_name":"OVERWATCH","video_path":"https://www.youtube.com/watch?v=fT-HvMPJvhA"},
        {"game_name":"WORLD OF WARCRFT","video_path":"https://www.youtube.com/watch?v=qnkjIm8uEfE"},
        {"game_name":"Stardew Valley","video_path":"https://www.youtube.com/watch?v=dkYOLIirm5w"},
    ]

    reviews = [
        {"game_name":"ARK:Survival Invovled","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"The Binding of Isaac: Rebirth","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"Don't Starve Together","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"Euro Truck Simulator 2","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"The Forest","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"Hearthstone","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"OVERWATCH","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"Stardew Valley","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
        {"game_name":"WORLD OF WARCRFT","user_name":"czx","number_likes":"2","number_dislikes":"3","text":"good"},
    ]

    users = [
        {"game_name":"ARK:Survival Invovled","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"The Binding of Isaac: Rebirth","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"Don't Starve Together","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"Euro Truck Simulator 2","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"The Forest","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"Hearthstone","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"OVERWATCH","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"Stardew Valley","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
        {"game_name":"WORLD OF WARCRFT","user_name":"czx","user_email":"347748393@gmail.com","user_password":"hdekddj29348","user_picture":"good"},
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
               add_game(game["category"],game["name"],p,game["year_released"],game["game_content"])
    
    for game in Game.objects.all():
        for picture in pictures:
            if picture["game_name"] == game.name:
                add_picture(game,picture["picture_path"])

    for game in Game.objects.all():
        for video in videos:
            if video["game_name"] == game.name:
                add_video(game,video["video_path"])
    
    



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

def add_video(game,path):
    vi = Video.objects.get_or_create(game_name=game,video_path=path)[0]
    vi.save()
    return vi

# Start execution here!
if __name__ == '__main__':
    print("Starting wegame population script...") 
    populate()
