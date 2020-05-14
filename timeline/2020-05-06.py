from models import Event, Source

Event(
  date="2020-05-06",
  title="Trump has begun questioning accuracy of death count in private",
  description="""
  From the article:
  > President Trump has complained to advisers about the way coronavirus deaths are being calculated, suggesting the 
  real numbers are actually lower — and a number of his senior aides share this view, according to sources with direct 
  knowledge.
  
  Why it matters: The only way not to look bad at this point, Trump thinks, is if the dead people... maybe aren't dead?
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump and some top aides question accuracy of virus death toll",
      publication="Axios",
      published="2020-05-06",
      url="https://www.axios.com/trump-coronavirus-death-toll-d8ba60a4-316b-4d1e-8595-74970c15fb34.html",
      article_copy="sources/2020-05-06-axios-trump-death-toll.pdf",
    ),
  ],
)

Event(
  date="2020-05-06",
  title="Trump says he will dissolve the coronavirus task force",
  description="""
  > “We will have something in a different form,”
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Does the Coronavirus Task Force Even Matter for Trump?",
      publication="The New York Times",
      published="2020-05-07",
      url="https://www.nytimes.com/2020/05/07/us/politics/coronavirus-task-force-trump.html",
      article_copy="sources/2020-05-07-the-new-york-times-does-the-coronavirus-task-force-even-matter-for-trump.pdf",
    ),
  ],
)
