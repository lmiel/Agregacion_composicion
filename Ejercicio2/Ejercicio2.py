class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.var_yang = yang 
 
print(yang) 
print(yin.var_yang)
print(yang is yin.var_yang) 
del(yang) 
del(yin.var_yang)
print("?") 

#Se imprime antes "?" porque el objeto Yang no se borra ya que tiene una referencia desde el objeto Yin.
#Si se borra la referencia desde el objeto Yin, se borra el objeto Yang y se imprime "Yang destruido"
