from models import Event, Source

Event(
  date="2020-04-06",
  title="FEMA is seizing coronavirus supplies ordered by hospitals and states",
  description="""
  Despite directing states and hospitals to get their own supplies however they can, the federal government has at the
  same time been seizing the medical supplies that states have ordered.
  
  Multiple governors and hospitals in multiple states are reporting that FEMA has commandeered shipments of masks, 
  ventilators, thermometers, and other medical equipment that had been ordered by various states and hospitals.
  
  It is not at all clear how this equipment is then being routed to various states.
  """,
  orgs=["FEMA"],
  people=["Trump", "Kushner", "Pence"],
  sources=[
    Source(
      title="‘Swept Up by FEMA’: Complicated Medical Supply System Sows Confusiond",
      publication="The New York Times",
      published="2020-04-06",
      url="https://www.nytimes.com/2020/04/06/us/politics/coronavirus-fema-medical-supplies.html",
      article_copy="./sources/2020-04-06-new-york-times-swept-up-by-fema.pdf",
    ),
    Source(
      title="Hospitals say feds are seizing masks and other coronavirus supplies without a word",
      publication="Los Angeles Times",
      published="2020-04-07",
      url="https://www.latimes.com/politics/story/2020-04-07/hospitals-washington-seize-coronavirus-supplies",
      article_copy="./sources/2020-04-07-la-times-feds-seizing-coronavirus-supplies.pdf",
    ),
  ],
)
