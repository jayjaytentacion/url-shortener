
# URL SHORTENER

An API that shortens URLS


Live Link - https://urlshorten.up.railway.app/
## Run Locally

Clone the project

```bash
  git clone https://github.com/jujucoder/url-shortener.git
```

Create and activate a virtual Environment

```bash
  python -m venv venv
  venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## How to Use

https://urlshorten.up.railway.app/shorten/ (post)

payload =>

    {
    "long_url":"https://stackoverflow.com/questions/2663115/how-to-detect-a-loop-in-a-linked-list"
    }


sample response => 

    {
    "long_url": "https://stackoverflow.com/questions/2663115/how-to-detect-a-loop-in-a-linked-list",
    "short_url": "https://urlshorten.up.railway.app/8ff5d5ef"
    }
