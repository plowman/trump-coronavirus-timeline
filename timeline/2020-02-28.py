from models import Event, Source

Event(
  date="2020-02-28",
  title="Trump says \"Democrats are politicizing the Coronavirus\", says, \"this is their new hoax\".",
  description="""
A lot of Trumpkins are debating this quote now, but he clearly says the coronavirus is "their new hoax" in the same way
that impeachment was a hoax.

The full Trump quote is this:

"Now the Democrats are politicizing the coronavirus. You know that coronavirus? They're politicizing it. 

We did one of the great jobs. You say, "How's president Trump doing?" They go, "oh not good not good."

They have no truth they don't have any clue they can't even count their votes in Iowa they can't even they can't count 
their votes.

One of my people came up to me and said Mr. President they tried to beat you on Russia Russia Russia that didn't work 
out too well they couldn't do it they tried the impeachment hoax that was on a perfect conversation they tried anything 
they tried it over and over they've been doing it since you got in it's all turning they lost it's all turning think of
it think of it and *this is their new hoax.*

But you know we did something that's been pretty amazing we're 15 people in this massive country and because of the fact
that we went early we went early we could have had a lot more than that."
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Donald Trump holds \"Keep America Great\" rally in Charleston, S.C.",
      publication="Global News on YouTube",
      published="2020-02-28",
      url="https://youtu.be/NbwCjL7HC1c?t=293",
      article_copy="./sources/2020-02-28-global-news-youtube-charleston-trump-rally.jpg",
    ),
  ],
)

Event(
  date="2020-02-28",
  title="Trump blames covid outbreak on 'Democrat policy of open borders'.",
  description="""
  Also at the South Carolina rally, Trump said "The Democrat policy of open borders is a direct threat to the health and
  well-being of all Americans. Now you see it with the coronavirus, you see it. You see it with the coronavirus."
  """
)
