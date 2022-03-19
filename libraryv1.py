import sqlite3

connectionHandler = sqlite3.connect('library.db')

cursor = connectionHandler.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Artist (
                               ArtistID int PRIMARY KEY,
                               ArtistSurname TEXT,
                               ArtistName TEXT);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ALbum (
                               AlbumID int PRIMARY KEY,
                               ArtistID int,
                               AlbumName TEXT,
                               FOREIGN KEY (ArtistID)
                               REFERENCES Artist (ArtistID)
                               );''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                               CustomerID int PRIMARY KEY,
                               UserName TEXT
                               ); ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Subscription (
                               SubscriptionID int PRIMARY KEY,
                               AlbumID int,
                               CustomerID int,
                               FOREIGN KEY (AlbumID) REFERENCES Album (AlbumID),
                               FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
                               );''')




cursor.execute('''INSERT INTO Artist VALUES (1, 'Jenny', 'Hval')   ''')
cursor.execute('''INSERT INTO Artist VALUES (2, 'Alice', 'Coltraine')   ''')
cursor.execute('''INSERT INTO Artist VALUES (3, 'Smith', 'Patty')   ''')
cursor.execute('''INSERT INTO Artist VALUES (4, 'Ersoy', 'Bulent')   ''')
cursor.execute('''INSERT INTO Artist VALUES (5, 'King', 'Carol')   ''')


cursor.execute('''INSERT INTO Album VALUES (1, 1, 'Classic Objects')   ''')
cursor.execute('''INSERT INTO Album VALUES (2, 2, 'Journey in Satchidananda')   ''')
cursor.execute('''INSERT INTO Album VALUES (3, 3, 'Horses')   ''')
cursor.execute('''INSERT INTO Album VALUES (4, 4, 'Alaturka 2000')   ''')
cursor.execute('''INSERT INTO Album VALUES (5, '5', 'Tapestry')   ''')

cursor.execute('''INSERT INTO Customer VALUES (1, 'melanie')   ''')
cursor.execute('''INSERT INTO Customer VALUES (2, 'mikki')   ''')
cursor.execute('''INSERT INTO Customer VALUES (3, 'kaia')   ''')
cursor.execute('''INSERT INTO Customer VALUES (4, 'harper')   ''')


cursor.execute('''INSERT INTO Subscription VALUES (1, 1, 1)   ''')
cursor.execute('''INSERT INTO Subscription VALUES (2, 2, 1)   ''')
cursor.execute('''INSERT INTO Subscription VALUES (3, 3, 1)   ''')
cursor.execute('''INSERT INTO Subscription VALUES (4, 4, 1)   ''')


def lookUpAlbum(n):
    global cursor
    parameter = (n, )
    #cursor = cursor.execute("SELECT * FROM Album WHERE AlbumName = ?",parameter)
    cursor = cursor.execute("SELECT AlbumName, ArtistSurname, ArtistName "
                            "FROM Artist INNER JOIN Album on Album.ArtistID = Artist.ArtistID "
                            "WHERE AlbumName = ?;",parameter)


    result = []
    for row in cursor:
        result.append(row)
    return result

    
def uiManager():
    print("1. Look up details")
    print("2. Add new album")
    print("3. Add new user")
    print("4. Add new album")
    choice = input()
    if choice == "1":
        print("1. Look up album")
        print("2. Look up artist")
        print("3. Loop up artist")
        choice = input()
        if choice == "1":
            print("Enter album name:")
            answer = input()
            albumName = answer.strip('\n')
            print(lookUpAlbum(albumName))

uiManager()