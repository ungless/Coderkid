Functions are quite a general topic in programming. They are a way of expressing bits of code very quickly. 

Functions can be run as `**function_name**()`. 

Nothing goes within the brackets unless the function takes parameters, but we'll get to that later.

```language-python
def greetings():
    greeting = "I love Python!"
    return greeting

print(greetings())
```

There are two things that are key here:

- `return`
- `def`

`return` is what the function will give back when it ends. There is always a return at the end of a function, and if you do not specify it, then Python will insert it for you as `return false`.

`def` is the way that we define functions. It must come before the name of the function.

Also - **don't forget to indent your code!**

#### Functions with parameters

One can also make functions that take parameters. 

They are passed in through the `()` and are **comma-separated**.

```language-python
def add_numbers(a, b):
    return a + b

print(add_numbers(1, 5))
```

```language-bash
$ 6
```

This is an excellent example of using parameters.

The parameters that we name in `add_numbers` are simple variables. The name given to them DOESNT MATTER.