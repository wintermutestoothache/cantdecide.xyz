import random
import json
from youdecide.config import PATHS

class RecipeSearchAndReturn(object):

    #because Recipes.objects.all() is so slow, particularly as
    #the database grows, I've opted to make manual changes to 
    #amount total amount of recipes to search
    CURRENT_RECIPE_COUNT = PATHS['RECIPE_COUNT'] 

    def __init__(self,searchDictPath, quantity):
        self.quantity = quantity
        with open(searchDictPath, 'r') as f:
            self.searchDict = json.loads(f.read())

    def __str__(self):
        pass


    def find_recipes(self, request):
        '''
        takes django http request which can contain a search
        restriction query string and returns recipes
        that match the requirements.

        will return 1 if no item can be found
        '''
        restrictions = request.GET.getlist('restrictions')
        search = request.GET.getlist('search')
        if search: search = search[0].split(',')

        optionSet = set(self.searchDict[''])
        search += restrictions

        optionSet = self.searchHelp(
            search)if search else set(self.searchDict[''])

        if len(optionSet) < self.quantity:
            returnList = [_ for _ in optionSet] if optionSet else [1]
            if returnList[-1] != 1 or not returnList:
                returnList.append(1)
            return returnList

        return random.sample(optionSet,self.quantity)


    def searchHelp(self, searchList):
        searchResults = []
        for item in searchList:
            item = item.lower().strip()
            if item not in self.searchDict:
                with open(
                    'youdecide/searches/searchFiles/'
                    +'errorLog.txt','a') as f:
                    f.write(item)
            else:
                searchResults.append(set(self.searchDict[item]))

        return set.intersection(
            *searchResults) if searchResults else {1}




