import time
import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

words_by_level = {
    "facil": {
        "gato": "cat",
        "perro": "dog",
        "manzana": "apple",
        "leche": "milk",
        "sol": "sun"
    },
    "medio": {
        "platano": "banana",
        "escuela": "school",
        "amigo": "friend",
        "ventana": "window",
        "amarillo": "yellow"
    },
    "dificil": {
        "tecnologia": "technology",
        "universidad": "university",
        "informacion": "information",
        "pronunciacion": "pronunciation",
        "imaginacion": "imagination"
    }
}

p1 = input("¿qué dificultad quieres usuario? 😎 (facil / medio / dificil): ")

if p1 not in words_by_level:
    print("Dificultad no válida")
    exit()

print("buscando palabra para usar...⏱️")
time.sleep(2)

r2 = random.choice(list(words_by_level[p1].keys()))
correct = words_by_level[p1][r2]

print("Palabra en español:", r2)
print("Di la traducción en inglés 🎤")

# 🎤 GRABAR VOZ
duration = 5
sample_rate = 44100

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

wav.write("output.wav", sample_rate, recording)

print("Reconociendo voz...")

recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:

    text = recognizer.recognize_google(audio, language="en-US").lower()

    print("\n📊 RESULTADO")
    print("Palabra en español:", r2)
    print("Respuesta correcta en inglés:", correct)
    print("Lo que dijiste:", text)

    if correct in text:
        print("🎉 ¡Correcto!")
    else:
        print("❌ Incorrecto")

except sr.UnknownValueError:
    print("⚠ No se pudo reconocer el habla")

except sr.RequestError as e:
    print("Error del servicio:", e)
