%global debug_package %{nil}
%global url https://github.com/catppuccin/gtk
%global SUMMARY Catppuccin theme inspired by the Colloid theme made by Vinceliuice
# Per upstream docs, these packages are required
%global REQUIRES gtk-murrine-engine, gtk3 >= 3.20, gnome-themes-extra

Name:           %{_name}
Version:        %{_version}
Release:        %{_release}%{?dist}
Summary:        %{SUMMARY}

License:        GPL-3.0
URL:            %{url}
Source0:        %{url}/releases/download/%{_gittag}/Catppuccin-blue.zip
Source1:        %{url}/releases/download/%{_gittag}/Catppuccin-green.zip
Source2:        %{url}/releases/download/%{_gittag}/Catppuccin-orange.zip
Source3:        %{url}/releases/download/%{_gittag}/Catppuccin-pink.zip
Source4:        %{url}/releases/download/%{_gittag}/Catppuccin-purple.zip
Source5:        %{url}/releases/download/%{_gittag}/Catppuccin-red.zip
Source6:        %{url}/releases/download/%{_gittag}/Catppuccin-teal.zip
Source7:        %{url}/releases/download/%{_gittag}/Catppuccin-yellow.zip
BuildArch:      noarch
BuildRequires:  sassc

%description
Apply the Catppuccin palette to your GTK-based desktop.

%package blue
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description blue
Catppuccin Blue GTK theme

%package green
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description green
Catppuccin Green GTK theme

%package orange
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description orange
Catppuccin Orange GTK theme

%package pink
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description pink
Catppuccin Pink GTK theme

%package purple
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description purple
Catppuccin Purple GTK theme

%package red
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description red
Catppuccin Red GTK theme

%package teal
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description teal
Catppuccin Teal GTK theme

%package yellow
Summary:        %{SUMMARY}
Requires:       %{REQUIRES}
%description yellow
Catppuccin Yellow GTK theme

%prep
# Abuse the %setup macro and unzip all the sources cleanly.
%setup -q -c -n %{_name}-blue
%setup -T -D -a 1 -q -c -n %{_name}-green
%setup -T -D -a 2 -q -c -n %{_name}-orange
%setup -T -D -a 3 -q -c -n %{_name}-pink
%setup -T -D -a 4 -q -c -n %{_name}-purple
%setup -T -D -a 5 -q -c -n %{_name}-red
%setup -T -D -a 6 -q -c -n %{_name}-teal
%setup -T -D -a 7 -q -c -n %{_name}-yellow

%build
# no build required

%install
INSTALL_DIR=%{buildroot}%{_datadir}/themes/

install --mode 755 --directory $INSTALL_DIR
# Install each color
cp -r %{_builddir}/%{_name}-blue/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-green/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-orange/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-pink/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-purple/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-red/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-teal/* $INSTALL_DIR
cp -r %{_builddir}/%{_name}-yellow/* $INSTALL_DIR

%files blue
/usr/share/themes/Catppuccin-blue*

%files green
/usr/share/themes/Catppuccin-green*

%files orange
/usr/share/themes/Catppuccin-orange*

%files pink
/usr/share/themes/Catppuccin-pink*

%files purple
/usr/share/themes/Catppuccin-purple*

%files red
/usr/share/themes/Catppuccin-red*

%files teal
/usr/share/themes/Catppuccin-teal*

%files yellow
/usr/share/themes/Catppuccin-yellow*

%changelog
* Sat Apr 16 2022 braheezy <https://github.com/mbraha/>
- Initial specfile
