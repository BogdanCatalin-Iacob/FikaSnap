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