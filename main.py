
# Importation des librairies nécessaires
import asyncio
import base64
import os

from dotenv import load_dotenv
from rodiumai import RodiumAI


# DEFINITION DES DIFFENTS MODELES A UTILISER POUR L'EXERCICE
CHAT_MODEL = "google/gemini-3.8-flash"
IMAGE_MODEL = "google/gemini-3.1-flash-lite-image"
VIDEO_MODEL = "openai/sora-2"


# chargement des variables d'environnements
load_dotenv()

API_KEY = os.getenv("RODIUMAI_API_KEY")


client = RodiumAI(
    api_key=API_KEY,
    timeout=30,
    stream_timeout=150
)


# ETAPE 1 : LE CHAT CONVERSATIONNEL

async def chat():
    question = input("Votre question : ")

    try:
        response = await client.chat(
            [
                {
                    "role": "user",
                    "content": question
                }
            ],
            model=CHAT_MODEL,
            temperature=0.7,
            max_tokens=1500
        )

        print("\nRéponse :")
        print(response.choices[0].message.content)

        print(f"Coût : {response.cost_rodi} RODI")

    except Exception as e:
        print(f"Erreur : {e}")


# ÉTAPE 2 : IMAGE

async def image():
    description = input("Décrivez l'image : ")

    try:
        response = await client.images(
            model=IMAGE_MODEL,
            prompt=description,
            n=1,
            size="1024x1024",
            quality="medium"
        )

        image_base64 = response.data[0].b64_json

        image = base64.b64decode(image_base64)

        with open("image.png", "wb") as fichier:
            fichier.write(image)

        print("Image enregistrée : image.png")

    except Exception as e:
        print(f"Erreur : {e}")


# ÉTAPE 3 : VIDÉO

async def video():
    description = input("Décrivez la vidéo : ")

    try:
        response = await client.videos(
            model=VIDEO_MODEL,
            prompt=description,
            duration_seconds=4,
            aspect_ratio="9:16",
            timeout=150
        )

        video_data = response.data[0]

        if video_data.b64_json:
            video = base64.b64decode(video_data.b64_json)

            with open("video.mp4", "wb") as fichier:
                fichier.write(video)

            print("Vidéo enregistrée : video.mp4")

        elif video_data.url:
            print(f"Vidéo disponible à cette adresse : {video_data.url}")

    except Exception as e:
        print(f"Erreur : {e}")


# PROGRAMME PRINCIPAL

async def main():

    etapes = [chat, image, video]
    position = 0

    while True:

        print(f"\n=== Étape {position + 1} ===")

        await etapes[position]()

        if position == 0:

            choix = input(
                "\nRester sur cette étape (r) ou passer à la suivante (s) ? "
            ).lower()

            if choix == "s":
                position = 1

        elif position == 1:

            choix = input(
                "\nRevenir en arrière (b), rester (r) ou passer à la suivante (s) ? "
            ).lower()

            if choix == "b":
                position = 0

            elif choix == "s":
                position = 2

        else:

            choix = input(
                "\nRevenir en arrière (b), rester (r) ou quitter (q) ? "
            ).lower()

            if choix == "b":
                position = 1

            elif choix == "q":
                print("Au revoir.")
                break


asyncio.run(main())
