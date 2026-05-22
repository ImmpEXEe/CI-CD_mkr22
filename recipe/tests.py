from django.test import TestCase
from .models import Category, Recipe

class ModelsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Cake", 
            description="Sweet", 
            instructions="Bake it", 
            ingredients="Flour, sugar", 
            category=self.category
        )

    def test_category(self):
        self.assertEqual(self.category.name, "Desserts")
        self.assertEqual(len(list(self.category)), 1)

    def test_recipe(self):
        self.assertEqual(self.recipe.title, "Cake")
        self.assertEqual(self.recipe.category.name, "Desserts")
        self.assertTrue(self.recipe.created_at)