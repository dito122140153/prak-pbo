import random

def log_init_and_exit(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        result = func(*args, **kwargs)
        return result
    return wrapper

def log_destructor(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        result = func(*args, **kwargs)
        return result
    return wrapper

class GachaHSR:
    def __init__(self):
        self.chara = ["Black Swan", "Sparkle", "Acheron", "Aventurine", "KING YUAN","March 7th","Tingyun","Argenti","Arlan","Asta","Bailu","Blade","Bronya","Clara","DanHeng","DanHeng IL","Fu Xuan","Dr. Ratio","Gallagher","Gepard","Guinaifen","Hanya","Herta","Himeko","BOKEM","HuoHuo","Jingliu","Kafka","Luka","Luocha","Lynx","Misha","Natasha","Pela","Qingque","Ruan Mei","Sampo","Seele","Serval","Silver Wolf","Sushang","Topaz And Numby","Welt","Xueyi","Yangqing","Yukong"]
        print(f"Special Banner created.")

    @log_init_and_exit
    def pull(self):
        item = random.choice(self.chara)
        print(f"Starting to pull: {item}")
        return item

    @log_destructor
    def __del__(self):
        print(f"Banner duration ended.")

gacha_machine = GachaHSR()

num_pulls = int(input("Enter the number of pulls: "))

for _ in range(num_pulls):
    result = gacha_machine.pull()

