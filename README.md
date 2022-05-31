# Mortal Typthon

[Live site can be found here](#)

Mortal Typthon is a text based battle game written in Python. The basic idea of the game is for you, the player, to beat your AI opponent, by attacking or healing as needed. Which player wins is determined by which players health reaches 0 or below first. The game will continue to play in a loop until the player quits.

## Features
On starting the game, the player is greeted with a welcome message, as well as a prompt to enter their name as illustrated below:


Welcome Screen:

![Welcome-Screen](screenshots/welcome-screen-shot.png)

Once the user enters their name, the player and opponents health are shown, as well as the options of: 1 "attack", 2 "heal", 3 "exit game" and 4 "display results" as per illustration below:

Options Screen:

![Options-Screen](screenshots/options-screen-shot.png)

The player must then select options 1-4 by typing in the relevent number.

1) Attack:
This will decrease both player and opponent health by a random number between 10 and 20 as shown below:

![Attack-Screen](screenshots/attack-screen-shot.png)

2) Heal:
This will increase the player's health by a maximum of 16, although, the opponent's attack may also lessen or even wipe out the amount of health the player is given when healing as per below:

![Heal-Screen](screenshots/healing-screenshot.png)

3) Exit Game:
This option speaks for itself and will exit the player out of the game completely, while displaying current player and opponent health as per below:

![Exit-Screen](screenshots/exit-screen-shot.png)


### Technologies Used:
- HTML5

 - CSS3

 - Javascript

 - Font awsome font library

 - Google fonts

### Existing Features

 - Task Counter
 This is set to remain at zero while the task list is empty and increase relevent to the amount of tasks on the list at any given time as illustrated below.

 ![task-counter](assets/images/screenshots/task-counter.png)

  ![task-counter-increase](assets/images/screenshots/counter-increase.png)

 

- __Home page__

 - The main list area contains a title, task counterm input field to add to type your tasks and a highlighted red button to add tasks to the list.

  - At the bottom of the main home page, there is a link to a set of instructions, as well as social media icon links to facebook, twitter and instagram. These are illustrated below.


  ![instructions-link-social](assets/images/screenshots/instructions-link-social.png)


 - As the user adds a task, a trash min icon appears beside that task to enable the user to later remove that task once it has been completed, as illustrated below.
    
 ![trash-can-delete](assets/images/screenshots/trash-can-delete.png)

 - __Instructions page__

 - This is to give the user a simple and basic set on instructions on how to use the app.

 - There are also suggestions as to possible uses for the app as well as a link back to the main page and facebook, twitter and instagram social media icons. These are also illustrated below.

  ![Instructions-main](assets/images/screenshots/instructions-main.png)



 ### Features Left to Implement

 - Would like to add a number beside each list item which increases according to the number of items on the list, as well as the already included counter at the top of the list.
 - Would like to improve app layout on smaller screens in future to reduce the need for the user to scroll.
 - Favicon nto displaying properly on live site so had to remove for now as also causing console errors.


## Testing

- Main input field and add button kept popping out of the container on smaller screen sizes. Changed CSS property on input field to 100% of container size to rectify issue.
- Errors in html validator after making social icons live caused by open tags. Rectified tags as needed.
- Tested app live on Samsung Galaxy S22 and found instructions were not fully visbale on smaller screens as they would not scroll. Amended html markup to rectify.
- Social icons and links too close to margins on smaller screens, inserted media quueries to compensate.
- Removed redundent variables cuasing warning in jshint, updated js with es6 code to prevent es6 related errors using const.
- Portrait on medium to small screens hding the input field and could not be accessed. Added scroll to Y axis and allowed input field to move as items added to list to compensate.
- Favicon not displaying unless files are in root directory. Chose to have favicon and leave files in root directory.


### Validator Testing

- HTML
- No errors displayed when code was run through HTML Validator ![html validator](assets/images/screenshots/html-%20validator.png)

https://validator.w3.org/

- CSS

- No errors displayed when code was run through CSS Validator  ![CSS Validator](assets/images/screenshots/css-validator.png)

https://jigsaw.w3.org/css-validator/

- Js

- No errors displayed when code was run through Js Validator
![js Validator](assets/images/screenshots/js-validator-screenshot.png)

https://jshint.com/


## Deployment


The site was deployed to GitHub pages. The steps to deploy are as follows:

1. Login to github and select the correct repository.
2. Select the settings tab at the top the the repository.
3. On the side bar, under the 'code and automation' heading, select 'pages'.
4. Under the source heading, click the 'none' dropdown and select 'masterbranch'.
5. Once done, the page will automaticallty refresh.
6. Site is now live under https://matt70iu.github.io/JavaScript-milestone-V1/ in github pages.

Making a local clone:

1. Login to gitbub and download github desktop.
2. Select the correct repository from the dropdown list in the top left.
3. Secect the 'repository' menu and from it select 'pull'.
4. Select 'open in visual studio code' from the home screen.
5. The repository can now be worked on locally, without the need to gitpod etc.

Forking the repository:

1. Login to Gitbut and select the relevent repository.
2. At the top the the repository (not page), select settings.
3. Then select fork. I am currently not able to fork the repository as I own it, but this this the procedure one would normally follow.


## Credits

- Youtube tutorials used to help build site:

https://www.youtube.com/watch?v=mC45hUE0dNs&t=2s

Channel Link:https://www.youtube.com/channel/UC_H7wrnwGU3g1xrLasMf6Gg (Samir Saini)

- Helped drastically in terms of basic site template as well as putting js code theory into proctise as a real live example.

-----------------------------------------------------------------

https://www.youtube.com/watch?v=-pRg_daFjfk&t=550s

Channel Link:https:https://www.youtube.com/channel/UCCcK9DoXcPYcUYU2aSR7zzQ (learn-webdev)

- Found this very helpful and easy to follow. Helped me to understand targeting of elements better between html and js.

-----------------------------------------------------------------

https://www.youtube.com/watch?v=MkESyVB4oUw&t=1264s

Channel Link:https://www.youtube.com/channel/UCBBGM84ZOs7z5jpTQAaZ_Hg (Tyler Potts)

- Slightly more feature rich example which gave me some great ideas in terms of possible future developement of site/app.

-----------------------------------------------------------------

https://www.youtube.com/watch?v=3T_Jy1CqH9k&t=284s

Channel Link: https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw (kevin Powell)

- Really helped in terms of styling and editing of backgound image(s).

-----------------------------------------------------------------

https://www.youtube.com/watch?v=IhmSidOJSeE&t=715s

 Channel Link: https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw (kevin Powell)

 ----------------------------------------------------------------





### Content

- All wording was written by the developer with the aim of creating a simple, useful to do list.
- Social media icons contained in the footer were sourced from https://www.fontawsome.com.
- Added favicon to site using https://favicon.io/ although could not use in final version.
- Used https://cssgradient.io/ to get backgournd colours.

### Acknowledgements

- My mentor for all his help and advise.
- The tutors at code institue for their helpful assistance.
- The youtubers whose tutorials helped further develop my coding skills.



