# Example of Single Script

This is simple example of how to write a single script that lives in the "root" directory of your project.

The goal was to write something that was as simple as possible.

## Building

To create the virtualenv necessary to build the python wheel:

`make dev`


## Testing

One can install a build wheel file into a local directory to verify that the wheel actually works
with `pip install`

`make test-install`

