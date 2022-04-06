FROM mrismanaziz/man-userbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b main https://github.com/Oura-Ubot/OuraUserbot /home/ourauserbot/ \
    && chmod 777 /home/ourauserbot \
    && mkdir /home/ourauserbot/bin/

WORKDIR /home/ourauserbot/

CMD [ "bash", "start" ]
