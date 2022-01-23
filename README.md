# CI_MS4_Kicks

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

### Frameworks, libraries and other tools

[Sass](https://sass-lang.com/)

- Sass was used as a CSS extension to speed up development of stylesheets. The features of Sass such as variables, mixins, nesting and seperation of logic was very helpful in this project. 

[Git](https://git-scm.com/)

- Git was used for version control within VSCode to push the code to GitHub.

[GitHub](https://github.com/)

- GitHub was used as a remote repository to store project code.

[Unsplash](https://unsplash.com/)

- All images used in the website apart from the logo were from the online copyright-free repository, Unsplash. See Credits for more information.

[Am I Responsive](http://ami.responsivedesign.is/)

- Am I Responsive was used to create the multi-device mock-up you see at the start of this README.md file.

[Visual Studio Code (VSCode)](https://code.visualstudio.com/)

- VSCode was the IDE used to write the code for this project. The following extensions were used for this project:

- *markdownlint*: To keep consistent styling on markdown files.
- *SpellChecker*: To spell check markdown files.
- *TODO Highlight*: To keep track of outstanding tasks, bugs that need to be fixed and annotations throughout the development process.
- *Tokyo Night*: For syntax highlighting & styling of VSCode.
- *vscode-pdf*: To view the wireframes.pdf file within VSCode.
- *Terminal Tools*: Provides buttons among terminal for command shorthands, making interacting with the terminal faster.
- *Live Sass Compiler*: Watches for changes in scss files and compiles them to css files automatically. I've customised the settings to compile my .scss files into a singular .min.css file in my static directory.

[Tiny PNG](https://tinypng.com/)

- TinyPNG was used to compress images for improved website performance.

[Gorgias SKU Generator](https://www.gorgias.com/tools/sku-generator)

- Gorgias SKU Generator was used to generate SKU values. Please see [Database Design](#Database-Design) for more information on SKU architecture within the fixtures.

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

- **Bug 1**: Product model throwing errors when attempting to make migration
- **Fix**:  Change attribute on an IntegerField from max_digits to the Django method MaxValueValidator. Add on_delete attribute to ForeignKeys. Add max_digits attribute to DecimalFields.
- **Bug 2**: When searching using the search bar Django would throw a FieldError and could not resolve 'name_icontains'.
- **Fix**: From consulting Django documentation I realised I had mistakenly only used one underscore (_) instead of two before 'icontains'.

## Deployment

## Credits

### Code

- **Stack Overflow**: For fixing [max_length on IntegerField](https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield) bug.

- **test-driven-django-development**: For [model unit testing methods](https://test-driven-django-development.readthedocs.io/en/latest/02-models.html).

- **Cory House**: For [adding aria-current attributes to current pages](https://twitter.com/housecor/status/1476910306702077954/photo/1)

- **Ignacio Lozano** - For [using coverage in Django for testing](https://www.bedjango.com/blog/package-week-coverage-django/)

- **Eduardo Boucas** - For [approaching media queries in sass](https://css-tricks.com/approaches-media-queries-sass/)

- **CSS Tricks** - For [approaching nesting in sass](https://css-tricks.com/the-sass-ampersand/)

- **Lucy Wheel** - For [zoom image hover effect](https://codepen.io/lucy_wheel/pen/VxYzKP)

- **Code Institute** - For their lessons on Python and Django, particularly the Boutique Ado project.

- **Chris Bongers** - For [a star rating system made of SVG paths](https://codepen.io/rebelchris/pen/dyXORMd)

### Media

All images were sourced from the copyright-free image repositories [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/). For full image rights and credit, please see the seperate [media.md](/docs/media.md) file.

The images were edited using [Canva](https://www.canva.com/). The logo for 'KICKS' was also made in Canva.

### Acknowledgements

- To my wife Yasmine Rhoseyn for her testing support and feedback on this project.
- To my mentor Mo Shami for his feedback, advice and support.
- To the Code Institute slack community of students and alumni for their helpful advice, resources, guidance and support.
