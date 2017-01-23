from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import tweepy
from tweepy import OAuthHandler


class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        self.get_tweet(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

    @staticmethod
    def get_tweet(tweet):

        if tweet.coordinates is not None:
            x, y = map(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            map.plot(x, y, 'ro', markersize=2)
            plt.draw()


if __name__ == '__main__':

    # Size of the map
    fig = plt.figure(figsize=(18, 4), dpi=250)

    # Set a title
    plt.title("Tweet's around the world")

    # Declare map projection, size and resolution
    map = Basemap(projection='merc',
                  llcrnrlat=-80,
                  urcrnrlat=80,
                  llcrnrlon=-180,
                  urcrnrlon=180,
                  lat_ts=20,
                  resolution='l')

    map.drawcoastlines(linewidth=0.25)

    # Set interactive mode ON
    plt.ion()

    # Display map
    plt.show()

    # Get access and key from another class
    consumer_key = 'Gg3EQ1Net3sg7o0bSCvdCe6Dm'
    consumer_secret = 'yALVe9MhFjRqmy5jMQJ9EJhMKndAZhMa2qFE4tMOz19QZ0ftcx'
    access_token = '762993015208103936-ospQpj6GdbRVMZhibXk71GZ0kUJpVKg'
    access_secret = '9PSOkPcoREX7wYIXY2dBEmO4uEZUmcDh5C3BZo6TbEH8C'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)

    streamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    myStream.filter(locations=[-180, -90, 180, 90], async=True)