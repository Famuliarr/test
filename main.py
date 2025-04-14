import random

def music_recommendation():
    genres = ["рок", "поп", "электроника", "джаз", "классика"]
    moods = ["весёлое", "грустное", "расслабляющее", "энергичное"]
    artists = {
        "рок": ["Queen", "The Beatles", "Nirvana"],
        "поп": ["Taylor Swift", "Ariana Grande", "Ed Sheeran"],
        "электроника": ["Daft Punk", "The Chemical Brothers", "Deadmau5"],
        "джаз": ["Louis Armstrong", "Miles Davis", "Ella Fitzgerald"],
        "классика": ["Mozart", "Beethoven", "Chopin"]
    }
    
    print("\nРекомендация музыки:")
    print("Выберите жанр или настроение")
    print("Доступные жанры:", ", ".join(genres))
    print("Доступные настроения:", ", ".join(moods))
    
    choice = input("Ваш выбор: ").lower()
    
    if choice in genres:
        rec = random.choice(artists[choice])
        print(f"Рекомендуем исполнителя: {rec}")
    elif choice in moods:
        if choice == "весёлое":
            rec = random.choice(artists["поп"] + artists["электроника"])
        elif choice == "грустное":
            rec = random.choice(artists["джаз"] + artists["классика"])
        elif choice == "расслабляющее":
            rec = random.choice(artists["джаз"] + artists["классика"])
        else:  # энергичное
            rec = random.choice(artists["рок"] + artists["электроника"])
        print(f"Рекомендуем исполнителя для {choice} настроения: {rec}")
    else:
        print("Не удалось распознать ваш выбор")

def mood_community():
    communities = {
        "весёлое": "Радостные меломаны",
        "грустное": "Грустные романтики",
        "расслабляющее": "Чилл-сообщество",
        "энергичное": "Энергия музыки"
    }
    
    print("\nСообщество по настроению:")
    print("Доступные варианты:", ", ".join(communities.keys()))
    
    choice = input("Выберите настроение: ").lower()
    
    if choice in communities:
        print(f"Рекомендуем сообщество: {communities[choice]}")
    else:
        print("Не удалось распознать ваш выбор")

def main():
    print("Текстовый бот-помощник")
    
    while True:
        print("\n1 — Рекомендация музыки")
        print("2 — Сообщество по настроению")
        print("0 — Выход")
        
        choice = input("Выберите действие (0-2): ")
        
        if choice == "1":
            music_recommendation()
        elif choice == "2":
            mood_community()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Пожалуйста, выберите 0, 1 или 2")

if __name__ == "__main__":
    main()