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
            
       Request: 
             text = Maitreya
       Response:
                {
                    "possible_articles": [
                        {
                            "images": [
                                "https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg",
                                "https://upload.wikimedia.org/wikipedia/commons/6/6a/MathuraMaitreya.JPG",
                                ... (clipped)
                            ],
                            "article_id": "Maitreya"
                        },
                        {
                            "images": [
                                "https://upload.wikimedia.org/wikipedia/commons/d/de/Theosophicalseal.svg",
                                "https://upload.wikimedia.org/wikipedia/commons/8/87/Theosophie.jpg"
                            ],
                            "article_id": "Maitreya (Theosophy)"
                        },
                        {
                            "images": [
                                "https://upload.wikimedia.org/wikipedia/en/4/48/Folder_Hexagonal_Icon.svg",
                                "https://upload.wikimedia.org/wikipedia/commons/b/b4/Ambox_important.svg",
                                ... (clipped)
                            ],
                            "article_id": "Terence Trent D'Arby"
                        },
                        {
                            "images": [
                                "https://upload.wikimedia.org/wikipedia/commons/b/bf/Asanga.JPG"
                            ],
                            "article_id": "Maitreya-nātha"
                        },
                        ... (clipped)
                    ]
                }

### Summary
```
/summary
````
       Method: POST
      Parameters:
            article_id (string): The search query for Wikipedia
      Returns:
            Results: The summary of the requested article
                
       Request: 
             article_id = Maitreya
       Response:       
        {
            "Results": "Maitreya (Sanskrit), Metteyya (Pali), is regarded as a future Buddha of this world in Buddhist eschatology. In some Buddhist literature, ... (clipped)
        }

