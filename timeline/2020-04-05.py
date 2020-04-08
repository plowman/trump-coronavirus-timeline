from models import Event, Source

Event(
  date="2020-04-05",
  title="Trump again pushes Hydroxychloroquine, saying 'What do you have to lose?'",
  description="""
  “If it does work, it would be a shame we did not do it early,” Mr. Trump said, noting the federal government had 
  purchased and stockpiled 29 million pills of the drug. “We are sending them to various labs, our military, we’re 
  sending them to the hospitals.”

  “There are side effects to hydroxychloroquine,” Dr. Ranney, an emergency physician at Brown University. “It causes 
  psychiatric symptoms, cardiac problems and a host of other bad side effects.”
  
  Why it's bad: this is a pretty serious drug with serious side effects. It's unbelievably irresponsible to tell people
  to just take it and not worry about it.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Ignoring Expert Opinion, Trump Again Promotes Use of Hydroxychloroquine",
      publication="The New York Times",
      published="2020-04-05",
      url="https://www.nytimes.com/2020/04/05/us/politics/trump-hydroxychloroquine-coronavirus.html",
      article_copy="./sources/2020-04-05-new-york-times-ignoring-expert-opinion.pdf",
    ),
  ],
)
