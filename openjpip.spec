# TODO:
# - opj_viewer (Java-based, requires xerces-j)
# - FCGI configuration for web server
# - library and headers?
%define fver    %(echo %{version} | tr . _)
Summary:	OpenJPIP - implementation of JPEG 2000 Part 9: Interactivity tools, APIs and protocols
Summary(pl.UTF-8):	OpenJPIP - implementacja JPEG 2000 Part 9: narzędzia, API i protokoły interaktywne
Name:		openjpip
Version:	1.0.1
Release:	0.1
License:	BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/openjpeg/downloads/list
Source0:	http://openjpeg.googlecode.com/files/%{name}_v%{fver}.tar.gz
# Source0-md5:	04a651a01341302f66ff987dbba24f4a
Patch0:		%{name}-opt.patch
URL:		http://www.openjpeg.org/
BuildRequires:	fcgi-devel
BuildRequires:	openjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenJPIP software is an implementation of JPEG 2000 Part 9:
Interactivity tools, APIs and protocols (JPIP).

For more info about JPIP, check the website:
<http://www.jpeg.org/jpeg2000/j2kpart9.html>.
The current implementation uses some results from the 2KAN project:
<http://www.2kan.org/>.

First Version 1.0 covers:
 - JPT-stream (Tile based) media types
 - Session, channels, cache model managements
 - JPIP over HTTP
 - Indexing JPEG 2000 files
 - Embedding XML formatted metadata
 - Region Of Interest (ROI) requests

%description -l pl.UTF-8
OpenJPIP to implementacja JPEG 2000 Part 9, czyli narzędzi, API i
protokołów interaktywnych (JPIP).

Więcej informacji o JPIP można znaleźć na stronie:
<http://www.jpeg.org/jpeg2000/j2kpart9.html>.
Obecna implementacja wykorzystuje część pracy projektu 2KAN:
<http://www.2kan.org/>.

Wersja 1.0 pokrywa:
 - strumienie JPT (oparte na kaflach)
 - zarządzanie sesjami, kanałami, pamięcią podręczną
 - JPIP po HTTP
 - indeksowanie plików JPEG 2000
 - osadzanie metadanych w formacie XML
 - żądania ROI (Region Of Interest)

%prep
%setup -q -n %{name}_v1_0
%patch0 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/fastcgi"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install opj_server/opj_server $RPM_BUILD_ROOT%{_bindir}
install opj_client/opj_dec_server/opj_dec_server $RPM_BUILD_ROOT%{_bindir}
install tools/{addXMLinJP2,jpt_to_j2k,jpt_to_jp2} $RPM_BUILD_ROOT%{_bindir}
install tools/indexer/index_create $RPM_BUILD_ROOT%{_bindir}/opj_index_create
# TODO: opj_client/opj_viewer (Java)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/jpip_protocol.png
%attr(755,root,root) %{_bindir}/addXMLinJP2
%attr(755,root,root) %{_bindir}/jpt_to_j2k
%attr(755,root,root) %{_bindir}/jpt_to_jp2
%attr(755,root,root) %{_bindir}/opj_dec_server
%attr(755,root,root) %{_bindir}/opj_index_create
%attr(755,root,root) %{_bindir}/opj_server

# TODO: libs and headers?
