from models import Event, Source

Event(
  date="2020-05-05",
  title="Former HHS official says Trump pushed him to award contracts to cronies",
  description="""
  Rick Bright, who was recently fired for his anti-hydroxychloroquine stance, is back, claiming he was pressured to 
  award contracts to Trump cronies during his tenure at the HHS.

  From the article:
  > Rick Bright, the ousted chief of the Biomedical Advanced Research and Development Agency, said he was pressured to 
  steer millions of dollars to the clients of a well-connected consultant.
  
  Why it matters: When we award contracts to connected companies instead of the best companies, it makes our response 
  to this kind of crisis worse.
  """,
  people=["Rick Bright", "Trump", "Kushner", "Robert Kadlec"],
  sources=[
    Source(
      title="Virus Whistle-Blower Says Trump Administration Steered Contracts to Cronies",
      publication="The New York Times",
      published="2020-05-05",
      url="https://www.nytimes.com/2020/05/05/us/politics/rick-bright-coronavirus-whistleblower.html",
      article_copy="sources/2020-05-05-the-new-york-times-virus-whistleblower-says-trump-administration-steered-contracts-to-cronies.pdf",
    ),
  ],
)
