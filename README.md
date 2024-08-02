# FikaSnap
This social media app allows users to create an account, connect, and share posts with friends. It gives to users the option to like or comment on other users posts.

## Table of contents
* [User experience design(UX)](#user-experience-design)
    * [User stories](#user-stories)
    * [Structure](#structure)
    * [Design](#design)
        * [Colour scheme](#colour-scheme)
    * [Database](#database)
        * [User profile model](#user-profile-model)
    * [Deployment](#deployment)
        * [Project Creation]
        * [Deploying to Heroku]
        * [Local Development]
    
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
        2. Createa an `env.py` file. It needs to contain the following:
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