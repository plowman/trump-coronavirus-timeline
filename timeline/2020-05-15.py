from models import Event, Source

Event(
  date="2020-05-15",
  title="Trump fires State Department inspector general",
  description="""
  From the article,
  > A Democratic congressional aide said Linick was looking into Pompeo’s “misuse of a political appointee at the 
  Department to perform personal tasks for himself and Mrs. Pompeo.”
  """,
  people=["Trump", "Pompeo"],
  sources=[
    Source(
      title="Top Democrats launch investigation into late-night firing of State Department inspector general",
      publication="The Washington Post",
      published="2020-05-16",
      url="https://www.washingtonpost.com/politics/2020/05/16/state-department-inspector-general-fired-democrats-decry-dangerous-pattern-retaliation/",
      article_copy="sources/2020-05-16-the-washington-post-top-democrats-launch-investigation-into-latenight-firing-of-state-department-inspector-general.pdf",
    ),
  ],
)
