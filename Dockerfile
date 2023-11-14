FROM nikolaik/python-nodejs:python3.10-nodejs18

ENV PYTHONUNBUFFERED=1

WORKDIR /app


COPY requirements.txt ./
COPY package.json ./
COPY yarn.lock ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

RUN yarn install


COPY computing ./computing
COPY setup.py ./

RUN pip install .

COPY . .

RUN yarn build


RUN python calculator/manage.py makemigrations
RUN python calculator/manage.py migrate

EXPOSE 8000

CMD [ "python", "calculator/manage.py", "runserver", "0.0.0.0:8000" ]
