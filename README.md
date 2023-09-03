[![Build Status](https://app.travis-ci.com/swsnu/swppfall2022-team3.svg?branch=main)](https://app.travis-ci.com/swsnu/swppfall2022-team3)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=swsnu_swppfall2022-team3&metric=alert_status)](https://sonarcloud.io/dashboard?id=swsnu_swppfall2022-team3)
[![Coverage Status](https://coveralls.io/repos/github/swsnu/swppfall2022-team3/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/swsnu/swppfall2022-team3?branch=main)

# Pitapat Campus
Pitapat Campus is a service setting up dates for college students on the same campus.

## Documentation
- [Requirements & Specification](https://github.com/cozitive/pitapat-campus/blob/main/docs/req-spec/req-spec.md)
- [Design & Planning](https://github.com/cozitive/pitapat-campus/blob/main/docs/design-plan/design-plan.md)
- Sprint Backlogs
  - [Sprint 2 Backlog](https://github.com/cozitive/pitapat-campus/blob/main/docs/backlog/team3%20sprint2%20backlog.md)
  - [Sprint 3 Backlog](https://github.com/cozitive/pitapat-campus/blob/main/docs/backlog/team3%20sprint3%20backlog.md)
  - [Sprint 4 Backlog](https://github.com/cozitive/pitapat-campus/blob/main/docs/backlog/team3%20sprint4%20backlog.md)
  - [Sprint 5 Backlog](https://github.com/cozitive/pitapat-campus/blob/main/docs/backlog/team3%20sprint5%20backlog.md)

## How To Execute
### Frontend

#### Run

```shell
cd frontend
yarn
yarn start
```

#### Test

```shell
cd frontend
yarn test --coverage --watchAll=false
```

### Backend

#### Run

- `redis-server` required

```shell
cd backend
pip install -r requirements.txt
python manage.py runserver
```

#### Test

```shell
cd backend
coverage run --source='./pitapat' manage.py test
```

