import hashlib
from random import randrange
from flask import Flask, render_template , request , Response , jsonify , make_response
import json
import database as db
from datetime import date
import databb as bd
from datetime import timedelta  

app = Flask(__name__)

def hashPassword(password, salt):
    salted_password = salt + password
    return hashlib.md5(salted_password.encode()).hexdigest()


@app.route("/")
def shiva():
    return render_template('index.html') 

@app.route("/json" , methods = ['POST'])
def jsonn():
    if request.is_json:
        req = request.get_json()
        response = {
            "message" : "JSON recieved",
            "name" : req['name']
        }
        res = make_response(jsonify(response) , 200)
        return res
    else:
        res = make_response(jsonify({"message : No JSON recevied"}) , 400)
        return res

@app.route("/signUpListener" , methods = ['POST'])
def signUpListener():
    if request.is_json:
        req = request.get_json()
        if db.is_registered(req['username'] , req['email']) == True:
            return  make_response(jsonify({ "message" :  "email or username is already taken!"})  , 200)  
        salt = str(randrange(10 ** 48, 10 ** 49))
        hashed_password = hashPassword(req['pass'], salt)
        db.add_user(req['username'] , req['email'] , hashed_password, salt , req['question'] , req['answer'] , 'listener')
        db.add_listener(req['username'], req['yearOfBirth'] , req["firstName"] , req['lastname'] , req['nationality'])
        db.add_free(req['username'])
        db.add_playlist(req["username"] + "LikedSong" ,req['username'] , "liked song" , date.today())
        db.add_playlist_to_usersPlaylist(req["username"] + "likedSong" , req['username'])
        response = {
            "message" : "JSON recieved",
            "name" : req.get('username')
        }

        res = make_response(jsonify(response) , 200)
        return res
    else:
        res = make_response(jsonify({"message : No JSON recevied"}) , 400)
        return res


@app.route("/signUpArtist" , methods = ['POST'])
def signUpArtist():
    if request.is_json:
        req = request.get_json()

        if db.is_registered(req['username'] , req['email']):
            return  make_response(jsonify({ "message" :  "email or username is already taken!" , "name" : req.get('username')}) , 200)
        
        salt = str(randrange(10 ** 48, 10 ** 49))
        hashed_password = hashPassword(req['pass'], salt)

        db.add_user(req['username'] , req['email'] , hashed_password , salt , req['question'] , req['answer'] , req['userType'])
        db.add_artist(req['username'] , req['artisticName'] , req['startDate'] , req['nationality'])
        response = {
            "message" : "JSON recieved",
            "name" : req.get('username')
        }
        res = make_response(jsonify(response) , 200)
        return res
    else:
        res = make_response(jsonify({"message : No JSON recevied"}) , 400)
        return res

@app.route("/login" , methods = ['POST'])
def login():
    if request.is_json:
        req = request.get_json()
        response = {
            "message" : "JSON recieved",
            "name" : req.get('username')
        }
        if db.get_pass(req['username']) == "-1":
           return  make_response(jsonify({ "message" : "email or username is already taken!", "name" : req.get('username')}) , 200)

        salt = db.get_salt(req['username'])
        hashed_password = hashPassword(req['pass'], salt)

        if hashed_password == db.get_pass(req['username']): 
            return  make_response(jsonify({ "message" : "correct", "name" : req.get('username')}) , 200)
        else:
          return  make_response(jsonify({ "message" :  "incorrect" , "name" : req.get('username')}) , 200)
    else:
        res = make_response(jsonify({"message : No JSON recevied"}) , 400)
        return res

