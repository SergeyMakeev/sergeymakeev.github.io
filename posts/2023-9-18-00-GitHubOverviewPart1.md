# A Dive into My GitHub Treasures (Part 1/?)

Alright, folks, I thought I'd shake things up a bit by diving into some of my GitHub repositories.
Why? Well, it's part reflection, part code storytelling, and a dash of pushing my writing skills.  


Without further ado, let's dive in.


## TaskScheduler

https://github.com/SergeyMakeev/TaskScheduler  

Back in 2016 (yes, that was a while ago), I stumbled upon Christian Gyrling's GDC presentation about writing a user-mode task scheduler with fibers.
It sparked a plan: a quick (private) prototype, just to taste what using fibers for user-mode scheduling looks like.

It turned out to be way bigger than that and later was used as a production solution for numerous cross-platform games.
Looking back, I see multiple areas for improvement (more scalable, performant, and simpler solution possible).  

But hey, some of these insights made their way into Roblox's proprietary Task Scheduler. Isn't that exciting?

## smmalloc

https://github.com/SergeyMakeev/smmalloc  

During my time at my.games, we were elbows deep in porting [Warface](https://warface.com/en/) for PS4/X1/Switch - an FPS game built using CryEngine.
And, of course, performance was the most challenging thing to solve (it is never enough, especially if you work on a competitive PvP shooter game).
A staggering number of tiny memory allocations dragging performance down was the problem (as you all may know, Jaguar is not the most powerful CPU).  

I decided to write a (pool) memory allocator that sits in front of the OS memory allocator and only handles specific (small) allocation sizes.
If my allocator can't handle the allocation request, then it automatically redirects the memory request to the default OS memory allocator.
Hence, I called this a "proxy allocator".  

It turned out to be blazing fast (~40 CPU cycles per allocation) and solved most of the problems caused by "Typical C++ Builshit".
And of course, I shamelessly named it `smmalloc`, which stands for Sergey Makeev Memory Allocator :) 

Please note that modern memory allocators (like `mimalloc` & co) should be able to handle arbitrary-sized allocations reasonably well,
so you might not get too much performance benefits in that case. But if you still rely on a default OS memory allocator,
it totally makes sense to give `smmaloc` a try, especially if your application is doing millions of small allocations per second. 



More code tales to come...
