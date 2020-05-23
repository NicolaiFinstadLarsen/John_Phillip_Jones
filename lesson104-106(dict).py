#https://www.youtube.com/watch?v=Rii4QJuXrlQ&list=PL6lxxT7IdTxFKo9DguLxGM2dhgb8-u976&index=104

mine_aksjer = {
    "akso":6.25,
    "mowi":165
    }
mine_aksjer["bakkafrost"]=605

print(mine_aksjer)
print(mine_aksjer["akso"])
print(mine_aksjer["mowi"])  

print() #for plass

print(mine_aksjer, len(mine_aksjer))

print() #for plass

del mine_aksjer["akso"]
print(mine_aksjer, len(mine_aksjer))

print() #for plass

mine_aksjer.clear()
print(mine_aksjer, len(mine_aksjer))

print()

print(dir(dict))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
#'setdefault', 'update', 'values'
#Dette er beskjedene vi kan gi vår dict. Beskjeder blir gitt via en "."
#eks: mine_aksjer.clear()

print()#for plass

