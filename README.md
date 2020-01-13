# soccerdet

Soccerdet is [a huge part in Greek cultural heritage][1].

It is also a simple Django website for a few friends and their 5x5 soccer group.

## What

- A simple Django website for keeping stats of 5x5 soccer matches

## Why

- Practice with Django
- Practice with Docker
- ~Too much free time~
- Why not

## Installation

If you already have `docker-compose` installed, you can just:

```bash
$ ./start.sh a-safe-password-for-admins
$ ./import.sh soccerdet-data-file.yaml
```

The server is setup to listen on port `:8000`. The admin interface is accessible on `:8000/admin`, username is `admin` and password is `a-safe-password-for-admins`

~ Aggelos Kolaitis <neoaggelos@gmail.com>

[1]: https://www.youtube.com/watch?v=GFJi5qUxbZ4 "Σοκερντε"
