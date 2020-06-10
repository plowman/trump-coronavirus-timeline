from models import Event, Source

Event(
  date="2020-05-20",
  title="Trump says having most cases is 'a badge of honor'",
  description="""
  Unable to actually help the country fight this pandemic, Trump tried instead to selling it as a success in testing
  effectiveness.
  
  “I view it as a badge of honor,” Trump explained. “Really, it’s a badge of honor.”
  
  He continued,
  > “When we have a lot of cases,” Trump continued, “I don’t look at that as a bad thing. I look at that as, in a 
  certain respect, as being a good thing because it means our testing is much better.”
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Says U.S. Having World’s Most Confirmed Coronavirus Cases Is “a Badge of Honor”",
      publication="Slate",
      published="2020-05-20",
      url="https://slate.com/news-and-politics/2020/05/trump-worlds-most-coronavirus-cases-badge-of-honor-good-bad-thing.html",
      article_copy="sources/2020-05-20-slate-trump-says-us-having-worlds-most-confirmed-coronavirus-cases-is-a-badge-of-honor.pdf",
    ),
  ],
)
