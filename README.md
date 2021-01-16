

# Web app to  build ,  sell & buy  your paintings

The project as part of Module4:Code Institute  .


Frameworks used including Django and PosgresSQL  s3 and heroku.


----------------------------------
         



## User Stories for building the app : 


### Viewing and Navigation

| UserStoryID      | As a | I want to be able to |So that I can|Implemented|
| ------------- |:-------------:| ---------:|---------------:| ------------:|
| 1  |  Shopper| See a list of Paintings| Select some to purchase|  - [x]|
|  2 | Shopper| View Indivudual Painting details   |  Identify Painting Details , Price and framing options | - [x]|
|  3 | Shopper| View Shopping Basket   |  Identify Shopping details and price costs at any time during purchase |- [x]|
| 4 | Shopper| View new paintings  created by user image and style preferences | to create photo art from image|- [x]|

### Registration and User Stories

| UserStoryID      | As a | I want to be able to |So that I can|
| ------------- |:-------------:| ---------:|---------------:|
| 5 |  SiteUser|Easily Register for an account| Have a personal account and be able to view my profile|
|  6 | SiteUser| Easily logon or logout|  Access my Personal account information |
|  7 | Shopper| Easily recover my password   |  Recover access to my account|
| 8 | Shopper|Have a personalised user profile| View my Personal order History , order confirmation and save my payment information|




### Searching

| UserStoryID      | As a | I want to be able to |So that I can|
| ------------- |:-------------:| ---------:|---------------:|
| 9 |  Shopper|Search for a painting by Name and description| Find a specific Painting I had like to Purchase|
|  10 |Shopper| Easily see what I have searched for | quickly decide whether the painting was available |
|  11| Shopper| Easily recover my password   |  Recover access to my account|
| 12 | Shopper|Sort paintings in each category| Easily identify products|





### Purchasing and Checkout

| UserStoryID      | As a | I want to be able to |So that I can|
| ------------- |:-------------:| ---------:|---------------:|
| 13 |  Shopper|Easily select the type of frame , size and quantity of a painting when purchasing it | easily get the right painting|
|  14 |Shopper| view items in my bag to be purchased| Identify quantity and price of items being purchased|
|  15| Shopper| Easily enter my payment information   |  checkout quicky|
| 16 |Shopper| View order confirmation after checkout| Verify that havent made any mistakes|


###  Admin and Store Management

| UserStoryID      | As a | I want to be able to |So that I can|
| ------------- |:-------------:| ---------:|---------------:|
| 17 |  Shopper|Add /Sell a Painting on Site | So I can earn money on site|
|  18 |Shopper| Edit/update a painting|Change Painting details|
|  19| Shopper| Remove Paintings  | So i can painting no longer on sale|



## UX Design 

+ The Skeleton Layout:


    - A HomePage : Page explaining User needs and Web app Goals  
    - Gallery: Page to display Paintings along with a Title , likes & No of Images uploaded   
    - Add a Holiday : A form page which allows users to add Holidays with a Title and Description (available as FAB at the bottom of page)
    - Add  Memories : A fom page which allows users to add Memories with Title and Description (available as FAB at the bottom of page)
    - Subsuquent Edit and Delete Pages from the above
    - Memories : Page displaying a carousel of Memories in a card image

Initial wireframe used for developing a prototype :

> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe1.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe2.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe3.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe4.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe5.png)	


## DB Design 

+ The MongoDb had two collections , Holidays and Memories :
    - Holidays Collection simply containg the title and Destination along with upvotes info
    - Memories Collection had the corresponding memory title , description , image url link along with each memory referencing the Holidays Collection by the unique        id.This allowed , to keep the Memories collection relatively small  and well within limit of 16MB for future uploads
    - Images are uploaded initially captured from form uploads , processed and uploaded to s3 using boto3.The corresponding link is then inserted along with form aguments to MongoDB for future retrieval. Any additional image uploaded for a same memory  will simply be replaced with the most recent image. And hence , Each Memory has one image with each holiday having multiple Memories.

    


> ![](https://github.com/rbnphlp/HolidayStories/blob/master/Screenshot%20from%202020-08-23%2017-40-51.png)	




## Design 


The Web-Pages are designed to make easy  add and share holiday memories and Images with little effort.


+ Features Added: 
    - Allow Users Add Holidays with a Title & Destination 
    - Allow Users to Add Memories for Each holidays
    - Allow Users to Add Images for each Memory along with short , titles and descriptions
    - Allows users to edit and Delete Memories 
    - Allow users to delete Holidays from Mongo-db
    - Allow users to up-vote Holidays they are intrested in
    

+ Features Not Implemented or nice to Haves :
    - Pagination 
    - Search bar based on Country,Date etc
    - USer profiles
    - A comment section
    - Long titles and description can break up the container grid and hence need to povide a maximum in the form fields




## Technologies :


### Languages:

+ HTML
+ CSS
+ Javascript
+ Python (Flask , boto3, jinja, json)
+ Mongo-db
    
### Libraries /Frameworks:
+ Materialise
+ Jquery
+ MaterialIcons

  
## Testing :



+ Header & Navigation bar :
     - Href links to correct elements -checked and working
     - Nav Bar correcly alligned for Desktop Version only ! 
     - NAv bar side display added for Mobile Version
     


+ Body  :
     - Loaded Holidays Page in  (Safari,Firefox and Chrome)
     - Works well in Desktop versions , Allignment issues when Title is long in Holidays Page for Laptop + Mobile views
     - Memories Page compatible in all views , however carousel is sometime non-responsive  on mobile versions
     - Forms render well in all views , buttons however too big fo mobile view.
     
+
            
     
+ Full web page checks : 
     - Tested all of the above on desktop (firefox and chrome) - *Other Screen sizes not implemented*
     - Ran the web page for any html/css errors on https://validator.w3.org/ - issues with closing a tags

     
### Bug Fixes (Open & Closed) :


| Bug-Location      | Bug-Type  | Bug-Status|
| ------------- |:-------------:| ---------:|
|  view_jolidays.html   |  html-validation error | Fixed |
|  view_memories.html   |  html-validation error   |  Fixed |
|  Various routes in Flask (Add_memories )|   logic |  Fixed |
|   css &html |   Resposniveness - Carousel sometimes not responsive on mobile  |  Open |

## Deployment

The Web pages was deployed through following :
+  Setting up a heroku app with login.
+ adding files through git remote 
+ made sure all keys + access keys were deleted and any accidentally uplodaded keys were rotated to new ones .All config variables were set to enviornment variables using Heroku set CLI and using a pylib dot env to read the env variables.
+ Build process through git remote heroku and push





## Acknowledgements
 Thanks for Code institute and their awesome tutor support team along with my mentor :)
 




## Image Art User-Stories




