def createEmptySolution(instance):
    solution={} #mi solución va a ser un diccionanrio donde gurdes los nodos que cooges
    solution['sol']=set() #set sirve para buscar si un elemeto está o no está, porque in recorre todos los elementos y es muy lento
    solution['of']=0 #valor de la función objetivo
    solution['instance']= instance #no hace copia de la instancia
    return solution
def evaluate(sol): #evaluar la solución, dada mi solución recorro todos los nodos y sumos las distancias entre ellos
    of=0
    for s1 in sol['sol']:
        for s2 in sol['sol']:
            if s1<s2: # se puede hacer esto o dividir entre 2 of
                of += sol['instance']['d'][s1][s2]
    return of

def addToSolution (sol, u, ofVariation=-1):    #añade a una solución un elemento
    if ofVariation== -1:
        for s in sol['sol']:   #me recorro todas las soluciones y les sumo el incremento
            sol['of']+= sol['instance']['d'][u][s]
    else:
        sol['of'] += ofVariation
    sol['sol'].add(u)


def removeFromSolution(sol, u, ofVariation=-1):
    sol['sol'].remove(u) #si quito un elemento quierp quitar su distancia
    if ofVariation==-1:
        for s in sol['sol']: #me recorro todas las soluciones y les resto el incremento
            sol['of'] -= sol['instance']['d'][u][s]
    else:
        sol['of'] -= ofVariation

def contains(sol, u):
        return u in sol['sol']

def distanceToSolution(sol, u, without=-1):
        d = 0
        for s in sol['sol']:
            if s != without:
                d += sol['instance']['d'][s][u]
        return round(d, 2)

def isFeasible(sol):
        return len(sol['sol']) == sol['instance']['p']

def printSol(sol):
        print("SOL: " + str(sol['sol']))
        print("OF: " + str(round(sol['of'], 2)))
