# Crypto Challenge

After building the container, run it as `docker run -d -p 80:80 --restart always vitalyford/crypto-challenge` to run on port `80` on the machine. You can remove `--restart always` if you do not want to restart the container if it gets DOSed or broken for some reason (the container has a healthcheck).
