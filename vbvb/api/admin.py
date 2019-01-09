# */vasserballverband/vbvb/api/admin.py
'''
    File path:   */vasserballverband/vbvb/api/admin.py
    Description: In Django, admin.py tells the admin that any object
                 we register should have an admin interface.
'''


from .models import Authority, City, Finish, State, Team, Tournament

from django.contrib.admin.site import register


register(Authority)  # Organizations that own pools and teams
register(City)       # Cities and places in the United States
register(Finish)     # Placement result in a tourney or game
register(State)      # States of the United States of America
register(Team)       # Any water polo team, NCAA, HS, Pro etc
register(Tournament) # Any water polo tournament
