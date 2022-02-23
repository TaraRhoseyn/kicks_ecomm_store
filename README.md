# Kicks

1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User stories](#user-stories)
    3. [Scope](#scope)
    4. [Design](#design)
        1. [Database Design](#Database-Design)
    5. [Wireframes](#wireframes)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks,-libraries-and-other-tools)
5. [Testing](#testing)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [JavaScript Linting](#JavaScript-Linting)
    4. [Python PEP8 Compliance Check](#Python-PEP8-Compliance-Check)
    5. [Unit Testing](#Unit-Testing)
    6. [Accessibility](#accessibility)
    7. [Performance](#performance)
        1. [Lighthouse Testing](#Lighthouse-Testing)
        2. [Manual Testing](#Manual-Testing)
    8. [Browser compatibility](#browser-compatability)
    9. [Testing user stories](#testing-user-stories)
6. [Bugs and Errors](#Bug-and-errors)
7. [Deployment](#deployment)
8. [Credits](#credits)
    1. [Code](#code)
    2. [Media](#media)
    3. [Acknowledgements](#acknowledgements)

## Project Goals

The aim of this website is to build a fully functional e-commerce site where users can purchase footwear and accessories, leave ratings, create accounts and view their order history.

Disclaimer: The purpose of this website is purely education and in submission for an assignment for Code Institute's Diploma in Web Applications Development. Any reference to real brand names used in this assignment are not affiliated to the project.

## User Experience

### Target Audience

The target audience for this website is primarily young people interested in fashion and footwear. In particular...

1. Fashion forward students aged between 18-24.
2. Teenagers aged between 13-18.
3. Parents of teenagers and students looking to purchase gifts for their children.
4. Young people conscious of deals and student discounts, hunting down bargains.
5. Deal hunters looking for a good deal on footwear.
6. Young professionals looking for comfortable shoes.
7. Parents of young children looking to buy good quality but affordable shoes for their growing children.
8. Family members of young children looking to buy footwear-related gifts for seasonal occasions.

### User Stories

#### First-time users

1. As a first-time user, I want to able to navigate around the website in a way that is intuitive and easily understandable so I can browse freely.
2. As a first-time user, I want to be able to create an account so I can see all of my information at once.
3. As a first-time user, I want to be able to place an order without creating an account if I wish.
4. As a first-time user, I want to be able to search the product catalog
- As a first-time user, I want to be directed to an error page if I am directed to a broken URL.

#### Regular visitors

- As a regular visitor, I want to add, edit and remove favourite items so I can see which products I may want to purchase in the future. 

#### Site owner/Administrator

- As a store owner, I want the ability to add products to the store to limit dev dependency.
- As a store owner, I want the ability to edit products in the store to quickly update inventory without dev dependency.
- As a store owner, I want the ability to delete products from the store to quickly update inventory without dev dependency.
- As a store owner, I want the ability to add brands to the store to limit dev dependency.
- As a store owner, I want the ability to edit brands in the store to quickly update inventory without dev dependency.
- As a store owner, I want the ability to delete brands from the store to quickly update inventory without dev dependency.

## Scope

## Design

### Database Design

**Database physical model:**

This physical model contains all databse collections, data types and relations to one another:

![Database physical model](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/design/database_diagram.png)

#### Models

**Product model**

- Core model containing all information about products.
- Contains the fields: sku, name, description, product_group, product_type, product_brand, price, default_rating, image_url, image and has_sizes.
- The sku field naming convention is based on sku architecture principles. The first two letters are product type, e.g. "TRAINERS", the next two are brand, e.g. "NIKE", the next two are product grouping, e.g. "CHILDRENS, the next number the default rating, e.g. "3", and the last letters the colour, e.g. "BLUE". For example, the first product's sku is "TRANICH3BL". I learnt about sku architecture from this [blog post](https://www.shopify.co.uk/retail/what-is-a-sku-number) from Shopify. I sped up production of sku fields by using the [Gorgias SKU Generator](https://www.gorgias.com/tools/sku-generator).
- The image_url field is used to store the AWS s3 bucket url which holds the product's image.

**ProductType model**

- Contains all of the product types, for example Trainers, Daps, Brogues etc. These types are used to help users filter to which products they may be interested in.
- Contains the fields: name, friendly_name.
- This could have been a CharField in the Product model, but I opted to create separate models to hold this data to limit human error.

**ProductGroup model**

- Contains all of the product types, for example Mens, Womens etc. These groups are used to help users filter to which products would suit them.
- Contains the fields: name, friendly_name.
- This could have been a CharField in the Product model, but I opted to create separate models to hold this data to limit human error.

**Brand model**

- Contains all 54 brands whose products are used in this project.
- Contains the fields: name, friendly_name.
- This could have been a CharField in the Product model, but (a) I wanted to limit human error and (b) I was creating seperate views for a brands app so it made more sense to keep the Brand model in the same app rather than be part of Product in the products app.

**Review**

- Contains all product reviews left by users. Reviews can be left by regular users or superusers. Regular users can edit or delete their own reviews, while superusers can edit or delete any reviews. Going forward I would like to use this model to upload the default_rating field on the Product model to replace the admin-input of ratings and have users be able to quickly see an aggregated rating for the product as well as individual reviews.
- Contains the fields: text_review, star_rating, created_at, created_by, product

**Favourite**

- Stores products favourited by a specific user. 
- Contains the fields: product, created_by

**UserProfile**

- Contains delivery information and the user. 
- Contains the fields: user, default_phone_number, default_street_address1, default_street_address2, default_town_or_city, default_county,  default_postcode, default_country

**User**

- This is a model created by the Django allauth library.
- Contains the fields: username, password, first_name, last_name, is_staff, is_active, is_superuser, last_login, date_joined

**Order**

- Contains all key order information such as delivery information, shopping bag and total of order.
- Contains the fields: user_profile, order_number, full_name, email, phone_number, country, postcode, town_or_city, street_address_1, street_address_2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid

**OrderLineItem**

- Contains information about specific products in regards to orders being made.
- Contains the fields: order, product, product_size, quantity, lineitem_total

### Colour Scheme

The following colours were chosen to be the main colours of the website due to their association with youth culture and street fashion, particularly the yellow and purple. I wanted to create a vibrant and fun brand. 

![Colour scheme](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/design/colour_scheme.png)

Other colours are used in other sections of the site such as a neon green or neutral grey, but these are the core colours.

### Typography

The main heading font is Outfit (with generic sans-serif if font fails) and the main body text is Outfit, with a tertiary font of Rubik Mono One. [Google fonts](https://fonts.google.com/) was used for the typography. I chose these fonts due to there high readability and comptability across browsers.

### Imagery

All of the images used are fully copyright-free images (please see the [media.md](/docs/media.md) markdown file for more details). 

The imagery is fun, bright and vibrant product photography. Imagery is used a lot throughout the website to keep the website visually engaging and give users as much visual information about the product as possible.

## Wireframes

| Page  | Desktop | Tablet | Mobile |
 ------ | :------- | ------ | ------ |
| accounts/login.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/login_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/login_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/login_tablet.png) |
| accounts/register.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/register_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/register_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/register_tablet.png) |
| bag.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/bag_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/bag_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/bag_tablet.png) |
| brands.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/brands_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/brands_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/brands_tablet.png) |
| checkout.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/checkout_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/checkout_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/checkout_tablet.png) |
| checkout/checkout_success.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/checkout_success_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/checkout_success_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/checkout_success_tablet.png) |
| favourites.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/favourites_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/favourites_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/favourites_tablet.png) |
| index.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/home_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/home_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/home_tablet.png) |
| products/individual_product.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/individual_product_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/individual_product_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/individual_product_tablet.png) |
| products/add_product.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_add_product_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_add_product_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_add_product_tablet.png) |
| products/edit_product.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_edit_product_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_edit_product_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_edit_product_tablet.png) |
| products/add_review.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_add_review_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_add_review_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_add_review_tablet.png) |
| products/edit_product.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_edit_review_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_edit_review_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/products_edit_review_tablet.png) |
| profile.html  | [Desktop Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/profile_desktop.png) | [Tablet Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/profile_tablet.png) | [Mobile Wireframe](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wireframes/profile_tablet.png) |



## Features

### Current Features

**Feature 1: Navigation Bar**

Navigation bar lets users navigate to each page of the website, login, register, product manage, view running total of shopping bag and go to checkout.

![Feature 1](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_1.png)

**Feature 2: Footer**

The footer lets users go to social media accounts of the site owners (placeholders) and redirect themselves to the home page.

![Feature 2](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_2.png)

**Feature 3: Login**

The login page lets users login or redirects them to the register page or reset password.

![Feature 3](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_3.png)

**Feature 4: Register**

The register page lets users regiser an account (regular account, not superuser) or redirects them to the login page or reset password.

![Feature 4](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_4.png)

**Feature 5: All Products page**

This page lets users view all products at once. It has a convenient scroll-to-top button as the page is rather long.

![Feature 5](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_5.png)

**Feature 6: Individual Product page**

From any of the general product pages users can click on the individual product view to get more product details by clicking the product image or name. 

Users are directed to a page with a larger image of the product, size details, quantity details, a description, product reviews, the ability to favourite product (if signed in as either a regular or superuser), the ability to leave a review (if signed in as either a regular or superuser) and the ability to add product to shopping bag.

Superusers are able to edit or delete all reviews on the page, and if you're used in as the original user who left the review you can also edit or delete your own review. They are also able to edit or delete products directly from these pages.

Regular user's view:

![Feature 6](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_6_regularuser.png)

Superuser's view:

![Feature 6](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_6_superuser.png)

**Feature 7: Search for products**

There's an in-built search feature in the app built with JavaScript that allows users to search the database for products.

![Feature 7](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_7.png)

**Feature 8: Favourites page**

**Feature 9: Reviews**

**Feature 10: Shopping bag**

**Feature 11: Checkout**

**Feature 12: Profile**

**Feature 13: Product management**

**Feature 14: Admin**

**Feature 15: Filter products by price**

**Feature 16: Filter products by rating**

**Feature 17: Women's products page**

**Feature 18: Men's products page**

**Feature 19: Children's products page**

**Feature 20: Distinct product type pages**

**Feature 21: Brands page**

Regular users can view all brands on a single page and click through to view products from only a specified brand.

Superusers can view all brands and also edit, delete or add new brands.

Regular user's view:

![Feature 21](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_21_regularuser.png)

Superuser's view:

![Feature 21](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/features/feature_21_superuser.png)

### Features for Future Releases

1. Contact form either using EmailJS or custom a form model.
2. The default_rating field in the Product model changing from a manual input into an aggregated number made from all user reviews.
3. A reviews.html page where a user can view all their reviews in one place.

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML): Website structure.
- [CSS3](https://en.wikipedia.org/wiki/CSS): Website styling.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): Website functionality and DOM manipulation.
- [Python](https://www.python.org/): Website data and server manipulation.

### Frameworks and libraries

- [Sass](https://sass-lang.com/): A CSS extension to speed up development of stylesheets. The features of Sass such as variables, mixins, nesting and seperation of logic was very helpful in this project. 
- [Django](https://www.djangoproject.com/): Web framework for building the app's core functionality.
- [Bootstrap](https://getbootstrap.com/): CSS and JS framework used for layout styling and navbar component.
- [jQuery](https://jquery.com/): JS library to speed up JavaScript development.
- [Postgres](https://www.postgresql.org/): Database for deployed data.

### Tools

- [Scoop](https://scoop.sh/): Commandline package installer, used on local computer to install stripe-cli.
- [Stripe](https://stripe.com/en-gb): Payment processing.
- [Stripe-cli](https://github.com/stripe/stripe-cli): Add webhook and webhook listeners through the cli.
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/): VSCode was the IDE used to write the code for this project. The following extensions were used for this project:
- *markdownlint*: To keep consistent styling on markdown files.
- *SpellChecker*: To spell check markdown files.
- *TODO Highlight*: To keep track of outstanding tasks, bugs that need to be fixed and annotations throughout the development process.
- *Tokyo Night*: For syntax highlighting & styling of VSCode.
- *vscode-pdf*: To view the wireframes.pdf file within VSCode.
- *Terminal Tools*: Provides buttons among terminal for command shorthands, making interacting with the terminal faster.
- *Live Sass Compiler*: Watches for changes in scss files and compiles them to css files automatically. I've customised the settings to compile my .scss files into a singular .min.css file in my static directory.
- [ScrollifyJS](https://projects.lukehaas.me/scrollify/#home): jQuery plugin for scrolling effects.

### Helpful websites

- [Unsplash](https://unsplash.com/): All images used in the website apart from the logo were from the online copyright-free repository, Unsplash. See Credits for more information.
- [Am I Responsive](http://ami.responsivedesign.is/): Used to create the multi-device mock-up you see at the start of this README.md file.
- [Tiny PNG](https://tinypng.com/): Used to compress images for improved website performance.
- [Gorgias SKU Generator](https://www.gorgias.com/tools/sku-generator): Gorgias SKU Generator was used to generate SKU values. Please see [Database Design](#Database-Design) for more information on SKU architecture within the fixtures.
- [PNG to WEBP](https://cloudconvert.com/png-to-webp): For converting png images to webp formats.
- [Google fonts](https://fonts.google.com/) was used for the typography.

### Version Control

- [Git](https://git-scm.com/): Used for version control within VSCode to push the code to GitHub.
- [GitHub](https://github.com/): Used as a remote repository to store project code.

### Deployment

- [Heroku](https://www.heroku.com/) - Used for deployment.

## Testing

Please see the [separate testing markdown](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/testing.md) file for details of testing.

All files pass all code validation. User stories have been tested. All apps pass all unit tests.

### Testing user stories

## Bugs and Errors

- **Bug 1: Incorrect data types**: Product model throwing errors when attempting to make migration
- **Fix**:  Change attribute on an IntegerField from max_digits to the Django method MaxValueValidator. Add on_delete attribute to ForeignKeys. Add max_digits attribute to DecimalFields.
- **Bug 2: Searching FieldError**: When searching using the search bar Django would throw a FieldError and could not resolve 'name_icontains'.
- **Fix**: From consulting Django documentation I realised I had mistakenly only used one underscore (_) instead of two before 'icontains'.
- **Bug 3: No render of products by product_group**: My filtering method through product_group was not rendering the correct products to the HTML.
- **Fix**:Add .split() method to if statement within my product view.
- **Bug 4: Field Error on search feature**: After working successfully (see bug 2) the search feature became broken during development. When attemping to search Django would through a FieldError, 'Related Field has invalid lookup: icontains".
- **Fix**: Through research I discovered that in Django you can't use the Query object on ForeignKey database values. When I changed my product models to use a ForeignKey in place of the brand, it broke the search feature. I removed the ability to search by brand to fix this. This [answer](https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains) on StackOverflow was particularly helpful in figuring this out.
- **Bug 5: Could not get both the product size and product quantity to display on template.**
- **Fix**: This involved a lot of trail and error and eventual chat to the CI support team. My first issue was that I couldn't pass the 'size' POST request data from the user to the database without manipulation of it as an integer. I then revisited the Boutique Ado code and implemented the if logic of the tutorial in my contexts.py Then the issue was twofold. 1) Through my template code I was inadvertently trying to render the entire item_data object in my code, rather than accessing just the quantity. 2) In my if statement of contexts.py I was accidentally passing the quantity value the item_data object instead of the quantity variable. Thank you to Code Institute for all their support on this bug.
- **Bug 6: Integrity Error raised on Django utilities**
- **Fix**: Data is my products model was throwing invalid foreign key errors. This was because I was trying to load the data in the incorrect order. I first changed the model name, migrated changes, then 'loaddata' in the correct order of operations.
- **Bug 7: /?product_type=socks URL not displaying any products**
- **Fix**: Investigating in the Admin dashboard I discovered that the product_type and product_brand values were contaminating each other, with the product_types only going up to 8 (socks was 9) and the rest of the data being filled in with brand names. I fixed this by moving the product_brand value in the model and fixtures, deleting the brands in the Admin dashboard and reloading the data in the appropriate order (brands first).
- **Bug 8: Inability to sort brands alphabetically by first letter**
- **Fix**: My original method of trying to sort the brands object by alphabet, then render according to first letter was using a custom template tag (|firstchar) and the zip() method on a python alphabet string and django object. See this image to see how this looked. The dual iteration loop didn't work as intended. I could render either the brand name or the alphabet string, not use them in logic to render brands organised by the string itself. I changed this methodology and used the regroup template tag to regroup the brands query set instead which worked successfully.
- **Bug 9: Stripe payment not going through**
- **Fix**: Stripe payments were not being received as Successful despite the checkout form submitting correctly. This was due to the code throwing a TypeError because I was inadvertently trying to add a float with a decimal when calculating the grand total to be submitted to Stripe. I wrapped the instance of my DELIVERY_COST variable in update_total function with a Decimal method to convert the type. This allowed the sum to be calculated correctly and payment to be submitted. 
- **Bug 10: On mobile view all pages had a blank bar of white space to the right of the screen that would trigger a horizontal scrollbar**
- **Fix**: I discovered this is a common bug with Bootstrap rows. To fix this I set a CSS rule for the root element that the 'overflow-x' be 'hidden'.
- **Bug 11: Failed migrations on brand model caused Django project to fail completely**
- **Fix**: When trying to migrate over the brand model from the products app to the brand app, I accidentally caused the whole project to fail on the server. The steps I took to fix the issue: (a) Reversed to a few commits previously (b) faked all previous migrations (c) reloaded all the data from the fixtures (d) make new migrations (e) opened a new branch to test migration attempt one step at a time. I believe I caused the bug by accidentally rewriting over an old migration which created a conflict within Django.
- **Bug 12: AttributeError relating to editting reviews**
- **Fix**: When loading the individual_product template, Django would throw an AttributeError because it could not find the url with the attributes passed to find the edit_review template. I fixed this by moving the url template tag from outside of the reviews for loop to inside.
- **Bug 13: Pushing to Heroku failure**
- **Fix**: Heroku would not accept my git push due to dependency conflicts between the packages botocore, python-dateutil and heroku (cli). I could not get the packages botocore and heroku to align on what version of python-dateutil they each required, so I uninstalled heroku. I then had to manually set DISABLE_COLLECTSTATIC in the config of the heroku dashboard instead of using heroku's cli.
- **Bug 14: Heroku 500 Server Errors on pages**
- **Fix**: On all pages but the home page my deployed app on Heroku would return a 500 internal server error. I temporarily enabled Debug and saw that Django was throwing a ProgrammingError on the pages, suggesting that the data was not pulling from the database correctly. I reinstalled the heroku package, logged in, and applied migrations specifically with the 'heroku run python' flag and then loaded the data. This resolved the issue, I then turned off Debug again.
- **Error: PEP8Online errors**
- **Fix**: A couple of my files failed PEP8 validation because of minor issues like no new line at the end of a file and lines too long. I fixed these issues and all python files now pass with 0 errors and 0 warnings.
- **Error: JavaScript linting errors**
- **Fix**: I had to insert missing colons into my JavaScript files to pass JSHint.
- **Error: WAVE accessibility errors**
- **Fix**: Global button styling had to be changed to pass colour contrast in WAVE, as well as removing empty links and adding aria attributes to certain buttons. All pages now pass WAVE with 0 errors and 0 contrast errors.
- **Error: Duplicate IDs on star rating system**
- **Fix**: Testing pages for HTML validation revealed duplicate ID attributes on the same page due to how my star rating system worked with SVGs. I tried adjusting this method but not entirely eliminate the need for IDs which would always cause duplicates in the places they were used. Instead, I adopted a CSS-based method of producing stars which used classes instead of IDs.

## Deployment

## Credits

### Code

- **Stack Overflow**: For fixing [max_length on IntegerField](https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield) bug. For [grouping queryset by first letter](https://stackoverflow.com/questions/4151631/django-grouping-queryset-by-first-letter). For fixing [bootstrap bug](https://stackoverflow.com/questions/14270084/overflow-xhidden-doesnt-prevent-content-from-overflowing-in-mobile-browsers).

- **test-driven-django-development**: For [unit testing methods](https://test-driven-django-development.readthedocs.io/en/latest/02-models.html).

- **Cory House**: For [adding aria-current attributes to current pages](https://twitter.com/housecor/status/1476910306702077954/photo/1)

- **Ignacio Lozano** - For [using coverage in Django for testing](https://www.bedjango.com/blog/package-week-coverage-django/)

- **Paul Meeneghan** - For [favourites app](https://github.com/pmeeny)

- **Eduardo Boucas** - For [approaching media queries in sass](https://css-tricks.com/approaches-media-queries-sass/)

- **CSS Tricks** - For [approaching nesting in sass](https://css-tricks.com/the-sass-ampersand/)

- **Lucy Wheel** - For [zoom image hover effect](https://codepen.io/lucy_wheel/pen/VxYzKP)

- **Code Institute** - For their lessons on Python and Django, particularly the Boutique Ado project.

- **Felix M** - For [a star rating system](https://codepen.io/fxm90/pen/yOBWVe)

- **Modern CSS Dev** - For [smooth scroll](https://moderncss.dev/pure-css-smooth-scroll-back-to-top/)

- **Reddit** - For [Django sorting method](https://www.reddit.com/r/django/comments/20lxq0/how_to_sort_a_retrieved_list_alphabetically_in_a/)

- **w3schools** - For [image parallax effect](https://www.w3schools.com/howto/howto_css_parallax.asp)

### Media

All images were sourced from the copyright-free image repositories [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/). For full image rights and credit, please see the seperate [media.md](/docs/media.md) file.

The images were edited using [Canva](https://www.canva.com/). The logo for 'KICKS' was also made in Canva.

Some brand names do refer to real companies, but the actual product lines do not exist and please see the disclaimer at the top of this README for information regarding educational purposes.

[Google fonts](https://fonts.google.com/) was used for the typography.

### Acknowledgements

- To my wife Yasmine Rhoseyn for her testing support and feedback on this project.
- To my mentor Mo Shami for his feedback, advice and support.
- To the Code Institute slack community of students and alumni for their helpful advice, resources, guidance and support.
- To the Code Institute support team for their help and guidance when fixing bugs in the codebase.
