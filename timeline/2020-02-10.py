from models import Event, Source
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-02-10",
  title="Trump proposes 16 percent cut to CDC",
  description="""
  The Trump budget this year included a 16 percent cut to the CDC. It appears his budget tries to cut the CDC budget 
  basically every year. That he would still attempt to do so during the early signs of a pandemic is insane.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump budget cuts funding for health, science, environment agencies",
      publication="The Washington Post",
      published="2020-02-10",
      url="https://www.washingtonpost.com/science/trump-budget-cuts-funding-for-health-science-environment-agencies/"
          "2020/02/10/9c8dd784-4c2d-11ea-b721-9f4cdc90bc1c_story.html",
      article_copy="./sources/2020-02-10-washington-post-trump-budget-cuts-funding.pdf",
    ),
  ],
)

Event(
  date="2020-02-10",
  title="Trump says, 'I think the virus is going to be — it’s going to be fine.'",
  description="""
  That's the whole quote. I haven't dug into the original source yet.
  """,
  people=["Trump"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)
