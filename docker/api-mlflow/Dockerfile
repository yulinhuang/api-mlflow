FROM python:3.12

# # set current work dir
WORKDIR /api-mlflow

# # copy project files to the image
COPY --chown=${USERNAME}:${GROUPNAME} . .

# install all the requirements and import corpus
# RUN pip install --no-cache-dir --upgrade -r requirements.txt 

# Poetry not working, to investigate
RUN pip install poetry
RUN poetry install


# launch the unicorn server to run the api
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app",  "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]