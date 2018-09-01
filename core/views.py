from django.shortcuts import render
import meetup.api

# Create your views here.

# Index view
def index(request):
    return render(request, 'core/index.html')

# About view
def about(request):
    return render(request, 'core/about.html')

# Code of Conduct view
def coc(request):
    return render(request, 'core/coc.html')

# Contact view
def contact(request):
    return render(request, 'core/../templates/contact/contact.html')

####
# Events view
def events(request):
   client = meetup.api.Client('c1b77c1a3d36296a3141f803e7f7c')
   events = client.GetEvents({'group_urlname': 'CLE-PyLadies'})
   group_events = events.__dict__['results']
   return render(request, 'core/events.html', {'group_events': group_events})

# # Meetup list view
# def events(request):
#     response = requests.get('https://api.meetup.com/CLE-PyLadies/events?&sign=true&photo-host=public&page=20')
#     data = response.json()
#     # num_events = len(json.loads(data))
#     return render(request, 'core/events.html', {
#         'event_name': data['name'],
#         'event_date': data['local_date'],
#         'event_time': data['local_time']
#         # 'event_location': data['venue']
#     })

####
# Join view
def join(request):
    return render(request, 'core/join.html')

# Partners view
def partners(request):
    return render(request, 'core/partners.html')

# Resources view
def resources(request):
    return render(request, 'core/resources.html')

# Values view
def values(request):
    return render(request, 'core/values.html')