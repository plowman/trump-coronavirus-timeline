from models import Event, Source

Event(
  date="2020-03-11",
  title="World Health Organization declares covid-19 a pandemic",
  description="""
  The director of the WHO declared that they consider covid-19 to be a pandemic.
  """,
  people=[],
  sources=[
    Source(
      title="WHO Director-General's opening remarks at the media briefing on COVID-19 - 11 March 2020",
      publication="World Health Organization",
      published="2020-03-11",
      url="https://www.who.int/dg/speeches/detail/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020",
      article_copy="sources/2020-03-11-who-director-declares-pandemic.pdf",
    ),
  ],
)
