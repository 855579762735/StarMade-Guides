# Introduction to StarMade

StarMade is a voxel-based space sandbox game. You explore a procedurally generated universe, build ships and stations block by block, gather resources, craft items, fight enemies, and team up with other players.

## The Universe at a Glance

The universe is divided into **sectors** and **systems**.

## Core Gameplay Loop

1. **Explore** — fly through space, discover planets, asteroids, and trading stations
2. **Mine** — collect raw ores and crystal shards from asteroids and planet surfaces
3. **Craft** — refine materials into components and build blocks
4. **Build** — construct and upgrade ships and stations
5. **Survive** — defend yourself against pirates and rival players

## Game Modes

### Singleplayer
You host your own universe. All admin commands are available. Blueprints are saved to your local `StarMade/blueprints/` folder.

### Multiplayer
You connect to a shared server. Server rules govern admin commands and what you can build. Blueprints saved to a server are stored server-side.

## First Steps

When you first spawn, you will be in **astronaut mode** — a floating humanoid character. The spawn location is configured by the server; on a default setup you will start in a sector where you can find a **trading station** to buy basic supplies.

Your immediate goals:

- Get comfortable with [character movement](03-character-movement.md)
- Familiarise yourself with the [HUD](01-hud-and-interface.md)
- Learn [basic controls](02-basic-controls.md)
- Find some asteroids and mine your first resources

> **Tip:** Check the navigation panel (`N` by default) to locate nearby trading stations, asteroids, and planets from your starting position.

## StarMade Galaxy

StarMade Galaxy is a new version of StarMade built in Unity SRP that one of the developers of the original game is working on in their free time. This version of the game is publicly unavailble, however you can support [Schema via Patreon](https://patreon.com/StarMade) to gain access to the experimental branch of StarMade Galaxy, but there is currently [no build yet](https://discord.com/channels/100173352475303936/1476338467406610665/1516863860995391509). Note that this is completely optional, and that the official Java version is still maintained and widely used throughout the community. If you're new to StarMade the suggestion remains to stick to the **Java version** [from Steam](https://store.steampowered.com/app/244770/StarMade/) or the [official StarMade site](https://www.star-made.org/download/). There is a teaser trailer of StarMade Galaxy available on [YouTube](https://www.youtube.com/watch?v=3QalCPiWq-k).

### Galaxy FAQ

As you might expect the community has a lot of questions regarding how the two StarMades compare and what might one day be transferable. I've tried to compile the most commonly asked questions beloew and the answers from the developers. Please note, all of this is **subject to change without notice** and is just what we know so far as a community, not an actual plan for development. Please do not yell at our lovely developers due to any of these comments!

1. What shape will planets take in StarMade Galaxy?
> "Cube planets with smoothed terrain edges" [DukeofRealms](https://discord.com/channels/100173352475303936/1476338467406610665/1516851710994415817)

2. What about all the work that's gone into round planets?
> "The round planets that was worked on is still coming in Java StarMade. Although, they were lots of plates, Derp can explain more on that." [DukeofRealms](https://discord.com/channels/100173352475303936/1476338467406610665/1516852563956338749)

3. What about all the good work the community has put into StarMade? 
> "most features will be ported" [VideoGoose](https://discord.com/channels/100173352475303936/1476338467406610665/1516853742685786152)

4. Will StarMade Galaxy have dedicated servers?
> "Yes." [DukeofRealms](https://discord.com/channels/100173352475303936/1476338467406610665/1516853807622127669)

5. Will dedicated servers require GPUs?
> "No, it's not required" [DukeofRealms](https://discord.com/channels/100173352475303936/1476338467406610665/1516868258538721461)

> "GPU will always be faster" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516868414579150979)

6. Will I be able to import ship blueprints?
> "I have some different systems planned, a lot of optimization, and some for just better utility and gameplay however, blueprints will be importable on a block basis - just don't expect your ship to work, lol" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516859038309027890)

7. How will star systems be structured now?
> "In the map, you see Regions (the cake slices + 1 middle) and Zones (in regions). Each zone will have a system that determines who controls it. This will be NPC or unowned. But I also plan to make each region matter for not only who's there, what's there, and other gameplay elements" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516862504863666176)

> "Systems are still technically defined in a cube, but sectors are more or less not the deciding factor anymore" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516863193627234426)

8. Can I help make StarMade Galaxy?
> "I'll be open for it. Also for the mod team of course" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516864188624928949)

9. Will most of the non game infrastructure like the Discord and dock be carried over?
> "Yeah, we'll be also launching a [fluxer](https://fluxer.app/) instance. Because discord is getting wild" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516864601181130784)

10. So you jump to a system now and then fly inside of it?
> "yes, the only limiting factor would be that planets can't generate fast enough. They are a few hundreds of magnitude fasten than the old system, but still the planets you see in the video take ~3-5 sec to generate" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516866776787325118)

11. Will there be moons?
> "there are also moons, which I'll probably make round" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516867085496614934)

> "they will not be bumpable like asteroids are and they will likely get gravity" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516886555514634422)

12. Will there be fauna and aliens?
> "ye" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516885360028946462)

13. Will we get water physics for planetary water?
> "planned" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516879243584475229)

14. Will we get cross entity lighting?
> "It's within possibility but not yet there, since it would cost a bit, but it's theoretically possible, yes. Also I'll do some dynamic lighting up close either way" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516882798949040159)

15. Why the rebase to Unity?
> "It's mostly because such deep cuts would have to be made to the old engine that it essentially would be a rewrite either way. I'm using the parts of unity that are actually good. Unity has a ton of problems, mostly the stuff they put upfront. All the good stuff is in the back" [Schema](https://discord.com/channels/100173352475303936/1476338467406610665/1516881371472072706)
