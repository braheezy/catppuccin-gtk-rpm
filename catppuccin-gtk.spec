%global debug_package %{nil}
%global url https://github.com/catppuccin/gtk
%global SUMMARY Catppuccin theme inspired by the Colloid theme made by Vinceliuice
# Per upstream docs, these packages are required
%global REQUIRES gtk-murrine-engine, gtk3 >= 3.20, gnome-themes-extra, glib2-devel

Name:           %{_name}
Version:        %{_version}
Release:        %{_release}%{?dist}
Summary:        %{SUMMARY}

# Upstream uses GPL-3 :(
License:        GPL-3.0
URL:            %{url}
Source0:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Green.zip
Source1:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Grey.zip
Source2:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Lavender.zip
Source3:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Mauve.zip
Source4:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Peach.zip
Source5:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Pink.zip
Source6:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Red.zip
Source7:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Teal.zip
Source8:        %{url}/releases/download/%{_gittag}/Catppuccin-Latte-Yellow.zip
Source9:        %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Green.zip
Source10:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Grey.zip
Source11:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Lavender.zip
Source12:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Mauve.zip
Source13:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Peach.zip
Source14:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Pink.zip
Source15:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Red.zip
Source16:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Teal.zip
Source17:       %{url}/releases/download/%{_gittag}/Catppuccin-Mocha-Yellow.zip
Source18:        %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Green.zip
Source19:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Grey.zip
# Source11:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Lavender.zip
Source20:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Mauve.zip
# Source13:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Peach.zip
Source21:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Pink.zip
Source22:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Red.zip
Source23:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Teal.zip
Source24:       %{url}/releases/download/%{_gittag}/Catppuccin-Macchiato-Yellow.zip
Source25:        %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Green.zip
Source26:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Grey.zip
# Source20:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Lavender.zip
# Source27:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Mauve.zip
# Source22:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Peach.zip
Source27:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Pink.zip
Source28:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Red.zip
Source29:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Teal.zip
Source30:       %{url}/releases/download/%{_gittag}/Catppuccin-Frappe-Yellow.zip
Source31:       gnome-shell-theme.gresource.xml
BuildArch:      noarch

%description
Apply the Catppuccin palette to your GTK-based desktop.

%package Latte
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte
Catppuccin Latte GTK theme

%package Latte-Green
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Green
Catppuccin Latte-Green GTK theme

%package Latte-Grey
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Grey
Catppuccin Latte-Grey GTK theme

%package Latte-Lavender
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Lavender
Catppuccin Latte-Lavender GTK theme

%package Latte-Mauve
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Mauve
Catppuccin Latte-Mauve GTK theme

%package Latte-Peach
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Peach
Catppuccin Latte-Peach GTK theme

%package Latte-Pink
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Pink
Catppuccin Latte-Pink GTK theme

%package Latte-Red
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Red
Catppuccin Latte-Red GTK theme

%package Latte-Teal
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Teal
Catppuccin Latte-Teal GTK theme

%package Latte-Yellow
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Latte-Yellow
Catppuccin Latte-Yellow GTK theme

%package Mocha
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha
Catppuccin Mocha GTK theme

%package Mocha-Green
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Green
Catppuccin Mocha-Green GTK theme

%package Mocha-Grey
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Grey
Catppuccin Mocha-Grey GTK theme

%package Mocha-Lavender
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Lavender
Catppuccin Mocha-Lavender GTK theme

%package Mocha-Mauve
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Mauve
Catppuccin Mocha-Mauve GTK theme

%package Mocha-Peach
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Peach
Catppuccin Mocha-Peach GTK theme

%package Mocha-Pink
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Pink
Catppuccin Mocha-Pink GTK theme

%package Mocha-Red
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Red
Catppuccin Mocha-Red GTK theme

%package Mocha-Teal
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Teal
Catppuccin Mocha-Teal GTK theme

%package Mocha-Yellow
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Mocha-Yellow
Catppuccin Mocha-Yellow GTK theme

%package Macchiato
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato
Catppuccin Macchiato GTK theme

