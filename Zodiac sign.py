# WAP to show the user its zodiac sign
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")  
engine.setProperty(f"voice", voices[1].id) 
engine.setProperty('rate', 130) 

name=input("Your Name: ").strip().capitalize()
print(f"Greetings {name}")
month = input("Enter Your Birth Month: ").strip().lower()
date=int(input("Enter Your Date of Birth: "))
if (month == "march" and date >= 21) or (month == "april" and date <= 19):
    sign = "♈ Aries"
elif (month == "april" and date >= 20) or (month == "may" and date <= 20):
    sign = "♉ Taurus"
elif (month == "may" and date >= 21) or (month == "june" and date <= 20):
    sign = "♊ Gemini"
elif (month == "june" and date >= 21) or (month == "july" and date <= 22):
    sign = "♋ Cancer"
elif (month == "july" and date >= 23) or (month == "august" and date <= 22):
    sign = "♌ Leo"
elif (month == "august" and date >= 23) or (month == "september" and date <= 22):
    sign = "♍ Virgo"
elif (month == "september" and date >= 23) or (month == "october" and date <= 22):
    sign = "♎ Libra"
elif (month == "october" and date >= 23) or (month == "november" and date <= 21):
    sign = "♏ Scorpio"
elif (month == "november" and date >= 22) or (month == "december" and date <= 21):
    sign = "♐ Sagittarius"
elif (month == "december" and date >= 22) or (month == "january" and date <= 19):
    sign = "♑ Capricorn"
elif (month == "january" and date >= 20) or (month == "february" and date <= 18):
    sign = "♒ Aquarius"
elif (month == "february" and date >= 19) or (month == "march" and date <= 20):
    sign = "♓ Pisces"
else:
    sign = "Invalid Date"
print(f"{name} Your zodiac sign is {sign}.")

engine.say(f"{name} Your zodiac sign is {sign}.")
engine.runAndWait()