@app.route("/changePassPhase1" , methods = ['POST'])
def askQuestion():
    if request.is_json:
        req = request.get_json()

        question = db.get_question(req['username'])
        if question == "-1":
            return make_response(jsonify({ "message" : "cant find username"}) , 200)
        return  make_response(jsonify({ "question" :  question , "name" : req.get('username')}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/changePassPhase2" , methods = ['POST'])
def getAnswer():
    if request.is_json:
        req = request.get_json()
 
        question = db.get_question(req['username'])
        if question == "-1":
            return make_response(jsonify({ "message" : "cant find username"}) , 200)
        answer = db.get_answer(req['username'])
        if answer == req['answer']:
            return make_response(jsonify({ "message" : "identify correctly"}) , 200)
        else:
            return make_response(jsonify({ "message" : "wrong!"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/changePassPhase3" , methods = ['POST'])
def changePass():
    if request.is_json:
        req = request.get_json()
 
        if db.valid_username(req['username']) == False:
              return make_response(jsonify({ "message" : "cant find username"}) , 200)
        db.change_pass(req['username'] , req['pass'])
        return make_response(jsonify({ "message" : "password change sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/deleteArtist" , methods = ['POST'])
def deleteArtist():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
              return make_response(jsonify({ "message" : "cant find username"}) , 200)
        db.delete_user(req['username'])
        db.delete_artist(req['username'])
        db.delete_follow(req['username'])
        return make_response(jsonify({"message" : "Artist delete sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res


@app.route("/deleteListener" , methods = ['POST'])
def deleteUser():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
              return make_response(jsonify({ "message" : "cant find username"}) , 200)
        db.delete_user(req['username'])
        db.delete_listener(req['username'])
        db.delete_follow(req['username'])
        return make_response(jsonify({"message" : "listener delete sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/modifyUser" , methods = ['POST'])
def modify_user():
    if request.is_json:
        req = request.get_json()

        if db.valid_username(req['username']) == False:
              return make_response(jsonify({ "message" : "cant find username"}) , 200)

        db.modify_listener(req['username'], req["firstName"] , req['lastName'])
        return make_response(jsonify({"message" : "listener modify sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/follow" , methods = ['POST'])
def follow():
    if request.is_json:
        req = request.get_json()

        if db.valid_username(req['follower']) == False or db.valid_username(req['following']) == False:
              return make_response(jsonify({ "message" : "cant find follower or following"}) , 200)

        db.follow(req['follower'], req["following"])
        return make_response(jsonify({"message" : "operation done sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res
    

@app.route("/unfollow" , methods = ['POST'])
def unfollow():
    if request.is_json:
        req = request.get_json()

        if db.valid_username(req['follower']) == False or db.valid_username(req['following']) == False:
              return make_response(jsonify({ "message" : "cant find follower or following"}) , 200)

        db.unfollow(req['follower'], req["following"])
        return make_response(jsonify({"message" : "operation done sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res
    

@app.route("/ArtistAddAblbum" , methods = ['POST'])
def artist_addـalbum():
    if request.is_json:
        req = request.get_json()

        if db.valid_username(req['artistName']) == False:
              return make_response(jsonify({ "message" : "cant find artist"}) , 200)

        db.add_album(req["albumName"] , req["releasedDate"])
        db.add_album_genre(req['albumName'], req['albumGenre'])
        db.artist_add_album(req['artistName'], req['albumName'])
        return make_response(jsonify({"message" : "album add succesfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res



@app.route("/insertMusicToAlbum" , methods = ['POST'])
def add_music():
    # insert music
    # insert music genre
    if request.is_json:
        req = request.get_json()

        if db.valid_album(req['albumName']) == False:
              return make_response(jsonify({ "message" : "cant find album"}) , 200)

        db.add_music(req['musicId'], req['musicName'], req['releasedDate'], req['albumName'], req['artist'] ,req['duration'] )
        db.add_music_genre(req['musicId'] , req['musicGenre'])
        return make_response(jsonify({"message" : "music add sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/playSong" , methods = ['POST'])
def playSong():
    if request.is_json:
        req = request.get_json()

        if db.valid_music(req['musicId']) == False:
              return make_response(jsonify({ "message" : "cant find music"}) , 200)
        if db.valid_username(req['username']) == False:
                return make_response(jsonify({ "message" : "cant find user"}) , 200)

        db.add_listen(req['username'], req['musicId'], req['listenDate'])
        number_of_playing = db.get_number_of_playing(req['musicId']) + 1
        db.change_number_of_playing(req['musicId'] , number_of_playing)
        db.change_last_listen(req['musicId'] , req['username'])
        return make_response(jsonify({"message" : "operation done sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/createPlaylist" , methods = ['POST'])
def create_playlist():
    if request.is_json:
        req = request.get_json()

        if db.valid_username(req['username']) == False:
            return make_response(jsonify({ "message" : "cant find user"}) , 200)

        if db.get_typeof_listener(req['username']) == "free":
            if db.get_number_of_playList(req['username']) >= 5:

                return make_response(jsonify({"message" : "can't have more thant 5 playlist"}) , 200)

        db.add_playlist(req['playlistId'], req['username'], req['playListName'], date.today())
        db.add_playlist_to_usersPlaylist(req['playlistId'] , req['username'])
        return make_response(jsonify({"message" : "operation done sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res


@app.route("/insertSongToPlaylist" , methods = ['POST'])
def insert_song_to_playlist():
    if request.is_json:
        req = request.get_json()

        if db.valid_playlist(req['playlistId']) == False:
                return make_response(jsonify({ "message" : "cant find playlist"}) , 200)

        db.add_song_to_playlist(req['playlistId'], req['musicId'], date.today())
        return make_response(jsonify({"message" : "operation done sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res

@app.route("/deleteMusicFromPlaylist" , methods = ['POST'])
def delete_song_from_playlist():
    if request.is_json:
        req = request.get_json()

        if db.valid_playlist(req['playlistId']) == False or db.valid_music(req['musicId']) == False:
                return make_response(jsonify({"message" : "cant find playlist or music"}) , 200)

        db.delete_music_from_playlist(req['playlistId'], req['musicId'])
        return make_response(jsonify({"message" : "operation done sucessfully"}) , 200)
    else:
        res = make_response(jsonify({"message" : "No JSON recevied"}) , 400)
        return res


@app.route("/updatePlaylist", methods=['POST'])
def update_playlist():
    if request.is_json:
        req = request.get_json()

        if db.valid_playlist(req['playlistId']) == False :
            return make_response(jsonify({"message": "cant find playlist"}), 200)

        db.edit_playlist(req['playlistId'], req['playListName'])
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/likeSong", methods=['POST'])
def like_song():
    if request.is_json:
        req = request.get_json()

        if db.valid_music(req['musicId']) == False or db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  music or username"}), 200)

        db.add_liked_music(req['username'] , req['musicId'])
        db.add_song_to_playlist(req["username"] + "LikedSong", req["musicId"], date.today())
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res

@app.route("/unlikeSong", methods=['POST'])
def unlike_song():
    if request.is_json:
        req = request.get_json()

        if db.valid_music(req['musicId']) == False or db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  music or username"}), 200)

        db.delete_music_from_likedSong(req['username'], req['musicId'])
        db.delete_music_from_playlist(
            req['username'] + "LikedSong", req['musicId'])
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res




@app.route("/likedPlaylist", methods=['POST'])
def like_playlist():
    if request.is_json:
        req = request.get_json()

        if db.valid_playlist(req['playlistId']) == False or db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  playlist or username"}), 200)

        db.add_like_playlist(req['playlistId'] , req['username'])
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/colabPlaylist", methods=['POST'])
def colab_playlist():
    if request.is_json:
        req = request.get_json()
        if db.valid_playlist(req['playlistId']) == False or db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  playlist or username"}), 200)
        db.add_playlist_to_usersPlaylist(req['playlistId'],req['username'])
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/changeToPremium", methods=['POST'])
def change_to_premium():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        db.add_premium(req['username'], req['subscriptionType'] , req['subscreationDate'] , req['cardNumber'], req['cardExpirationDate'])
        db.delete_free(req['username'])
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res
    



@app.route("/adminConfirmed", methods=['POST'])
def admin_confirmed():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        db.admin_confirmed(req['username'])
        
        return make_response(jsonify({"message": "operation done sucessfully"}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/findFollower", methods=['POST'])
def find_number_of_follower():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        result = db.get_followers_of_users(req['username'])
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/findFollowing", methods=['POST'])
def find_number_of_following():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        result = db.get_following_of_users(req['username'])

        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/showAlbumInfo", methods=['POST'])
def show_album_info():
    if request.is_json:
        req = request.get_json()
        if db.valid_album(req['albumId']) == False:
            return make_response(jsonify({"message": "cant find  album"}), 200)

        result = db.get_info_of_album(req['albumId'])
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/showPlaylistInfo", methods=['POST'])
def show_playlist_info():
    if request.is_json:
        req = request.get_json()
        if db.valid_playlist(req['playlistId']) == False:
            return make_response(jsonify({"message": "cant find  playlist"}), 200)

        result = db.get_info_of_playlist(req['playlistId'])
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/changeUsersToFree", methods=['POST'])
def change_to_free():
    if request.is_json:
        result = db.change_type_of_users()
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/showLastListenFollowing", methods=['POST'])
def show_last_following_listen():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        result = db.last_listen_following(req["username"])
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res

@app.route("/showTopFive", methods=['POST'])
def show_top_five():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        result = bd.top_five_song(req["username"])
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/showTopFiveSongInWeek", methods=['POST'])
def show_top_five_song_in_week():
    if request.is_json:
        req = request.get_json()

        start_date = date.today()
        end_date = date.today() - timedelta(days=7)
        result = bd.top_five_in_week(end_date, start_date)
        return make_response(jsonify(result), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/search", methods=['POST'])
def search():
    if request.is_json:
        req = request.get_json()
        final_res = {}
        final_res['Album'] = db.search_album(req['search'])
        final_res['Music'] = db.search_music(req['search'])
        final_res['PlayList'] = db.search_playlist(req['search'])
        final_res['Artist'] = db.search_artist(req['search'])
        final_res['Listener'] = db.search_listener(req['search'])

        return make_response(jsonify(final_res), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/showProfile", methods=['POST'])
def show_profile():
    if request.is_json:
        req = request.get_json()
        final_res = {}
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        user_type = db.get_userType(req['username'])

        if user_type == "artist":
            res = db.get_artist_name(req['username'])
            final_res["username"] = res[0][0]
            final_res["artisticName"] = res[0][1]

        else:
            res = db.get_listener_name(req['username'])
            final_res["username"] = res[0][0]
            final_res["firstName"] = res[0][1]
            final_res["lastname"] = res[0][2]
        final_res["number Of follower"] = db.get_number_of_follower(req['username'])
        final_res["number of following"] = db.get_number_of_following(req['username'])
        res = db.get_users_playlist(req['username'])
        playlist = []
        for item in res:
            number_of_music = db.get_playList_music(item[0])
            last_update = db.get_last_update_of_playlist(item[0])
            playlist.append({"playlistName" : item[0], "numberOfSong" : number_of_music, "last_update" : last_update})
        final_res["playList"] = playlist 
        artist_info = []
        if user_type == "artist":
            res = bd.get_albums_of_artist(req['username'])
            album_of_artist = []
            for item in res:
                album_of_artist.append({"Album Name" : item[0] , "released Date" : item[1]})
            most_played_song = bd.get_most_played(req['username'])
            dominant_genre = bd.get_dominant_genre(req['username'])
            artist_info.append({"album's info" :album_of_artist , "most played song" : most_played_song,
                                "Dominant genre" : dominant_genre})
        final_res["artist info"] = artist_info
        return make_response(jsonify(final_res), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/adminCheckArtistiInOrder", methods=['POST'])
def admin_check():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)
        res = bd.artist_in_order()
        return make_response(jsonify({"Artists" : res}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/favGenre", methods=['POST'])
def fav_genre():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)
        final_res = {}
        final_res["popular"] = bd.commen_music_base_on_genre(req["username"])
        final_res["new"] = bd.new_music_base_on_genre(req["username"])
        return make_response(jsonify(final_res), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/recommendArtist", methods=['POST'])
def recommend_artist():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)
        res = bd.favoriteGenreOfUser(req["username"])
        artist = bd.recommend_artist_based_on_genre(res)
        return make_response(jsonify({"artist" : artist}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/recommendRandomforPlaylist", methods=['POST'])
def recommend_random_for_playlist():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)
        res = bd.recommend_random_for_playlist(req['username'])
        return make_response(jsonify(res), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res

@app.route("/recommendSong", methods=['POST'])
def recommendSong():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)
        res = db.favoriteGenreOfUser(req["username"])
        song = db.recommendPopularMusicBasedOnGenre(res)
        return make_response(jsonify({"artist": artist}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/findSupporter", methods=['POST'])
def findSupport():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)

        return make_response(jsonify({"artist": bd.findFans(req["username"])}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/recommendBaseOnRigion", methods=['POST'])
def recommend_base_on_region():
    if request.is_json:
        req = request.get_json()
        if db.valid_username(req['username']) == False:
            return make_response(jsonify({"message": "cant find  username"}), 200)
        nationaliy = bd.find_user_natinality(req['username'])
        return make_response(jsonify({"albums": bd.album_in_same_region(nationaliy)}), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res

@app.route("/adminFollowUp", methods=['POST'])
def admin_follow_up():
    if request.is_json:
        req = request.get_json()
        res = db.find_suspects_listener()
        return make_response(jsonify(res), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res


@app.route("/leastArtist", methods=['POST'])
def least_artist():
    if request.is_json:
        req = request.get_json()

        return make_response(jsonify(bd.least_artist()), 200)
    else:
        res = make_response(jsonify({"message": "No JSON recevied"}), 400)
        return res

if __name__ == "__main__":
    app.run(debug = True)
