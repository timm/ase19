Module src.boot
===============
Baseline utilities: must be loaded before anything else.

Classes
-------

`Pretty(*args, **kwargs)`
:   A class that pretty prins itself, attributes sorted alphabetically,
    ignoring 'private' attributes (those starting with '_').

    ### Descendants

    * src.boot.o

`o(i, **d)`
:   Class for names attributes
    
    Fast specification of attributes and their defaults.

    ### Ancestors (in MRO)

    * src.boot.Pretty

    ### Methods

    `cloner(i)`
    :   Return something that can make new things of this type.

    `d(i)`
    :   Convenience method, shortcut access to internal dictionary.