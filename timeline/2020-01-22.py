from models import Event, Source
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-01-22",
  title="Trump's first comments on Coronavirus: 'we have it totally under control. ... It’s going to be just fine.'",
  description="""
  President Trump made his first public comments about the coronavirus in a TV interview from Davos with CNBC’s Joe 
  Kernen. The first American case had been announced the day before, and Kernen asked Trump, “Are there worries about a 
  pandemic at this point?”

  Trump said, “No. Not at all. And we have it totally under control. It’s one person coming in from China, and we have 
  it under control. It’s going to be just fine.”
  """,
  people=["Trump", "Joe Kernen"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)

Event(
  date="2020-01-22",
  title="Feds turn down offer from US mask producer to ramp up production",
  description="""
  From the article:
  > Bowen’s medical supply company, Prestige Ameritech, could ramp up production to make an additional 1.7 million N95 
  masks a week.
  
  > “I don’t believe we as an government are anywhere near answering those questions for you yet,” Laura Wolf, director 
  of the agency’s Division of Critical Infrastructure Protection, responded that same day.
  """,
  people=["Robert Kadlec"],
  orgs=["HHS"],
  sources=[
    Source(
      title="In the early days of the pandemic, the U.S. government turned down an offer to manufacture millions of N95 masks in America",
      publication="The Washington Post",
      published="2020-05-09",
      url="https://www.washingtonpost.com/investigations/in-the-early-days-of-the-pandemic-the-us-government-turned-down-an-offer-to-manufacture-millions-of-n95-masks-in-america/2020/05/09/f76a821e-908a-11ea-a9c0-73b93422d691_story.html",
      article_copy="sources/2020-05-09-the-washington-post-in-the-early-days-of-the-pandemic-the-us-government-turned-down-an-offer-to-manufacture-millions-of-n-masks-in-america.pdf",
    ),
  ],
)
