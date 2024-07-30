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
        | owner | CharField | ForeignKey(User) | on_delete=models.CASCADE |
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
        | owner | CharField | ForeignKey(User) | related_name='following', on_delete=models.CASCADE |  
        | followed | CharField | ForeignKey(User) | related_name='followed', on_delete=models.CASCADE |  
        | created_at | DateTimeField |  | auto_now_add=True | 

    *   #### Like

        | name | type | key | other |
        | ---- | ---- | --- | ----- |
        | id | BigAuto |  |  |
        | owner | CharField | ForeignKey(User) | on_delete=models.CASCADE |
        | post | CharField | ForeignKey(Post) | on_delete=models.CASCADE, related_name='likes' |
        | created_at | DateTimeField |  | auto_now_add=True |
    
    *   #### Comment

        | name | type | key | other |
        | ---- | ---- | --- | ----- |
        | id | BigAuto |  |  |
        | owner | CharField | ForeignKey(User) | on_delete=models.CASCADE |
        | post | CharField | ForeignKey(Post) | on_delete=models.CASCADE |
        | created_at | DateTimeField |  | auto_now_add=True |
        | updated_at | DateTimeField |  | auto_now=True |
        | content | TextField |  |  |


## Technologies
*   Python
*   Django - REST
*   [Cloudinary](https://cloudinary.com) -> for images storage
*   [DBDiagram](https://dbdiagram.io) -> create db diagram