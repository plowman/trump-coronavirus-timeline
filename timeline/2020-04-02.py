from models import Event, Source

Event(
  date="2020-04-02",
  title="White House blocks health officials from CNN in retaliation for coverage",
  description="""
  On April 2nd, Pence began blocking US health officials like Dr. Fauci from appearing on CNN. "When you guys cover the 
  briefings with the health officials then you can expect them back on your air," a Pence spokesperson told CNN. CNN had
  only been showing the Trump Q&A portion because the whole thing was very long and full of, well, lies.
  
  On April 8th, CNN showed the full briefing, including the part with Pence. On April 9th, health officials were once 
  again allowed on CNN.
  """,
  people=["Pence", "Fauci"],
  orgs=["CNN", "CDC", "White House"],
  sources=[
    Source(
      title="White House reverses position after blocking health officials from appearing on CNN",
      publication="CNN",
      published="2020-04-09",
      url="https://www.cnn.com/2020/04/09/media/pence-office-tv-bookings-coronavirus/index.html",
      article_copy="./sources/2020-04-09-cnn-white-house-reverses-position.pdf",
    ),
  ],
)
