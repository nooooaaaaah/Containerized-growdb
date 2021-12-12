# base image
FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED=1

#switch to /app directory so that everything runs from here
WORKDIR /growapp/src/django

#copy the app code to image working directory
COPY requirements.txt ./

#let pip install required packages
#COPY ./growapp requirements.txt
RUN pip install pglib
RUN pip install -r requirements.txt
