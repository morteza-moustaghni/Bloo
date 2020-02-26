from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

req = Request('https://www.willys.se/butiker/alla', headers={'User-Agent': 'Mozilla/5.0'})

page_html = urlopen(req).read()





















from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///school.db', echo=True)
Base = declarative_base()


class School(Base):

    __tablename__ = "woot"

    id = Column(Integer, primary_key=True)
    name = Column(String)  


    def __init__(self, name):

        self.name = name    


Base.metadata.create_all(engine)

