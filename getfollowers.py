from twython import Twython
import csv
import time
import sys
import unicodecsv

#Fill out these settings
APP_KEY = ""
APP_SECRET = ""
USERNAME=""
#Set ADVANCED to 1 if you want to save extra information about profiles such as profile picture url
ADVANCED=0
FILE_LOC="followers-"+USERNAME+".csv"

#Initialize Twython
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

followers_file = unicodecsv.writer(open(FILE_LOC, "wb"))

#Run basic program
if(ADVANCED==0):
	#Write csv column headers
	followers_file.writerow(["User Name","Name","ID","Description","Location","URL"])

	next_cursor=-1
	p = 1
	while(next_cursor != 0):
		print "Loading page", p , "of results from Twitter"
		#Loop/set variables for each user in followers list
		followers = twitter.get_followers_list(screen_name = USERNAME, count = 200, cursor = next_cursor)

		print "Writing page", p , "to csv file"
		for result in followers['users']:
			screen_name = result['screen_name']
			name = result['name']
			tw_id = result['id']
			description = result['description']
			location = result['location']
			entities = result['entities']
			expanded_url = None
			if('url' in entities):
				entities_url = entities['url']
				entities_urls = entities_url['urls']
				for entities_result in entities_urls:
					expanded_url = entities_result['expanded_url']
			
			#Write csv file
			followers_file.writerow([screen_name, name, tw_id, description, location, expanded_url])
		next_cursor=followers['next_cursor']
		if(next_cursor !=0):
			p += 1
			#Wait 60 seconds to appease the Twitter API
			for i in xrange(60,0,-1):
				time.sleep(1)
				sys.stdout.write(" Waiting "+str(i)+" secs to keep from running into Twitter's rate limit  \r")
				sys.stdout.flush()
			print "\x1b[2K"

#Run advanced program
else:
	#Write csv column headers
	followers_file.writerow(["User Name","Name","ID","Description","Location","URL","profile_sidebar_fill_color","profile_sidebar_border_color","profile_background_tile","profile_image_url_https","created_at","profile_link_color","is_translator","default_profile","contributors_enabled","favourites_count","utc_offset","profile_use_background_image","listed_count","profile_text_color","lang","followers_count","protected","profile_background_image_url_https","profile_background_color","verified","geo_enabled","time_zone","default_profile_image","statuses_count","friends_count"])

	next_cursor=-1
	p = 1
	while(next_cursor != 0):
		print "Loading page", p , "of results from Twitter"
		#Get followers list
		followers = twitter.get_followers_list(screen_name = USERNAME, count = 200, cursor = next_cursor)

		print "Writing page", p , "to csv file"
		#Loop/set variables for each user in followers list
		for result in followers['users']:
			screen_name = result['screen_name']
			name = result['name']
			tw_id = result['id']
			description = result['description']
			location = result['location']
			entities = result['entities']
			expanded_url = None
			if('url' in entities):
				entities_url = entities['url']
				entities_urls = entities_url['urls']
				for entities_result in entities_urls:
					expanded_url = entities_result['expanded_url']
			profile_sidebar_fill_color = result['profile_sidebar_fill_color']
			profile_sidebar_border_color = result['profile_sidebar_border_color']
			profile_background_tile = result['profile_background_tile']
			profile_image_url_https = result['profile_image_url_https']
			created_at = result['created_at']
			profile_link_color = result['profile_link_color']
			is_translator = result['is_translator']
			default_profile = result['default_profile']
			contributors_enabled = result['contributors_enabled']
			favourites_count = result['favourites_count']
			utc_offset = result['utc_offset']
			profile_use_background_image = result['profile_use_background_image']
			listed_count = result['listed_count']
			profile_text_color = result['profile_text_color']
			lang = result['lang']
			followers_count = result['followers_count']
			protected = result['protected']
			profile_background_image_url_https = result['profile_background_image_url_https']
			profile_background_color = result['profile_background_color']
			verified = result['verified']
			geo_enabled = result['geo_enabled']
			time_zone = result['time_zone']
			default_profile_image = result['default_profile_image']
			statuses_count = result['statuses_count']
			friends_count = result['friends_count']

			#Write csv file
			followers_file.writerow([screen_name, name, tw_id, description, location, expanded_url, profile_sidebar_fill_color, profile_sidebar_border_color, profile_background_tile, profile_image_url_https, created_at, profile_link_color, is_translator, default_profile, contributors_enabled, favourites_count, utc_offset, profile_use_background_image, listed_count, profile_text_color, lang, followers_count, protected, profile_background_image_url_https, profile_background_color, verified, geo_enabled, time_zone, default_profile_image, statuses_count, friends_count])
		next_cursor=followers['next_cursor']
		if(next_cursor !=0):
			p += 1
			#Wait 60 seconds to appease the Twitter API
			for i in xrange(60,0,-1):
				time.sleep(1)
				sys.stdout.write(" Waiting "+str(i)+" secs to keep from running into Twitter's rate limit  \r")
				sys.stdout.flush()
			print "\x1b[2K"

print "Done!"
