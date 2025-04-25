# ICON-MAKER

Small Python script that generates multi-resolution icon files for macOS and Windows, based on a single source image.

# Requirements

Easiest to run by installing [UV](https://docs.astral.sh/uv/#installation)

# Usage

```shell
uv run ./make-icons.py -i path/to/source.png -o out/folder --name my-icon
```

This will generate two files, `my-icon.ico` and `my-icon.icns` in the `out/folder` directory. The directory will be created if it does not exist.

If any of the destination files exist, they will be overwritten.
