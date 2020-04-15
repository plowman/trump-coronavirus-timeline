from models import Event, Source

Event(
  date="2019-07-01",
  title="Trump discontinues CDC expert job in China",
  description="""
  The post was held by Dr. Linda Quick. Her job was to train Chinese epidemiologists to help track, investigate, and 
  contain diseases.

  From the article,
  > “It was heartbreaking to watch,” said Bao-Ping Zhu, a Chinese American who served in that role, which was funded by
    the U.S. Centers for Disease Control and Prevention, between 2007 and 2011. “If someone had been there, public health
    officials and governments across the world could have moved much faster.”
  
  Why it matters: If it's true that China knew earlier than anyone else, having CDC experts on the ground in China could
  have helped us realize the severity of the outbreak sooner.
  """,
  people=["Trump", "Linda Quick"],
  sources=[
    Source(
      title="Exclusive: U.S. axed CDC expert job in China months before virus outbreak",
      publication="Reuters",
      published="2020-03-22",
      url="https://www.reuters.com/article/us-health-coronavirus-china-cdc-exclusiv/exclusive-u-s-axed-cdc-expert-job-in-china-months-before-virus-outbreak-idUSKBN21910S",
      article_copy="",
    ),
  ],
)
