# Table of contents

- [Testing](#testing)
  - [Code validation](#code-validation)
  - [Unit Testing](#unit-testing)
  - [Device and browser testing](#device-and-browser-testing)
  - [Testing user stories](#testing-user-stories)


# Testing

## Code validation

### PEP8 Compliance

PEP8 compliance was manually tested with [PEP8Online](http://pep8online.com/).

Files tested and their result:

| File  | Result | PEP8Online file |
 ------ | :------------ | ---------------- |
bag/apps.py | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_bag_apps.txt) |
bag/contexts.py | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_bag_contexts.txt) |
bag/test_urls.py | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_bag_urls.txt) |
bag/test_views.py | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_bag_testviews.txt) |
bag/views.py | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_bag_views.txt) |
brands/admin.py | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_admin.txt) |
brands/apps.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_apps.txt) |
brands/forms.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_forms.txt) |
brands/models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_models.txt) |
brands/test_forms.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_testforms.txt) |
brands/test_models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_testmodels.txt) |
brands/test_urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_testurls.txt) |
brands/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_urls.txt) |
brands/views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_brands_views.txt) |
checkout/admin.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_admin.txt) |
checkout/apps.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_apps.txt) |
checkout/forms.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_forms.txt) |
checkout/models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_models.txt) |
checkout/signals.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_signals.txt) |
checkout/test_forms.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_testforms.txt) |
checkout/test_models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_testmodels.txt) |
checkout/test_urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_testurls.txt) |
checkout/test_views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_testviews.txt) |
checkout/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_urls.txt) |
checkout/views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_views.txt) |
checkout/webhook_handler.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_webhookhandler.txt) |
checkout/webhooks.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_checkout_webhooks.txt) |
favourites/admin.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_admin.txt) |
favourites/apps.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_apps.txt) |
favourites/models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_models.txt) |
favourites/test_models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_testmodels.txt) |
favourites/test_urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_testurls.txt) |
favourites/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_urls.txt) |
favourites/views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_favourites_views.txt) |
home/apps.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_home_apps.txt) |
home/test_urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_home_testurls.txt) |
home/test_views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_home_testviews.txt) |
home/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_home_urls.txt) |
home/views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_home_views.txt) |
kicks/settings.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_kicks_setting.txt) |
kicks/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_kicks_urls.txt) |
products/admin.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_admin.txt) |
products/apps.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_apps.txt) |
products/forms.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_forms.txt) |
products/models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_models.txt) |
products/test_models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_testmodels.txt) |
products/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_urls.txt) |
products/views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_views.txt) |
products/widgets.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_products_widgets.txt) |
profiles/apps.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_apps.txt) |
profiles/forms.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_forms.txt) |
profiles/models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_models.txt) |
profiles/test_models.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_testmodels.txt) |
profiles/test_views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_testviews.txt) |
profiles/urls.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_urls.txt) |
profiles/views.py| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/pep8_compliance/pep8_profiles_views.txt) |


### HTML Validation

All pages were manually validated with the [W3C Markup validation service](https://validator.w3.org/)

| File  | Result | HTML validation service |
 ------ | :------------ | ---------------- |
/ (home) | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/home.png) |
/accounts/login.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/accounts_login.png) |
/accounts/logout.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/accounts_login.png) |
/accounts/signup.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/accounts_logout.png) |
/accounts/password/reset.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/accounts_password_reset.png) |
/accounts/confirm-email.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/accounts_confirm_email.png) |
/bag.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/bag.png) |
/checkout.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/checkout.png) |
/checkout_success.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/checkout_checkout_success.png) |
/checkout_success.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/checkout_checkout_success.png) |
/brands.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/brands.png) |
/brands/add_brand.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/brands.png) |
/brands/edit_brand.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/brands.png) |
/favourites.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/favourites.png) |
/products.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/products.png) |
/products/add_product.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/products_add_product.png) |
/products/edit_product.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/products_edit_product.png) |
/products/add_review.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/products_add_review.png) |
/products/edit_review.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/products_edit_review.png) |
/products/? (search query) | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/products_search_param_example.png) |
/profiles.html | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/html_validation/profile.png) |



