-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- The database name will be passed as an argument of the mysql command

SELECT tv_show.title, tv_show_genres.genre_id
  FROM tv_shows
INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
  ORDER Y tv_shows.title, tv_show_genres.genre_id ASC;
