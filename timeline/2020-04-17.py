from models import Event, Source

Event(
  date="2020-04-17",
  title="Trump encourages protests against states deciding what to do on their own",
  description="""
  After releasing formal guidelines that say states get to decide on their own when to open, Trump's next logical step
  was then to encourage protests of states doing exactly that. He doesn't want the blame for opening states early, nor
  does he want the blame for the economy if it's still on the rocks in November, so the best he can do is complain but
  not do anything.
  
  He tweeted, "LIBERATE VIRGINIA, and save your great 2nd Amendment. It is under siege!", "LIBERATE MINNESOTA!", and 
  "LIBERATE MICHIGAN!" while small protests took place in each of those states against stay at home orders. It will not
  surprise you to learn that those three states all have Democratic governors.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Encourages Protest Against Governors Who Have Imposed Virus Restrictions",
      publication="The New York Times",
      published="2020-04-17",
      url="https://www.nytimes.com/2020/04/17/us/politics/trump-coronavirus-governors.html",
      article_copy="sources/2020-04-17-new-york-times-trump-tweets-to-liberate-states.pdf",
    ),
  ],
)

Event(
  date="2020-04-17",
  title="Trump commencement will force 1,000 West Point cadets back to New York",
  description="""
  Trump surprised the West Point administration on April 17th by announcing that he would be giving the commencement 
  speech this year in person. At that point the West Point staff wasn't sure if there would even be a graduation this 
  year.

  Commencement will take place on June 13th. The 1,000 seniors will have to return to New York from their homes on May 
  31st and quarantine for the 14 days before graduation. They will have to isolate in their rooms for those two weeks.

  Why it matters: Trump has decided to drag a thousand soldiers and untold hundreds of staff members back to the 
  epicenter of the outbreak so that he can feel like a big deal.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Speech to Bring 1,000 West Point Cadets Back to Campus",
      publication="The New York Times",
      published="2020-04-24",
      url="https://www.nytimes.com/2020/04/24/us/politics/coronavirus-trump-west-point.html",
      article_copy="sources/2020-04-24-new-york-times-trump-west-point-speech.pdf",
    ),
  ],
)
