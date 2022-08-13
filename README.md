# Catppuccin GTK RPM
RPM build of the great theme produced by https://github.com/catppuccin/gtk.

Installing the RPM puts the theme in `/usr/share/themes/`. Available RPMs can be found in in [Releases](https://github.com/braheezy/prettybox-catppuccin/releases):

- `catppuccin-gtk` (All the flavors and colors!)
- `catppuccin-gtk-Frappe`
- `catppuccin-gtk-Frappe-<specific color>`
- `catppuccin-gtk-Mocha`
- `catppuccin-gtk-Mocha-<specific color>`
- `catppuccin-gtk-Macchiato`
- `catppuccin-gtk-Macchiato-<specific color>`
- `catppuccin-gtk-Latte`
- `catppuccin-gtk-Latte-<specific color>`

# Build
To build the RPMs yourself, you need a Linux distro that uses RPMs.

Run `configure.sh` to install prerequisite build tools.

Then issue the build command:

    make rpm

# Usage
After installing an RPM, start using the theme. This has only been tested on GNOME 41 so YMMV:
1. Install the tools that allow you to customize the theme:

        yum install gnome-tweaks gnome-extensions-app gnome-shell-extension-user-theme

2. Log out/back in. TBD why this is needed, but it updates the GNOME Extensions app to see the `user-theme` extension just installed.
3. Open GNOME Extensions app and toggle the button to allow **User Themes**.
4. Open GNOME Tweaks app and under the **Appearance** tab, update the **Applications** Theme and **Shell** Theme to the one you just installed.
5. Enjoy Catppuccin GTK :)
6. Bonus: Apply the theme to GDM too. The following steps are in `install-gdm-theme.sh` too.
  - Backup current theme file
      ```bash
          sudo cp -av /usr/share/gnome-shell/gnome-shell-theme.gresource{,~}
      ```
  - Compile new theme:
      ```bash
      THEME_NAME="$(gsettings get org.gnome.desktop.interface gtk-theme | sed "s/'//g")"
      THEME_SRC_DIR="/usr/share/themes/$THEME_NAME/gnome-shell"
      sudo glib-compile-resources --target="/usr/share/gnome-shell/gnome-shell-theme.gresource" --sourcedir="$THEME_SRC_DIR" "$THEME_SRC_DIR/gnome-shell-theme.gresource.xml"
      ```
  - Log out/in
7. More bonus: Change the GDM logo
  - Get an icon file that's 256x256 or smaller. Put it in `/usr/share/pixmaps/`. You can use `cat.png` from this project.
  - Create new file for the `gdm` user's dconf settings. Make sure it has this content:

        # /etc/dconf/profile/gdm
        user-db:user
        system-db:gdm
        file-db:/usr/share/gdm/greeter-dconf-defaults
  - Define the keyfile to set the logo:

        # /etc/dconf/db/gdm.d/02-logo
        [org/gnome/login-screen]
        logo='/usr/share/pixmaps/cat.png'
  - Update the dconf database

        sudo dconf update
  - Log out/in
