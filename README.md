# Knotelry
Knotelry is a proof-of-concept web application serving primarily as a journaling alternative to [Ravelry](https://en.wikipedia.org/wiki/Ravelry). With a stronger focus on multi-craftual experiences and personal project logging (rather than Ravelry's strong database of knitting and crafting-related information), Knotelry will allow for greater flexibility of different crafts, from knitting to crocheting, from spinning to weaving, from sewing to needlework, and much more!
<br />
Knotelry is a small practice project for me to familiarize myself with a VueJS framework.


[Link to Live Site (Please be patient for the site to wake up)](https://knotelry.herokuapp.com/)

<br />

# Technologies Used
Knotelry is  built on a VueJS frontend, a Python / Flask backend, and a PostgreSQL database. Additionally, AWS S3 is implemented for image uploads.
<br />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" height=40/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height=40/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height=40/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg" height=40 />  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" height=40/>  <img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"  height=40/>  <img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"  height=40/>  <img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"  height=40/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-plain-wordmark.svg" height=40/>  <img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"  height=40/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height=40/>  <img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"  height=40/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" height=40 />

<br />

# How to Get Started
1. Clone this repository
```bash
   git clone https://github.com/kim-yura/knotelry
```
2. Install dependencies in the root directory
```bash
   pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
```
3. `CD` into the `/vue-app` directory and install dependencies
```bash
   npm install
```
4. Create a `.env` file based on the example with proper settings for your development environment, including an AWS S3 account for image uploads if desired
5. Set up a PostgreSQL user based on your `.env` file
6. Start your shell, migrate your database, seed your database, and run the `flask app`
```bash
   pipenv shell
   flask db upgrade
   flask seed all
   flask run
```
7. In a new terminal, `CD` into `/vue-app` and run the Vue app
```bash
   npm run serve
```

<br />

# Features

## User Authentication and Profile
Users may sign up for a new account, log in to an existing account, or try out the site using the demo account provided. In addition to full authentication, users are presented with a number of profile customization options, as well as a user profile page from which they can view their stats and link to other features. As more features are added to Knotelry, more user control over the specific stats to be displayed can be expected.
<br /> <br />
![Screenshot of user profile page](https://user-images.githubusercontent.com/89601983/164038923-e7300f3a-a643-4993-9869-156b75c35e4d.png)
![Screenshot of user profile customization options](https://user-images.githubusercontent.com/89601983/164038940-18a27013-5000-48b0-b7f6-6e91bb190380.png)

<br />

## Toolbox (Full CRUD)
Every maker knows we need our tools! The toolbox is a way for users to catalog and keep track of their various multicraftual tools. Users may upload new tools with information fields for title, an image, description, date acquired, status (more options to come soon), and as many craft buttons as are applicable. Users may edit or delete uploaded tools. An exhaustive search option in the main view allows users to search and filter through their toolbox for the perfect tool for their next project.
<br />
In addition, tools can be linked to in projects (more on that in the Projects feature).
<br /> <br />
![Screenshot of DemoUser's toolbox](https://user-images.githubusercontent.com/89601983/164040865-63da92b4-f65a-4fbc-b4c0-8eb2a5ec1295.png)
![Screenshot of editing an existing tool](https://user-images.githubusercontent.com/89601983/164040867-7e2ca5e9-9a2d-4c20-ab3a-9598b6045211.png)

<br />

## Stash (Full CRUD)
Knotelry's Stash feature allows users to catalog and keep track of the various items in their crafting stash. Currently, yarn and fiber are supported, but plans to incorporate fabric, threads, and embroidery floss are upcoming. In addition to uploading, editing, and deleting stash items, users may use the search feature to filter through their stash, including by type, status, title or description, colors, minimum fiber weight (for fiber), and minimum yardage (for yarn).
<br />
In addition, stash items can be linked to in projects (more on that in the Projects feature).
<br /> <br />
![Screenshot of DemoUser's stash view](https://user-images.githubusercontent.com/89601983/164041894-80a0056d-59d1-4000-8b39-f528100edf48.png)
![Screenshot of detailed stash view](https://user-images.githubusercontent.com/89601983/164041899-d5d0b0cb-6011-486a-a7c7-79e6b2722c2b.png)
![Screenshot of editing an existing stash item](https://user-images.githubusercontent.com/89601983/164041896-da01aaf7-015e-4ec9-9a0d-1acdcc925eb4.png)

<br />

## Projects (Full CRUD)
Regardless of the number of crafts incorporated, users may create appropriate Project pages. Projects include metadata fields such as title, pattern used (if any), description, status, tags, attributes, and start and finish dates. Projects may also include craft-specific fields such as needle sizes used for knitting, and grist, WPI, and spin directions for spinning. Users may upload as many photos of their project as they desire.
<br />
Additionally, users may link any tools in their toolbox and any item in their stash to projects. With stash items, users may also specify the quantity used. Currently, only yarn items will update amounts remaining in their stash page, but fiber and future types of stash items will have analogous remainders calculated for the user.
<br /> <br />
![Screenshot of DemoUser's project view](https://user-images.githubusercontent.com/89601983/164045901-cec5faa6-97e0-4dc7-8388-6ed84211f203.png)
![Screenshot of an example knitting project](https://user-images.githubusercontent.com/89601983/164045904-22181e8f-2529-4db9-a9a3-fdfd50f19a4a.png)
![Screenshot of an example spinning project](https://user-images.githubusercontent.com/89601983/164045906-a34155de-4b6e-4747-8433-73441db7ecdd.png)

<br />

## Additional Quality-of-Life Features

### Auto-Populating Fields for Yarn
Users no longer have to manually calculate length based on weight. If the user knows the length and weight in one skein, they only need to input one of the following -- total skeins, length, or weight (length and weight are utilizing units of the user's choosing) -- to calculate the other two values.
<br /> <br />
![GIF of auto-populating fields in action](https://user-images.githubusercontent.com/89601983/164046797-348d76db-51cb-4d35-96c2-8b21a0153268.gif)

### Customizable Project Forms
Users may mix-and-match craft types to create custom project forms. By limiting the number of options available to the user based on the project chosen, but by allowing the user the freedom to choose as many crafts as they want, Knotelry aims to give users a streamlined experience that is not overwhelming but suits their multicraftual needs.
<br /> <br />
![GIF of customizable project forms in action](https://user-images.githubusercontent.com/89601983/164046799-1f402598-7cc9-4b17-8bc0-9ddbd07258be.gif)

### Dynamic Search in Projects
When editing projects, users may link to existing tools and stash items using the dynamic search and link feature. This feature searches through using title and description of items.
<br /> <br />
![GIF of dynamic search in action](https://user-images.githubusercontent.com/89601983/164048334-53a2dcfd-4074-4a9f-a729-4a1b73604424.gif)

<br />

# Future Additions

Additional crafts and material types will need to be supported, including:

### Crafts:
<li> Weaving </li>
<li> Sewing </li>
<li> Needlework </li>

### Materials:
<li> Fabric </li>
<li> Thread </li>
<li> Embroidery Floss </li>

<br />

While Knotelry is more of a proof-of-concept rather than an actual project, it may be fun and worthwhile to get the crafting community's input on future features to implement!

Although there are no plans at the moment to incorporate a Ravelry-style database of patterns, that may be something to consider.

The primary goal of this project was for me to teach myself VueJS, and I'm happy to say that I think I've succeeded. 😊🧶
