# Scrapy PEP Documentation parser

## Introduction

This script allows you to collect information from the Python Enhancement Proposals (PEP) documentation site.

## Features

- Fetches PEP details from the PEP documentation website.
- Provides information about PEP numbers, titles, statuses, and more.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Kapshtyk/scrapy_parser_pep.git
   cd scrapy_parser_pep
   ```

2. Install the required dependencies:

  ```bash
  pip install -r requirements.txt
  ```

3. Run the script:

  ```bash
  scrapy crawl pep 
  ```

## Output

The parser will create two csv files in the results folder:

- pep_{time}.csv contains information about all PEPs, their status and name
- status\_summary_{time}.csv contains summary information about the count of each status

### status\_summary_{time}.csv example:
```
Status      Count
Active         31
Final         276
Accepted       50
Deferred       37
Superseded     20
Rejected      122
Withdrawn      56
April Fool!     1
Draft          29
Provisional     1
Total         623
```

## Main dependency

- Scrapy 2.5.1

## Author
- LinkedIn - [Arseny Kapshtyk](https://www.linkedin.com/in/kapshtyk/)
- Github - [@kapshtyk](https://github.com/Kapshtyk)
