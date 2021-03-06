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
                "Ubisoft":"United States",
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
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic1.jpg"},
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic2.jpg"},
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic3.jpg"},
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic4.jpg"},
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic5.jpg"},
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic6.jpg"},
        {"game_name":"Assassin's Creed Origins","picture_path":"/media/game-pic/Assassin's-Creed-pic/pic7.jpg"},

    ]

    games = [
        {"category":"Survival","name":"ARK:Survival Invovled","publisher_name":"Studio WildCard","year_released":"2017-08-27","game_content":"Stranded on the shores of a mysterious island, you must learn to survive. Use your cunning to kill or tame the primeval creatures roaming the land, and encounter other players to survive, dominate... and escape!", "image": "/static/home-pic/ARK.jpeg"},
        {"category":"RPG","name":"Stardew Valley","publisher_name":"ConcernedApe","year_released":"2016-02-16","game_content":"You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home?", "image": "/static/home-pic/stardew-valley.png"},
        {"category":"Indie","name":"The Binding of Isaac: Rebirth","publisher_name":"Nicalis, Inc.","year_released":"2014-11-04","game_content":"The Binding of Isaac: Rebirth is a randomly generated action RPG shooter with heavy Rogue-like elements. Following Isaac on his journey players will find bizarre treasures that change Isaac’s form giving him super human abilities and enabling him to fight off droves of mysterious creatures, discover secrets ", "image": "/static/home-pic/the-binding-of-isaac.png"},
        {"category":"Survival","name":"Don't Starve Together","publisher_name":"Klei Entertainment","year_released":"2016-04-21","game_content":"Don't Starve Together is the standalone multiplayer expansion of the uncompromising survival game Don't Starve.", "image": "/static/home-pic/starve.jpeg"},
        {"category":"Simulation","name":"Euro Truck Simulator 2","publisher_name":"SCS Software","year_released":"2012-10-12","game_content":"Travel across Europe as king of the road, a trucker who delivers important cargo across impressive distances! With dozens of cities to explore from the UK, Belgium, Germany, Italy, the Netherlands, Poland, and many more, your endurance, skill and speed will all be pushed to their limits.", "image": "/static/home-pic/EU-truck.jpg"},
        {"category":"Survival","name":"The Forest","publisher_name":"Endnight Games Ltd","year_released":"2018-04-30","game_content":"As the lone survivor of a passenger jet crash, you find yourself in a mysterious forest battling to stay alive against a society of cannibalistic mutants. Build, explore, survive in this terrifying first person survival horror simulator.", "image": "/static/home-pic/the-forest.jpg"},
        {"category":"RPG","name":"OVERWATCH","publisher_name":"Blizzard Entertainment","year_released":"1991-02-22","game_content":"In Overwatch, you control one of several heroes in competitive 6-person team shooting matches. Battle over objectives, take down the other team, and achieve victory.", "image": "/static/home-pic/overwatch.jpeg"},
        {"category":"RPG","name":"WORLD OF WARCRAFT","publisher_name":"Blizzard Entertainment","year_released":"1991-02-19","game_content":"Check out Battle for Azeroth's dedicated website and discover what the future holds for World of Warcraft including new features, gameplay, story, and more!", "image": "/static/home-pic/WoW.jpg"},
        {"category":"Card","name":"Hearthstone","publisher_name":"Blizzard Entertainment","year_released":"1991-02-05","game_content":"Hearthstone is a free-to-play online digital collectible card game developed and published by Blizzard Entertainment. Originally subtitled Heroes of Warcraft, Hearthstone builds upon the existing lore of the Warcraft series by using the same elements, characters, and relics.", "image": "/static/home-pic/Hearthstone.jpg"},
        {"category":"RPG","name":"Assassin's Creed Origins","publisher_name":"Ubisoft","year_released":"2007-11-13","game_content":"The game is set in Ancient Egypt near the end of the Ptolemaic period (49–47 BCE) and recounts the secret fictional history of real-world events.", "image": "/static/home-pic/Assassin-Creed.jpeg"},
    ]
    
    videos = [
        {"game_name":"ARK:Survival Invovled","video_path":"https://www.youtube.com/embed/E9Wb_zRnJek","video_infor_pic_path":"/media/game-pic/Ark-pic/video.jpg"},
        {"game_name":"The Binding of Isaac: Rebirth","video_path":"https://www.youtube.com/embed/DALFKiVsoDk","video_infor_pic_path":"/media/game-pic/Binding-Of-Isaac-pic/video.jpg"},
        {"game_name":"Don't Starve Together","video_path":"https://www.youtube.com/embed/k3fUJpDXxs","video_infor_pic_path":"/media/game-pic/Dont-Starve-pic/video.jpg"},
        {"game_name":"Euro Truck Simulator 2","video_path":"https://www.youtube.com/embed/2bfVnhxFvfQ","video_infor_pic_path":"/media/game-pic/EU-Truck-pic/video.jpg"},
        {"game_name":"The Forest","video_path":"https://www.youtube.com/embed/FM28K6ABbQs","video_infor_pic_path":"/media/game-pic/Forest-pic/video.jpg"},
        {"game_name":"Hearthstone","video_path":"https://www.youtube.com/embed/HaZH57Q9B18","video_infor_pic_path":"/media/game-pic/Hearthstone-pic/video.jpg"},
        {"game_name":"OVERWATCH","video_path":"https://www.youtube.com/embed/fT-HvMPJvhA","video_infor_pic_path":"/media/game-pic/Overwatch-pic/video.png"},
        {"game_name":"WORLD OF WARCRAFT","video_path":"https://www.youtube.com/embed/qnkjIm8uEfE","video_infor_pic_path":"/media/game-pic/WOW-pic/video.jpg"},
        {"game_name":"Stardew Valley","video_path":"https://www.youtube.com/embed/dkYOLIirm5w","video_infor_pic_path":"/media/game-pic/Stardewvalley-pic/video.png"},
        {"game_name":"Assassin's Creed Origins","video_path":"https://www.youtube.com/embed/cK4iAjzAoas","video_infor_pic_path":"/media/game-pic/Assassin's-Creed-pic/video.jpg"},
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
        {"game_name":"Assassin's Creed Origins","username":"Nelson","number_likes":"4","number_dislikes":"1","text":"Show off your extraordinary warrior abilities and shift the tides of battle during one of the deadliest conflicts of the time, the Peloponnesian War. Charge into epic clashes between Sparta and Athens in big battles pitting 150 vs. 150 soldiers against each other."},
        {"game_name":"ARK:Survival Invovled","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"The developers state that it is possible to obtain every available structure, item and enhancement without having to spend any money. Free gifts pop up every couple of hours that can be redeemed by watching ads."},
        {"game_name":"The Binding of Isaac: Rebirth","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"Crazier, funnier and bigger. Rebirth is a proper rebuilt of one of the most brilliant games we've enjoyed lately. There are a handful of new features and probably even more content than we could've asked for, even though die-hard fans might consider rebuying a game that's very much the same, but widely expanded."},
        {"game_name":"Don't Starve Together","username":"EdmundKuras","number_likes":"2","number_dislikes":"3","text":"Don't Starve Together does little to fix the original's glaring problems, but still, conquering the wilderness together with friends is a lot of fun."},
        {"game_name":"Euro Truck Simulator 2","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"A surprising truly well-done simulation that puts you behind a truck letting you enjoy discovering and exploring Europe."},
        {"game_name":"The Forest","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"The Forest is an awkward open-world survival game. It's thrilling to play because of the intense atmosphere, but confusing maps and annoying enemies make it really hard for me to immerse into the game."},
        {"game_name":"Hearthstone","username":"Nelson","number_likes":"2","number_dislikes":"3","text":"Between its friendly design and its flexible approach to a free-to-play economy, Hearthstone has successfully pulled me into a genre that I didn't care about in the least. But even more incredibly, it's kept me rapt longer than any games I've played in years, and shows no signs of letting up."},
        {"game_name":"OVERWATCH","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"A gaming experience that’s more polished and exciting than I have ever had the pleasure of experiencing and one I’ll be sure to continue to play for the foreseeable future. If not for the inclusion of microtransactions, this would have been a perfect game in my book."},
        {"game_name":"Stardew Valley","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"The charming RPG Stardew Valley is so much more than just another farming simulator and feels right at home on the Switch."},
        {"game_name":"WORLD OF WARCRAFT","username":"EllisonZhang","number_likes":"2","number_dislikes":"3","text":"Battle for Azeroth, despite the endless grind, has been an exciting expansion this far. However, raids and additional content are what makes the game great. Blizzard has made the entry level into the new expansion welcoming for new players and some die-hard critics have shared their concerns with the current direction Blizzard are going with making the gaming “easier.”"},
        {"game_name":"Assassin's Creed Origins","username":"EllisonZhang","number_likes":"3","number_dislikes":"2","text":"Discover a world rich with myths and legends. From ancient rituals to famed statues, come face to face with Greece's legendary figures and discover the true nature of its most daunting mythological beasts."},
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
                add_video(game,video["video_path"],video["video_infor_pic_path"])
    
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

def add_video(game,path,infor_pic):
    vi = Video.objects.get_or_create(game_name=game,video_path=path,video_infor_pic_path=infor_pic)[0]
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
