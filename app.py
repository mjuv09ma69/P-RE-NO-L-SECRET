from discord.ext.commands import Bot
import discord

import random
import time



les_bros = {
    "doge_holder" : ["ID_DISCORD", "https://upload.wikimedia.org/wikipedia/commons/5/58/Shiba_inu_taiki.jpg"],
    "doge_lover" : ["ID_DISCORD", "https://upload.wikimedia.org/wikipedia/commons/5/58/Shiba_inu_taiki.jpg"]
    
}

def melange(dictionnaire):
    valeurs = list(dictionnaire.keys())
    random.shuffle(valeurs)
    attribution = {}
    i = 0
    for cle in dictionnaire:
        attribution[cle] = valeurs[i]
        i += 1
    return attribution

def verification_melange(dictionnaire):
    """
    Définition de quelques règles en plus pour le père noel secret.
    Ici : On ne peut pas être le père noel secret de notre père secret. Nécessite + de 2 participants.
    """
    for personne in dictionnaire:
        if dictionnaire[dictionnaire[personne]] == personne:
            return False
    return True

attribution_noel = melange(les_bros)

while(not verification_melange(attribution_noel)): 
    attribution_noel = melange(les_bros)

bot = Bot("!")

@bot.event
async def on_ready():
    print('{0.user} est lancé.'.format(bot))

    await tirage()
        

@bot.command(pass_context=True)
async def tirage():
    color = discord.Colour.from_rgb(r=255, g=70, b=75)

    for nom in les_bros:
        user = await bot.fetch_user(les_bros[nom][0])
        e = discord.Embed(title='**Tirage**',
                          description="**Le tirage au sort du père noel secret a eu lieu. Tu devras offrir un cadeau à :** " + attribution_noel[nom]+'.',
                          colour=color)
        e.set_thumbnail(url=les_bros[attribution_noel[nom]][1])
        e.set_footer(text="Texte du footer", icon_url="https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png")
        await user.send(embed=e)
        print(nom, "fait")
        time.sleep(1) 


@bot.command(pass_context=True)
async def verification_potos():
    """
    Affiche chaque prénom associé à son tag discord.
    """
    for nom in les_bros:
        user=await bot.fetch_user(les_bros[nom][0])
        print(nom , ":", user)


bot.run("TOKEN DISCORD")
