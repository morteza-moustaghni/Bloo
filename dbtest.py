from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.ica.se'
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

p_s = soup(page_html, "html.parser")
p_s























# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Date, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///school.db', echo=True)
# Base = declarative_base()


# class School(Base):

#     __tablename__ = "woot"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)  


#     def __init__(self, name):

#         self.name = name    


# Base.metadata.create_all(engine)