### JSHints


JavaScript validation was manually tested with [JSHint](https://jshint.com/)

Files tested and their result:

| File  | Result | JShint report |
 ------ | :------------ | ---------------- |
checkout/stripe_elements.js | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/jshint/checkout_stripelements.png) |
products/templates/product.html (filtering feature) | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/jshint/products.png) |
profiles/static/profiles/js/countryfield.js | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/jshint/profiles_countryfield.png) |
static/js/search.js | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/jshint/static_search.png) |

### CSS Validation

CSS validation was manually tested with the [W3C CSS validation service](https://jigsaw.w3.org/css-validator/)

| File  | Result | CSS validation service |
 ------ | :------------ | ---------------- |
checkout/static/checkout/css/checkout.css | 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/css_validation/css_validation.png) |
static/css/base.css| 0 errors, 0 warnings | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/css_validation/css_validation.png) |

### WAVE accessibility tool

All pages were manually checked using [WebAIM's WAVE tool](https://wave.webaim.org/)

| Page  | Result | WAVE report |
 ------ | :------------ | ---------------- |
home | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/home_index.png) |
accounts/verification_sent | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/account_emailsent.png) |
accounts/login | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/account_login.png) |
accounts/logout | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/account_logout.png) |
accounts/password_change | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/account_password_change.png) |
accounts/password_reset_done | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/account_password_reset_done.png) |
accounts/register | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/account_register.png) |
bag | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/bag.png) |
brands/{all brands} | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/brands_allbrands.png) |
brands/{example brand} | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/brands_example.png) |
checkout | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/checkout.png) |
checkout/checkout_success | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/checkout_success.png) |
favourites | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/favourites.png) |
product/{all products} | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/product_allproducts.png) |
product/{individual_product} | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/product_individual_product.png) |
product/?product_group=childrens | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/product_kids.png) |
product/?product_group=womens | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_womens.png) |
product/?product_group=mens | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_mens.png) |
product/?product_type=baby| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_baby.png) |
product/?product_type=boots| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_boots.png) |
product/?product_type=brogues| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_brogues.png) |
product/?product_type=daps| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_daps.png) |
product/?product_type=heels| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_heels.png) |
product/?product_type=pumps| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_pumps.png) |
product/?product_type=socks| 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/products_socks.png) |
review/add_review | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/review_add_review.png) |
review/edit_review | 0 errors, 0 contrast errors | [Report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/wave/review_edit_review.png) |



## Unit Testing

Unit testing was used across the project to test key functionality.

I reached a coverage of 60%, ideally I would have liked to reach more but had time constraints so chose to focus on the core essentials of each app. Please see below evidence of this coverage, and please see the [full coverage report](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/coverage_full_report.pdf) if you would like more details.

![Coverage report example](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/coverage_percentage.png)

All tests are passing.

Bag app unit tests:

![Bag unit tests](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/unit_testing_bag_app.png)

Brands app unit tests:

![Brands unit tests](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/unit_testing_brands_app.png)

Favourites app unit tests:

![Favourites unit tests](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/unit_testing_favourites_app.png)

Home app unit tests:

![Home unit tests](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/unit_testing_home_app.png)

Products app unit tests:

