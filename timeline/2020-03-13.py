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

Event(
  date="2020-03-13",
  title="Trump tries to blame Obama for testing problems",
  description="""
  Tacitly admitting that there were testing problems, which is a small victory for reality, Trump then tried to shift
  the blame to his favorite scapegoat, Obama.
  
  His full tweet was:
  > For decades the @CDCgov looked at, and studied,  its testing system, but did nothing about it. It would always be 
  inadequate and slow for a large scale pandemic, but a pandemic would never happen, they hoped. President Obama made 
  changes that only complicated things further.....
  .... Their response to H1N1 Swine Flu was a full scale disaster, with thousands dying, and nothing meaningful done to 
  fix the testing problem, until now. The changes have been made and testing will soon happen on a very large scale 
  basis. All Red Tape has been cut, ready to go!
  
  It's true that the CDC under Obama did propose increased oversight of medical testing, but it was just a proposal that
  was never implemented. 
  
  Even if Trump had inherited a CDC that was not prepared, he is in charge of it and can thus direct it to change as he
  sees fit. The problem is that he didn't move more quickly.
  """,
  people=["Trump", "Obama"],
  orgs=["CDC"],
  sources=[
    Source(
      title="Everyone and everything Trump has blamed for his coronavirus response",
      publication="The Washington Post",
      published="2020-03-31",
      url="https://www.washingtonpost.com/politics/2020/03/31/everyone-everything-trump-has-blamed-his-coronavirus-response/",
      article_copy="sources/2020-03-31-washington-post-everyone-trump-has-blamed.pdf",
    ),
  ],
)