%package Macchiato-Green
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Green
Catppuccin Macchiato-Green GTK theme

%package Macchiato-Grey
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Grey
Catppuccin Macchiato-Grey GTK theme

# %package Macchiato-Lavender
# Summary:        %{SUMMARY}
# Requires:       %{REQUIRES}
# %description Macchiato-Lavender
# Catppuccin Macchiato-Lavender GTK theme

%package Macchiato-Mauve
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Mauve
Catppuccin Macchiato-Mauve GTK theme

# %package Macchiato-Peach
# Summary:        %{SUMMARY}
# Requires:       %{REQUIRES}
# %description Macchiato-Peach
# Catppuccin Macchiato-Peach GTK theme

%package Macchiato-Pink
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Pink
Catppuccin Macchiato-Pink GTK theme

%package Macchiato-Red
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Red
Catppuccin Macchiato-Red GTK theme

%package Macchiato-Teal
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Teal
Catppuccin Macchiato-Teal GTK theme

%package Macchiato-Yellow
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Macchiato-Yellow
Catppuccin Macchiato-Yellow GTK theme

%package Frappe
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe
Catppuccin Frappe GTK theme

%package Frappe-Green
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe-Green
Catppuccin Frappe-Green GTK theme

%package Frappe-Grey
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe-Grey
Catppuccin Frappe-Grey GTK theme

# %package Frappe-Lavender
# Summary:        %{SUMMARY}
# Requires:       %{REQUIRES}
# %description Frappe-Lavender
# Catppuccin Frappe-Lavender GTK theme

# %package Frappe-Mauve
# Summary:        %{SUMMARY}
# Requires:       %{REQUIRES}
# %description Frappe-Mauve
# Catppuccin Frappe-Mauve GTK theme

# %package Frappe-Peach
# Summary:        %{SUMMARY}
# Requires:       %{REQUIRES}
# %description Frappe-Peach
# Catppuccin Frappe-Peach GTK theme

%package Frappe-Pink
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe-Pink
Catppuccin Frappe-Pink GTK theme

%package Frappe-Red
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe-Red
Catppuccin Frappe-Red GTK theme

%package Frappe-Teal
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe-Teal
Catppuccin Frappe-Teal GTK theme

%package Frappe-Yellow
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description Frappe-Yellow
Catppuccin Frappe-Yellow GTK theme

%prep
# (Ab)use the %setup macro and unzip all the sources cleanly.
%setup -q -c -n %{_name}-Latte-Green
%setup -T -D -a 1 -q -c -n %{_name}-Latte-Grey
%setup -T -D -a 2 -q -c -n %{_name}-Latte-Lavender
%setup -T -D -a 3 -q -c -n %{_name}-Latte-Mauve
%setup -T -D -a 4 -q -c -n %{_name}-Latte-Peach
%setup -T -D -a 5 -q -c -n %{_name}-Latte-Pink
%setup -T -D -a 6 -q -c -n %{_name}-Latte-Red
%setup -T -D -a 7 -q -c -n %{_name}-Latte-Teal
%setup -T -D -a 8 -q -c -n %{_name}-Latte-Yellow
%setup -T -D -a 9 -q -c -n %{_name}-Mocha-Green
%setup -T -D -a 10 -q -c -n %{_name}-Mocha-Grey
%setup -T -D -a 11 -q -c -n %{_name}-Mocha-Lavender
%setup -T -D -a 12 -q -c -n %{_name}-Mocha-Mauve
%setup -T -D -a 13 -q -c -n %{_name}-Mocha-Peach
%setup -T -D -a 14 -q -c -n %{_name}-Mocha-Pink
%setup -T -D -a 15 -q -c -n %{_name}-Mocha-Red
%setup -T -D -a 16 -q -c -n %{_name}-Mocha-Teal
%setup -T -D -a 17 -q -c -n %{_name}-Mocha-Yellow
%setup -T -D -a 18 -q -c -n %{_name}-Macchiato-Green
%setup -T -D -a 19 -q -c -n %{_name}-Macchiato-Grey
# %setup -T -D -a 11 -q -c -n %{_name}-Macchiato-Lavender
%setup -T -D -a 20 -q -c -n %{_name}-Macchiato-Mauve
# %setup -T -D -a 13 -q -c -n %{_name}-Macchiato-Peach
%setup -T -D -a 21 -q -c -n %{_name}-Macchiato-Pink
%setup -T -D -a 22 -q -c -n %{_name}-Macchiato-Red
%setup -T -D -a 23 -q -c -n %{_name}-Macchiato-Teal
%setup -T -D -a 24 -q -c -n %{_name}-Macchiato-Yellow
%setup -T -D -a 25 -q -c -n %{_name}-Frappe-Green
%setup -T -D -a 26 -q -c -n %{_name}-Frappe-Grey
# %setup -T -D -a 11 -q -c -n %{_name}-Frappe-Lavender
# %setup -T -D -a 27 -q -c -n %{_name}-Frappe-Mauve
# %setup -T -D -a 13 -q -c -n %{_name}-Frappe-Peach
%setup -T -D -a 27 -q -c -n %{_name}-Frappe-Pink
%setup -T -D -a 28 -q -c -n %{_name}-Frappe-Red
%setup -T -D -a 29 -q -c -n %{_name}-Frappe-Teal
%setup -T -D -a 30 -q -c -n %{_name}-Frappe-Yellow

