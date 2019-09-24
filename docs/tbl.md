Module src.tbl
==============
Manage a list of rows, keep column statitics in Nums or Syms

Functions
---------

    
`cells(src)`
:   convert strings into their right types

    
`cols(src)`
:   skip columns whose name contains '?'

    
`prep(x)`
:   return a function that can compile things of type 'x'

    
`r(...)`
:   random() -> x in the interval [0, 1).

    
`rows(src)`
:   convert lines into lists, killing whitespace
    and comments. skip over lines of the wrong size

Classes
-------

`Tbl(i, cols=None)`
:   An object that updates column statistics when a row is added.

    ### Ancestors (in MRO)

    * boot.Pretty

    ### Methods

    `clone(i)`
    :   Create an empty table of the same form as self.

    `read(i, src)`
    :   Fo all rows in src, fill in the table.