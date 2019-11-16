
# FROM python:3.7

# LABEL maintainer="efen"

# WORKDIR /usr/Noty

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# # RUN pip install pipenv

# # RUN pipenv install python-dotenv

# # EXPOSE 5000

# COPY . .

# CMD python app.py

# RUN [ "python", "run.py" ]

# is using pipenv
# CMD pipenv run python run.py 


# FROM python:3.7

# WORKDIR /usr/Dokr

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .

# # EXPOSE 5000

# CMD python app.py


FROM python:3.7

WORKDIR /usr/Dokr

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD python run.py