%build
# no build required

%install
INSTALL_DIR=%{buildroot}%{_datadir}/themes

install --mode 755 --directory $INSTALL_DIR
# Install each color
cp -fr %{_builddir}/%{_name}-Latte-Green/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Grey/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Lavender/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Mauve/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Peach/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Pink/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Red/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Teal/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Latte-Yellow/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Green/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Grey/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Lavender/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Mauve/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Peach/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Pink/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Red/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Teal/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Mocha-Yellow/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Green/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Grey/* $INSTALL_DIR
# cp -fr %{_builddir}/%{_name}-Macchiato-Lavender/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Mauve/* $INSTALL_DIR
# cp -fr %{_builddir}/%{_name}-Macchiato-Peach/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Pink/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Red/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Teal/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Macchiato-Yellow/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Frappe-Green/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Frappe-Grey/* $INSTALL_DIR
# cp -fr %{_builddir}/%{_name}-Frappe-Lavender/* $INSTALL_DIR
# cp -fr %{_builddir}/%{_name}-Frappe-Mauve/* $INSTALL_DIR
# cp -fr %{_builddir}/%{_name}-Frappe-Peach/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Frappe-Pink/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Frappe-Red/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Frappe-Teal/* $INSTALL_DIR
cp -fr %{_builddir}/%{_name}-Frappe-Yellow/* $INSTALL_DIR

# Install file that allows theme to apply to GDM
# TODO: Obtain the source directly with %{_sourcedir} is too hacky
GDM_THEME_FILE=%{_sourcedir}/gnome-shell-theme.gresource.xml

cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Green/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Grey/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Lavender/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Mauve/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Peach/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Pink/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Red/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Teal/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Latte-Yellow/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Green/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Grey/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Lavender/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Mauve/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Peach/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Pink/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Red/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Teal/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Mocha-Yellow/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Green/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Grey/gnome-shell/
# cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Lavender/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Mauve/gnome-shell/
# cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Peach/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Pink/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Red/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Teal/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Macchiato-Yellow/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Green/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Grey/gnome-shell/
# cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Lavender/gnome-shell/
# cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Mauve/gnome-shell/
# cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Peach/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Pink/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Red/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Teal/gnome-shell/
cp $GDM_THEME_FILE $INSTALL_DIR/Catppuccin-Frappe-Yellow/gnome-shell/

%files
/usr/share/themes/Catppuccin-Latte-*
/usr/share/themes/Catppuccin-Mocha-*
/usr/share/themes/Catppuccin-Macchiato-*
/usr/share/themes/Catppuccin-Frappe-*

%files Latte
/usr/share/themes/Catppuccin-Latte-*

%files Latte-Grey
/usr/share/themes/Catppuccin-Latte-Grey*

%files Latte-Lavender
/usr/share/themes/Catppuccin-Latte-Lavender*

%files Latte-Mauve
/usr/share/themes/Catppuccin-Latte-Mauve*

%files Latte-Peach
/usr/share/themes/Catppuccin-Latte-Peach*

%files Latte-Red
/usr/share/themes/Catppuccin-Latte-Red*

%files Latte-Pink
/usr/share/themes/Catppuccin-Latte-Pink*

%files Latte-Teal
/usr/share/themes/Catppuccin-Latte-Teal*

%files Latte-Yellow
/usr/share/themes/Catppuccin-Latte-Yellow*

%files Mocha
/usr/share/themes/Catppuccin-Mocha-*

%files Mocha-Green
/usr/share/themes/Catppuccin-Mocha-Green*

%files Mocha-Lavender
/usr/share/themes/Catppuccin-Mocha-Lavender*

%files Mocha-Grey
/usr/share/themes/Catppuccin-Mocha-Grey*

%files Mocha-Mauve
/usr/share/themes/Catppuccin-Mocha-Mauve*

%files Mocha-Peach
/usr/share/themes/Catppuccin-Mocha-Peach*

%files Mocha-Pink
/usr/share/themes/Catppuccin-Mocha-Pink*

%files Mocha-Red
/usr/share/themes/Catppuccin-Mocha-Red*

%files Mocha-Teal
/usr/share/themes/Catppuccin-Mocha-Teal*

%files Mocha-Yellow
/usr/share/themes/Catppuccin-Mocha-Yellow*

%files Macchiato
/usr/share/themes/Catppuccin-Macchiato-*

%files Macchiato-Green
/usr/share/themes/Catppuccin-Macchiato-Green*

# %files Macchiato-Lavender
# /usr/share/themes/Catppuccin-Macchiato-Lavender*

%files Macchiato-Grey
/usr/share/themes/Catppuccin-Macchiato-Grey*

%files Macchiato-Mauve
/usr/share/themes/Catppuccin-Macchiato-Mauve*

# %files Macchiato-Peach
# /usr/share/themes/Catppuccin-Macchiato-Peach*

%files Macchiato-Pink
/usr/share/themes/Catppuccin-Macchiato-Pink*

%files Macchiato-Red
/usr/share/themes/Catppuccin-Macchiato-Red*

%files Macchiato-Teal
/usr/share/themes/Catppuccin-Macchiato-Teal*

%files Macchiato-Yellow
/usr/share/themes/Catppuccin-Macchiato-Yellow*

%files Frappe
/usr/share/themes/Catppuccin-Frappe-*

%files Frappe-Green
/usr/share/themes/Catppuccin-Frappe-Green*

# %files Frappe-Lavender
# /usr/share/themes/Catppuccin-Frappe-Lavender*

%files Frappe-Grey
/usr/share/themes/Catppuccin-Frappe-Grey*

# %files Frappe-Mauve
# /usr/share/themes/Catppuccin-Frappe-Mauve*

# %files Frappe-Peach
# /usr/share/themes/Catppuccin-Frappe-Peach*

%files Frappe-Pink
/usr/share/themes/Catppuccin-Frappe-Pink*

%files Frappe-Red
/usr/share/themes/Catppuccin-Frappe-Red*

%files Frappe-Teal
/usr/share/themes/Catppuccin-Frappe-Teal*

%files Frappe-Yellow
/usr/share/themes/Catppuccin-Frappe-Yellow*

%changelog
* Thu Aug 11 2022 braheezy <https://github.com/braheezy/>
- Update for new Frappe and Macchiato flavors
* Wed Aug 3 2022 braheezy <https://github.com/braheezy/>
- Update for new Latte and Mocha flavors
* Sat Apr 16 2022 braheezy <https://github.com/braheezy/>
- Add build for RPM including all colors
* Sat Apr 16 2022 braheezy <https://github.com/braheezy/>
- Initial specfile
