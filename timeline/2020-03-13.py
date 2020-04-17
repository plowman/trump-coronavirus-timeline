from models import Event, Source

Event(
  date="2020-03-13",
  title="Trump says 'I don't take responsibility at all' for the slowness to ramp up testing",
  description="""
  Here is the full question:
  > Dr. Fauci said earlier this week that the lag in testing was in fact a failing do you 
  take responsibility for that? And when can you guarantee that every single American who needs a test will be able to 
  have a test what's the date of that?
  
  And his response was:
  > Yeah no I don't take responsibility at all because we were given a a set of circumstances and we were given rules 
  regulations and specifications from a different time. [... long meandering nonsense]
  
  It will not surprise you to learn that there was no mythical Obama regulations that slowed anyone down.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump’s False Claims About His Response to the Coronavirus",
      publication="The New York Times",
      published="2020-03-13",
      url="https://www.nytimes.com/2020/03/13/us/politics/fact-check-trump-coronavirus.html",
      article_copy="sources/2020-03-13-new-york-times-trump-i-dont-take-responsibility.pdf",
    ),
    Source(
      title="President Trump Holds a News Conference",
      publication="The White House YouTube Channel",
      published="2020-03-13",
      url="https://youtu.be/feycmqjsLNw?t=4931",
      article_copy="sources/2020-03-13-white-house-youtube-trump-press-conference.png"
    ),
  ],
)
