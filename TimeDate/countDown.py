"""
count down for Brisbane Olympics 
23 July 2023
"""
from datetime import date
Oly_date = date.fromisoformat("2032-07-23")
today = date.today()
print(f"Countdown to Brisbane Olympic 2032: {Oly_date - today}")
