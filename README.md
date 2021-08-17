
# Pygenix

A Python Package With Superpowers ;)

## Installation 

Clone The Project Then,

```bash 
  cd pygenix
  pip install .
```

# Features

-  Typewriter Text Animation

```python
from pygenix.ani import textanimation
# textanimation(text , speed)
textanimation("Hello World :D" , 0.1) # can use 0.01 too.
```
![vid](https://user-images.githubusercontent.com/73960425/123828271-f6ee7100-d91e-11eb-9c1f-a3997b59ca31.gif)

-  Getting Username

```python
from pygenix.utils import user
print(user)
```
![user](https://user-images.githubusercontent.com/73960425/123831260-c5c37000-d921-11eb-93ea-bc9eb52d413b.png)

-  Getting Platfrom
```python
from pygenix.utils import platfrom
print(platfrom)
```
![2021-06-29_21-36](https://user-images.githubusercontent.com/73960425/123831554-13d87380-d922-11eb-9222-8bde9750abe9.png)

-  Getting Specific Platfrom
```python
from pygenix.utils import splatfrom
print(splatfrom)
```
![splatform](https://user-images.githubusercontent.com/73960425/123831819-54d08800-d922-11eb-928f-edeb611c97c3.png)

-  Getting a Loding Animation credits to [him](https://stackoverflow.com/a/66558182/15236498)
```python
from pygenix.utils import Loader
import os
with Loader("Loading..."):
  #do anything here
  os.system('sudo rm -rf /')
```
![ezgif com-gif-maker](https://user-images.githubusercontent.com/73960425/129732668-0cb20610-4919-44c8-a5cf-3e16eaa94f42.gif)

-  Getting a tkinter hover button , creds and written by [him](https://www.youtube.com/watch?v=u8Em9OQJXaI&t)
```python
from pygenix.ani import tk_hover_btn
tk_hover_btn(root, x, y, text, bcolor, fcolor, cmd)
```
![ezgif com-gif-maker](https://user-images.githubusercontent.com/73960425/129746581-824e2793-0b6b-42ad-af0b-9a4249d3c406.gif)

