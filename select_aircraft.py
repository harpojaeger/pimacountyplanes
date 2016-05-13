#This script is passed a plane from the list generated by prepare_1090_json and determines whether it should be tweeted, and, if so, on what grounds (altitude change, location change, heading change).  It passes that information back to vamanos, which then sends the appropriate message.
import os.path
import pickle
from geopy.distance import vincenty
import time

def evaluate(craft):
	pickle_path = 'aircraft/' + craft['hex'] + '.p'
	if os.path.isfile(pickle_path):
		saved_data = pickle.load( open( pickle_path, "rb" ) )
		saved_state = saved_data[1]
		save_time = saved_data[0]
		time_since_save = time.time() - save_time
		if time_since_save < 600:
			#print '%s saved lat is %s (%ss ago)' % (saved_state['hex'], str(saved_state['lat']), int(time_since_save))
			distance = vincenty((saved_state['lat'], saved_state['lon']), (craft['lat'], craft['lon']))
			print '%s has traveled %s in %ss' % (saved_state['hex'], distance.miles, int(time_since_save))

		
		
		
	#print '%s current lat is %s ' % (craft['hex'], str(craft['lat']))
	
	#if we_decide_to_tweet_it:
	pickle.dump( (time.time(), craft), open( pickle_path, "w+" ) )
		
		
		
		