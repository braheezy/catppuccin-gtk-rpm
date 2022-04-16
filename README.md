# Catppuccin GTK RPM
RPM build of the great content produced by https://github.com/catppuccin/gtk.

For each main color, an RPM is generated containing all the assets. Installing the RPM puts the theme in `/usr/share/themes/`.

This has only been tested on Fedora 35 and will probably only work for modern RPM-based distros like that.

# Build
The following tools are used to produced the RPM. Install them for your distro:
- `rpm-build`
- `rpmdevtools` for `spectool`

The GTK themes depend on the following. Install them for your distro:
- `sassc`

Now issue the build command:

    make rpm

# Usage
1. Install the tools that allow you to customize the theme:

        yum install gnome-tweaks gnome-extensions-app gnome-shell-extension-user-theme

2. Log out/back in. TBD why this is needed, but it updates the GNOME Extensions app to see the extension just installed.
3. Open GNOME Extensions app and toggle the button to allow **User Themes**.
4. Open GNOME Tweaks app and under the **Appearance** tab, update the **Applications** Theme and **Shell** Theme to the one you just installed.
5. Enjoy Catppuccin GTK :)