![Products unit tests](https://github.com/TaraRhoseyn/CI_MS4_Kicks/blob/main/docs/unit_testing/unit_testing_products_app.png)

## Device and browser testing

### Devices tested

- Huawei PRA-LX1: Website and user stories work as expected.
- iPhone SE: Website and user stories work as expected.
- LENOVO IdeaCentre 3 Desktop PC with a 34" monitor: Website and user stories work as expected.
- DELL Inspiron 15 5593: Website and user stories work as expected.

### Browsers tested

- Google chrome: Website and user stories work as expected.
- Microsoft Edge: Website and user stories work as expected.
- Safari: Website and user stories work as expected.
- Firefox: Website and user stories work as expected.

## Testing user stories

| User story  | Feature(/s) | Action | Result |
 ------ | :------------ | ---------------- | ---- |
(1) As a first-time user, I want to checkout without creating an account for ease of use. | Bag, product and checkout pages | Add products to bag. Be prompted to register or login. Register or login. Go to bag. Checkout. Checkout success. Checkout success email | Works as expected, [view result]() |
(2) As a first-time user, I want to immediately understand what is being sold at the store. | Home page | Visit home page with three core sections to gain information on the store | Works as expected, [view result] |
(3) As a first-time/regular user, I want to able to navigate around the website in a way that is intuitive and easily understandable so I can browse freely.| Navigation bar | Navigation bar takes you to all core pages of the site, alongs you to search, access your bag, checkout, user profile, logout, and product management | Works as expected, [view result] |
(4) As a first-time/regular user, I want to view all products at once to freely browse.| Products page | See all products on the Products page | Works as expected, [view result] |
(5) As a first-time/regular user, I want to be able to search product by most expensive to least expensive so I can make a decision that makes sense with my budget. | Products page and all product pages with URL search params | Click 'Price' with down arrow and products filter by most to least expensive. | Works as expected, [view result] |
(6) As a first-time/regular user, I want to be able to search product by least expensive to most expensive so I can make a decision that makes sense with my budget. | Products page and all product pages with URL search params | Click 'Price' with up arrow and products filter by least to most expensive. | Works as expected, [view result] |
(7) As a first-time/regular user, I want to view products by how highly rated they are so I can feel confident in my purchasing decision. | Products page and all product pages with URL search params | Click 'Rating' with up arrow and products filter by most highly rated. | Works as expected, [view result] |
(8) As a first-time user/regular user, I want to be directed to an error page if I am directed to a broken URL or experience a server error. | Error pages | Type wrong URL into search bar and be directed an error page | Works as expected, [view result] |
(9) As a first-time user, I want to create an account so I can save and update delivery information. | Register, profile page | Click Register on icon drop down menu in navbar. Create account. Verify email. Log back in. Go to Profile page from icon drop down menu and view/update delivery information  | Works as expected, [view result] |
(10) As a first-time user, I want to create an account so I can view my future order history in one place. | Register, profile page | Click Register on icon drop down menu in navbar. Create account. Verify email. Log back in. Go to Profile page from icon drop down menu and view order history  | Works as expected, [view result] |
(11) As a first-time user, I want to create an account so I can favourite products that I can revisit later. | Register, profile, favourite page | View profile. Click 'See my favourites'. View favourites.  | Works as expected, [view result] |
(12) As a first-time/regular user, I want to see reviews of products so I can see if it’s the right product for me based on other user feedback. | Individual product pages, reviews | View individual product pages from products pages, view reviews.  | Works as expected, [view result] |
(13) As a first-time/regular user, I want to add items to shopping bag so I can order multiple items in one go. | Individual product pages, bag, checkout | Add products to bag from individual product view, go to bag, go to checkout, place order | Works as expected, [view result] |
(14) As a first-time/regular user, I want to see only women’s products at a time.| Women's page | View products filtered by only women's from clicking on the navigation bar link | Works as expected, [view result] |
(15) As a first-time/regular user, I want to see only men's products at a time.| Women's page | View products filtered by only men's from clicking on the navigation bar link | Works as expected, [view result] |
(16) As a first-time/regular user, I want to see only children's products at a time.| Women's page | View products filtered by only children's from clicking on the navigation bar link | Works as expected, [view result] |
(17) As a first-time/regular user, I want to see products related only to the type of product I’m interested in, e.g. socks or daps or trainers. | Product filtering | View products filtered by type from clicking on the navigation bar link | Works as expected, [view result] |
(18) As a first-time/regular user, I want to see all of the brands that sell products on the store. |  Brands page | View all brands by alphabetical order and with links from clicking on the navigation bar link | Works as expected, [view result] |
(19) As a first-time/regular user, I want to see items relating only to the specific brands I select. |  Products filtered by brand name individual view | Click on a brand name from the brands pagea and be directed to all products with the brand name that match | Works as expected, [view result] |
(20) As a first-time/regular user, I want quick user feedback when I have made a change to my account. |  Toasts, profiles page | Update account on profile page. Toast appears if successful. | Works as expected, [view result] |
(21) As a first-time/regular user, I want quick user feedback  when I have added an item to my shopping bag or removed it. |  Toasts | Add bag to item. Toast appears if successful. | Works as expected, [view result] |
(22) As a first-time/regular user, I want to view my profile to update delivery information.  |  Profiles page | Log in or register. Click 'My profile' on navbar. View profile page with delivery information to update. Update information. Recieve confirmation. | Works as expected, [view result] |
(23) As a first-time/regular user, I want to view my profile to view my order history.  |  Profiles page | Log in or register. Click 'My profile' on navbar. View profile page with order history. | Works as expected, [view result] |
(24) As a first-time/regular user, I want to favourite items that I can revisit later. |  Profiles page, favourites | Log in or register. View an individual product view. Hit the red heart. View 'My Favourites' from the icon drop down menu. View favourites on favourites page. | Works as expected, [view result] |
(25) As a first-time/regular user, I want to view my favourited items. | Favourites |Log in or register. View an individual product view. Hit the red heart. View 'My Favourites' from the icon drop down menu. View favourites on favourites page. | Works as expected, [view result] |
(26) As a first-time/regular user, I want to search the product catalog. | Search |Use the search bar in the navigation bar to search for products. | Works as expected, [view result] |
(27) As a first-time/regular user, I want feedback that my shopping bag is empty. | Bag page, navigation bar | Cart icon gives no positive indication of items and bag is empty when going to the bag page after clicking the cart icon. | Works as expected, [view result] |
(28) As a first-time/regular user, I want to view all the products in my shopping bag at once if not empty. | Bag page | Go to bag page from cart icon or toast. Finds all items. | Works as expected, [view result] |
(29) As a first-time/regular user, I want to easily remove or update items in the shopping bag.  | Bag page | Go to bag page from cart icon or toast. Finds all items. Update or delete any items. Receive confirmation of change via toast. | Works as expected, [view result] |
(30) As a first-time/regular user, I want to checkout with my delivery information, payment information and complete my order. | Checkout page | Go to bag page from cart icon or toast. G o to checkout. Input details. Hit checkout. See loading screen while payment awaiting. Checkout success. Email confirmation. | Works as expected, [view result] |
(31) As a first-time/regular user, I want positive confirmation that my order has been successfully completed. | Checkout page | Go to bag page from cart icon or toast. G o to checkout. Input details. Hit checkout. See loading screen while payment awaiting. Checkout success. Email confirmation. | Works as expected, [view result] |
(32) As a first-time/regular user, I want feedback that my order is currently being processed. | Checkout page | Go to bag page from cart icon or toast. G o to checkout. Input details. Hit checkout. See loading screen while payment awaiting. Checkout success. Email confirmation. | Works as expected, [view result] |
(33) As a regular user, I want to add reviews to products to give other users feedback. | Products page, reviews | Go to individual product view. Scroll to bottom. See reviews. See 'leave review'. Must be logged in. Go to review page. Input details. Leave review and rating. Review now appears in individual product view. | Works as expected, [view result] |
(34) As a regular user, I want to remove products from my favourites if I am no longer interested in. | Favourites | Go to favourites page from the profiles page (from the navbar). See all favourites and a button to remove. Or, stay on the individual product view of a favourited item and uncheck the red heart icon | Works as expected, [view result] |
(35) As a regular user, I want to reset my password in case I forget it. | Login page, Password reset | Go to log in page. Click reset password. Reset password. Receive confirmation. | Works as expected, [view result] |
(36) As a regular user, I want to edit product reviews if I wish to update it. | Product page, reviews | Go to individual product view. Scroll to bottom. See reviews. See 'edit'. Must be logged in. Go to review page. Input details. Update review and rating. Review now appears in individual product view. | Works as expected, [view result] |
(37) As a regular user, I want to remove product reviews if I change my mind. | Product page, reviews | Go to individual product view. Scroll to bottom. See reviews. See 'delete'. Must be logged in. Delete review. | Works as expected, [view result] |
(38) As a regular user, I want to log out of my account. |Log out page | Log out from the navigation bar drop down menu (must already be logged in). Go to confirmation page. Log out. | Works as expected, [view result] |
(39) As a store owner (superuser), I want to add products to the store to limit dev dependency. | Admin, product management page | Go to admin or product management page. Add product. | Works as expected, [view result] |
(40) As a store owner (superuser), I want to edit products in the store to quickly update inventory without dev dependency. | Admin, individual product page | Go to admin or individual product page. Edit product. Go to edit product page. Fill in details. Submit. Product is changed. | Works as expected, [view result] |
(41) As a store owner (superuser), I want to delete products from the store to quickly update inventory without dev dependency. | Admin, individual product page | Go to admin or individual product page. Delete product. Product is deleted. | Works as expected, [view result] |
(42) As a store owner (superuser), I want to edit or delete user reviews for reputational safety. | Admin, individual product page | Go to admin or individual product page. Edit or delete review. If edit, go to form page to edit. Save. Changes are made. | Works as expected, [view result] |
(43) As a store owner (superuser), I want to add brands to the store to limit dev dependency. | Admin, brand page, add brand page | Go to brand page (or admin), click Add Brand. Go to form page. Submit details. Brand is added. | Works as expected, [view result] |
(44) As a store owner (superuser), I want to edit brands in the store to quickly update inventory without dev dependency.| Admin, brand page, edit brand page | Go to brand page (or admin), click Edit next to a Brand name. Go to form page. Submit details. Brand is changed. | Works as expected, [view result] |
(45) As a store owner (superuser), I want to delete brands from the store to quickly update inventory without dev dependency.| Admin, brand page | Go to brand page (or admin), click Delete next to a Brand name. Go to form page. Brand is deleted. | Works as expected, [view result] |
(46) As a store owner (superuser), I want to add product types in the admin in case our inventory grows.| Admin | Go to admin as a superuser, go to product types model, add product type with all fields. Product type is added. | Works as expected, [view result] |
(47) As a store owner (superuser), I want to edit product types in the admin in case our inventory changes.| Admin | Go to admin as a superuser, go to product types model, edit product type with all fields. Product type is changed. | Works as expected, [view result] |
(48) As a store owner (superuser), I want to add product groups to the admin in case our inventory grows.| Admin | Go to admin as a superuser, go to product groups model, add product group with all fields. Product group is added. | Works as expected, [view result] |
(49) As a store owner (superuser), I want to edit product groups in the admin in case our inventory changes.| Admin | Go to admin as a superuser, go to product group model, edit product group with all fields. Product group is changed. | Works as expected, [view result] |
(50) As a store owner (superuser), I want to view product reviews in the admin to see which products are popular. | Admin | Go to admin as a superuser, go to reviews model, view all reviews | Works as expected, [view result] |
(51) As a store owner (superuser), I want to view what products users have favourited in the admin to see which products are popular.| Admin | Go to admin as a superuser, go to favourites, click user, view all favourites. | Works as expected, [view result] |
(52) As a store owner (superuser), I want to see orders placed in the admin so I can fulfil them. | Admin | Go to admin as a superuser, go to orders, view all orders. | Works as expected, [view result] |
(53) As a store owner (superuser), I want to edit orders placed in the admin in case a user gets in contact to make changes due to a mistake.  | Admin | Go to admin as a superuser, go to orders, view all orders. Click order. Make changes.  | Works as expected, [view result] |
(54) As a store owner (superuser), I want to see all other users of the website so I can see the popularity of the website, manage staff permissions or view customer details. | Admin | Go to admin as a superuser, go to users, view all users | Works as expected, [view result] |
(55) As a store owner (superuser), I want to see user email addresses associated with the website so I can create a marketing email list if the correct marketing permissions are set. | Admin | Go to admin as a superuser, go to users, view all users and their email addresses | Works as expected, [view result] |