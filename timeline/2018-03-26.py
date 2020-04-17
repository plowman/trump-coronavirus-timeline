from models import Event, Source

Event(
  date="2020-03-26",
  title="Robert Redfield, who has never worked in government, becomes CDC director",
  description="""
  How hard could it be, right? Seriously though, in his defense, he has done some great public health work on AIDS. 
  
  However, it's hard not to wonder if someone with experience in government could have done better. For example, the 5
  previous CDC directors all had experience in government.
  """,
  people=[""],
  sources=[
    Source(
      title="AIDS Researcher Robert R. Redfield Named to Lead the C.D.C.",
      publication="The New York Times",
      published="2020-03-21",
      url="https://www.nytimes.com/2018/03/21/health/cdc-robert-redfield-aids.html",
      article_copy="sources/2018-03-21-new-york-times-robert-redfield-appointed-to-cdc.pdf",
    ),
  ],
)
