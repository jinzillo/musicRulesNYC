import eventful, json

loop_counter = 0
all_events = []

api = eventful.API('95HzcLgHb9mKLh6P') 

while loop_counter < 3:  
    loop_counter = loop_counter + 1 
    print "loop-counter: ",  loop_counter ### tracking of this variable

    events = api.call('/events/search', q='tag: hiphop', date='2019111500-2019111600', category='concerts', location='New York City', within=10, page_count=10, page_number=loop_counter)
     
    all_events = all_events + events['events']['event'] ### this works and takes data out of list 
    # all_events.append(events) ### list.append() method allows me to append the entire elements dictionary to the all_events list
    # all_events.append('-----===========<*************>===========-----') ### marker so I can see where each record starts in the printout
    # print (all_events) 

with open('hiphop_events_Nov15NYC.json', 'w') as outfile:
	json.dump(all_events, outfile, indent=2)