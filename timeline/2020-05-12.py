from models import Source, Event

Event(
  date="2020-05-12",
  title="Trump holds coronavirus victory event, says \"We have met the moment and we have prevailed\"",
  description="""
  Upon questioning, Trump clarified that we have only prevailed over the testing portion of the "the moment".
  
  His full quote of course shows this is nonsense because he doesn't mention tests:
  > "In every generation through every challenge and hardship and danger, America has risen to the task. We have met the 
  moment and we have prevailed. Americans do whatever it takes to find solutions, pioneer breakthroughs and harness the 
  energies we need to achieve a total victory. Day after day we’re making tremendous strides with the dedication of our 
  doctors and nurses, these are incredible people, these are brave people, these are warriors."
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump wanted a coronavirus victory event. It ended when he stalked off after clashing with two female reporters.",
      publication="The Washington Post",
      published="2020-05-12",
      url="https://www.washingtonpost.com/nation/2020/05/12/trump-meltdown-coronavirus-testing/",
      article_copy="sources/2020-05-12-the-washington-post-trump-wanted-a-coronavirus-victory-event-it-ended-when-he-stalked-off-after-clashing-with-two-female-reporters.pdf",
    ),
  ],
)
