# A Dive into My GitHub Treasures (Part 2/?)

Continuation. The previous part is available [here.](/posts/2023-9-18-00-GitHubOverviewPart1.md)

## Arcade Car Physics

https://github.com/SergeyMakeev/ArcadeCarPhysics

I've always been fascinated by the thrill arcade racing games like Burnout, TrackMania, and others provide.
They let you pull off insane stunts, driving at breakneck speeds. Despite the seemingly chaotic gameplay, underlying predictability and control make the experience super fun.
I always wanted to work on something like this but never had the chance. During my tenure at my.games, we did collaborate with Slightly Mad Studios on a game called "World of Speed", but that's a different story.  


Eager to capture the essence of these games, I embarked on a mission: to dissect the mechanics behind arcade racers and to create my own playable racing demo.
I read through hundreds of technical papers, conference presentations, and open-source repositories before diving into custom arcade physics.

I picked the Unity engine for this endeavor, and I crafted a demo without relying on any built-in vehicle physics.
Now, I understand even better the delicate balance between simulation and arcade elements that gives players that exhilarating sense of control.
It's somewhat analogous to aim assist in console shooters: a lot is happening behind the scenes to ensure a best player's experience.  

![Arcade Car Physics](/media/arcade_car_physics.gif)

Later on, I came across [a technique involving a moving sphere.](https://twitter.com/KenneyNL/status/1107783904784715788)
It was simply elegant and blew my mind.

![Sphere Car](/media/sphere_car.gif)


Surprisingly, my prototype wasn't just a pet project.
It caught the attention of academia and made its way into [a research paper.](http://profs.ic.uff.br/~troy/papers/2019_EntComp.pdf)
I surely didn't see that coming!  


**P.S.** Regrettably, I had to remove the precompiled executable.  
Given recent changes with Unity, I'd rather avoid any unexpected financial obligations to them.  


More code tales to come...
