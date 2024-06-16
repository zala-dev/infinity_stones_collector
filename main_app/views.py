from django.shortcuts import render
from .models import InfinityStones

# infinity_stones = [
#     {'name': 'Space Stone', 'color': 'blue',
#         'description': 'controls space and allows teleportation', 'owner': 'Thanos'},
#     {'name': 'Reality Stone', 'color': 'red',
#         'description': 'alters reality according to the wielder\'s will', 'owner': 'Malekith'},
#     {'name': 'Power Stone', 'color': 'purple',
#         'description': 'grants immense power and energy manipulation', 'owner': 'Star-Lord'},
#     {'name': 'Mind Stone', 'color': 'yellow',
#         'description': 'enhances mental abilities and grants access to all thoughts', 'owner': 'Vision'},
#     {'name': 'Time Stone', 'color': 'green',
#         'description': 'controls time, allowing time travel and manipulation', 'owner': 'Doctor Strange'},
#     {'name': 'Soul Stone', 'color': 'orange',
#         'description': 'controls souls and grants access to the soul world', 'owner': 'Red Skull'},
# ]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def infinity_stones_index(request):
    stones = InfinityStones.objects.all()
    return render(request, 'infinity_stones/index.html', {
        'infinity_stones': stones
    })
