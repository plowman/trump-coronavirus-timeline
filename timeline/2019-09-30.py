from models import Event, Source

Event(
  date="2019-09-30",
  title="Trump ends Coronavirus early detection program",
  description="""
  The project, launched by the U.S. Agency for International Development in 2009, identified 1,200 different 
  viruses that had the potential to erupt into pandemics, including more than 160 novel coronaviruses. The initiative, 
  called PREDICT, also trained and supported staff in 60 foreign laboratories — including the Wuhan lab that identified 
  SARS-CoV-2, the new coronavirus that causes COVID-19.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump administration ended pandemic early-warning program to detect coronaviruses",
      publication="Los Angeles Times",
      published="2020-04-02",
      url="https://www.latimes.com/science/story/2020-04-02/coronavirus-trump-pandemic-program-viruses-detection",
      article_copy="./sources/2020-04-02-la-times-trump-administration-ended-coronavirus-detection-program.pdf",
    ),
  ],
)
