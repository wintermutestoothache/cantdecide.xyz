import os
import json

def translateIngredients(ingredients):
    '''
    take list of ingredients, creates a file, and sends it to the NY
    times ingredient parser
    '''
    toWrite = "\n".join(ingredients)

    with open('recipes/temp/ingredientsTemp.txt','w') as f:
        f.write(toWrite)

    os.system(
        'python youdecide/scripts/loadIngredients.py recipes/temp/'+
        'ingredientsTemp.txt recipes/temp/ingredientsEnd')
    os.remove('recipes/temp/ingredientsTemp.txt')

    f = open('recipes/temp/ingredientsEnd.json','r')
    ingredientList = json.loads(f.read())
    f.close()
    os.remove('recipes/temp/ingredientsEnd.json')

    fieldSet = set(['name','comment','other','display','qty','unit'])

    for i in ingredientList:
        for z in fieldSet:
            if z not in i:
                i[z] =''

    return ingredientList



