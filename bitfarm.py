import requests
from configparser import RawConfigParser
from threading import Thread
from time import sleep
import json
import requests
import time
def bot():
    requests.packages.urllib3.disable_warnings()

    session = requests.session()
    session.verify = False
    print("Bot initilized, now gathering resouces")
#%5BdeviceId%5D=9bf11bfff37298cc

    init_data = 'data%5Baction%5D=init&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bversion%5D=8&data%5Bdlang%5D=en&data%5Bulang%5D=en'
    buy_water = 'data%5Baction%5D=buy&data%5Bressource%5D=water&data%5Bnum%5D=0&data%5BdeviceId%5D=9bf11bfff37298cc'
    buy_hay = 'data%5Baction%5D=buy&data%5Bressource%5D=hay&data%5Bnum%5D=0&data%5BdeviceId%5D=9bf11bfff37298cc'
    buy_corn = 'data%5Baction%5D=buy&data%5Bressource%5D=corn&data%5Bnum%5D=0&data%5BdeviceId%5D=9bf11bfff37298cc'
    collect_cotton = 'data%5BdeviceId%5D=9bf11bfff37298cc&data%5Baction%5D=collect&data%5Bobj%5D=cotton'
    collect_eggs = 'data%5BdeviceId%5D=9bf11bfff37298cc&data%5Baction%5D=collect&data%5Bobj%5D=egg'
    collect_milk = 'data%5BdeviceId%5D=9bf11bfff37298cc&data%5Baction%5D=collect&data%5Bobj%5D=milk'
    buy_sugar = 'data%5Baction%5D=shopping&data%5Bobj%5D=sugar&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=8'
    buy_strawberries = 'data%5Baction%5D=shopping&data%5Bobj%5D=strawberry&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=5'
    craft_yogurt = 'data%5Baction%5D=craft&data%5Bobj%5D=yogurt&data%5BdeviceId%5D=9bf11bfff37298cc'

    init_headers = {
        "Host": "farmbit.gamevaultstudios.com",
        'Connection': 'keep-alive',
        "Content-Length": "115",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        'Origin': 'file://',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Plus Build/NPN25.137-83) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Crosswalk/17.46.448.10 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-us",
    }

    action__headers = {
        "Host": "farmbit.gamevaultstudios.com",
        'Connection': 'keep-alive',
        "Content-Length": "194",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        'Origin': 'file://',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Plus Build/NPN25.137-83) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Crosswalk/17.46.448.10 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-us",
    }

    action_url = 'http://farmbit.gamevaultstudios.com/private/'
    init_url = 'http://farmbit.gamevaultstudios.com/public/'
    session.post(init_url, headers=init_headers, data=init_data)


    def resources():
        print("Managing resources")
        session.post(action_url, headers=action__headers, data=collect_cotton)
        session.post(action_url, headers=action__headers, data=collect_eggs)
        session.post(action_url, headers=action__headers, data=collect_milk)
        session.post(action_url, headers=action__headers, data=buy_water)
        session.post(action_url, headers=action__headers, data=buy_corn)
        session.post(action_url, headers=action__headers, data=buy_hay)
        time.sleep(50)

    def chickens():

        while True:
            session.post(init_url, headers=init_headers, data=init_data)
            session.post(action_url, headers=action__headers, data=collect_eggs)
            print("Buying suplies for chicken")
            session.post(action_url, headers=action__headers, data=buy_corn)
            session.post(action_url, headers=action__headers, data=buy_water)
            buy_chickens3 = 'data%5Baction%5D=buy&data%5Bobj%5D=chickens3&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_chickens2 = 'data%5Baction%5D=buy&data%5Bobj%5D=chickens2&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_chickens1 = 'data%5Baction%5D=buy&data%5Bobj%5D=chickens1&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_chickens = 'data%5Baction%5D=buy&data%5Bobj%5D=chickens&data%5BdeviceId%5D=9bf11bfff37298cc'
            for i in range(8):
                session.post(action_url, headers=action__headers, data=buy_chickens3)
                session.post(action_url, headers=action__headers, data=buy_chickens2)
                session.post(action_url, headers=action__headers, data=buy_chickens1)
                session.post(action_url, headers=action__headers, data=buy_chickens)
            print("buying chickens")
            time.sleep(200)
            print("selling chicken stuff")



    def cows():

        while True:
            session.post(init_url, headers=init_headers, data=init_data)
            session.post(action_url, headers=action__headers, data=collect_milk)
            print("Buying suplies for cows")
            session.post(action_url, headers=action__headers, data=buy_hay)
            session.post(action_url, headers=action__headers, data=buy_hay)
            session.post(action_url, headers=action__headers, data=buy_water)
            session.post(action_url, headers=action__headers, data=buy_water)
            buy_cows3 = 'data%5Baction%5D=buy&data%5Bobj%5D=cows3&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_cows2 = 'data%5Baction%5D=buy&data%5Bobj%5D=cows2&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_cows1 = 'data%5Baction%5D=buy&data%5Bobj%5D=cows1&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_cows = 'data%5Baction%5D=buy&data%5Bobj%5D=cows&data%5BdeviceId%5D=9bf11bfff37298cc'

            for i in range(10):
                session.post(action_url, headers=action__headers, data=buy_cows3)
                session.post(action_url, headers=action__headers, data=buy_cows2)
                session.post(action_url, headers=action__headers, data=buy_cows1)
                session.post(action_url, headers=action__headers, data=buy_cows)
            print("buying cows")
            time.sleep(950)



    def sheeps():
        while True:
            session.post(init_url, headers=init_headers, data=init_data)
            session.post(action_url, headers=action__headers, data=collect_cotton)
            print("Buying suplies for sheep")
            session.post(action_url, headers=action__headers, data=buy_hay)
            session.post(action_url, headers=action__headers, data=buy_water)
            session.post(action_url, headers=action__headers, data=buy_hay)
            session.post(action_url, headers=action__headers, data=buy_water)
            print("Buying new Sheep ")
            buy_sheeps3 = 'data%5Baction%5D=buy&data%5Bobj%5D=sheeps3&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_sheeps2 = 'data%5Baction%5D=buy&data%5Bobj%5D=sheeps2&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_sheeps1 = 'data%5Baction%5D=buy&data%5Bobj%5D=sheeps1&data%5BdeviceId%5D=9bf11bfff37298cc'
            buy_sheeps = 'data%5Baction%5D=buy&data%5Bobj%5D=sheeps&data%5BdeviceId%5D=9bf11bfff37298cc'
            for i in range(14):
                session.post(action_url, headers=action__headers, data=buy_sheeps3)
                session.post(action_url, headers=action__headers, data=buy_sheeps2)
                session.post(action_url, headers=action__headers, data=buy_sheeps1)
                session.post(action_url, headers=action__headers, data=buy_sheeps)
            print("buying sheeps")
            time.sleep(380)

    def yogurt():
        while True:
            session.post(action_url, headers=action__headers, data=collect_cotton)
            session.post(action_url, headers=action__headers, data=collect_eggs)
            session.post(action_url, headers=action__headers, data=collect_milk)

            response = session.post(init_url, headers=init_headers, data=init_data)
            json_data = json.loads(response.text)
            print("selling Cotton and Eggs")
            sell_cotton = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=1000&data%5BdeviceId%5D=9bf11bfff37298cc'
            #sell_cotton = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + json_data["products"]['cotton'][0] + '&data%5BdeviceId%5D=9bf11bfff37298cc'
            sell_eggs = 'data%5Baction%5D=sell&data%5Bobj%5D=egg&data%5Bnumber%5D=1000&data%5BdeviceId%5D=9bf11bfff37298cc'
            #sell_eggs = 'data%5Baction%5D=sell&data%5Bobj%5D=egg&data%5Bnumber%5D=372&data%5BdeviceId%5D=9bf11bfff37298cc'
            sell_milk = 'data%5Baction%5D=sell&data%5Bobj%5D=milk&data%5Bnumber%5D=400&data%5BdeviceId%5D=9bf11bfff37298cc'
            print("Milk Quantity: " + json_data["products"]['milk'][0])
            milking = float(json_data["products"]['milk'][0])

            if int(float(json_data["products"]['cotton'][0])) > 2000:
                session.post(action_url, headers=action__headers, data=sell_cotton)
            if int(float(json_data["products"]['egg'][0])) > 2000:
                session.post(action_url, headers=action__headers, data=sell_eggs)

            print(json_data["userShopObj"])
            coins = json_data["coins"]
            if int(coins) >= 1000 and int(milking) >= 180:
                print('Making Yogurt :D, buying supplies')
            for i in range(5):
                session.post(action_url, headers=action__headers, data=buy_sugar)
                session.post(action_url, headers=action__headers, data=buy_strawberries)
                print("crafting yogurt")
            for i in range(5):
                    session.post(action_url, headers=action__headers, data=craft_yogurt)
            time.sleep(250)

    def bitcoin():
        while True:
            session.post(action_url, headers=action__headers, data=collect_cotton)
            session.post(action_url, headers=action__headers, data=collect_eggs)
            session.post(action_url, headers=action__headers, data=collect_milk)

            response = session.post(init_url, headers=init_headers, data=init_data)
            json_data = json.loads(response.text)
            print("selling Cotton and Eggs")
            #sell_cotton = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=1000&data%5BdeviceId%5D=9bf11bfff37298cc'
            sell_cotton = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + json_data["products"]['cotton'][0] + '&data%5BdeviceId%5D=9bf11bfff37298cc'
            #sell_eggs = 'data%5Baction%5D=sell&data%5Bobj%5D=egg&data%5Bnumber%5D=1000&data%5BdeviceId%5D=9bf11bfff37298cc'
            #sell_eggs = 'data%5Baction%5D=sell&data%5Bobj%5D=egg&data%5Bnumber%5D=372&data%5BdeviceId%5D=9bf11bfff37298cc'
            #sell_milk = 'data%5Baction%5D=sell&data%5Bobj%5D=milk&data%5Bnumber%5D=400&data%5BdeviceId%5D=9bf11bfff37298cc'
            print("Milk Quantity: " + json_data["products"]['milk'][0])
            print("Egg Quantity: " + json_data["products"]['egg'][0])
            milking = float(json_data["products"]['milk'][0])
            eqq_quantity = float(json_data["products"]['egg'][0])
            #if int(float(json_data["products"]['cotton'][0])) > 2000:
            session.post(action_url, headers=action__headers, data=sell_cotton)
            #if int(float(json_data["products"]['egg'][0])) > 2000:
            #    session.post(action_url, headers=action__headers, data=sell_eggs)

            print(json_data["userShopObj"])
            coins = json_data["coins"]
            if int(milking) >= 7500 and int(coins) >= 12500 and int(eqq_quantity) >= 4000:
                    print('Making Chantily creams :D, buying supplies')
                    session.post(action_url, headers=action__headers, data=buy_sugar)
                    print("crafting cream")
                    for i in range(500):
                        session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=chantilly cream&data%5BdeviceId%5D=9bf11bfff37298cc')
                        time.sleep(1)

            time.sleep(20)

    def dough(dough_amount):
        print('Making Doughs: ' + str(dough_amount))
        donedough = 0
        for i in range(dough_amount):
            session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=oil&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=6')
            session.post(action_url, headers=action__headers, data=buy_water)
            session.post(action_url, headers=action__headers, data=buy_corn)
            session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=dough&data%5BdeviceId%5D=9bf11bfff37298cc')
            donedough += 1
            print("Made " + str(donedough) + "/" + str(dough_amount) + 'dough')


    def cheese(cheese_amount):
        print('Making cheese: ' + str(cheese_amount))
        for i in range(cheese_amount):
            session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=oil&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=5')
            session.post(action_url, headers=action__headers, data=buy_water)
            session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=cheese&data%5BdeviceId%5D=9bf11bfff37298cc')

    def level():
        while True:
            levelup = session.post(init_url, headers=init_headers, data=init_data)
            levelup_data = json.loads(levelup.text)
            collections = levelup_data['achivement']['sell']
            print(collections)

            def cereal():
                cereal = levelup_data['achivement']['sell']['cereal']
                print(levelup_data['achivement']['sell']['cereal'])
                for i in range(0):
                    session.post(action_url, headers=action__headers, data=buy_corn)
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=sugar&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=10')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=honey&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=6')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=cereal&data%5BdeviceId%5D=9bf11bfff37298cc')
                    print("crafted a cereal")
                sell_cereal = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + str(cereal) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
                session.post(action_url, headers=action__headers, data=sell_cereal)


            def spaghetti():
                spaghetti = levelup_data['achivement']['sell']['spaghetti']
                print(levelup_data['achivement']['sell']['spaghetti'])
                for i in range(spaghetti):
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=salt&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=6')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=meat&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=15')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=tomato&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=20')
                    dough_amount = 25
                    dough(dough_amount)
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=spaghetti&data%5BdeviceId%5D=9bf11bfff37298cc')
                    print("crafted a spaghetti")
                sell_spaghetti = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + str(spaghetti) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
                session.post(action_url, headers=action__headers, data=sell_spaghetti)


            def bread():
                bread = levelup_data['achivement']['sell']['bread']
                print(levelup_data['achivement']['sell']['bread'])
                for i in range(bread):
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=salt&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=15')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=butter&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=3')
                    dough_amount = 26
                    dough(dough_amount)
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=bread&data%5BdeviceId%5D=9bf11bfff37298cc')
                    print("crafted a bread")
                sell_bread = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + str(bread) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
                session.post(action_url, headers=action__headers, data=sell_bread)

            def suchi():
                suchi = levelup_data['achivement']['sell']['suchi']
                print(levelup_data['achivement']['sell']['suchi'])
                for i in range(suchi):
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=salt&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=15')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=butter&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=3')
                    cheese_amount = 26
                    dough(cheese_amount)
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=suchi&data%5BdeviceId%5D=9bf11bfff37298cc')
                    print("crafted a suchi")
                sell_suchi = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + str(suchi) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
                session.post(action_url, headers=action__headers, data=sell_suchi)


            def chantilly_cream():
                chantilly_cream = levelup_data['achivement']['sell']['chantilly cream']
                print(levelup_data['achivement']['sell']['chantilly cream'])
                for i in range(chantilly_cream):
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=sugar&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=5')
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=chantilly cream&data%5BdeviceId%5D=9bf11bfff37298cc')
                    print("crafted a chantily cream")
                sell_chantilly_cream = 'data%5Baction%5D=sell&data%5Bobj%5D=chantilly cream&data%5Bnumber%5D=' + str(chantilly_cream) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
                session.post(action_url, headers=action__headers, data=sell_chantilly_cream)

            def cream():
                cream = levelup_data['achivement']['sell']['cream']
                print(levelup_data['achivement']['sell']['cream'])
                for i in range(cream):
                    session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=cream&data%5BdeviceId%5D=9bf11bfff37298cc')
                    print("crafted a cream")
                sell_cream = 'data%5Baction%5D=sell&data%5Bobj%5D=cotton&data%5Bnumber%5D=' + str(cream) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
                session.post(action_url, headers=action__headers, data=sell_cream)

            if 'cheese' in collections:
                Thread(target=cheese(levelup_data['achivement']['sell']['cheese'])).start()

            if 'dough' in collections:
                Thread(target=cheese(levelup_data['achivement']['sell']['dough'])).start()
            if 'chantilly cream' in collections:
                Thread(target=chantilly_cream).start()

            if 'cream' in collections:
                Thread(target=cream).start()

            if 'suchi' in collections:
                Thread(target=suchi).start()

            if "cereal" in collections:
                Thread(target=cereal).start()
            if "spaghetti" in collections:
                Thread(target=spaghetti).start()
            if "bread" in collections:
                Thread(target=bread).start()

            time.sleep(380)

    def chantilly_cream():
        #chantilly_cream = levelup_data['achivement']['sell']['chantilly cream']
        chantilly_cream = 10000
       # print(levelup_data['achivement']['sell']['chantilly cream'])
        print('Making Chantilly Creams: ' + str(chantilly_cream))
        donecream = 0
        for i in range(chantilly_cream):
            session.post(action_url, headers=action__headers, data='data%5Baction%5D=shopping&data%5Bobj%5D=sugar&data%5BdeviceId%5D=9bf11bfff37298cc&data%5Bnumber%5D=5')
            session.post(action_url, headers=action__headers, data='data%5Baction%5D=craft&data%5Bobj%5D=chantilly cream&data%5BdeviceId%5D=9bf11bfff37298cc')
            print("crafted a chantily cream")
            donecream += 1
            print("Made " + str(donecream) + "/" + str(chantilly_cream) + ' creams')
        sell_chantilly_cream = 'data%5Baction%5D=sell&data%5Bobj%5D=chantilly cream&data%5Bnumber%5D=' + str(chantilly_cream) + '&data%5BdeviceId%5D=9bf11bfff37298cc'
        #session.post(action_url, headers=action__headers, data=sell_chantilly_cream)

    Thread(target=chickens).start()
    Thread(target=sheeps).start()

    Thread(target=cows).start()
    Thread(target=resources).start()
    Thread(target=yogurt).start()
    #Thread(target=level).start()
    #Thread(target=bitcoin()).start()
   # Thread(target=chantilly_cream()).start()

print('running app')

if __name__ == "__main__":
    bot()
