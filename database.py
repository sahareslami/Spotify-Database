import mysql.connector
from datetime import date
from datetime import timedelta  

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'spotify'
)

cursor = db.cursor()

def is_registered(username , email):
    query = f"SELECT * FROM users where username = '{username}' or email = '{email}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        return True
    else:
        return False



def add_user(username, email , passw, salt,  question , answer , usertype):
    query = """INSERT INTO users (username, email, pass, salt , question, answer, userType) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values = (username, email, passw, salt , question, answer ,usertype )
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()



def add_listener(username, yearOfBirth , firstName, lastName , nationality):
    query = """INSERT INTO listener (username, yearOfBearth, firstName, lastName, nationality) VALUES (%s,%s,%s,%s,%s)"""
    values = (username, yearOfBirth, firstName, lastName, nationality)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()  


 


def get_pass(username):
    query = f"SELECT pass FROM users where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    print(result[0][0])
    return result[0][0]  # return password

def get_salt(username):
    query = f"SELECT salt FROM users where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]

def get_question(username):
    query = f"SELECT question FROM users where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]


def add_artist(username, artisticName, startDate, nationality):
    query = """INSERT INTO artist (username, artisticName, startDate, nationality , isConfirmed) VALUES (%s,%s,%s,%s,%s)"""
    values = (username, artisticName, startDate, nationality, False)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def get_answer(username):
    query = f"SELECT answer FROM users where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]

def valid_username(username):
    query = f"SELECT * FROM users where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        return True
    else:
        return False

def change_pass(username, newpass):
    query = f"UPDATE users SET pass = '{newpass}' WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 

def delete_artist(username):
    query = f"DELETE FROM artist WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 

def delete_user(username):
    query = f"DELETE FROM users WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 

def delete_follow(username):
    query = f"DELETE FROM follow WHERE follower = '{username}' or followed = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()

def delete_listener(username):
    query = f"DELETE FROM listener WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 


def modify_listener(username , firstName , lastName):
    query = f"UPDATE listener  SET firstName = '{firstName}', lastName= '{lastName}' WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()

def follow(follower , following):
    query = """INSERT INTO follow (follower, followed) VALUES (%s,%s)"""
    values = (follower , following)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def unfollow(follower , following):
    query = f"DELETE FROM follow WHERE follower = '{follower}' and followed = '{following}';"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 

def add_album(albumName ,releasedDate):
    query = """INSERT INTO album (albumName, releasedDate) VALUES (%s,%s)"""
    values = (albumName , releasedDate)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def add_album_genre(albumName, albumGenre):
    query = """insert into albumgenre(albumName, albumGenre) values (%s,%s)"""
    values = (albumName, albumGenre)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()


def artist_add_album(artistName, albumName):
    query = """INSERT INTO artistHaveAlbum (artistName, albumName) VALUES(%s, %s)"""
    values = (artistName, albumName)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()


def add_music(musicId, musicName, releasedDate, album, artist, duration):
    query = """insert into music(musicId, musicName, releasedDate, album, artist, duration) 
    values(%s,%s,%s,%s,%s,%s)"""
    values = (musicId, musicName, releasedDate, album, artist, duration)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()


def add_music_genre(musicId, musicGenre):
    query = """insert into musicGenre(musicId, musicGenre) values (%s, %s)"""
    values = (musicId, musicGenre)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

    # insert music
    # insert music genre

def valid_album(albumName):
    query = f"SELECT * FROM album where albumName = '{albumName}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        return True
    else:
        return False

def add_listen(username, musicId, listenDate):
    query = """insert into listen(username, music, listenDate) values (%s , %s, %s)"""
    values = (username, musicId, listenDate)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def valid_music(musicId):
    query = f"SELECT * FROM music where musicId = '{musicId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        return True
    else:
        return False

def change_number_of_playing(musicId , cnt):
    query = f"UPDATE music SET numberOfPlaying = '{cnt}' WHERE musicId = '{musicId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 

def get_number_of_playing(musicId):
    query = f"SELECT numberOfPlaying FROM music where musicId = '{musicId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]

def change_last_listen(musicId , username):
    query = f"UPDATE users SET lastListened = '{musicId}' WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 

def add_playlist(playListId, creator, playListName, creationDate):
    query = "insert into playList(playListId ,creator, playListName, creationDate) values (%s , %s , %s , %s)"
    values = (playListId , creator, playListName, creationDate)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def add_song_to_playlist(playListId, musicId, addedDate):
    query = "insert into palylistHaveMusic(playListId, musicId, addedDate) values (%s , %s , %s)"
    values = (playListId, musicId, addedDate)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def add_playlist_to_usersPlaylist(playLIstId, username):
    query = "insert into userhaveplaylist(playLIstId, username) values (%s , %s)"
    values = (playLIstId, username)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()

def get_number_of_playList(username):
    query = f"SELECT COUNT(playLIstId) FROM userhaveplaylist WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]

def get_typeof_listener(username):
    query = f"SELECT listenerType FROM listener where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]


def valid_playlist(playlistId):
    query = f"SELECT * FROM playlist where playListId = '{playlistId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        return True
    else:
        return False

def delete_music_from_playlist(playlistId , musicId):
    query = f"DELETE FROM palyListHaveMusic WHERE musicId = '{musicId}' and playlistId = '{playlistId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 


def edit_playlist(playListId, playListName):
    query = f"UPDATE playList SET playListName = '{playListName}' WHERE playListId = '{playListId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit() 


def add_liked_music(username, musicId):
    query = "insert into userlikemusic(username, musicId) values(%s, %s)"
    values = (username, musicId)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()


def delete_music_from_likedSong(username, musicId):
    query = f"DELETE FROM userlikemusic WHERE musicId = '{musicId}' and username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()


def add_like_playlist(playlistId , username):
    query = "insert into userLikePlayList(playlistId, username) values(%s , %s)"
    values = (playlistId, username)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()




def get_creator_of_playlist(playlistId):
    query = f"SELECT creator playlist users where username = '{playlistId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]


def get_name_of_playlist(playlistId):
    query = f"SELECT name playlist users where username = '{playlistId}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]



def add_report(username, musicId):
    query = "insert into report(username, musicId) values(%s,%s)"
    values = (username, musicId)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()


def add_premium(username, subscriptionType, subscreationDate, cardNumber, cardExpirationDate):
    query = """insert into premium(username, subscriptionType, subscreationDate, cardNumber, cardExpirationDate)
     values(%s,%s,%s, %s, %s)"""
    values = (username, subscriptionType, subscreationDate, cardNumber, cardExpirationDate)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()


def add_free(username):
    query = """insert into free(username) value(%s)"""
    values = (username,)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()



def delete_free(username):
    query = f"delete from free where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()


def admin_confirmed(username):
    query = f"UPDATE artist SET isConfirmed = true WHERE username =  '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()


def get_followers_of_users(username):
    follower_list = []
    query = f"select follower from follow where followed = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"

    for item in result:
        follower_list.append({"username" : item[0]})
    out = {"follower": follower_list}
    return out

def get_following_of_users(username):
    following_list = []
    query = f"select followed from follow where follower = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        following_list.append({"username": item[0]})
    out = {"following": following_list}
    return out


def get_info_of_album(albumName):
    album_info = []
    query = f"select musicName, duration, releasedDate from music where album = '{albumName}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        album_info.append(
            {"musicName": item[0], "Duration": item[1], "releasedDate": item[2]})
    out = {"Album": album_info}
    return out


def get_info_of_playlist(playlistId):
    playlist_info = []
    query = f""" select m.musicName, phm.addedDate, m.duration
    from palylisthavemusic as phm, music as m
    where phm.playListId = '{playlistId}' and phm.musicId = m.musicId"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        playlist_info.append({"musicName": item[0], "addedDate": item[1], "duration": item[2]})
    out = {"playlist": playlist_info}
    return out

