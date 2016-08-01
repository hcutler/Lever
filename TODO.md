Pipeline:

-Person gives you a SOURCE (url, article, person, companyName, opportunities)

SOURCE_e = entities = [person, companyName, organization]
-Scrape SOURCE_e and perform NER
-Tag NE's with labels
-Goals: build database of entities + identify experts


SOURCE_o = opportunities = [job, internship, fellowship, event, conference]
-Scrape SOURCE_o if possible and perform NER
-o/w add SOURCE_o to opportunity bulletin


Tools:
[Lever API](https://github.com/lever/postings-api)
BeautifulSoup

