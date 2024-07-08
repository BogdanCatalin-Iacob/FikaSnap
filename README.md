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
    *   #### User Profile Model

        | name | type | key | other |
        |------|------|-----|-------|
        | id | BigAuto | | |
        | owner | OneToOne | ForeignKey(user) | on_delete=models.CASCADE |
        | name | CharField | | max_length=255, blank=True |
        | content | TextField | | blank=True |
        | created_at | DateTimeField | | auto_now_add=True |
        | updated_at | DateTimeField | | auto_now=True |
        | image | ImageField | | upload_to='images/', default='../default_profile_utdxde.jpg' |


## Technologies
*   Python
*   Django - REST
*   Cloudinary -> for images storage