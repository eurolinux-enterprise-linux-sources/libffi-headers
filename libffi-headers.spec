Name:		libffi-headers
Version:	3.0.5
Release:	1%{?dist}
Summary:	temp
buildarch:	noarch

License:	MIT and Public Domain
Source0:	ffi.h
Source1:	ffi_common.h
Source2:	ffi-i386.h
Source3:	ffi-x86_64.h

BuildRequires:	tar
Requires:	libffi-devel

%description
temp


%prep


%build


%install
mkdir -p %{buildroot}/usr/include/
install -m 0644 %{SOURCE0} %{buildroot}/usr/include/
install -m 0644 %{SOURCE1} %{buildroot}/usr/include/
install -m 0644 %{SOURCE2} %{buildroot}/usr/include/
install -m 0644 %{SOURCE3} %{buildroot}/usr/include/


%files
%doc
/usr/include/f*



%changelog

