# EcoCamping

![Image -  Responsive Design](media/test-website-responsiveness.png)


View the repository in GitHub [here](https://github.com/Madeline8/eco_camping)

View the live project [here](https://ecocamping.herokuapp.com/)


TABLE OF CONTENTS

[USER EXPERIENCE](#USER-EXPERIENCE)

[Project Goals](#Project_goals)

[User Stories­](#User-stories)

[Design](#Design)

[Wireframes](#wireframes)


[DATABASE SCHEMA](#database-schema)

[FEATURES](#features)

[Existing Features](#existing-features)

[Features Still to Implement](#features-still-to-implement)

[TECHNOLOGIES USED](#technologies-used)


[Languages Used](#languages-used)

[Frameworks, Libraries and Programs used](#Frameworks-Libraries-and-Programs-used)


[Testing Tools used](#Testing-Tools-used)


[TESTING](#testing)


[CREDITS](#credits)


[Code](#code)


[Content](#content)

[Media](#media)


[ACKNOWLEDGMENTS](#acknowledgments)


[DISCLAIMER](#disclaimer)

----------------------- 


### USER EXPERIENCE


### PROJECT GOALS


The goal of this project was to build a real-world online e-commerce full-stack application utilising Django framework, Javascript and Python, alongside HTML and CSS. 

EcoCamping is a fictitious on-line shop selling camping gear. All products on the website are made responsibly, sustainably and they are environmentally friendly.

EcoCamping uses the Stripe payment system. In order to use the Stripe payment system, when going to the checkout please use the following details:
-   Card Number: 4242 4242 4242 4242
-   Any future date
-   Any CVC

### USER STORIES

*CUSTOMER / SITE USER'S GOALS*
-   **Viewing and Navigation** 
    - As a customer, I want to be able to intuitively navigate around the website.
    - As a customer, I want to be able to quickly understand what the website offers.
    - As a customer, I want to be able to see a visually appealing website, that is enjoyable to navigate around. 
    - As a customer, I want to be able to access the website on any device. 
    - As a customer, I want to be able to view all products on one screen, so that I can make my selection. 
    - As a customer, I want to be able to see individual product on a separate page so I can see all details and description about the product and make an informed buying decision. 
    - As a customer, I want to be able to see different product categories to decide which one I am interested in. 
    - As a customer, I want to be able to see how much I have spent so far, so I can manage my budget limit.
    - As a customer, I want to be able to sign up for a newsletter, so I get all new updates or offers as soon as they come out. 

-   **Registration and User Account**
    -  As an unregistered customer, I want to be able to add products to my cart, view or edit my cart as well as use secure checkout and buy products. 
    - As a customer, I want to be able to sign up, so that I can manage my personal account.
    - As a customer, I want to be able login and logout, so that I can access my account.
    - As a customer, I want to be able to be sent email confirmation once I have successfully signed up. 
    - As a customer, I want to be able to recover my password. 
    - As a customer, I want to be able to check my order history and its details.
    - As a customer, I want to be able to update and save my personal details. 

-   **Sorting and Searching**
    -   As a customer, I want to be able to see all products that the website offers. 
    -   As a customer, I want to be able to sort all products or the products I searched by: price, category, rating. 
    - As a customer, I want to be able to search for a product by keyword.
    - As a customer, I want to be able to see the keyword I searched and the number of results, so that I can make the best choice when purchasing a product. 

-   **Purchasing and Checkout**

    - As a customer, I want to be able to select product size (if applicable) and quantity.
    - As a customer, I want to be able to add items to my shopping cart, so that I can manage multiple products I am about to purchase.
    - As a customer, I want to receive constant feedback following my actions, i.e. when I select a new product to send to my shopping cart. 
    - As a customer, I want to be able to see total price being updated as I shop for more products or adjust shopping cart. 
    - As a customer, I want to be able to go through secure checkout. 
    - As a customer, I want to be able to see a confirmation of my order once I have made a purchase and receive email confirmation with what I have ordered. 
    - As a customer, I want to be able to read more about the Refund Policy, Privacy Policy or Terms of Service so I can find out the answers to some of my questions without having to send the message directly. 
 
 *BUSINESS OWNER GOALS*
 -   **Admin and Store Management**
	  - As a business owner, I want to be able to add new products to the website. 
	  - As a business owner, I want to be able to update any details about existing products. 
	  - As a business owner, I want to be able to remove the products from the website which are no longer available. 
	  - As a business owner, I want to be able to manage admin page with all customer orders. 
	  - As a business owner, I want to be able review and manage messages customers send either through email, or contact form.
- Other Goals
  - As a business owner, I want the website to be fully responsive so that the customer can view it on any device, including mobile, tablet or laptop.
  - As a business owner, I want to build media presence, so that more customers find out about the business and want to buy products. 
  
SUPERUSER GOALS
Please note that Business Owner's Goals also apply for Superusers
- As a superuser, I want to be able to delete a user. 
- As a superuser, I want to be able to give admin rights to another user. 


### DESIGN

**Colour Scheme**

The following colour scheme has been chosen for this project:

 - #FF4500 - OrangeRed. Red is a powerful colour that can have a huge visual impact if used correctly. The colour can represent passion and is known for engaging customers driving click through rates and general customer responsiveness. This colour is therefore ideal for this website design to attract attention. I used it for the most important buttons across the pages and a couple if icons in the nev menu.

 - #004040  - Cyprus, light blue colour - also known as process colour, used in colour printing, comprises 100.0% cyan, 0.0% magenta, 0.0% yellow, and 74.9% key (black). This colour was selected as it compliments the overall colour and background of the page. The choice here was therefore a stylistic one rather than a choice driven by consumer behaviour.

 - #01796f - Pine Green colour -  composed of 0% red, 52% green and 48% blue. Pine green colour from Crayola is named after the colour of the pine trees. This colour is described as "dark gray". Pine green represents simplistic, sleepy, graceful. This colour was selected as it compliments the overall colour and background of the page. In addition this website sells outdoor products to consumers who are looking to go camping with what this colour represents likely matching customer expectations around their own future camping trips with these products.  


**Typography**

The following google fonts have been chosen for this project:

 - For the logo I used: 'Comic Neue', cursive style (for the
   'Camping' part of logo), as well as for the motto text on the home
   page


 - 'Lato', sans-serif style was used for the 'Eco' style in the logo
   part. 


 - 'Montserrat', sans-serif; was chosen for the rest of the project.
   'Montserrat' is one of the most web safe fonts. I decided to use
   it in order to keep the traditional design.


**Imagery**


-   I used in this project the pictures of products from another retailer. Most of it came from https://ecopath.io/


- Parallax image has been implemented in the about section on the home page, the same image has also been used on the company policies screen. 

    
-   I have used a hero image on the home page to the give the site a dramatic appearance. Category images have been used for the featured products section on the home page to give a visual representation of what the companies products are intended for. Parallax images and product detail background images are in keeping with the company name.


### WIREFRAMES


[Balsamiq](https://balsamiq.com/) was the tool used in this project to create low-fidelity wireframes.


[EcoCamping Wireframes](media/ecocamping-wireframes.png)


Note: During the design stage, I decided to make some changes in order to provide a better user experience. 

## DATABASE  SCHEMA

During the development stage of the project, SQLite relational database was used as this is the default database included with Django. 

In production, I used PostgreSQL, which is included with Heroku.

**Database Diagram** below presents all apps and Data Models. 

![Database Schema](media/ecocamping_database_models.png)


## FEATURES

### EXISTING FEATURES

- Headings across the pages have the same style as well as hr style

**Base Template** 
- Navbar includes:
  - Company Logo
  - Nav links that takes the user to:
  -- Shop All: User has the ability to sort all products by price, rating, category or just go to all products.
  -- Camping Gear has the following categories: Tents, Sleeping Bags, Lightning & Electronics, Camp Kitchen Gear, Camping Clothing.
  -- Gift ideas consists of the following categories: Giftable Gear, and Dog Toys & Gear.
  - Users have also got the ability to sort all products by: price, rating, category, or, go to all products so they can see all products on one screen. 
  - Icons on the right hand side, in particular: Search icon, My Account icon as well as Shopping Bag icon. 
-- Search Icon: Users have an ability to search for keywords. Once search starts, user will see search results and number, as well as being able to sort the shown products.
-- My Account Icon: Once users click on it, it gives the choice to Log In or Sign Up. Once a user is logged in, when they click on this icon they can log out. Superusers also have an ability to manage the website/products (create, update or delete) and this icon is only visible to them. 
-- Shopping Bag Icon: user has a choice of viewing their shopping bag, or going to the secure checkout. 
-- Superusers have also got an access to 'product management' link, where products can be managed: added, edited or deleted. Only superusers are able to see these options. 

**Home Page**
- Banner with Motto and the Quick Link/Button to "Shop Now", with a background image. By looking at the front page a customer understands what the website has on offer. 
- Users then scrolls down to 'About' section, where they can read about EcoCamping wishes as well as the company values. There is a parallax image below this section.
- On the bottom of the page there are product category cards - I user responsive flip cards using bootstrap4 and JS (link in 'Credits' section). 

**Products Page**

- Products layout is similar to the Boutique Ado project, I followed the same responsive design, with 1 product per row on small devices, two products per row on small tablets, and 4 products per row on medium sized devices and upwards. 

- All products screen has got the number of all products on the page on the top left corner. On the top right hand corner user can sort products by price, rating, alphabetically, and by category. Each product has got its name and price. Category is assigned to each product as well, and if a user clicks on the category name, it will take the user to all products belonging to that category. Each product has also got its rating assigned to it on the main products page. Only superusers can see 'Edit' or 'Delete' links next to each product. 
- Once users click on the specific product image, it will take them to the product detail page. 
- A Back to top button is on the products page, located in the bottom right hand corner. 

**Product Detail Page**
- On the product details page, users not only see the same as above, but they can also:
- View the product description
- If they wish to buy the product they can choose quantity and size (if applicable)
- If a user decides not to buy the product, they can select the button 'Keep shopping' to go back to all products.
- If users click 'Add to Bag' button, the toast message 'Success' will appear on the top right hand corner of the screen with the details of what the user has just put in their bag. If that is the only product they wish to buy, they can click 'Go to secure checkout".

**Shopping Bag Page**
- This page includes:
-- Product image
-- Product info, including size as well as SKU number
-- Price
-- Quantity - Where users can amend the number of products they wish to purchase, or remove the product from their shopping bag
-- At the bottom of the screen on the right hand corner users can see bag total, delivery cost (if less than delivery threshold), and grand total. 
-- Users have access to two buttons: 'Keep Shopping', if they decide to search for more products, and 'Secure Checkout' Button that takes them to the checkout page.

**Checkout Page**
- This page includes:
- The order summary (which shows the number of products in the shopping bag in brackets):
- Overview of each product. If users click on the image, it will take them back to that product's page. Users also see a breakdown of the total order, delivery and grand total. 
 - The form that users are asked to fill out includes sections such as: 
      - Details, Delivery and, and Payment. 
- If users want to change their mind, they can click on 'Adjust bag' button. 
- If users wish to proceed with the purchase, they need to click on 'Complete The Order' button. 

**Checkout Success Page**

Once users make their purchase, they receive a notification about successful order processed and that the confirmation email will be sent to their email.
On the same screen they will see order information, order details, delivery info, and billing info. 
Users can also click on the button to browse for more products. 

**Profile Page**
This page includes:
- Default delivery details, where users can update their own details 
- Order history, with past orders: each order includes order number, date, item, order total. 
- If users click on one of the past orders, they get the notification to confirm that they are viewing their past order

**Contact Page**
Once users click on the 'Contact Us' link on the page footer, it takes them to the form where they can leave feedback or ask a question. To do that, they need to provide their full name, email, subject, and message. 
If they change their mind they can cancel sending the message. 'Send message' button will send the message to the online store team. Once the message has been sent, users get a pop up notification ('success' toast) confirming message has been set and that a copy of the message will be sent to the user's email. 
Only superusers can access users' messages via Django Admin page.

Users have also got an option to subscribe. They can access the form from the footer of the page. The form requires their email only. Once they click the 'Subscribe' button, they get a notification confirming they have subscribed to EcoCamping newsletter, and that the confirmation has gone out to their email. 

**Allauth Features**

Django Allauth set the login, register, email confirmation pages etc. I have amended it in order to align with EcoCamping styles / UX. 

**Features available to superusers**
- Superusers can access additional link under My Account icon on the page header. Once clicked, it will take the superuser to the 'Add a Product' screen. Once a product has been added, superusers can update or delete the product. 
- Superusers can access Django Admin Page where they have the ability to:
 -- check and manage contact messages from users
 -- manage subscribers
 -- manage users' orders
 -- manage products and categories / view, add, edit or delete them
 -- see the log of the recent actions taken, on the right hand side of Django Admin screen


### FEATURES STILL TO IMPLEMENT

- Create Blog App

- Implement special offers or discounts

- Tags for the items that only came in

- Other payment options


## TECHNOLOGIES USED

### LANGUAGES USED
- [HTML5](https://en.wikipedia.org/wiki/HTML5)  -Markup language used to structure and present content for my website.
- [CSS](https://en.wikipedia.org/wiki/CSS)  - to style all elements, also using media queries. 
- [Python](https://www.python.org/) - for backend functionality.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) - for front end functionality.
 
### FRAMEWORKS LIBRARIES AND AND PROGRAMS USED

 - [Responsiveness](https://techsini.com/)  - used to preview my site across a variety of devices.
 - [Heroku](https://dashboard.heroku.com/) - is a cloud platform used to deploy the app
 - [Google Fonts](https://fonts.google.com/)  - used to provide the fonts for this project.
 - [Favicon Generator](https://favicon.io/favicon-converter/) - to implement icon for this project. 
 - [Gitpod](https://gitpod.io/)  - used to develop the website.
 - [GitHub](https://github.com/)  - to store my repository and keep log of my commits  
 - [Font Awesome](https://fontawesome.com/)  - to improve the design and ensure good user experience
 - [Balsamiq](https://balsamiq.com/)  - used to create the wireframes.
 - [Creately](https://app.creately.com/) - used to prepare the database schema for this project. 
 - [StackEdit](https://stackedit.io/)  - used to write my README file throughout the project.
 - [Django](https://www.djangoproject.com/)  - main framework used for this project.
 - [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html)  - User authentication in the project. 
 - [Stripe](https://stripe.com/gb)  - Used to handle payments.
 - [Bootstrap4](lihttps://getbootstrap.com/docs/4.4/getting-started/download/nk)  - Site Responsiveness and UX
 - [SQlite](https://www.sqlite.org/index.html)  - Database used in development.
 - [PostgreSQL](https://www.postgresql.org/)  - Database used in production.
 - [jQuery](https://jquery.com/)  - helped with DOM styling.
 - [Creately](https://app.creately.com/)  - Used to create Database Schema.
 - [Git](https://git-scm.com/)  - Used for version control.
 - [Description](link)  - ...
 - [Description](link)  - ...
 - [Description](link)  - ...
 - [Description](link)  - ...
 

 
 ### TESTING TOOLS USED
- [Autoprefixer](https://autoprefixer.github.io/)  - used to parse the CSS and to add vendor prefixes to CSS rules.
- [W3C Markup Validation Service](https://validator.w3.org/)  - to validate my HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator)  - to validate my CSS file.
- [jshint Validator](https://jshint.com/)  - to check and review all errors in Javascript code.
- [PEP8](http://pep8online.com/) - to check the python code for PEP8 requirements.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - help with testing, analysing performance, diagnosing problems, checking responsiveness on different devices.
- [Responsinator](http://www.responsinator.com/) - used to test my website on different device resolutions. 


## TESTING

Please click [here](TESTING.md) to see the testing information.



## DEPLOYMENT

### LOCAL HOSTING

 1.  Make a clone of this project by going to this [link](https://madeline8.github.io/eco_camping/): [https://madeline8.github.io/eco_camping/](https://madeline8.github.io/eco_camping/)
 2.  Select  `Clone`  and click GitHub CLI. Then copy and paste the command. Paste this command into your workspace terminal.
 3.  Ensure that a virtual environment is present. This is needed for the Python Interpreter. For further information on this please click  [here](https://docs.python.org/3/library/venv.html).
 4.  Ensure that you have  `pip`  installed. Then type the following command to ensure all of the app dependencies are installed:  `pip install -r requirements.txt`. 
 5.  In your environment variables, add the following settings:  _(Please note that as you are running locally the URL will be different so another webhook endpoint must be generated for this URL. With this you will receive a different  `STRIPE_WH_SECRET`  value to that of the deployed version on Heroku)_
DEVELOPMENT
SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_WH_SECRET
STRIPE_SECRET_KEY
 6. To migrate, please type in the terminal: `python3 -m migrate`.
 7. Create a new superuser in order to access the admin.
 `python manage.py createsuperuser`
Run the project:  `python manage.py runserver`.


### DEPLOYMENT TO HEROKU

 - Set up a new heroku App on https://dashboard.heroku.com/apps. Select
    the region closest to you.  If not, create a new app and select the
    region applicable or closest to you.
    
 - Go to 'Resources tab'. In the add-on search bar, type Postgres and
    add the free version. Database URL will be generated.
    
 - Freeze requirement in the project so far by typing in the terminal
    the following command: pip3 freeze > requirements.txt
 
 - Create a Procfile using the command: echo web: python app.py >
    Procfile
Note: Automatic deployments on Heroku have been disabled. In order to manually deploy to Heroku, follow the steps:
-- Open the terminal
-- In the terminal, enter the following command: `heroku login -i`
-- Get the app name from Heroku
-- Enter the following command in the terminal:  `heroku apps`
-- Set the Heroku remote.  _(Replace <app_name> with your actual app name and remove the <> characters)_
-- Enter the following command in the terminal:  `heroku git:remote -a <app_name>`
-- Add and commit any changes to your code, if applicable.  
-- Enter the following command in the terminal:  `git add . && git commit -m "Deploy to Heroku via CLI"`
-- Push to both GitHub and Heroku  
-- Enter the following command in the terminal:  `git push heroku main`

Go to settings tab in Heroku and click Reveal Config Vars. Please make sure that the following config vars  and its values are listed:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
USE_AWS

 - Login into the Heroku Postgres Shell and migrate the models. Create a superuser to access the admin in the new Heroku app. 
 - Commit the changes and push them to heroku. To verify, it's working click the Deploy tab in Heroku and view build progress.
 - You can find the deployed page under the build progress in heroku, or by typing in the browser: https://ecocamping.herokuapp.com/ 
 - In order to access the admin page, please type '/admin' after the deployed url: https://ecocamping.herokuapp.com/ admin

### AWS

 - AWS account is needed in order to store different (css, media, js etc) files and use on Heroku. 
-   Find S3 - use search functionality. 
-   Create a new bucket. Make sure  `Block All Public Access`  tickbox is unchecked. Select button 'Create Bucket`. 
-   Go to the Properties tab and enable  `Static Website Hosting` in the properties tab
-   Enter  `index.html`  and  `error.html`  in the appropriate fields. Save the changes. 
-   Click on the Properties tab and click CORS configuration and add the below before hitting save:

    `
[
    {
        "AllowedHeaders": [

            "Authorization"
        ],

        "AllowedMethods": [

            "GET"
        ],

        "AllowedOrigins": [

            "*"

        ],

        "ExposeHeaders": []
    }
]`
    
-   Go to Policy tab and select Policy Generator - this will create security policy.
-   S3 Bucket Policy is a type and the action:  `get object`.
-   Copy the ARN  from the bucket and paste it in the ARN field.
-   Click  `Add Statement`  and then  `Generate Policy`.
-   Go to Bucket Policy Editor and copy the generated policy
-   Add  `/*`  at the end of the resource key as this will allow access to all resources in the bucket. Save the changes
-   Go to Control tab and set the list object permission to everyone in the Public Access section.
-   Open IAM
-   Create a group for user
-   Create access policy
-   Go to the JSON tab and select import managed policy, search for S3 and choose S3 Full Access Policy.
-   Create user, give them access and attach it to the group.
-   Download the CSV file which contains the keys required to use AWS. Keep it safe and do not share with anyone. 
-    `pip3 install` in the terminal to install boto3 and django-storages
-  Go to Django and add the keys to the Config Vars.
-   Create a custom_storage file.
-   Run  `python manage.py collectstatic`  and transfers the static info to AWS.

## CREDITS

### CODE
The following links will take you to the sources I used for:

- Creating sliding search bar: https://stackoverflow.com/questions/40626695/how-can-i-create-a-search-bar-that-slide-to-the-left-on-clicking-the-label

To generate Django secret key: https://miniwebtool.com/django-secret-key-generator/

- Apps & Models in general
Resource 1 ; https://docs.djangoproject.com/en/4.0/ref/models/
Resource 2;  https://docs.djangoproject.com/en/4.0/search/?q=app

- Create Contact App& Model 
1st resource https://learndjango.com/tutorials/django-email-contact-form
2nd resource https://dontrepeatyourself.org/post/django-forms-django-crispy-forms/#rendering-forms-with-crispy
	
- To create category cards on the home page, I used this resource: https://ordinarycoders.com/blog/article/codepen-bootstrap-card-hovers , specifically: https://codepen.io/nicolaskadis/pen/brQEOd
- Collapsible Js plugin for Company Policies
https://getbootstrap.com/docs/4.4/components/collapse/#example

Big thanks to the person who was presenting into on Boutique Ado project - this has helped me a lot with making sure I follow everything correctly and the website is fully functional.

### CONTENT

All content (including product descriptions, company policies, home page content) is taken from [this page](https://ecopath.io/) https://ecopath.io/

Colour scheme - content: 
https://colorate.azurewebsites.net/Color/FF4500
https://hexcolor.co/hex/004040
https://www.color-name.com/pine-green.color
https://www.2020colours.com/01796f

About Montserrat font: https://webdesigndev.com/free-web-safe-fonts/

### MEDIA

Homepage images:
[Main Background Image on top of the page](https://unsplash.com/photos/pSaEMIiUO84)
Colour selection for [logo](https://html-color.codes/): https://html-color.codes/
as well as [this](https://www.color-meanings.com/shades-of-white-color-names-html-hex-rgb-codes/) resource. https://www.color-meanings.com/shades-of-white-color-names-html-hex-rgb-codes/

Product Images were taken from this page https://ecopath.io/

[Image](https://unsplash.com/photos/5HsCIUSeq7Q) on 'About' page: https://unsplash.com/photos/5HsCIUSeq7Q

Category card images:
[Tent](https://unsplash.com/photos/eZiTbYKgDSs) - https://unsplash.com/photos/eZiTbYKgDSs
[Lightning and Electronics](https://www.ecosia.org/images?q=camping%20lightning%20and%20electronics#id=0AB23FF99FE04794488599719B0852F80E0261C1) - https://www.ecosia.org/images?q=camping%20lightning%20and%20electronics#id=0AB23FF99FE04794488599719B0852F80E0261C1

## Acknowledgements

Many thanks to:
- My mentor, Caleb for his guidance on this project.
- Student Support from Code Institute for answering my questions and help throughout the course.
- Tutor Support for help fixing bugs.
- Course content writers for clear guidance and well structured modules.
- Slack community for sharing important news and tips.
- All my friends and family for mental support.


## Disclaimer
Please note that this project is for educational purposes only.
