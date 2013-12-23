%define		_state		stable
%define		orgname		juk
%define		qtver		4.8.1

Summary:	A jukebox like program
Summary(pl.UTF-8):	Program spełniający funkcję szafy grającej
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	a5796a638ca9f7113bd92c78cd0e5cf2
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	taglib-devel >= 1.5
Requires:	kde4-kdebase >= %{version}
Requires:	taglib >= 1.5
Obsoletes:	kde4-kdemultimedia-juk < 4.8.99-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(R) or RealOne(R). As is typical with many jukebox applications,
JuK allows you to edit the "tags" of the audio files, and manage your
collection and playlists.

%description -l pl.UTF-8
Juk (czyt. dżuk, jak w Jukebox) to szafa grająca i zarządca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umożliwia modyfikowanie znaczników plików
dźwiękowych i zarządzanie kolekcją oraz playlistami.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang juk		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f juk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/kde4/services/ServiceMenus/jukservicemenu.desktop
%{_desktopdir}/kde4/juk.desktop
%{_iconsdir}/*/*/*/juk*.png
%{_datadir}/dbus-1/interfaces/org.kde.juk.collection.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.player.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.search.xml
