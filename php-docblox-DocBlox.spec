# TODO
# - system jquery, jquery-ui
# - graphviz is optional, adjust code to be so
%define		status		beta
%define		pearname	DocBlox
%define		php_min_version  5.2.1
Summary:	%{pearname} - PHP 5.3 compatible API Documentation generator aimed at projects of all sizes and Continuous Integration
Name:		php-docblox-DocBlox
Version:	0.10.0
Release:	0.3
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.docblox-project.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	ce67ba9e42a66bec3df8225968ddd19a
Patch0:		paths.patch
URL:		http://pear.docblox-project.org/package/DocBlox/
BuildRequires:	php-channel(pear.docblox-project.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
#Requires:	ZendFramework >= 1.11.3
Requires:	ZendFramework-Zend_Loader
Requires:	ZendFramework-Zend_Log
Requires:	php-channel(pear.docblox-project.org)
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pear
Requires:	php-pear-Image_GraphViz >= 1.3.0
Requires:	php-pear-PEAR-core >= 1:1.4.0
#Requires:	php-pear.michelf.com-MarkdownExtra >= 1.2.4
Requires:	php-xsl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	 pear(markdown.php)

%description
DocBlox is a Documentation Generation Application (DGA) for use with
PHP applications.

It is capable of transforming the comments in your source code into a
full API reference document.

DocBlox is built to be PHP 5.3 compatible, fast, having a low memory
consumption and easily integratable into Continuous Integration.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# pear packaging a bit messed up, 'src' and 'data' dirs ing wrong place
mv .%{php_pear_dir}/DocBlox .
mv .%{php_pear_dir}/data/DocBlox/* .

mv DocBlox/src/DocBlox .%{php_pear_dir}
mv DocBlox/data/* .%{php_pear_dir}/data/DocBlox

mv DocBlox/LICENSE .
mv DocBlox/README .
mv DocBlox/docs/CHANGELOG .
mv DocBlox/docs/TODO .

# ELF binary blobs?!
rm -rf DocBlox/src/wkhtmltopdf

%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc LICENSE README CHANGELOG TODO
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/docblox
%{php_pear_dir}/DocBlox
%{php_pear_dir}/data/DocBlox
