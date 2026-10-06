import os
from groq import Groq


client = Groq(api_key="IDE_ILLESZD_BE_A_SAJAT_API_KULCSODAT")

print("--- Python AI Asszisztens elindulva! (Írd be, hogy 'kilépés' a bezáráshoz) ---")

while True:
    felhasznalo_kerdese = input("\nTe: ")

    if felhasznalo_kerdese.lower() == "kilépés":
        print("Viszlát!")
        break


    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": felhasznalo_kerdese}
        ],
        temperature=0.7,
    )

    valasz = completion.choices[0].message.content
    print(f"AI: {valasz}")
