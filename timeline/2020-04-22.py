from models import Event, Source

Event(
  date="2020-04-22",
  title="Vaccine expert removed from HHS post for questioning hydroxychloroquine",
  description="""
  From the article,
  > Dr. Rick Bright was abruptly dismissed this week as the director of the Department of Health and Human Services’ 
  Biomedical Advanced Research and Development Authority, or BARDA, and removed as the deputy assistant secretary for 
  preparedness and response.
  
  His quote brings the real fire:
  > “I believe this transfer was in response to my insistence that the government invest the billions of dollars 
  allocated by Congress to address the Covid-19 pandemic into safe and scientifically vetted solutions, and not in 
  drugs, vaccines and other technologies that lack scientific merit,” he said in his statement. “I am speaking out 
  because to combat this deadly virus, science — not politics or cronyism — has to lead the way.”
  
  Why it matters: especially with growing evidence that hydroxychloroquine doesn't work, he is one more example of how
  Trump would rather slow down vaccine development than have anyone question him.
  """,
  people=["Dr. Rick Bright"],
  orgs=["HHS"],
  sources=[
    Source(
      title="A vaccine expert says he was removed for questioning hydroxychloroquine",
      publication="The New York Times",
      published="2020-04-22",
      url="https://www.nytimes.com/2020/04/22/us/coronavirus-live-coverage.html#link-48b66328",
      article_copy="sources/2020-04-22-new-york-times-doctor-forced-out-for-questioning-nonsense-drugs.pdf",
    ),
  ],
)
