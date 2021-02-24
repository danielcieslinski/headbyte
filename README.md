# 𐂀 Headbyte

<sub> [<span style="background-color: blue">𐂀</span>] In active development </sub> 

Associative personal knowledge manager and modest assistant.

## Introduction
For now, rather than assistants it's collection of some scripts, I use for managing my notes and data.
This repo is cleaned and tied up, version of my private one, which I'd been using for managing (__or rather just grouping__) various scripts, that I created, mostly for managing my thoughts.


### Creating private instance
For now I still keep my data in the old repo, but as I'm moving all the data here, creating [private-fork](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274#file-private_fork-md) 
seem like reasonable solution for generalized case of templating active repo.


## File structure

```
.privdata/
server/
src/
  - module1
  - module2
data/
cli.py
```

1. `cli.py` is top level entry \
∴ `server/` shall not call cli.py and make direct calls to `src/`

2. All the private data, if has to be kept in this directory, should be put in `.privdata/`

---

