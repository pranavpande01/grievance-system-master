from imap_tools import MailBox
import os
from dotenv import load_dotenv 

load_dotenv()
PASSWORD=os.getenv("EMAIL_PASS")
EMAIL_ADDRESS=os.getenv("EMAIL_USER")

covered_mails=[]
with MailBox("imap.gmail.com").login(EMAIL_ADDRESS, PASSWORD,"Inbox") as mb:
    for i in mb.fetch(criteria='FROM "f20212785@pilani.bits-pilani.ac.in" UNSEEN', mark_seen=True): 
        covered_mails.append(i.subject)

print(covered_mails)