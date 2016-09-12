from django.db import models

class Recipes(models.Model):
    url = models.URLField(default ="")
    title = models.CharField(max_length=200, default='')
    yiel = models.IntegerField(default=0)
    active_time = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)
    time_plus = models.CharField(max_length=1, default='')
    
    def __str__(self):
        return self.title

class Instructions(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    step = models.TextField(default ='')
    def __str__(self):
        return self.step

#class Ingredient_list(models.Model):
    #recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    #ingredient = many to many rel 

class Ingredient(models.Model):
    item = models.CharField(max_length=100, default='')
    amount = models.CharField(max_length=100, default='')
    original_txt = models.TextField(default='')
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    def __str__(self):
        return self.item
