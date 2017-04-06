# Setup

Add `-i repo_path` to the status_command statement in your i3 config.

Example:
```
bar {
    status_command py3status -i ~/src/aalto_outside_i3
}
```

Add a ```order += "aalto_outside_i3"``` statement into your
i3status.conf to enable the module.

The module has a format configuration parameter. It's a standard python
format string and the valid argument names are ```temp```, ```pres```,
```moist``` and ```lum```. All arguments are floating point values and
their units are °C, hPa, RH% and lux, respectively.

Example:
```
aalto_outside_i3 {
    format = '{temp:.2f} °C'
}
```

