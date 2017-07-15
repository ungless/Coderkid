There are several key bindings in i3. Actually, there are `infinite` key bindings in i3.

To define a keybinding in our `config` file:

```
bindsym <key> <action>
```

Say we want to launch Chrome with `$mod and c`, we will use the `exec` keyword.

```
bindsym $mod+c exec google-chrome
```