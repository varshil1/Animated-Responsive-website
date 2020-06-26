from django.shortcuts import render
from django.http import HttpResponse
from p_club_app.models import Login,Events,Resources,Timeline,About_us,Team,Home_about_us,Home_desc
# Create your views here.
def index(request):
    #dict to send data of resources
    src_list = Resources.objects.raw('SELECT * FROM p_club_app_resources LIMIT 6')
    id_dict = {'resource':src_list}
    # event_list = Events.objects.raw('SELECT * FROM p_club_app_events where event_date BETWEEN date() AND date(date(),"+6 month") ORDER BY event_date LIMIT 3')
    
    #dict to send data of events
    event_list = Events.objects.raw('SELECT * FROM p_club_app_events where event_pref="High" LIMIT 3')
    date_dict = {'event':event_list}
    #dict to send data of about us
    about_list=Home_about_us.objects.raw('SELECT * FROM p_club_app_Home_about_us ORDER BY id DESC LIMIT 1')
    about_dict={'about':about_list}
    #dict to send data of home description
    home_list=Home_desc.objects.raw('SELECT * FROM p_club_app_Home_desc ORDER BY id DESC LIMIT 1')
    home_dict={'details':home_list}
    # mix the dictionary to pass all data
    mix_dict={'resource':src_list,'event':event_list,'details':home_list,'about':about_list}
    return render(request,'p_club_app/index.html',context=mix_dict)  

def event(request):
    #dict to send data of events
    event_list = Events.objects.order_by('event_date')
    date_dict = {'event':event_list}
    past_list=Events.objects.raw('SELECT * FROM p_club_app_events  ORDER BY event_date')
    present_list=Events.objects.raw('SELECT * FROM p_club_app_events ORDER BY event_date')
    future_list=Events.objects.raw('SELECT * FROM p_club_app_events ORDER BY event_date')
    ev_dict={'past':past_list,'present':present_list,'future':future_list}    
    return render(request,'p_club_app/event.html',context=ev_dict)

def about_us(request):
    #dict to send data of about us
    about_us_list=About_us.objects.order_by('id')
    abt_list_dict={'about_us':about_us_list}
    team_list=Team.objects.order_by('position_order')
    team_dict={'team':team_list}
    mix_dict={'team':team_list,'about_us':about_us_list}
    return render(request,'p_club_app/about_us.html',context=mix_dict)

def resource(request):
        #dict to send data of resource

    src_list = Resources.objects.order_by('resource_id')
    id_dict = {'resource':src_list}
    return render(request,'p_club_app/resource.html',context=id_dict)    
