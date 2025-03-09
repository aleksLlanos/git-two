# Definimos tres proposiciones como funciones
def implica(p, q):
    return (not p) or q  # lógica de la implicación p → q

# Ejemplo de proposiciones
def p(): return True     # p es verdadera
def q(): return True     # q es verdadera
def r(): return True   # r es falsa

# Silogismo hipotético:
# Si p → q y q → r, entonces p → r

# Evaluamos cada implicación
pq = implica(p(), q())
qr = implica(q(), r())
pr = implica(p(), r())

# Mostramos los valores
print("p → q:", pq)
print("q → r:", qr)
print("p → r:", pr)

# Evaluación del silogismo
if pq and qr:
    print("Por silogismo hipotético, p → r debe ser:", pr)
else:
    print("No se cumple el silogismo.")
