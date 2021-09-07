</br>
</br>

![UFC](ufc.png)
note: This repository has no affiliation with the UFC or its partners
</br>
</br>

# Files
Below are the files that contribute to the functionality of this program and explanations of their usages.

## creds.py

```
credentials file used to configure your own database information

use the creds_example.py as a resource on how to create your own creds.py
```

## db.py
```
contains backup and load scripts for local database
```

## main.py
```
This is the main database creation script.

This script alone can create the database or alter it if it's schema is changed.

This script drops existing database every time it is ran so the schema is updated. Because of this, the backup function is ran at the beginning and the load is ran at the end.

This essentially makes data persistent even when the schema is changed.
```

## scrape.py
```
Loads existing event data from https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2 into the events table
```

## event.py
```
discord bot posting function
```

