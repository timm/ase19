Module src.thing
================
Keep knowledge about Num or Sym columns.

Functions
---------

    
`r(...)`
:   random() -> x in the interval [0, 1).

Classes
-------

`Num(i, inits=[], pos=0, txt='', w=1, key=<function same at 0x10e05b840>)`
:   Track numbers seen in a column

    ### Ancestors (in MRO)

    * src.thing.Thing
    * boot.Pretty

    ### Methods

    `add(i, x)`
    :

    `sd(i)`
    :

    `sub(i, x)`
    :

    `variety(i)`
    :

`Sym(i, inits=[], pos=0, txt='', w=1, key=<function same at 0x10e05b840>)`
:   Abstract class for Nums and Syms

    ### Ancestors (in MRO)

    * src.thing.Thing
    * boot.Pretty

    ### Methods

    `add(i, x)`
    :

    `ent(i)`
    :

    `sub(i, x)`
    :

    `variety(i)`
    :

`Thing(*args, **kwargs)`
:   Abstract class for Nums and Syms

    ### Ancestors (in MRO)

    * boot.Pretty

    ### Descendants

    * src.thing.Num
    * src.thing.Sym

    ### Methods

    `xpect(i, j)`
    :