def delete_from_premium(username):
    query = f""" delete from premium where username = '{username}'"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()

def update_listener_type(username):
    query = f"""update listener set listenerType = 'free' where username = '{username}'"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    db.commit()


 

def change_type_of_users():
    changed_users = []
    query = "select username, subscriptionType, subscreationDate from premium"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        if item[1] == "1 Year":
            if item[2] + timedelta(days=365) > date.today():
                delete_from_premium(item[0])
                update_listener_type(item[0])
                add_free(item[0])
                changed_users.append({"username" : item[0]})
        if item[1] == "3 Month":
            if item[2] + timedelta(days = 90) > date.today():
                delete_from_premium(item[0])
                update_listener_type(item[0])
                add_free(item[0])
                changed_users.append({"username": item[0]})
        if item[1] == "1 Month":
            if item[2] + timedelta(days = 30) > date.today():
                delete_from_premium(item[0])
                update_listener_type(item[0])
                add_free(item[0])
                changed_users.append({"username": item[0]})

    out={"change_users": changed_users}
    return out

def get_last_listen(username):
    query = f"select lastListened from users where username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]

def last_listen_following(username):
    following_list = []
    query = f"select followed from follow where follower = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        music = get_last_listen(item[0])
        following_list.append({"username": item[0] , "musicname" : music})
    out = {"following": following_list}
    return out


