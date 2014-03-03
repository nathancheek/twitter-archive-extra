twitter-archive-extra
=====================

Archives information that Twitter's archive does not

###Introduction###

These python scripts allow you to archive information that is not included in Twitter's archive tool.
Currently the scripts create CSV files of your followers and following lists.

###Implementation###

####Python libraries####
Required libraries:
* [Twython](https://github.com/ryanmcgrath/twython)
* [unicodecsv](https://github.com/jdunck/python-unicodecsv)
If you have easy_install installed, use:

```$ sudo easy_install twython```

```$ sudo easy_install unicodecsv```

####Twitter API####
You will need to create a Twitter API application.
You can do so at [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new).
You will need to fill out the ```APP_KEY``` and ```APP_SECRET``` from the Twitter application in the python files.

####File settings####
+ ```APP_KEY``` - The app key from your Twitter application
+ ```APP_SECRET``` - The app secret from your Twitter application
+ ```USERNAME``` - The username you wish to get the information for
+ ```ADVANCED``` - Saves other returned information such as time zone and language; disabled by default
