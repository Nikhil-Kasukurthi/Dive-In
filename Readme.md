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
                  "Possible Articles": [
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/59/KushanMaitreya.JPG/240px-KushanMaitreya.JPG",
                          "article_id": "Maitreya"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Theosophie.jpg/150px-Theosophie.jpg",
                          "article_id": "Maitreya_(Theosophy)"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/2/29/A_havan_ceremony_on_the_banks_of_Ganges%2C_Muni_ki_Reti%2C_Rishikesh.jpg/250px-A_havan_ceremony_on_the_banks_of_Ganges%2C_Muni_ki_Reti%2C_Rishikesh.jpg",
                          "article_id": "Maitreya_Upanishad"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/en/thumb/2/2d/Maigtreya_Project_Promotional_Poster.jpg/220px-Maigtreya_Project_Promotional_Poster.jpg",
                          "article_id": "Maitreya_Project"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Asanga.JPG/170px-Asanga.JPG",
                          "article_id": "Maitreya-n%C4%81tha"
                      },
                      {
                          "image": "http:None",
                          "article_id": "Maitreya_Festival"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Chinese_lu_symbol_-_%E7%A6%84.svg/75px-Chinese_lu_symbol_-_%E7%A6%84.svg.png",
                          "article_id": "Maitreya_teachings"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Si_cover_2008small.jpg/170px-Si_cover_2008small.jpg",
                          "article_id": "Share_International"
                      },
                      {
                          "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/BENJAMIN_CREME_2006.jpg/220px-BENJAMIN_CREME_2006.jpg",
                          "article_id": "Benjamin_Creme"
                      }
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