def top_five_song(username):
    top_five = []
    query = f"""select musicName, releasedDate from music where artist = '{username}'
    order by releasedDate asc"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        top_five.append({"musicName": item[0], "releasedDate": item[1]})
        
        out = {"top_five": top_five}
    return out


def favorit_artist(username):
    query = f""" select m.artist, count(musicId)
    from listen as l, music as m
    where l.username = '{username}'
    group by(m.artist)"""

    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    
    max_count = 0
    fav_artist = ""
    for item in result:
        if item[1] > max_count:
            max_count = item[1]
            fav_artist = item[0]

    out = {"top_five": [{"username" : fav_artist}]}
    return out

def top_five_in_week(startDate , endDate):
    top_list = []
    query = f""" select music, count(music) from listen where listenDate > '{startDate}' and listenDate < '{endDate}' group by(music) """
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    sorted(result, key=lambda x: x[1])
    for item in result:
        top_list.append({"musicId": item[0]})

    out = {"top_five": top_list}
    return out

def search_album(searched_text):
    artist_list = []
    query = f"select albumName, artistName from artisthavealbum WHERE albumName LIKE '%{searched_text}%'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"

    for item in result:
        artist_list.append({"albumName": item[0], "artistName": item[1]})

    return artist_list


def search_music(searched_text):
    music_list = []
    query = f"""select musicName, artist from music WHERE musicName or musicId LIKE '%{searched_text}%';"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"

    for item in result:
        music_list.append({"musicName": item[0], "artistName": item[1]})

    return music_list


def search_playlist(searched_text):
    playlist_list = []
    query = f"""select playListId from playlist WHERE playListName LIKE '%{searched_text}%'"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"

    for item in result:
        playlist_list.append({"playListId": item[0]})

    return playlist_list


def search_artist(searched_text):
    artist_list = []
    query = f"""select username, artisticname from artist WHERE username or artisticName LIKE '%{searched_text}%'"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"

    for item in result:
        artist_list.append({"username": item[0], "artisticName": item[1]})
    return artist_list


def search_listener(searched_text):
    listener_list = []
    query = f"""select username, firstname from listener WHERE username or firstname LIKE  '%{searched_text}%'"""
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"

    for item in result:
        listener_list.append({"username": item[0], "firstname": item[1]})
    return listener_list

def get_userType(username):
    query = f"select userType from users WHERE username = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result[0][0]


def get_artist_name(username):
    query = f"select username, artisticName from artist WHERE username  = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result


def get_listener_name(username):
    query = f"select username, firstname, lastname from listener WHERE username  = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result

def get_number_of_follower(username):
    query = f"SELECT COUNT(follower) FROM follow where followed = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result



def get_number_of_following(username):
    query = f"SELECT COUNT(followed) FROM follow where follower = '{username}'"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result


def get_users_playlist(username):
    query = f" select playListName from playlist WHERE creator = '{username}' "
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result
    


def get_playList_music(playlistId):
    query = f"SELECT COUNT(musicId) FROM palylisthavemusic where playListId = '{playlistId}' "
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result


def get_last_update_of_playlist(playlistId):
    query = f"""SELECT max(addedDate) AS "Max Date" FROM palylisthavemusic where playlistId = '{playlistId}' """
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result

def number_of_music_of_artist(username):
    query = f"select a.username, count(musicId) from artist as a, music as m where a.username = m.artist group by(a.username)"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    sorted(result, key=lambda x: x[1])
    return result



