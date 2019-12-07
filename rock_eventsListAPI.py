import eventful, json

loop_counter = 0
all_events = []

api = eventful.API('API Key Required')  

while loop_counter < 26:  
    loop_counter = loop_counter + 1 ### 
    print "loop-counter: ",  loop_counter ### debug tracking of this variable

    events = api.call('/events/search', q='tag: rock', date='2019110100-2019113000', category='concerts', location='New York City', within=10, page_count=20, page_number=loop_counter)
    ## query, date and location can be changed for various searches
    
    all_events = all_events + events['events']['event'] ### this works and takes data out of list 
    # all_events.append(events) ### list.append() method allows me to append the entire elements dictionary to the all_events list
    # all_events.append('-----===========<*************>===========-----') ### marker so I can see where each record starts in the printout
    # print (all_events) 

with open('rock_events_NovemberNYC.json', 'w') as outfile:
	json.dump(all_events, outfile, indent=2)
