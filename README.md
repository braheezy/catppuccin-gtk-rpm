# Catppuccin GTK RPM
RPM build of the great theme produced by https://github.com/catppuccin/gtk.

Installing the RPM puts the theme in `/usr/share/themes/`.

- catppuccin-gtk (All the colors!)
- catppuccin-gtk-blue
- catppuccin-gtk-green
- catppuccin-gtk-orange
- catppuccin-gtk-pink
- catppuccin-gtk-purple
- catppuccin-gtk-red
- catppuccin-gtk-teal
- catppuccin-gtk-yellow

# Build
Install the RPM build tools for your distro:
- `rpm-build`
- `rpmdevtools`

The themes have dependencies themselves. Install it for your distro:
- `sassc`

Now issue the build command:

    make rpm

# Usage
After installing an RPM, start using the theme. This has only been tested on GNOME 41 so YMMV:
1. Install the tools that allow you to customize the theme:

        yum install gnome-tweaks gnome-extensions-app gnome-shell-extension-user-theme

2. Log out/back in. TBD why this is needed, but it updates the GNOME Extensions app to see the `user-theme` extension just installed.
3. Open GNOME Extensions app and toggle the button to allow **User Themes**.
4. Open GNOME Tweaks app and under the **Appearance** tab, update the **Applications** Theme and **Shell** Theme to the one you just installed.
5. Enjoy Catppuccin GTK :)