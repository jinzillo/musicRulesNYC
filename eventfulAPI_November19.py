import eventful

api = eventful.API('API Key Required')

# If you need to log in:
# api.login('username', 'password')
# q= 'music', c='music', 

events = api.call('/events/search', q='tag: rock', date='2019111500-2019111600', category='concerts', location='New York City', within=10)


for event in events['events']['event']:
    # print (event['title'], event['city_name'], event['venue_name'], event['start_time'])
    print(events)
