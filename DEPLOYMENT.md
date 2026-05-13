# Deployment Guide - FastAPI Calculator

This guide provides instructions for deploying the FastAPI Calculator application in various environments.

---

## Table of Contents

1. [Local Development](#local-development)
2. [Docker & Docker Compose](#docker--docker-compose)
3. [GitHub Actions CI/CD](#github-actions-cicd)
4. [Production Deployment](#production-deployment)
5. [Troubleshooting](#troubleshooting)

---

## Local Development

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Virtual environment tool (venv)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/sullyyi/FastAPICalculator.git
   cd fastapi-calculator
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers (for E2E tests)**
   ```bash
   playwright install
   ```

5. **Run the application**
   ```bash
   python main.py
   ```
   
   Or with uvicorn:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the application**
   - Open browser to `http://localhost:8000`

---

## Docker & Docker Compose

### Prerequisites

- Docker Desktop installed and running
- Docker Compose (included with Docker Desktop)

### Running with Docker Compose

```bash
# Build and start all services
docker compose up --build

# Run in background
docker compose up --build -d

# Stop all services
docker compose down

# Remove all data (including database)
docker compose down -v
```

### Services Included

1. **FastAPI Web Application** (Port 8000)
   - Main calculator application
   - Hot-reload enabled for development

2. **PostgreSQL Database** (Port 5432)
   - Database credentials: postgres/postgres
   - Database name: fastapi_db

3. **pgAdmin** (Port 5050)
   - Web-based PostgreSQL management interface
   - Email: admin@example.com
   - Password: admin

### Accessing Services

- **Calculator UI:** http://localhost:8000
- **pgAdmin:** http://localhost:5050
- **API Health Check:** http://localhost:8000/health

### Docker Build Only

```bash
# Build image without starting services
docker build -t fastapi-calculator:latest .

# Run container
docker run -p 8000:8000 fastapi-calculator:latest
```

---

## GitHub Actions CI/CD

### Workflow Overview

The CI/CD pipeline runs automatically on every push to `main` or `develop` branches and on all pull requests.

### Pipeline Stages

#### 1. Unit & Integration Tests
- Runs `test_operations.py` - 59 unit tests
- Runs `test_main.py` - 41 integration tests
- Generates JUnit XML report
- **Status:** Required to pass

#### 2. End-to-End Tests
- Installs Playwright browsers
- Starts FastAPI server
- Runs `test_e2e.py` - 18 end-to-end tests
- Generates JUnit XML report
- **Status:** Requires unit/integration tests to pass first

#### 3. Coverage Report
- Generates coverage metrics for unit and integration tests
- Uploads to Codecov (if configured)
- Creates HTML coverage report as artifact
- **Status:** Informational (doesn't block deployment)

#### 4. Docker Build
- Builds Docker image successfully
- Only runs on `main` branch with push events
- Validates Dockerfile and dependencies
- **Status:** Required to pass before production deployment

#### 5. Summary
- Provides final status report
- Lists all completed checks

### Viewing Results

1. Go to GitHub repository
2. Click **Actions** tab
3. Select workflow run
4. Download artifacts:
   - `test-results-unit-integration` - Unit and integration test report
   - `test-results-e2e` - E2E test report
   - `coverage-report` - HTML coverage analysis

### Local Testing Before Push

```bash
# Run all tests locally
pytest -v

# Run specific test types
pytest test_operations.py -v          # Unit tests
pytest test_main.py -v                # Integration tests
pytest test_e2e.py -v                 # E2E tests (requires server running)

# Generate coverage report
pytest --cov=. --cov-report=html
```

---

## Production Deployment

### Option 1: Deploy to Cloud (Heroku, AWS, Azure, GCP)

#### Heroku Example

1. **Install Heroku CLI**
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create fastapi-calculator
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **Open app**
   ```bash
   heroku open
   ```

### Option 2: Deploy with Docker to Container Registry

#### Docker Hub

1. **Build image**
   ```bash
   docker build -t sullyyi/fastapi-calculator:latest .
   ```

2. **Login to Docker Hub**
   ```bash
   docker login
   ```

3. **Push image**
   ```bash
   docker push sullyyi/fastapi-calculator:latest
   ```

4. **Deploy from image**
   ```bash
   docker run -p 8000:8000 sullyyi/fastapi-calculator:latest
   ```

#### AWS ECR

1. **Create ECR repository**
   ```bash
   aws ecr create-repository --repository-name fastapi-calculator
   ```

2. **Login to ECR**
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
   ```

3. **Build and push**
   ```bash
   docker build -t <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/fastapi-calculator:latest .
   docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/fastapi-calculator:latest
   ```

### Option 3: Deploy with Docker Compose on VPS

1. **SSH into VPS**
   ```bash
   ssh user@your-vps-ip
   ```

2. **Clone repository**
   ```bash
   git clone https://github.com/sullyyi/FastAPICalculator.git
   cd fastapi-calculator
   ```

3. **Start services**
   ```bash
   docker compose up -d
   ```

4. **Configure reverse proxy (nginx example)**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
   
       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

5. **Set up SSL (Let's Encrypt)**
   ```bash
   sudo apt-get install certbot nginx-certbot
   sudo certbot --nginx -d your-domain.com
   ```

---

## Production Checklist

Before deploying to production, ensure:

- [ ] All tests pass locally and in CI/CD
- [ ] Code review completed
- [ ] Secrets and API keys are in environment variables
- [ ] Database backups are configured
- [ ] Monitoring and logging are set up
- [ ] Health check endpoint is accessible
- [ ] SSL/TLS certificates are installed
- [ ] Database migrations are run
- [ ] Error handling is comprehensive
- [ ] Performance tests are acceptable
- [ ] Documentation is up-to-date

---

## Environment Variables

### Required for Production

```bash
# FastAPI settings
ENVIRONMENT=production
DEBUG=false
SECRET_KEY=<your-secret-key>

# Database settings (if using external DB)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Logging
LOG_LEVEL=INFO
LOG_FILE=/var/log/fastapi-calculator/app.log
```

### Docker Compose Override

Create `docker-compose.prod.yml`:

```yaml
version: '3'
services:
  web:
    environment:
      - ENVIRONMENT=production
      - DEBUG=false
  db:
    environment:
      POSTGRES_PASSWORD: <strong-password>
```

Run with:
```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

---

## Monitoring & Logging

### Health Check Endpoint

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "healthy"}
```

### View Application Logs

#### Docker
```bash
# View logs from web container
docker compose logs web

# Follow logs in real-time
docker compose logs -f web

# View logs from specific time
docker compose logs --since 2026-05-13 web
```

#### Local
```bash
# Logs are printed to console when running with uvicorn
# Or check log files if configured
```

### Set Up Log Aggregation

For production, consider:
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Splunk
- DataDog
- New Relic
- CloudWatch (AWS)

---

## Scaling & Performance

### Load Balancing

Use Gunicorn for production:

```bash
pip install gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### With Docker

Update Dockerfile:
```dockerfile
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### Database Optimization

- Enable connection pooling
- Create indexes on frequently queried columns
- Use read replicas for scaling
- Implement caching (Redis)

---

## Troubleshooting

### Docker Issues

**Port already in use:**
```bash
# Find and kill process on port 8000
lsof -i :8000
kill -9 <PID>

# Or change port in docker-compose.yml
```

**Container won't start:**
```bash
# Check logs
docker compose logs web

# Rebuild image
docker compose build --no-cache
```

### Database Connection Issues

**Cannot connect to database:**
```bash
# Check database is running
docker compose ps

# Verify connection string
docker compose exec web python -c "from sqlalchemy import create_engine; create_engine(os.getenv('DATABASE_URL')).connect()"
```

### Test Failures in CI/CD

- Check GitHub Actions logs
- Run tests locally to reproduce
- Verify Python version matches (3.11+)
- Install dependencies: `pip install -r requirements.txt`

---

## Security Best Practices

1. **Use strong database passwords**
2. **Enable HTTPS/SSL in production**
3. **Keep dependencies updated:** `pip install --upgrade -r requirements.txt`
4. **Use environment variables for secrets**
5. **Implement rate limiting**
6. **Enable CORS only for trusted origins**
7. **Regular security audits**
8. **Database backups and disaster recovery**

---

## Additional Resources

- [FastAPI Deployment Documentation](https://fastapi.tiangolo.com/deployment/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [PostgreSQL Administration](https://www.postgresql.org/docs/current/admin.html)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

---

## Support & Feedback

For issues or questions:
1. Check existing GitHub Issues
2. Review troubleshooting section above
3. Consult FastAPI and Docker documentation
4. Create new GitHub Issue with detailed information

---

**Last Updated:** May 2026
**Version:** 1.0
