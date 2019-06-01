# anyselector

Make selector easier.

Use to replace `methodcaller`, `itemgetter`, `attrgetter` from `operator`.

## Usage

``` py
from anyselector import attr, item, const, arg, kwarg

attr('a') # like attrgetter('a')
item('k') # like itemgetter('k')
arg(0)(1, 2, 3) == 1 # use arg() select from args.
kwarg('a')(a=2) == 2 # use kwarg() select from kwargs.

# Then select:
selector = attr('a').attr('b').attr('c')
assert selector(obj) == obj.a.b.c

# Deep select:
selector = attr(arg(1))
assert selector(obj, 'a') == obj.a
```
