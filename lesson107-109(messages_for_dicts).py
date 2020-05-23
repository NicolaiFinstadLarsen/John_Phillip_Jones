#https://www.youtube.com/watch?v=Rii4QJuXrlQ&list=PL6lxxT7IdTxFKo9DguLxGM2dhgb8-u976&index=107

### Metoder for dict class ###

#EPISODE 107
print("ep.107")
    #pop() tar ut valgt key/value pair. Man kan også sette verdien av dette parret til en variabel 
    # for så å printe den verdien ut.
    
mine_aksjer = {
    "akso":6.25,
    "mowi":165
    }

returned_value = mine_aksjer.pop("akso")
print(mine_aksjer)
print(returned_value)
print() #for plass 


#EPISODE 108
print("ep.108")
    #popitem()
    #popitem tar ingen parametere. den velger et tilfeldig par...

mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }

returned_value = mine_aksjer.popitem()
print(mine_aksjer)
print(returned_value)
print() # for plass


#EPISODE 109
print("ep.109")
    #keys()
    #finner alle keys og man kan f.eks sette de i en variabel å printe de ut.
    #her lager jeg også en liste av de. 

mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }

returned_value = list(mine_aksjer.keys())
print(returned_value)
print() #for plass


#EPISODE 110
print("ep.110")
    #values
    #samme som keys, men behandler verdiene istedenfor keys i dict.

mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }
returned_value = (mine_aksjer.values())
print(returned_value)
print(list(returned_value))
print() # for plass


#EPISODE 111
print("ep.111")
    #get()
    #vi kan bruke get() hvis vi ikke vil skrive en kode med try/exept keywords 
    #hvis get() ikke finner argumentet, returnerer det "none"
    #hvis man ikke bruker noen av disse, vil man få en error når man ikke har key'en man leter etter.
       
mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }

try:
    print(mine_aksjer["akso"])
    print(mine_aksjer["SalMar"])
except KeyError:
    print("SalMar is not here")
    
print() #for plass

print(mine_aksjer.get("akso"))
print(mine_aksjer.get("SalMar"))
print() #for plass 


#EPISODE 112
print("ep.112")
    #items()
    #printer ut key:value pairs i hver sin tuple, alt samlet i en liste.
    
mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }
print(mine_aksjer.items())
print()#for plass
print(list(mine_aksjer.items()))
print()#for plass
aksje_liste = list(mine_aksjer.items())
print(aksje_liste[-1])
print() # for plass


#EPISODE 113
print("ep.113")
    #update()
    #man kan oppdatere sin dict fra en annen dict ved å legge inn den dict 
    #du vil legge inn, som et argument i hoveddict.update(dict_du_vil_ha_inn)
    
mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }

flere_aksjer = {"SalMar":195, "NOFI":66}

print(mine_aksjer)
print(flere_aksjer)

mine_aksjer.update(flere_aksjer)

print(mine_aksjer)
print(flere_aksjer)
print() #for plass


#EPISODE 114
print("ep.114")



