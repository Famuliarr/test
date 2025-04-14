import random

def music_recommendation():
    genres = {
        1: "рок", 
        2: "поп", 
        3: "электроника", 
        4: "джаз", 
        5: "классика"
    }
    moods = {
        1: "весёлое", 
        2: "грустное", 
        3: "расслабляющее", 
        4: "энергичное"
    }
    artists = {
        "рок": ["Queen", "The Beatles", "Nirvana"],
        "поп": ["Taylor Swift", "Ariana Grande", "Ed Sheeran"],
        "электроника": ["Daft Punk", "The Chemical Brothers", "Deadmau5"],
        "джаз": ["Louis Armstrong", "Miles Davis", "Ella Fitzgerald"],
        "классика": ["Mozart", "Beethoven", "Chopin"]
    }
    
    print("\nРекомендация музыки:")
    print("1 - Выбрать по жанру")
    print("2 - Выбрать по настроению")
    
    while True:
        choice_type = input("Ваш выбор (1-2): ")
        if choice_type in ["1", "2"]:
            break
        print("Пожалуйста, введите 1 или 2")
    
    if choice_type == "1":
        print("\nВыберите жанр:")
        for num, genre in genres.items():
            print(f"{num} - {genre}")
        
        while True:
            choice = input("Введите номер жанра (1-5): ")
            if choice in ["1", "2", "3", "4", "5"]:
                genre = genres[int(choice)]
                rec = random.choice(artists[genre])
                print(f"\nРекомендуем исполнителя: {rec}")
                break
            print("Пожалуйста, введите число от 1 до 5")
    
    else:
        print("\nВыберите настроение:")
        for num, mood in moods.items():
            print(f"{num} - {mood}")
        
        while True:
            choice = input("Введите номер настроения (1-4): ")
            if choice in ["1", "2", "3", "4"]:
                mood = moods[int(choice)]
                if mood == "весёлое":
                    rec = random.choice(artists["поп"] + artists["электроника"])
                elif mood == "грустное":
                    rec = random.choice(artists["джаз"] + artists["классика"])
                elif mood == "расслабляющее":
                    rec = random.choice(artists["джаз"] + artists["классика"])
                else:  # энергичное
                    rec = random.choice(artists["рок"] + artists["электроника"])
                print(f"\nРекомендуем исполнителя для настроения '{mood}': {rec}")
                break
            print("Пожалуйста, введите число от 1 до 4")

def mood_community():
    communities = {
        1: ("весёлое", "Радостные меломаны"),
        2: ("грустное", "Грустные романтики"),
        3: ("расслабляющее", "Чилл-сообщество"),
        4: ("энергичное", "Энергия музыки")
    }
    
    print("\nСообщество по настроению:")
    for num, (mood, community) in communities.items():
        print(f"{num} - {mood}")
    
    while True:
        choice = input("Введите номер настроения (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            mood, community = communities[int(choice)]
            print(f"\nРекомендуем сообщество: {community}")
            break
        print("Пожалуйста, введите число от 1 до 4")

def main():
    print("Текстовый бот-помощник")
    
    while True:
        print("\n1 - Рекомендация музыки")
        print("2 - Сообщество по настроению")
        print("0 - Выход")
        
        while True:
            choice = input("Выберите действие (0-2): ")
            if choice in ["0", "1", "2"]:
                break
            print("Пожалуйста, введите 0, 1 или 2")
        
        if choice == "1":
            music_recommendation()
        elif choice == "2":
            mood_community()
        else:
            print("До свидания!")
            break

if __name__ == "__main__":
    main()