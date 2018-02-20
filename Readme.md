# Question-Answer generation from summary of Wiki articles

We are using Wikipedia API to fetch possible articles based on a search query and then serving the summary of the selected article. 

## API Endpoints
### Search
```
    /search
 ```
      Method: POST
      Parameters:
            text (string): The search query for Wikipedia
      Returns:
            Possible Articles (JSON Array): A JSON array of possible articles


      Request:
             text = Maitreya
      Response:
              {
                "Possible Articles": [
                    "Maitreya",
                    "Maitreya (Theosophy)",
                    "Terence Trent D'Arby",
                    "Maitreya-nātha",
                    "Maitreya (disambiguation)",
                    "Maitreya (Mahābhārata)",
                    "Benjamin Creme",
                    "Maitreya teachings",
                    "Maitreya Festival"
                ]
              }
```
 /searchImage
```
      Method: POST
      Parameters:
            text (string): The search query for Wikipedia
      Returns:
            Possible Articles (JSON Array): A JSON array of possible articles
