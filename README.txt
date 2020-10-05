
STEPS TO RUN THE CODE:

1. pip3 install -r requirements.txt
2. python3 manage.py makemigrations
3. python3 manage.py migrate
4. python manage.py createsuperuser
5. python3 manage.py collectstatic 
6. To Populate test data in the db
    python3 manage.py shell < dbdefault.py
7. python3 manage.py runserver

API Definitions:
1. Register:
    - To register the new user
2. Login:
    - Login Authentication or the registered user
3. List Songs:
    - To list the songs in the db
4. Playlist - Post:
    - To create a new playlist for the user 
5. Playlist - Get:
    - To list all the playlist(s) of the user
6. Playlist - Put:
    - To Add/Remove a song from the user based on the flag in request body
7. UserRating:
    - Update the overall rating of the song based on the star rating given
        by the user
8. GroupSongs:
    - Group the songs in db based on genre and return a result with grouped 
        songs
9. AutoSuggest Songs:
    - Suggesting similar songs to the user based on the genre of the songs
        in the playlist
10. UserRecommndations - Post:
    - Recommend a song to another user
11. UserRecommndations - Get:
    - Get all the song recommendations from one/more users 


