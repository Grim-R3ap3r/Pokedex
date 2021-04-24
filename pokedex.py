import pypokedex
import PIL.Image,PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window=tk.Tk()
window.geometry("600x500")
window.title("Pokedex/Creator:Rathin")
window.config(padx=10,pady=10)

title_label=tk.Label(window,text="Pokedex")
title_label.config(font=("ARIAL",32))
title_label.pack(padx=10,pady=10)

pokemon_image=tk.Label(window)
pokemon_image.pack(padx=10,pady=10)

poke_info=tk.Label(window)
poke_info.config(font=("ARIAL",20))
poke_info.pack(padx=10,pady=10)

poke_types=tk.Label(window)
poke_types.config(font=("ARIAL",20))
poke_types.pack(padx=10,pady=10)

#function to access pokemon
def load_pokemon():
     pokemon=pypokedex.get(name=text_idname.get(1.0,"end-1c"))
     #end-1c is to ignore \n in the string
     http=urllib3.PoolManager()
     response=http.request('GET',pokemon.sprites.front.get('default'))
     image=PIL.Image.open(BytesIO(response.data))
     #putting the pokemon image into a pillow object

     img=PIL.ImageTk.PhotoImage(image)
     #putiing the object into tkinter 
     pokemon_image.config(image=img)
     pokemon_image.image=img 
     
     poke_info.config(text=f"{pokemon.dex} - {pokemon.name}")
     poke_types.config(text=" , ".join([type for type in pokemon.types]))
     



label_idname=tk.Label(window,text="ID OR NAME")
label_idname.config(font=("ARIAL",15))
label_idname.pack(padx=10,pady=10)

text_idname=tk.Text(window,height=1)
text_idname.config(font=("ARIAL",15))
text_idname.pack(padx=10,pady=10)

btn_load=tk.Button(window,text="LOAD POKEMON",command=load_pokemon)
#command=load_pokemon works like a function call
btn_load.config(font=("ARIAL",15))
btn_load.pack(padx=10,pady=10)








window.mainloop()
