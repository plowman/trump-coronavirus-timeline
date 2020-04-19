from models import Event, Source

Event(
  date="2020-04-16",
  title="Trump releases guidelines on reopening country: states decide what to do on their own",
  description="""
  Switching back again to his previous stance, Trump agrees once more that states are in charge of how they open.
  
  To this end, he released a set of nonbinding guidelines that basically tell states to open things gradually based on
  how bad things are in each state.
  
  Determined to say as little as possible, he said states could start reopening as soon as May 1st or earlier. Which is
  a verbose way of saying they can open "at some point".
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Says States Can Start Reopening While Acknowledging the Decision Is Theirs",
      publication="The New York Times",
      published="2020-04-16",
      url="https://www.nytimes.com/2020/04/16/us/politics/coronavirus-trump-guidelines.html",
      article_copy="sources/2020-04-16-new-york-times-coronavirus-trump-guidelines.pdf",
    ),
  ],
)
