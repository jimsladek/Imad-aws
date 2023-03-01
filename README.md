# Imad-aws
docker build -t backend .

docker-compose up -d --force-recreate

docker-compose down


mysql -uroot -p
USE products_db;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    emailId VARCHAR(255)
);

