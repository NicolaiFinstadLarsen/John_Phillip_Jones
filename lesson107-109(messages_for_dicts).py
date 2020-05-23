#https://www.youtube.com/watch?v=Rii4QJuXrlQ&list=PL6lxxT7IdTxFKo9DguLxGM2dhgb8-u976&index=107


#EPISODE 107
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

