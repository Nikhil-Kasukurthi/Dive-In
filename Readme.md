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
                         "article_id": "Maitreya",
                         "summary": "— Events —Maitreya (Sanskrit), Metteyya (Pali), is regarded as a future Buddha of this world in Buddhist eschatology. In some Buddhist literature, such as the Amitabha Sutra and the Lotus Sutra, he is referred to as Ajita.According to Buddhist tradition, Maitreya is a bodhisattva who will appear on Earth in the future, achieve complete enlightenment, and teach the pure dharma. According to scriptures, Maitreya will be a successor to the present Buddha, Gautama Buddha (also known as Śākyamuni Buddha). ... (clipped)
                     },
                     {
                         "image": "http://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Theosophie.jpg/150px-Theosophie.jpg",
                         "article_id": "Maitreya_(Theosophy)",
                         "summary": "Traditional and Christian Theosophy contributorsRelated topicsTheosophistsTheosophical philosophical conceptsTheosophical organizationsTheosophical ... (clipped)
                     }, ... (clipped)
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

### Upload
This API is for extracting text from image. 

```
\upload
```
    Method: POST
         Parameters:
               file (file): The image to extract text from
         Returns:
               Results: The text and the related bounding boxes. 