def get_dominant_genre(username):
    query = f""" select albumGenre as genre , count(ag.albumGenre) as count
    from artisthavealbum as aHaveA, albumgenre as ag
    where aHaveA.albumName = ag.albumName and aHaveA.artistName = '{username}'
    group by(ag.albumGenre) """

    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    sorted(result, key=lambda x: x[1])
    return result[-1]


def get_albums_of_artist(username):
    query = f""" select aha.albumName , a.releasedDate
    from artisthavealbum as aha, album as a
    where  aha.artistName = '{username}' and aha.albumName = a.albumName """

    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    return result


def get_most_played(username):
    query = f""" select musicName, numberOfPlaying
    from music as m
    where m.artist = '{username}'"""

    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    sorted(result, key=lambda x: x[1])
    return result[-1]



""" select aha.albumName , a.releasedDate
from artisthavealbum as aha, album as a
where  aha.artistName = 'sahar' and aha.albumName = a.albumName"""
# 10 ======================


def favorite_genre_of_music(username):
    query = f"""
            select mg.musicGenre, count(l.music)
            from listen as l, music as m, musicgenre as mg
            where l.music = m.musicId and mg.musicId = m.musicId
	        and l.username = {username}
            group by(mg.musicGenre)"""

    genres = []
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return '-1'
    for item in result:
        genres.append({'genre_name': item[0]})
    out = {"favorite_genres": genres}
    return out


def recommend_music_based_on_genre(beginningDate, endDate, musicGenre):
    query = f"""
    select musicName
    from music as m, musicgenre as mg
    where m.musicId = mg.musicId and mg.musicGenre = {musicGenre} 
	and m.releasedDate < {endDate} and m.releasedDate > {beginningDate}
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    musics = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        musics.append({'musci_name': item[0]})
    out = {"recommended_music": musics}
    return out


def recommendPopularMusicBasedOnGenre(musicGenre):
    query = f"""
    select musicName, count(l.music)
    from listen as l, music as m, musicgenre as mg
    where l.music = m.musicId and m.musicId = mg.musicId and mg.musicGenre = {musicGenre}
    group by(l.music)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    musics = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        musics.append({'musci_name': item[0], 'count': item[0]})
    out = {"recommended_music": musics}
    return out


# 11 ==========================
def dominantGenreOfPlaylist(playlistId):
    query = f"""
    select mg.musicGenre, count(phm.musicId)
    from playlist as p, palylisthavemusic as phm, musicgenre as mg
    where p.playListId = phm.playListId and mg.musicId = phm.musicId and p.playListId = {playlistId}
    group by(musicGenre)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    genres = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        genres.append({'music_name': item[0], 'count': item[1]})
    out = {"dominant_genres": genres}
    return out


def find_suspects_listener():
    ans = []
    query = "select  username from free"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        ans.append({"username" : item[0]})
    out = {" suspects_listener" : ans}
    return out



def recommendPopularMusicBasedOnGenre(musicGenre):
    query = f"""
    select musicName, count(l.music)
    from listen as l, music as m, musicgenre as mg
    where l.music = m.musicId and m.musicId = mg.musicId and mg.musicGenre = {musicGenre}
    group by(l.music)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    genres = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        genres.append({'music_name': item[0], 'count': item[1]})
    out = {"music_name": genres}
    return out


# 12 ===============================
def findFans(artist_username):
    query = f"""
    select l.username, count(musicId)
    from listen as l, music as m
    where l.music = m.musicId and artist = 'kasra'
    group by(l.username)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    listeners = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        listeners.append({'listener_id': item[0], 'count': item[1]})
    out = {"listeners": listeners}
    return out


def favoriteGenreOfUser(username):
    favorite_genre_of_music(username)


# def dominantGenre(artist_name):
#     dominantGenre


# 13 ===============================

def recommendArtistToListene(listener_username):
    query = f"""
    select  a.artisticName
    from listener as l, artist as a
    where l.nationality = a.nationality and l.username = {listener_username}
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    artists = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        artists.append({'musci_name': item[0]})
    out = {"recommended_artists": artists}
    return out


