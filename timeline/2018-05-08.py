from models import Event, Source

Event(
  date="2018-05-08",
  title="Trump fires official in charge of Pandemic response, Timothy Ziemer",
  description="""
  Trump removed Timothy Ziemer from the National Security Council. Ziemer was the Senior Director for Global Health 
  Security and Biothreats. His responsibilities included preparedness against infectious diseases, including leading the
  response in case of a pandemic.
  
  Ziemer's departure follows the earlier departure of homeland security Tom Bossert. Neither Ziemer nor Bossert were 
  ever replaced.
  """,
  people=["Trump", "Bolton", "Ziemer"],
  sources=[
    Source(
      title="Top White House official in charge of pandemic response exits abruptly",
      publication="Washington Post",
      published="2018-05-10",
      url="https://www.washingtonpost.com/news/to-your-health/wp/2018/05/10/top-white-house-official-in-charge-of-pandemic-response-exits-abruptly/",
      article_copy="./sources/2018-05-10-washington-post-top-white-house-official.pdf",
    ),
  ],
)
