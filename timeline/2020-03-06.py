from models import Event, Source

TRUMP_SAYS_ANYONE_WHO_WANTS_A_TEST_CAN_GET_ONE = Source(
  title="Trump Says ‘People Have to Remain Calm’ Amid Coronavirus Outbreak",
  publication="The New York Times",
  published="2020-03-06",
  url="https://www.nytimes.com/2020/03/06/us/politics/trump-coronavirus-cdc.html",
  article_copy="sources/2020-03-06-new-york-times-trump-coronavirus-cdc.pdf",
)

Event(
  date="2020-03-06",
  title="Trump says, 'Anyone who wants a test can get one'",
  description="""
  This was, of course, not true. At this time only ~10,000 tests had been run in the entire US.
  """,
  people=["Trump"],
  sources=[
    TRUMP_SAYS_ANYONE_WHO_WANTS_A_TEST_CAN_GET_ONE,
    Source(
      title="Testing in the U.S.",
      publication="CDC",
      published="2020-04-14",
      url="https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/testing-in-us.html",
      article_copy="sources/2020-04-14-cdc-coronavirus-testing.pdf",
    ),
  ],
)

Event(
  date="2020-03-06",
  title="Trump wants infected Americans to stay on cruise ship to keep case numbers low",
  description="""
  His full quote is this:
  > “They would like to have the people come off,” he said. “I would like to have the people stay. I told them to make 
    the final decision. I would rather — because I like the numbers being where they are. I don’t need to have the 
    numbers double because of one ship that wasn’t our fault. And it wasn’t the fault of the people on the ship either. 
    OK? It wasn’t their fault, either. And they are mostly Americans.”
  
  Why it matters: Trump is saying the health of humans is less important than how good he thinks he looks. He would 
  rather have 3,533 passengers, mostly Americans, suffer and get infected at sea than have his case count increase. 103 
  passengers eventually tested positive and at least 3 died.
  """,
  people=["Trump"],
  sources=[
    TRUMP_SAYS_ANYONE_WHO_WANTS_A_TEST_CAN_GET_ONE,
  ],
)
