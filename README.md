# FikaSnap
This social media app allows users to create an account, connect, and share posts with friends. It gives to users the option to like or comment on other users posts.

## Table of contents
* [User experience design(UX)](#user-experience-design)
    * [User stories](#user-stories)
    * [Structure](#structure)
    * [Design](#design)
        * [Colour scheme](#colour-scheme)
    * [Database](#database)
        * [User  model](#user-model---django-default)
        * [User profile model](#user-profile-model)
        * [Post model](#post)
        * [Follower model](#follower)
        * [Like model](#like)
        * [Comment model](#comment)
    * [Deployment](#deployment)
        * [Local Development](#local-development)
            * [Making a clone](#making-a-clone)
            * [Forking the repository](#forking-the-github-repository)
            * [Local Development](#setting-up-local-environment)
            * [Remote Deployment](#remote-deployment)
            * [Deploying to Heroku](#deployment-to-heroku)
    
## User experience design
*   ### User stories
*   ### Structure
*   ### Design
    *   #### Colour scheme
*   ### Database
    *   #### Database Schema
        *   ![Database Schema](assets\images\db_diagram.png)
    
    *   #### User Model - django default

        | name | type | key | other |
        | ---- | ---- | --- | ----- |
        | id | BigAuto |  |  |
        | username | CharField |  |  |
        | password | CharField |  |  |

    *   #### User Profile Model

        | name | type | key | other |
        |------|------|-----|-------|
        | id | BigAuto | | |
        | owner | OneToOne | ForeignKey(User) | on_delete=models.CASCADE |
        | name | CharField | | max_length=255, blank=True |
        | content | TextField | | blank=True |
        | created_at | DateTimeField | | auto_now_add=True |
        | updated_at | DateTimeField | | auto_now=True |
        | image | ImageField | | upload_to='images/', default='../default_profile_utdxde.jpg' |

    *   #### Post

        | name | type | key | other |
        |------|------|-----|-------|
        | id | BigAuto|  |  |
        | owner | ForeignKey | ForeignKey(User) | on_delete=models.CASCADE |
        | created_at | DateTimeField |  | auto_add_now=True |
        | updated_at | DateTimeField |  | auto_add=True |
        | title | CharField |  | max_length=255 |
        | content | TextField |  | blank=True |
        | image | ImageField |  | upload_to='/images', default='../default_post_fw8lmy', blank=True |
        | image_filter | CharField |  | max_length=32, choices=image_filter_choices, default='normal' |
    
    *   #### Follower

        | name | type | key | other |
        | ---- | ---- | --- | ----- |  
        | id | BigAuto |  |  |  
        | owner | ForeignKey | ForeignKey(User) | related_name='following', on_delete=models.CASCADE |  
        | followed | ForeignKey | ForeignKey(User) | related_name='followed', on_delete=models.CASCADE |  
        | created_at | DateTimeField |  | auto_now_add=True | 

    *   #### Like

        | name | type | key | other |
        | ---- | ---- | --- | ----- |
        | id | BigAuto |  |  |
        | owner | ForeignKey | ForeignKey(User) | on_delete=models.CASCADE |
        | post | ForeignKey | ForeignKey(Post) | on_delete=models.CASCADE, related_name='likes' |
        | created_at | DateTimeField |  | auto_now_add=True |
    
    *   #### Comment

        | name | type | key | other |
        | ---- | ---- | --- | ----- |
        | id | BigAuto |  |  |
        | owner | ForeignKey | ForeignKey(User) | on_delete=models.CASCADE |
        | post | ForeignKey | ForeignKey(Post) | on_delete=models.CASCADE |
        | created_at | DateTimeField |  | auto_now_add=True |
        | updated_at | DateTimeField |  | auto_now=True |
        | content | TextField |  |  |


## Technologies
*   Python
*   Django - REST
*   [Cloudinary](https://cloudinary.com) -> for images storage
*   [DBDiagram](https://dbdiagram.io) -> create db diagram
*   [Heroku](heroku.com) -> django deploy

## Deployment
*   ### Local Development
    * #### Making A Clone
        1.   Login to GitHub and locate the [GitHub Repository](https://github.com/BogdanCatalin-Iacob/FikaSnap)
        2.   Click the <br>![Code](assets\images\github_code_button.png) <br> and then choose your method
        3.   To clone repository using HTTPS, under the "HTTPS" tab copy the link.
        You could also choose to open it with Github Desktop, Visual Studio or download it as zip file.
        4.   Open the command promp on your computer
        5.   Go to the location where you want the clone to be created
        6.   Type `git clone`, and then paste the URL you copied in Step 3
        ```$ git clone https://github.com/BogdanCatalin-Iacob/FikaSnap.git```
        7. Pressing `Enter` on keyboard will create a clone of the repository
    
    * #### Forking the Github Repository
        Forking means making a copy of the original repository on your own GitHub account.
        This gives you your own version to make changes without affecting the original repository.

        1. Login to GitHub and locate the [GitHub Repository](https://github.com/BogdanCatalin-Iacob/FikaSnap)
        2. Locate the `Fork` button at the right top of the github page
        3. Click this to see `Create a new Fork`. Click `Create fork` and you shoud have a copy of the original repository in your GitHub account.
    
    * #### Setting up local environment
        1. Open project in a text editor or IDE.
        2. Create an `env.py` file. It needs to contain the following:
            * DATABASE_URL - this can be obtained from the db host of your choice.
            * SECRET_KEY - This django secretkey for the app. It can be anything you like or use the [django secret key generator](https://djecrety.ir/)
            * CLOUDINARY_URL = This can be obtained from [Cloudinary](https://cloudinary.com)
            * DEV - This variable is used for development environment
        
        ```
        import os
        os.environ["DATABASE_URL"] = 'postgres://xxxxxxxxxxxxxxxxxxxxxxxx'
        os.environ["SECRET_KEY"] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        os.environ["Cloudinary_URL"] = 'cloudinary://xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        os.environ["DEV] = '1'
        ```

        3. Install app requirements
        ```
        $ pip install -r requirements.txt
        ```

        4. Migrate the database models
        ```
        $ python manage.py makemigrations
        $ python manage.py migrate
        ```

        5. Create a super user and follow instructions
        ```
        $ python manage.py createsuperuser
        ```

        6. Run the app locally
        ```
        $ python manage.py runserver
        ```
*   ### Remote Deployment
    The backend of this project was deployed using Heroku.    
    If you don't have an account you can create one [here](https://dashboard.heroku.com/apps "Heroku").

    <br>

*   ### Deployment to Heroku
    1. Login to Heroku account
    2. Create a new app -name must be unique and can be different than your project's name
    3. Setup the following variables:
        * DATABASE_URL - See `Setting up your local environment` above
        * CLOUDINARY_URL - See `Setting up your local environment` above
        * SECRET_KEY - See `Setting up your local environment` above
    4. Go to your local clone folder and make sure it has a Procfile containing 
    ```
    release: python manage.py makemigrations && python manage.py migrate
    web: gunicorn fikasnap_api.wsgi
    ```
    5. Open `settings.py` in your project and add your Heroku app name to ALLOWED_HOSTS:
    e.g. `ALLOWED_HOSTS = ['&lt;heroku app name&gt;.heroku.com', 'localhost'].
    6. Commit chabges to github.
    7. Go back to Heroku app page and click `Deploy`.
    8. On Heroku app page, go to `Deployment method` section and choose [Github](https://github.com/).
    9. A new section will appear called `Connect with Github` giving you an entry box for the repository name to connect to.
    10. Enter the name of your github project and click `Search`.
    11. If the repository exists Heroku will list it. Click `Connect`
    12. Now go down to the next section called `Automatic Deploys`.
    13. Click `Enable automatic deploys` if you want changes pushed to github to be automatically deployed to Heroku.
    14. Click `Deploy branch`.
    You will see the progress bar of the deployment until finally it will say `Your app was successfully deployed`
    15. Now you can open your live app