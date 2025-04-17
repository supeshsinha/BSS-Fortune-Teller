# Name: Supesh Kumar Sinha
# Adm No: 21JE0969
import random

def predict(mood):

    fortunes = {
        "happy": [
            "Supesh's Fortune predictor: Happiness opens doors — today, one will swing wide for you!",
            "Supesh's Fortune predictor: The sunshine you feel will spread to others.",
            "Supesh's Fortune predictor: Joy is the magnet of miracles. Expect a surprise today!"
        ],
        "sad": [
            "Supesh's Fortune predictor: Storms don't last forever. Better days are coming.",
            "Supesh's Fortune predictor: Your sadness is valid, but it will pass like the clouds.",
            "Supesh's Fortune predictor: Even the darkest nights end with sunrise. Hold on — light is near."
        ],
        "neutral": [
            "Supesh's Fortune predictor: A surprising opportunity will knock at your door.",
            "Balance is beautiful. Embrace the calm.",
            "Supesh's Fortune predictor: A quiet day can still bring loud opportunities. Stay aware."
        ],
        "stressed": [
            "Supesh's Fortune predictor: Breathe in peace, breathe out stress. You're stronger than you think.",
            "Supesh's Fortune predictor: Even mountains are climbed one step at a time.",
            "Supesh's Fortune predictor: This pressure is shaping you — diamonds form under stress."
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("That's not a valid mood. Try happy, sad, neutral or stressed.")
    


print("""Welcome to BSS Fortune Teller
      
Made by:
Name: Supesh Kumar Sinha
Adm No: 21JE0969
""")

mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

predict(mood)