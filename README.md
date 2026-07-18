# ✈️ Flask Flight Booking System

A web-based Flight Booking System built using **Flask**, **SQLAlchemy**, and **Docker**. This project demonstrates how to containerize a Flask application and deploy it using Docker.

---

##  Features

- User Registration & Login
- Flight Search
- Flight Booking
- SQLite Database
- Responsive UI
- Docker Support

---

##  Tech Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Docker

---

##Project Structure

```
flask-flight-booking/
│── app.py
│── requirements.txt
│── Dockerfile
│── README.md
│── templates/
│── static/
└── database.db
```

---

# 🐳 Docker Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/OM0126/flask-flight-booking.git
cd flask-flight-booking
```

---

## Step 2: Build Docker Image

```bash
docker build -t flight-booking .
```

---

## Step 3: Run Docker Container

```bash
docker run -d --name flight-app -p 5000:5000 flight-booking
```

---

## Step 4: Verify Container

```bash
docker ps
```

Expected Output

```
CONTAINER ID   IMAGE              PORTS
xxxxxxxxxxxx   flight-booking     0.0.0.0:5000->5000/tcp
```

---

## Step 5: Open Application

### Local Machine

```
http://localhost:5000
```

### AWS EC2

```
http://<EC2-PUBLIC-IP>:5000
```

---

# 🐳 Useful Docker Commands

## View Running Containers

```bash
docker ps
```

## View All Containers

```bash
docker ps -a
```

## View Images

```bash
docker images
```

## View Logs

```bash
docker logs -f flight-app
```

## Stop Container

```bash
docker stop flight-app
```

## Start Container

```bash
docker start flight-app
```

## Remove Container

```bash
docker rm -f flight-app
```

## Remove Image

```bash
docker rmi flight-booking
```

---

# 🔄 Rebuild After Making Changes

```bash
docker stop flight-app

docker rm flight-app

docker build -t flight-booking .

docker run -d --name flight-app -p 5000:5000 flight-booking
```

---

#  Common Mistakes

##  Wrong

```bash
docker bulid -t flight-booking .
```

## Correct

```bash
docker build -t flight-booking .
```

---

## Wrong

```bash
git staus
```

## Correct

```bash
git status
```

---

## Wrong

```bash
git commit -u "Added Dockerfile"
```

##  Correct

```bash
git commit -m "Added Dockerfile"
```

---

##  Wrong

```bash
docker logs booking
```

**Reason:** `booking` is an **image**, not a container.

## Correct

```bash
docker logs flight-app
```

---

## Wrong

```bash
docker run -it flight-booking
```

This starts an interactive container without publishing the port.

##  Correct

```bash
docker run -d --name flight-app -p 5000:5000 flight-booking
```

---

#  Troubleshooting

## Application not opening?

Check the following:

- Flask is running with:

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

- Docker container is running

```bash
docker ps
```

- Port mapping is correct

```bash
-p 5000:5000
```

- EC2 Security Group allows **TCP Port 5000**

- Verify locally

```bash
curl http://localhost:5000
```

---


---

# 📈 Future Improvements

- MySQL/PostgreSQL Support
- User Authentication
- Payment Gateway
- Admin Dashboard
- Flight API Integration
- CI/CD Pipeline using GitHub Actions
- Docker Compose
- Kubernetes Deployment

---

# Contributing

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---



---

#  Author

Om 
