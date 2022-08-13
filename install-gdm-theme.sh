# Install requirements
sudo yum install glib2-devel
# Backup current GDM theme
sudo cp -av /usr/share/gnome-shell/gnome-shell-theme.gresource{,~}
# Compile new theme GResource
THEME_NAME="$(gsettings get org.gnome.desktop.interface gtk-theme | sed "s/'//g")"
THEME_SRC_DIR="/usr/share/themes/$THEME_NAME/gnome-shell"
sudo glib-compile-resources --target="/usr/share/gnome-shell/gnome-shell-theme.gresource" --sourcedir="$THEME_SRC_DIR" "$THEME_SRC_DIR/gnome-shell-theme.gresource.xml"
