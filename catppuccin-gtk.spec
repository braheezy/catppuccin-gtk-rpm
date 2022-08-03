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
Source18:       gnome-shell-theme.gresource.xml
BuildArch:      noarch
BuildRequires:  sassc

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

%files
/usr/share/themes/Catppuccin-Latte-*
/usr/share/themes/Catppuccin-Mocha-*

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

%changelog
* Wed Aug 3 2022 braheezy <https://github.com/braheezy/>
- Update for new Latte and Mocha flavors
* Sat Apr 16 2022 braheezy <https://github.com/braheezy/>
- Add build for RPM including all colors
* Sat Apr 16 2022 braheezy <https://github.com/braheezy/>
- Initial specfile
