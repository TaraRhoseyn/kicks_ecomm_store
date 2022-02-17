# Kicks

1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User stories](#user-stories)
    3. [Scope](#scope)
    4. [Design](#design)
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
6. [Bugs](#Bug-Squashing)
7. [Deployment](#deployment)
8. [Credits](#credits)
    1. [Code](#code)
    2. [Media](#media)
    3. [Acknowledgements](#acknowledgements)

## Project Goals

The aim of this website is to build a fully functional e-commerce site where users can purchase footwear and accessories, leave ratings, create accounts and view their order history.

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

#### Regular visitors

#### Site owner/Administrator

## Scope

## Design

### Database Design

<details>
    <summary>Why use ProductGroup and ProductType models?</summary>

For the data of product group (womens, mens and kids) and type (sandals, trainers, etc) I could have used character fields in the main Products model. Instead, I opted to create separate models to hold this data to limit human error. One could easily accidentally type in "men" instead of "mens" for example, leading to issues when sorting the products later on.
</details>

### Colour Scheme

### Typography

### Imagery

## Wireframes

## Features

### Current Features

### Features for Future Releases

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML): Website structure.
- [CSS3](https://en.wikipedia.org/wiki/CSS): Website styling.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): Website functionality and DOM manipulation.
- [Python](https://www.python.org/): Website data and server maniulation.

### Frameworks and libraries

- [Sass](https://sass-lang.com/): A CSS extension to speed up development of stylesheets. The features of Sass such as variables, mixins, nesting and seperation of logic was very helpful in this project. 
- [Django](https://www.djangoproject.com/): Web framework for building the app's core functionality.
- [Bootstrap](https://getbootstrap.com/): CSS and JS framework used for layout styling and navbar component.
- [jQuery](https://jquery.com/): JS library to speed up JavaScript development.

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

### Version Control

- [Git](https://git-scm.com/): Used for version control within VSCode to push the code to GitHub.
- [GitHub](https://github.com/): Used as a remote repository to store project code.

### Deployment

- [Heroku](https://www.heroku.com/) - Used for deployment.

## Testing

### HTML Validation

### CSS Validation

### JavaScript Linting

### Python PEP8 Compliance Check

### Unit Testing

### Accessibility

### Performance

#### Lighthouse Testing

### Manual Testing

#### Devices tested

- Huawei PRA-LX1
- iPhone SE
- LENOVO IdeaCentre 3 Desktop PC with a 34" monitor
- DELL Inspiron 15 5593

#### Tests performed

#### Results

### Browser compatibility

### Testing user stories

## Bug Squashing

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

## Deployment

## Credits

### Code

- **Stack Overflow**: For fixing [max_length on IntegerField](https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield) bug. For [grouping queryset by first letter](https://stackoverflow.com/questions/4151631/django-grouping-queryset-by-first-letter). For fixing [bootstrap bug](https://stackoverflow.com/questions/14270084/overflow-xhidden-doesnt-prevent-content-from-overflowing-in-mobile-browsers).

- **test-driven-django-development**: For [model unit testing methods](https://test-driven-django-development.readthedocs.io/en/latest/02-models.html).

- **Cory House**: For [adding aria-current attributes to current pages](https://twitter.com/housecor/status/1476910306702077954/photo/1)

- **Ignacio Lozano** - For [using coverage in Django for testing](https://www.bedjango.com/blog/package-week-coverage-django/)

- **Paul Meeneghan** - For [favourites app](https://github.com/pmeeny)

- **Eduardo Boucas** - For [approaching media queries in sass](https://css-tricks.com/approaches-media-queries-sass/)

- **CSS Tricks** - For [approaching nesting in sass](https://css-tricks.com/the-sass-ampersand/)

- **Lucy Wheel** - For [zoom image hover effect](https://codepen.io/lucy_wheel/pen/VxYzKP)

- **Code Institute** - For their lessons on Python and Django, particularly the Boutique Ado project.

- **Chris Bongers** - For [a star rating system made of SVG paths](https://codepen.io/rebelchris/pen/dyXORMd)

- **Modern CSS Dev** - For [smooth scroll](https://moderncss.dev/pure-css-smooth-scroll-back-to-top/)

- **Reddit** - For [Django sorting method](https://www.reddit.com/r/django/comments/20lxq0/how_to_sort_a_retrieved_list_alphabetically_in_a/)

- **w3schools** - For [image parallax effect](https://www.w3schools.com/howto/howto_css_parallax.asp)

### Media

All images were sourced from the copyright-free image repositories [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/). For full image rights and credit, please see the seperate [media.md](/docs/media.md) file.

The images were edited using [Canva](https://www.canva.com/). The logo for 'KICKS' was also made in Canva.

### Acknowledgements

- To my wife Yasmine Rhoseyn for her testing support and feedback on this project.
- To my mentor Mo Shami for his feedback, advice and support.
- To the Code Institute slack community of students and alumni for their helpful advice, resources, guidance and support.
- To the Code Institute support team for their help and guidance when fixing bugs in the codebase.
