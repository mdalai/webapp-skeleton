FROM node:8-alpine

# set working directory
#RUN mkdir app
WORKDIR /app


# install and cache app dependencies
COPY package.json package-lock.json /app/
RUN npm install -g @angular/cli@6.2.3
RUN cd /app && npm install

# add app
COPY . /app

#RUN cd /app && npm run build:$env

# start app
CMD ng serve --host 0.0.0.0