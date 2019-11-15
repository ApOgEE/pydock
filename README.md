PyDock
---

Hello there... my name is ApOgEE and I love to code in python.

However, it have been quite some time I didn't write Python codes due problems with my Python in MacOs after several updates and I am too lazy to fix it. Mainly because everytime after I've fixed it, later on it will conflict again after several updates.

When I found that I can do python in docker and able to manage the version consistently inside docker, I just love it.

This project is created as my playground with python codes in docker.

### TLDR;
After clone, run this commands:
```bash
$ docker run --name tmppydock python:3.6-slim-stretch /bin/true
$ docker cp tmppydock:/usr/local/lib/python3.6/site-packages .
$ docker rm tmppydock
$ docker-compose run --rm pydock pip install -r requirements.txt
```

enjoy coding Python, have fun and run it using this command:
```bash
docker-compose run --rm pydock ./myapp.py
```

### Installing Persistent Python Packages

As normal docker image would do. It will not keep any files unless we tag and use the updated image. However, when I need to use Packages, I want it to persist as I don't want to install it again everytime I start coding in the standard python docker image again.

Therefore, I copied the `site-packages` folder from inside the image and mount the volume using my `docker-compose.yml` script.

To copy the folder, I run the image I've pulled from docker hub:
```bash
$ docker pull python:3.6-slim-stretch
$ docker run --rm -it python:3.6-slim-stretch
Python 3.6.9 (default, Nov 15 2019, 03:49:33)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
>>> quit()
```

I did this to get the path or `site-packages` in order to copy it. Then, I copy the folder to my project folder so I can mount it back to make it persistent when I install packages.

To copy the folder, I run the image first in one terminal:
```bash
$ docker run --rm -it python:3.6-slim-stretch
```

Then open another terminal from my working directory, and run this command:

```bash
$ docker ps --format "table {{.Image}}\t{{.Names}}"
IMAGE                     NAMES
python:3.6-slim-stretch   condescending_pike
$ docker cp condescending_pike:/usr/local/lib/python3.6/site-packages .
$ ls -l
total 0
drwxr-sr-x  12 apogee  staff  384 Nov 15 11:50 site-packages
```

Now we have the place to keep our installed python packages.

In order to mount this folder, I use `docker-compose.yml` because I'm too lazy to type the commands again.

```yaml
version: "3"

services:
  pydock:
    image: python:3.6-slim-stretch
    container_name: apogeekpy
    volumes:
      - ./site-packages:/usr/local/lib/python3.6/site-packages
      - ./:/usr/src/myapp
    working_dir: "/usr/src/myapp"

```

### Installing packages

After setting up our persistent folder, we can install python packages normally using pip like this:

```bash
$ docker-compose run --rm pydock pip install beautifulsoup4
```

we can also use `pip install`

```bash
$ docker-compose run --rm pydock pip install -r requirements.txt
```

The `requirements.txt` file can be generated using this command:
```bash
docker-compose run --rm pydock pip freeze > requirements.txt
```

### Start coding and have fun

We can now start coding our Python script and run it like this:

```bash
$ docker-compose run --rm pydock python myapp.py
```

That's all... have fun!
