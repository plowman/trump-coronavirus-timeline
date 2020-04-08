from models import Event
from timeline.shared_sources import NAVARRO_CIRCULATES_MEMOS_WARNING_OF_HUGE_DEATH_POTENTIAL

Event(
  date="2020-02-23",
  title="Navarro sends second dire memo, warns 1-2 Million could die, warns of PPE and ventilator needs",
  description="""
  Trump economic advisor Peter Navarro circulated a second memo, this time to officials throughout the NSC.
  
  Specifically it warned:
  * 1-2 million people could die
  * 100 million people could catch the virus
  * We would need over a billion face masks, 200,000 Tyvek suits, 11,000 ventilator circuits, 25,000 powered 
  air-purifying respirators (PAPR's).
  
  It then asked for $3 Billion to support efforts at prevention, treatment, inoculation and diagnostics.
  """,
  people=["Navarro", "Trump"],
  sources=[
    NAVARRO_CIRCULATES_MEMOS_WARNING_OF_HUGE_DEATH_POTENTIAL,
  ],
)
