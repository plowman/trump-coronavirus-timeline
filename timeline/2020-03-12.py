from models import Event, Source

Event(
  date="2020-03-12",
  title="Trump adds Jared Kushner to the Coronavirus response team",
  description="""
  From the attached article, "Kushner was initially tapped to join the coronavirus response by Trump on March 12, when
  he moved quickly to address the testing shortfalls and pulled in allies with a track record of launching health care 
  companies."
  """,
  people=["Trump", "Kushner"],
  sources=[
    Source(
      title="Behind the scenes, Kushner takes charge of coronavirus response",
      publication="Politico",
      published="2020-04-01",
      url="https://www.politico.com/news/2020/04/01/jared-kushner-coronavirus-response-160553",
      article_copy="./sources/2020-04-01-politico-jared-kushner.pdf",
    ),
  ],
)
