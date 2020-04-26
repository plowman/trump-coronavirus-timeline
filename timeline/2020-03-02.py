from models import Event, Source

Event(
  date="2020-03-02",
  title="Trump asks if the flu vaccine might work on coronavirus",
  description="""
  “But the same vaccine could not work?” he said. “You take a solid flu vaccine — you don’t think that would have an 
  impact or much of an impact on corona?”
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump’s baffling coronavirus vaccine event",
      publication="The Washington Post",
      published="2020-03-03",
      url="https://www.washingtonpost.com/politics/2020/03/03/trumps-baffling-coronavirus-vaccine-event/",
      article_copy="sources/2020-03-03-washington-post-trump-vaccine-event.pdf",
    ),
  ],
)
