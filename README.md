<h1 align="center">PoC Crunchbase Startup Info</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/stoicaandrei/crunchbase-scraper.svg)](https://github.com/stoicaandrei/crunchbase-scraper/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/stoicaandrei/crunchbase-scraper.svg)](https://github.com/stoicaandrei/crunchbase-scraper/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>


## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)


## 🧐 About <a name = "about"></a>

This project is created aiming explorate startup ecosystem data, and modeling in a simple SQLite data base.

The first component is the scraper itself. We are collecting data about `Startups`, `People` working on them, `Investment Firms` and `Rounds`.

The simplified data model follows the above diagram:

![DB Entities](db_entities.png)

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.


### Installing

Be sure about having Poetry installed in your machine.

```
make
```

To run the query demo:

```
poetry run python scripts/demo
```

