There are several key bindings in i3. Actually, there are `infinite` key bindings in i3.

To define a keybinding in our `config` file:

```language-bash
bindsym <key> <action>
```

Say we want to launch Chrome with `$mod and c`, we will use the `exec` keyword.

```language-bash
bindsym $mod+c exec google-chrome
```