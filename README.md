docker build -t myhelloapp .
docker run -d -p 5000:5000 myhelloapp
docker ps
docker stop ade281cc548a