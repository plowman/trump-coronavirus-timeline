from models import Event, Source

Event(
  date="2020-04-18",
  title="Trump says there should be consequences if China was 'knowingly responsible'",
  description="""
  As usual, this is scary in part because a possible interpretation of "knowingly responsible" is that they did it on
  purpose, which is of course nonsense.
  
  The full quote is this:
  > Reporter: "do you think that there should be some consequences if in the end you know China was responsible for all 
  of this"
  Trump: well if they were knowingly responsible, certainly. If they did if, it was a mistake, a mistake is a mistake, 
  but if they were knowingly responsible yeah then there should be consequences.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Warns Of 'Consequences' If China Was 'Knowingly Responsible' For Outbreak",
      publication="NPR",
      published="2020-04-18",
      url="https://www.npr.org/2020/04/18/837545140/trump-to-hold-briefing-on-coronavirus-developments",
      article_copy="sources/2020-04-18-npr-trump-china-knowingly-responsible.pdf",
    ),
  ],
)
