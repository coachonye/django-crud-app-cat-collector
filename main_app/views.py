from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # or whatever template you’re using

# Temporary mock class
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Simulated list of cat instances
cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def cat_index(request):
    return render(request, 'cats/index.html', { 'cats': cats })

def about(request):
    return render(request, 'about.html')

