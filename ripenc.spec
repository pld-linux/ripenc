Summary:	Shell script to automate ripping and encoding of CD's
Summary(pl):	Skrypt shella do automatyzacji zrzucania i przetwarzania kompakt�w
Name:		ripenc
Version:	0.7
Release:	2
Group:		Applications/Sound
License:	GPL
Source0:	http://www.asde.com/~mjparme/%{name}%{version}.tar.gz
Patch0:		%{name}-HOME_ETC.patch
Patch1:		%{name}-defaults.patch
URL:		http://www.asde.com/~mjparme
Requires:	dialog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Bourne shell script that automates the ripping, encoding,
and naming of CD's. It uses cda for CDDB lookups, cdparanoia, cdda2wav
or tosha (a FreeBSD ripper) for ripping, and bladeenc, 8hz-mp3 or
l3enc to encode the wav files.

%description -l pl
To jest skrypt Bourne shella kt�ry automatyzuje zgrywanie,
przetwarzanie i nazywanie kompakt�w. U�ywa cda do wyszukiwania w bazie
CDDB, cdparanoi, cdda2wav lub tosha (pod FreeBSD) do zrzucania
zawarto�ci, oraz bladeenca, 8hz-mp3 lub l3enca do kodowania plik�w wav
do postaci mp3.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ripenc $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README Changelog KNOWN_BUGS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ripenc
%doc *.gz