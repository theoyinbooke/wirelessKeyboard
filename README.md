### What is this and how does it work?

-> Imagine you have a blue-tooth keyboard but instead of the keyboard it’s a laptop and instead of blue-tooth it’s WIFI (ipv4).

---

### So how does this work?

- Python stars a local server *using flask (library)* 
  - Port : 8000 (configurable)
  - ip : Local host ip (eg: 192.168.1.4)
- Listens for key strokes  *(through the browser interface)*
- Performs the keystrokes in the Laptop that is running this program 



>  Basically this transforms mobile/desktop to a virtual keyboard and runs on local-host

> Use full scenario:
>
> > While Playing a music in laptop (Play/Pause) (Skip) (Volume up/down) 
>
> > While Watching Movie 
>
> > It’s basically a keyboard 



To Do:

- Make it **super** responsive (remove the lag and need to refresh webpage *change from GET to POST*)
- Add multimedia Player interface
- *Turn in into a game pad controller so people can control games using phone *
- Package the application (so it’s easy for noobs to install? nah.)

*[My website](https://aayush.wtf)*

Feel free to raise an issue, submit feature request.
