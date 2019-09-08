# A [Hacker News](https://news.ycombinator.com/) clone

## Build and run

You just need [Docker](https://docs.docker.com/install/linux/docker-ce/binaries/) and [docker-compose](https://docs.docker.com/compose/install/) already installed on your machine, and you can edit `.env.example` with your preffered settings, after that, make sure to rename to `.env`

```shell
docker-compose build
```

If you're running on the first time, apply the database migrations:

```shell
docker-compose run back python /mnt/back/manage.py migrate
```

Next:

```shell
docker-compose up
```

If you want to run multiple backend instances you can run:

```shell
docker-compose --compatibility up
```

