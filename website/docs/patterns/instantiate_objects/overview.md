---
id: overview
title: Instantiating objects with Hydra
sidebar_label: Overview
---
[![Example applications](https://img.shields.io/badge/-Example%20applications-informational)](https://github.com/facebookresearch/hydra/tree/master/examples/instantiate)

One of the best ways to drive different behavior in an application is to instantiate different implementations of an interface.
The code using the instantiated object only knows the interface which remains constant, but the behavior
is determined by the actual object instance.

Hydra provides `hydra.utils.instantiate()` (and its alias `hydra.utils.call()`) for instantiating objects and calling functions. Prefer `instantiate` for creating objects and `call` for invoking functions.

Call/instantiate supports:
- Constructing an object by calling the `__init__` method
- Calling functions, static functions, class methods and other callable global objects

```python
def instantiate(config: Any, *args: Any, **kwargs: Any) -> Any:
    """
    :param config: An config object describing what to call and what params to use.
                   In addition to the parameters, the config must contain:
                   _target_ : target class or callable name (str)
                   _recursive_: Construct nested objects as well (bool).
                                True by default.
                                may be overridden via a _recursive_ key in
                                the kwargs
    :param args: Optional positional parameters pass-through
    :param kwargs: Optional named parameters to override 
                   parameters in the config object. Parameters not present
                   in the config objects are being passed as is to the target.
    :return: if _target_ is a class name: the instantiated object
             if _target_ is a callable: the return value of the call
    """
    ...

# Alias for instantiate
call = instantiate
```

The config passed to these functions must have a key called `_target_`, with the value of a fully qualified class name, class method, static method or callable.   
Any additional parameters are passed as keyword arguments to tha target.

### Simple usage

Your application may have a User class that looks like this:
```python title="user.py"
class User:
  name: str
  code : int
  
  def __init__(self, name: str, code: int):
    self.name = name
    self.code = code
```

<div className="row">

<div className="col col--6">

```yaml title="Config"
bond:
  _target_: user.User
  name: Bond
  code: 7






```


</div>

<div className="col col--6">

```python title="Instantiation"
user : User = instantiate(cfg.bond)
# User(name="Bond", code=7)

# Overriding the config on the callsite
user : User = instantiate(cfg.bond,
                          name="Batman")
# User(name="Batman", code=7)

# None config -> None result
assert instantiate(None) is None
```

</div>
</div>


### Recursive instantiation
Sometime it's useful to instantiate nested objects. Your app may have a class for a group of users:
```python title="group.py"
class Group:
  name: str
  users: List[User]

  def __init__(self, name: str, users: List[User]):
    self.name = name
    self.users = users
```


<div className="row">

<div className="col col--6">

```yaml title="Config"
group:
  _target_: group.Group
  name: Super heroes
  users:
    - _target_: user.User
      name: Batman
      code: 100
    - _target_: user.User
      name: Wolverine
      code: 666


```

</div>

<div className="col col--6">

```python title="Instantiation"
group: Group = instantiate(cfg.group)
# Group(
#   name="Super heroes",
#   users=[
#     User(name="Batman", code=100),
#     User(name="Wolverine", code=666)
#  ]
# )




```

</div>
</div>