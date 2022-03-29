# Note
 Full-Stack project for my programming class
 
# Features
login
register
change password
postgresql database saving sessions
add edit delete notes
upload photos to the notes
Docker Image

# Database
I have used Postgresql to create my apps database.

DB Schema:
![122](https://user-images.githubusercontent.com/68077710/159915675-f5f731d0-ed54-4c48-906e-a9ae59920844.png)

# Docker
Instructions:
( I have yet to create an image to persist data for postgresql docker image )

sudo docker pull koenry/noteappdatabase:2 \
sudo docker run -dt -p 5432:5432 --name dbdb  koenry/noteappdatabase:2 \
sudo docker exec -it dbdb bash \
su - postgres \
psql \
run commands from db folder \
CREATE EXTENSION IF NOT EXISTS pgcrypto; \
exit 3 times \

(Seems to be a bug with saving photos on linux will come back to fix this issue, probabaly over folder storing the images) \

sudo docker pull koenry/notebookapp:2 \
sudo docker run -dt -p 5000:5000 -p 80:80 --name appapp  koenry/notebookapp:2 \
sudo docker exec -it appapp bash \
cd Fl... ( tab to find the dir name ) \
python3 run.py \


# Future Roadmap
	roadmap: media queries, page titles, favicon,  register captcha, authentication
