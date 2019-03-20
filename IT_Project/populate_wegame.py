import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'IT_Project.settings')
import django
django.setup()
from WeGame.models import Publisher,Game,Picture,Review,Video
from accounts.models import CustomUser
from PIL import Image

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
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic1.jpg"},
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic2.jpg"},
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic3.jpg"},
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic4.jpg"},
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic5.jpg"},
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic6.jpg"},
        {"game_name":"WORLD OF WARCRAFT","picture_path":"/media/game-pic/WOW-pic/pic7.jpg"},
    ]

    games = [
        {"category":"Survival","name":"ARK:Survival Invovled","publisher_name":"Studio WildCard","year_released":"2017-08-27","game_content":"good game", "image": "/static/home-pic/ARK.jpeg"},
        {"category":"Cosplay","name":"Stardew Valley","publisher_name":"ConcernedApe","year_released":"2016-02-16","game_content":"good game", "image": "/static/home-pic/stardew-valley.png"},
        {"category":"Indie","name":"The Binding of Isaac: Rebirth","publisher_name":"Nicalis, Inc.","year_released":"2014-11-04","game_content":"good game", "image": "/static/home-pic/the-binding-of-isaac.png"},
        {"category":"Survival","name":"Don't Starve Together","publisher_name":"Klei Entertainment","year_released":"2016-04-21","game_content":"good game", "image": "/static/home-pic/starve.jpeg"},
        {"category":"Simulation","name":"Euro Truck Simulator 2","publisher_name":"SCS Software","year_released":"2012-10-12","game_content":"good game", "image": "/static/home-pic/EU-truck.jpg"},
        {"category":"Survival","name":"The Forest","publisher_name":"Endnight Games Ltd","year_released":"2018-04-30","game_content":"good game", "image": "/static/home-pic/the-forest.jpg"},
        {"category":"Cosplay","name":"OVERWATCH","publisher_name":"Blizzard Entertainment","year_released":"1991-02-22","game_content":"good game", "image": "/static/home-pic/overwatch.jpeg"},
        {"category":"Cospaly","name":"WORLD OF WARCRAFT","publisher_name":"Blizzard Entertainment","year_released":"1991-02-19","game_content":"good game", "image": "/static/home-pic/WoW.jpg"},
        {"category":"Card","name":"Hearthstone","publisher_name":"Blizzard Entertainment","year_released":"1991-02-05","game_content":"good game", "image": "/static/home-pic/Hearthstone.jpg"},
    ]
    
    videos = [
        {"game_name":"ARK:Survival Invovled","video_path":"https://www.youtube.com/embed/E9Wb_zRnJek"},
        {"game_name":"The Binding of Isaac: Rebirth","video_path":"https://www.youtube.com/embed/DALFKiVsoDk"},
        {"game_name":"Don't Starve Together","video_path":"https://www.youtube.com/embed/k3fUJpDXxs"},
        {"game_name":"Euro Truck Simulator 2","video_path":"https://www.youtube.com/embed/2bfVnhxFvfQ"},
        {"game_name":"The Forest","video_path":"https://www.youtube.com/embed/FM28K6ABbQs"},
        {"game_name":"Hearthstone","video_path":"https://www.youtube.com/embed/HaZH57Q9B18"},
        {"game_name":"OVERWATCH","video_path":"https://www.youtube.com/embed/fT-HvMPJvhA"},
        {"game_name":"WORLD OF WARCRAFT","video_path":"https://www.youtube.com/embed/qnkjIm8uEfE"},
        {"game_name":"Stardew Valley","video_path":"https://www.youtube.com/embed/dkYOLIirm5w"},
    ]

    reviews = [
        {"game_name":"ARK:Survival Invovled","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"Ark’s lofty ambitions and 3D graphics make for a demanding game that can make your battery beg for mercy. Assuming that your device isn’t too prehistoric (the last couple of generations only need apply) then you can download and begin playing for free. "},
        {"game_name":"The Binding of Isaac: Rebirth","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"The Binding of Isaac is the reference for the rogue-like genre - even if you already know the old Isaac inside out."},
        {"game_name":"Don't Starve Together","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"Don’t Starve Together is a multiplayer strategy sandbox game where every action a player makes can affect the player’s future. "},
        {"game_name":"Euro Truck Simulator 2","username":"GerardoAragonCamarasa","number_likes":"2","number_dislikes":"3","text":"A surprising truly well-done simulation that puts you behind a truck letting you enjoy discovering and exploring Europe."},
        {"game_name":"The Forest","username":"GerardoAragonCamarasa","number_likes":"2","number_dislikes":"3","text":"The Forest frequently flirts with perfection. A fantastic and engrossing survival-horror experience from start to finish."},
        {"game_name":"Hearthstone","username":"GerardoAragonCamarasa","number_likes":"2","number_dislikes":"3","text":"Hearthstone, the newest card game from Blizzard, will keep you hooked for hours thanks to the amazing presentation and the tactical, deep gameplay. This is free to play done right."},
        {"game_name":"OVERWATCH","username":"KevinKengne","number_likes":"2","number_dislikes":"3","text":"Easily one of the best multiplayer first person shooters. Vastly better than Team Fortress 2, which i used to play in the past."},
        {"game_name":"Stardew Valley","username":"KevinKengne","number_likes":"2","number_dislikes":"3","text":"The charming RPG Stardew Valley is so much more than just another farming simulator and feels right at home on the Switch."},
        {"game_name":"WORLD OF WARCRAFT","username":"KevinKengne","number_likes":"2","number_dislikes":"3","text":"Battle of Azeroth isn’t as good as Legion was. But the Horde vs Alliance conflict is stronger than ever, and being part of this big conflict is pure fun. Veterans will enjoy HL content and how the lore is constantly used."},
        {"game_name":"ARK:Survival Invovled","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"The developers state that it is possible to obtain every available structure, item and enhancement without having to spend any money. Free gifts pop up every couple of hours that can be redeemed by watching ads."},
        {"game_name":"The Binding of Isaac: Rebirth","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"Crazier, funnier and bigger. Rebirth is a proper rebuilt of one of the most brilliant games we've enjoyed lately. There are a handful of new features and probably even more content than we could've asked for, even though die-hard fans might consider rebuying a game that's very much the same, but widely expanded."},
        {"game_name":"Don't Starve Together","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"Don't Starve Together does little to fix the original's glaring problems, but still, conquering the wilderness together with friends is a lot of fun."},
        {"game_name":"Euro Truck Simulator 2","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"A surprising truly well-done simulation that puts you behind a truck letting you enjoy discovering and exploring Europe."},
        {"game_name":"The Forest","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"The Forest is an awkward open-world survival game. It's thrilling to play because of the intense atmosphere, but confusing maps and annoying enemies make it really hard for me to immerse into the game."},
        {"game_name":"Hearthstone","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"Between its friendly design and its flexible approach to a free-to-play economy, Hearthstone has successfully pulled me into a genre that I didn't care about in the least. But even more incredibly, it's kept me rapt longer than any games I've played in years, and shows no signs of letting up."},
        {"game_name":"OVERWATCH","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"A gaming experience that’s more polished and exciting than I have ever had the pleasure of experiencing and one I’ll be sure to continue to play for the foreseeable future. If not for the inclusion of microtransactions, this would have been a perfect game in my book."},
        {"game_name":"Stardew Valley","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"The charming RPG Stardew Valley is so much more than just another farming simulator and feels right at home on the Switch."},
        {"game_name":"WORLD OF WARCRAFT","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"Battle for Azeroth, despite the endless grind, has been an exciting expansion this far. However, raids and additional content are what makes the game great. Blizzard has made the entry level into the new expansion welcoming for new players and some die-hard critics have shared their concerns with the current direction Blizzard are going with making the gaming “easier.”"},
    ]

    users = [
        {"username":"EllisonZhang","password":"hdekddj29348","photo":"/static/leopard.jpg"},
        {"username":"Nelson","password":"hdekddj29348","photo":"/static/antilope.jpg"},
        {"username":"EdmundKuras","password":"hdekddj29348","photo":"/static/zebra.jpg"},
        {"username":"KevinKengne","password":"hdekddj29348","photo":"/static/tigre.jpg"},
        {"username":"GerardoAragonCamarasa","password":"hdekddj29348","photo":"/static/elephant.jpg"},
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
               add_game(game["category"],game["name"],p,game["year_released"],game["game_content"], game["image"])
    
    for game in Game.objects.all():
        for picture in pictures:
            if picture["game_name"] == game.name:
                add_picture(game,picture["picture_path"])

    for game in Game.objects.all():
        for video in videos:
            if video["game_name"] == game.name:
                add_video(game,video["video_path"])
    
    for user in users:
        add_user(user["username"], user["password"], user["photo"])
    
    for game in Game.objects.all():
        for user in CustomUser.objects.all():
            for review in reviews:
                if review["username"] == user.username and game.name == review["game_name"]:
                    add_review(game, user, review["number_likes"], review["number_dislikes"], review["text"])


def add_publisher(publisher,country):
    p = Publisher.objects.get_or_create(name=publisher,country=country)[0]
    p.save()
    return p

def add_game(category,name,publisher,year_released,game_content, game_image):
    g = Game.objects.get_or_create(category=category,name=name,
    publisher_name=publisher,year_released=year_released,game_content=game_content, image=game_image)[0]
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

def add_user(user_name, pass_word, pho_to):
    u = CustomUser.objects.get_or_create(username=user_name, password=pass_word,photo=pho_to)[0]
    u.save()
    return u

def add_review(game, user_used, numlikes, numdislikes, text):
    r = Review.objects.get_or_create(number_likes=numlikes, number_dislikes=numdislikes, comment_text=text, game_reviewed=game, user=user_used)[0]
    r.save()
    return r

# Start execution here!
if __name__ == '__main__':
    print("Starting wegame population script...") 
    populate()
