from django.db import models
import json

class Recipes(models.Model):
    url = models.URLField(default ="")
    title = models.CharField(max_length=200, default='')
    yiel = models.CharField(max_length=100, default='')
    active_time = models.CharField(max_length=100,default='')
    total_time = models.CharField(max_length=100,default='')
    time_plus = models.CharField(max_length=1, default='')
    imgUrl = models.URLField(default='')
    
    def __str__(self):
        return self.title

    def ingredients(self):
        return self.ingredient_set.all()

    def instructions(self):
        instruct = self.instructions_set.all()
        return [instruct[i].step for i in range(len(instruct)-1,-1,-1)]

    def returnJson(self):
        '''doesnt actually return json since Djangos new JsonResponse returns it automatically. Instead method returns dict that is easily converted into json'''

        toConvert = {'url':self.url, 'title':self.title,'yiel':self.yiel,'active_time':self.active_time,'total_time':self.total_time,'imgUrl':self.imgUrl, 'pk':self.pk}
        #converted = json.dumps(toConvert)
        return toConvert

class Instructions(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    step = models.TextField(default ='')
    def __str__(self):
        return self.step

class Ingredient(models.Model):
    item = models.CharField(max_length=100, default='')
    amount = models.CharField(max_length=100, default='')
    original_txt = models.TextField(default='')
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    def __str__(self):
        return self.item
