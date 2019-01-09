# */vasserballverband/vbvb/api/admin.py
'''
    File path:   */vasserballverband/vbvb/api/admin.py
    Description: In Django, admin.py tells the admin that any object
                 we register should have an admin interface.
'''


from .models import Authority, City, Finish, State, Team, Tournament

from django.contrib import admin


admin.site.register(Authority)  # Organizations that own pools and teams
admin.site.register(City)       # Cities and places in the United States
admin.site.register(Finish)     # Placement result in a tourney or game
admin.site.register(State)      # States of the United States of America
admin.site.register(Team)       # Any water polo team, NCAA, HS, Pro etc
admin.site.register(Tournament) # Any water polo tournament
