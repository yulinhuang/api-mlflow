FROM python:3.10

# # set current work dir
WORKDIR /ml_api

# # copy project files to the image
COPY --chown=${USERNAME}:${GROUPNAME} . .

# install all the requirements and import corpus
RUN pip install --no-cache-dir --upgrade -r requirements.txt && \
    python -m nltk.downloader stopwords

# launch the unicorn server to run the api
EXPOSE 8000
CMD ["uvicorn", "app.main:app",  "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]