def recommendArtistToArtist(artist_username):
    query = f"""
    select  a2.artisticName
    from artist as a1, artist as a2
    where a1.nationality = a2.nationality and a1.username = 'sahar'  and a1.username != a2.username
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    artists = []
    if cursor.rowcount > 0:
        result = cursor.fgetchall()
    else:
        return "-1"
    for item in result:
        artists.append({'musci_name': item[0]})
    out = {"recommended_artists": artists}
    return out
# 10 ======================


def favoriteGenreOfUser(username):
    query = f"""
            select mg.musicGenre, count(l.music)
            from listen as l, music as m, musicgenre as mg
            where l.music = m.musicId and mg.musicId = m.musicId
	        and l.username = {username}
            group by(mg.musicGenre)"""

    genres = []
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return '-1'
    for item in result:
        genres.append({'genre_name': item[0]})
    out = {"favorite_genres": genres}
    return out


def recommend_music_based_on_genre(beginningDate, endDate, musicGenre):
    query = f"""
    select musicName
    from music as m, musicgenre as mg
    where m.musicId = mg.musicId and mg.musicGenre = {musicGenre}
	and m.releasedDate < {endDate} and m.releasedDate > {beginningDate}
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    musics = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        musics.append({'musci_name': item[0]})
    out = {"recommended_music": musics}
    return out


def recommendPopularMusicBasedOnGenre(musicGenre):
    query = f"""
    select musicName, count(l.music)
    from listen as l, music as m, musicgenre as mg
    where l.music = m.musicId and m.musicId = mg.musicId and mg.musicGenre = {musicGenre}
    group by(l.music)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    musics = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        musics.append({'musci_name': item[0], 'count': item[0]})
    out = {"recommended_music": musics}
    return out


# 11 ==========================
def dominantGenreOfPlaylist(playlistId):
    query = f"""
    select mg.musicGenre, count(phm.musicId)
    from playlist as p, palylisthavemusic as phm, musicgenre as mg
    where p.playListId = phm.playListId and mg.musicId = phm.musicId and p.playListId = {playlistId}
    group by(musicGenre)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    genres = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        genres.append({'music_name': item[0], 'count': item[1]})
    out = {"dominant_genres": genres}
    return out


# 12 ===============================
def findFans(artist_username):
    query = f"""
    select l.username, count(musicId)
    from listen as l, music as m
    where l.music = m.musicId and artist = 'kasra'
    group by(l.username)
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    listeners = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        listeners.append({'listener_id': item[0], 'count': item[1]})
    out = {"listeners": listeners}
    return out


# def dominantGenre(artist_name):
#     dominantGenre


# 13 ===============================

def recommendArtistToListene(listener_username):
    query = f"""
    select  a.artisticName
    from listener as l, artist as a
    where l.nationality = a.nationality and l.username = {listener_username}
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    artists = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        artists.append({'music_name': item[0]})
    out = {"recommended_artists": artists}
    return out


def recommendArtistToArtist(artist_username):
    query = f"""
            select  a2.artisticName
            from artist as a1, artist as a2
            where a1.nationality = a2.nationality and a1.username = {artist_username}  and a1.username != a2.username
    """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    artists = []
    if cursor.rowcount > 0:
        result = cursor.fgetchall()
    else:
        return "-1"
    for item in result:
        artists.append({'music_name': item[0]})
    out = {"recommended_artists": artists}
    return out

# 15 =============================


def startDateOfArtist():
    query = f"""
            select username, startDate
            from artist
            """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    artists = []
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        artists.append({'artist_username': item[0]})
    out = {"recommended_artists": artists}
    return out


# def followerNumber():
    # search 2


# def followingNumber

# 16 ====================
def userListeningTimeEachDay(date):


    query = f"""select sum(m.duration)
                from listen as l, music as m
                where l.music = m.musicId and l.listenDate = {date}
                group by(l.username)
                """
    cursor.db.execute(buffered=True)
    cursor.execute(query)
    listeners = []
    if cursor.rowcount > 0:
            result = cursor.fetchall()
    else:
        return "-1"
    for item in result:
        listeners.append({'username': item[0], 'time': item[1]})
    out = {"listeners": listeners}
    return out

def list_of_artist():
    query = f"select a.username, count(musicId) from artist as a, music as m where a.username = m.artist group by(a.username)"
    cursor = db.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        return "-1"
    sorted(result, key=lambda x: x[1])
    return result
