from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instatiate session
Session = sessionmaker(db)
# open session
session = Session()


# create database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - Select all records from "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" <> ")
    print(artist.Name)


# Query 2 - Selecto only "Queen" from the "Artist" table
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" <> ")


# Query 3 - Selecto only by "ArtistId" from the "Artist" table
artistById = session.query(Artist).filter_by(ArtistId=51).first()
print(artistById.ArtistId, artistById.Name, sep=" <> ")


# Query 4 - select only the albums with "ArtistId" #51 on the "Album" table
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" <> ")


# Query 5 - 
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId, 
        track.Name, 
        track.AlbumId, 
        track.GenreId, 
        track.Composer, 
        track.Milliseconds, 
        track.Bytes, 
        track.UnitPrice, 
        sep=" | "
    )
