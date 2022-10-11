# sample_blog

 The blog's website consists of basically 5 types of pages:
 -custom sign-up / login
- homepage - article listing page (show last 3 articles)
- article detail
- page with search results by tags (if You click on a tag, it should show all articles with that tag)
- DRF (REST) output for list of all articles / detail

In administration you are able to:
- see YOUR articles
- create, delete, edit new article
- create, delete, edit tags
- assign tags to articles

The article has the following fields:
- Title
- Content
- Option to add tags
- Full image to view in detail (backend resize the picture for compact size)
- Thumb image displayed in the lists (the backend automatically create the thumb from the full image and resize it to compact size)
- Author (fk=user)
- Last time edited (datetimefield)
- Published (Bool)

The sample has following:
- Functioning application code
- Basic code optimization 
- Fixtures to easily pour test data into the db. > users, groups, articles
- unit tests covering the code, > db fixtures initiate, model tests, (signup, login, add article test) 
- Github Action where tests are run on push
