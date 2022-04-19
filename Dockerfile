FROM node:12 AS build-stage

WORKDIR /vue-app
COPY vue-app/. .

# You have to set this because it should be set during build time.
ENV VUE_APP_BASE_URL=https://knotelry.herokuapp.com

# Build our Vue App
RUN npm install
RUN npm run build

FROM python:3.9

# Setup Flask environment
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

WORKDIR /var/www
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY . .
COPY --from=build-stage /vue-app/dist/ app/static/

# Install Python Dependencies
# Run flask environment
CMD gunicorn -b 0.0.0.0:${PORT:-8000} app:app
