#pop() tar ut valgt key/value pair. Man kan også sette verdien av dette parret til en variabel 
# for så å printe den verdien ut.
#ref episode 107

mine_aksjer = {
    "akso":6.25,
    "mowi":165
    }

retur_aksje = mine_aksjer.pop("akso")
print(mine_aksjer)
print(retur_aksje)

print() #for plass 

#episode 108, popitem()
#popitem tar ingen parametere. den velger et tilfeldig par...

mine_aksjer = {
    "akso":6.25,
    "mowi":165,
    "bakkafrost":605,
    }

returned_value = mine_aksjer.popitem()
print(mine_aksjer)
print(returned_value)
    