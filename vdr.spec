
%define name	vdr
%define version	1.6.0
%define maintpatch 2
%define oapiversion 1.6.0
%define rel	10

# Increased when ABI compatibility is broken by patches
# Reset to 1 when %oapiversion is raised
%define vdr_sub_abi	4
%define vdr_abi		%{oapiversion}_%{_lib}_abi_%{vdr_sub_abi}
%define apiversion	%{oapiversion}.%{vdr_sub_abi}

# backportability
%define _localstatedir		%{_var}

%define vdr_plugin_dir		%{_libdir}/%{name}
%define vdr_plugin_datadir	%{vdr_datadir}
%define vdr_plugin_cfgdir	%{vdr_cfgdir}/plugins
%define vdr_plugin_paramdir	%{vdr_datadir}/defaults
%define vdr_plugin_cachedir	%{_var}/cache/%{name}
%define vdr_videodir		%{_localstatedir}/lib/%{name}/video
%define vdr_cfgdir		%{_localstatedir}/lib/%{name}/config
%define	vdr_datadir		%{_datadir}/%{name}
%define vdr_chanlogodir		%{vdr_datadir}/chanlogos
%define vdr_themedir		%{_localstatedir}/lib/%{name}/themes
%define vdr_epgimagesdir	%{_var}/cache/%{name}/epgimages

%define vdr_plugin_flags	-fPIC

%if %{maintpatch}
%define fullversion		%{version}-%{maintpatch}
%else
%define fullversion		%{version}
%endif

Summary:	Video Disk Recorder - PVR suite
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.cadsoft.de/vdr/
Source:		ftp://ftp.cadsoft.de/vdr/%{name}-%{version}.tar.bz2

Source1:	vdr.init
Source2:	vdr-runvdr
Source3:	vdr-shutdown.sh.example
Source4:	vdr.sysconfig
Source5:	vdr-sky.cron
Source6:	vdr-sky.sysconfig
Source7:	vdr-README.mdv
Source8:	vdr-plugin-filetriggers.script

# Patches last checked for updates: 2009/07/25

# Drop DVB API version check, it is bumped arbitrarily:
Patch0:		vdr-drop-dvbapi-check.patch
# Configurable logident for multi-vdr systems:
Patch1:		vdr-1.6.0-logident.patch
# Make HasDecoder() return true even while in pmExtern playmode
Patch2:		vdr-1.6.0-hasdecoder.patch
# printf format warnings:
Patch3:		vdr-printf-format.patch
Patch4:		vdr-1.6.0-rsvps.patch
Patch5:		vdr-1.6.0-vdrversion.patch
# CanHandleOver2BitSubtitles() hack:
Patch6:		vdr-1.6.0-dxr3.patch
# Use monospace as default monospace font,
# sans serif as default large font:
Patch7:		vdr-1.6.0-default-fonts-mdv.patch
# Show more font aliases:
Patch8:		vdr-1.6.0-show-more-aliasfonts.patch
# Add options to disable use of device input or output:
Patch9:		vdr-1.6.0-shared-devices.patch
# For streamdev:
Patch10:	vdr-1.6.0-intcamdevices.mod.patch
# warning: cannot pass objects of non-POD type ‘class cString’ through ‘...’; call will abort at runtime
Patch18:	vdr-1.6.0-h264-non-pod-type.patch

# From http://users.tkk.fi/~rahrenbe/vdr/
# and http://www.saunalahti.fi/~rahrenbe/vdr/patches/
# Updated with each version, gunzipped
# Note that they are usually just rediffed, no actual changes
Patch11:	vdr-1.6.0-cap_sys_nice.patch
Patch12:	vdr-1.6.0-liemikuutio-1.27.diff
Patch13:	vdr-1.6.0-cutter-marks.diff
Patch14:	vdr-1.6.0-parentalrating-content.diff
Patch15:	vdr-1.6.0-thread-name.diff
Patch16:	vdr-1.6.0-frontend-facilities.patch
Patch19:	vdr-1.6.0-subtitles-button.patch
Patch31:	vdr-1.6.0-hitk.patch
Patch32:	vdr-1.6.0-ionice.patch

# From iptv
Patch17:	vdr-1.6.0-pluginparam.patch
Patch33:	vdr-1.6.0-plugindev-disable-ca-updates.patch

# From http://e-tobi.net/ Debian repository
Patch20:	vdr-1.4.0-analogtv.patch
Patch21:	vdr-1.6.0-sort-options.patch
Patch22:	vdr-1.6.0-dd-record-option.patch
Patch23:	vdr-1.6.0-yaepg.patch
Patch24:	vdr-1.6.0-menuorg.patch
Patch25:	vdr-1.6.0-pin.patch
Patch26:	vdr-1.6.0-graphtft.patch
Patch27:	vdr-1.6.0-sourcecaps.patch
Patch28:	vdr-1.6.0-noepg.patch
Patch29:	vdr-1.6.0-reelchannelscan.patch
Patch30:	vdr-1.6.0-pvrinput.patch

# From VDR mailinglist
Patch34:	vdr-1.6.0-ConfigurableLNBshare_1_5_10.diff
# fixes build with gcc4.4
Patch35:	vdr-1.7.7-grab.diff
# ditto
Patch36:	vdr-1.6.0-const.diff

# From rotor plugin
Patch40:	vdr-1.5.5-rotor.diff

# From http://toms-cafe.de/vdr/download/
Patch50:	http://toms-cafe.de/vdr/download/vdr-jumpplay-1.0-1.6.0.diff
Patch52:	http://toms-cafe.de/vdr/download/vdr-timer-info-0.5-1.5.15.diff
Patch53:	http://toms-cafe.de/vdr/download/vdr-cmdsubmenu-0.7-1.6.0.diff

# From epgsearch
Patch64:	vdr.epgsearch-exttimeredit-0.0.2.diff
Patch65:	MainMenuHooks-v1_0.patch
Patch66:	timercmd-0.1_1.6.0.diff

# From VDR mailinglist, Reinhard Nissl
Patch67:	vdr-1.5.18-h264-syncearly-framespersec-audioindexer-fielddetection-speedup.diff
Patch68:	vdr-1.5.18-addon-fix_nid_tid_channel_iterator.diff

# From ttxtsubs
Patch70:	vdr-1.6.0-2-ttxtsubs.patch

%if %maintpatch
%(for n in {1..%maintpatch}; do
	echo "Patch7$n: ftp://ftp.cadsoft.de/vdr/Developer/vdr-%version-$n.diff"
done)
%endif

BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libcap-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libncursesw-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype2-devel
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(post):	vdr-common = %{version}
Requires:	vdr-common = %{version}
Provides:	vdr-abi = %{vdr_abi}
Obsoletes:	vdr-plugin-subtitles < 0.5.0-8
Requires(post):	ccp >= 0.4.1
# Plugins:
Requires:	ccp >= 0.4.1
%if %{mdkversion} == 200910
# fixed filetriggers
Requires(post):	rpm >= 1:4.6.0-2.2
%endif

%description
VDR (Video Disk Recorder) is a very powerful and customizable PVR
suite. One of the most common usage cases of VDR is as a digital
set-top-box with the picture displayed on a television set. VDR can
also be used on desktop or even without any video output devices.
There are also lots of different plugins available to extend VDR's
capabilities.

See http://www.linuxtv.org/vdrwiki/ for more information.

VDR in this package is patched with the patches known as
liemikuutio, cutter-marks, parentalrating-content, thread-name,
menuorg, sort-options, dd-record-option, configurableLNBshare,
sourcecaps, jumpplay, timer-info, cmdsubmenu, h264, and with
patches which are required by various plugins.
%if %maintpatch
This build is additionally patched to the maintenance release
%version-%maintpatch.
%endif

%package common
Summary:	Common files for VDR
Group:		Video
Requires(pre):	rpm-helper
Requires(postun): rpm-helper

%description common
VDR (Video Disk Recorder) is a very powerful and customizable PVR
suite.

This package contains the default "vdr" user required by VDR and
some other related tools.

%package devel
Summary:	VDR development headers
Group:		Development/C++
Requires:	gettext

%description devel
This package contains the headers that are needed to build
plugins for VDR.

%package plugin-hello
Summary:	VDR plugin: A friendly greeting
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-hello
This is a small demo of the VDR plugin interface.

%package plugin-osddemo
Summary:	VDR plugin: Demo of arbitrary OSD setup
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-osddemo
Demonstration of how a plugin can have its very own OSD setup.

It's a very primitive game that opens a small window in which the
user can draw lines with the Up, Down, Left and Right buttons.
The color buttons are used to switch color.
Press Ok to close the window.

%package plugin-skincurses
Summary:	VDR plugin: A text only skin
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-skincurses
The 'skincurses' plugin implements a VDR skin that works in a
shell window, using only plain text output. It re-implements
what used to be available by compiling VDR versions before 1.3.7
with the DEBUG_OSD macro set.

%package plugin-sky
Summary:	VDR plugin: Sky Digibox interface
Group:		Video
Requires:	wget
Requires:	vdr-abi = %vdr_abi

%description plugin-sky
The 'sky' plugin implements a new device for VDR, which is based on the
MPEG2 encoder card described at linuxtv.org/mpeg2/kfir.xml. It
allows you to connect the analog a/v output of your Sky Digibox to VDR,
so that you can enjoy the full recording flexibility of VDR with your
Sky subscription. Note that this is NOT something that does anything
illegal, like decrypting the Sky programme without a subscription. You
will need a Sky Digibox and a valid subscription in order to use this
plugin.

%package plugin-status
Summary:	VDR plugin: Status monitor test
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-status
This is an example that shows the use of cStatus.

%package plugin-servicedemo
Summary:	VDR plugin: Service demo
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-servicedemo
Demonstration of how plugins can communicate with each other.

%package plugin-svdrpdemo
Summary:	VDR plugin: How to add SVDRP support to a plugin
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-svdrpdemo
This plugin shows how to add SVDRP support to a plugin.

%package plugin-pictures
Summary:	VDR plugin: A simple picture viewer
Group:		Video
Requires:	vdr-abi = %vdr_abi

%description plugin-pictures
The 'pictures' plugin implements a simple picture viewer.

There is already an 'image' plugin out there which has a lot more
functionality than this one, but it's way too complex for my taste,
and also converts the image files on-the-fly, which makes it slow
on slow hardware.

This plugin assumes that the pictures have already been converted to
MPEG frames (with the 'pic2mpg' script that comes with this archive),
and doesn't implement any fancy features like zooming, panning or
tiled previews. It's just a very simple viewer.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch70 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch65 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch34 -p1
%patch40 -p1
%patch50 -p1
%patch52 -p1
%patch53 -p1
%patch67 -p1
%patch68 -p0
%patch6 -p1
%patch10 -p1
%patch11 -p1
%patch19 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch64 -p1
%patch66 -p1
%patch35 -p0
%patch36 -p1
%patch18 -p1

%if %maintpatch
%(for n in {1..%maintpatch}; do
	echo "%%patch7$n -p1"
done)
%endif

sed -i "/isyslog(\"VDR version %%s started\", VDRVERSION);/s/VDRVERSION/\"%{fullversion} (%{version}-%{release})\"/" vdr.c
sed -ri '/define APIVERSION/s/^(.*")%{oapiversion}(".*)$/\1%{apiversion}\2/' config.h
sed -ri '/define VDRVERSION/s/^(.*")%{fullversion}(".*)$/\1%{version}-%{release}\2/' config.h

# check that the macros are set correctly
[ $(sed -rn '/define APIVERSION/s/^.*"(.*)".*$/\1/p' config.h) == "%apiversion" ]
[ $(sed -rn '/define VDRVERSION/s/^.*"(.*)".*$/\1/p' config.h) == "%version-%release" ]

cp -a %SOURCE3 shutdown.sh.example

cat %SOURCE7 | sed 's,@vdr_plugin_dir@,%{vdr_plugin_dir},' > README.mdv

mkdir i18n-to-gettext
mv i18n-to-gettext.pl i18n-to-gettext/

# Comment default examples out
perl -pi -e "s/^S/# S/" diseqc.conf

cat > README.1.6.0.upgrade.urpmi <<EOF
VDR 1.6 series is a major upgrade and you may need to make configuration
changes to adapt for this new series.
See UPDATE-1.6.0 for a summary of changes.
EOF

cat > Make.config <<EOF
CFLAGS   = %optflags %{?ldflags}
CXXFLAGS = \$(CFLAGS)

BINDIR   = %{_bindir}
MANDIR   = %{_mandir}
LOCDIR   = %{_datadir}/locale

PLUGINLIBDIR = %{vdr_plugin_dir}
VIDEODIR = %{vdr_videodir}
CONFDIR = %{vdr_cfgdir}
LIBDIR = .
EOF

cat > README.install.urpmi <<EOF
VDR is an advanced PVR suite and configuring it may not be easy for the
inexperienced. Please take a look at the provided documentation before
trying to configure it.

Note that VDR does not support output to X11 or framebuffer without
additional plugins, such as xineliboutput or softdevice.

VDR initscript is provided for your convenience. Instead of running vdr
directly, you should use the vdr service.

Mandriva VDR packages have the following filesystem layout:

%{_sysconfdir}/sysconfig/vdr
Mandriva VDR configuration file; the settings in this file are used to
construct the VDR parameters.

%{_sysconfdir}/sysconfig/vdr-PLUGINNAME
Mandriva VDR plugin configuration files; the settings in these files are used
to construct the parameters for VDR plugins.

%vdr_videodir
Default VDR recordings directory.

%vdr_cfgdir
Default VDR configuration directory.

%vdr_chanlogodir
Default channel logo directory; The channel logos are used by plugins that
support them. The most compatible format is 64x48px 16-color xpm.

For more information on VDR and its plugins, see http://linuxtv.org/vdrwiki/ .
EOF

## TODO: move this out of .spec
cat > vdr.macros <<EOF
## VDR plugin macros ##

%%vdr_version		%{version}-%{release}
%%vdr_rpmversion	%version
%%vdr_apiversion	%apiversion
%%vdr_abi		%vdr_abi

%%vdr_plugin_flags	%%{optflags} %vdr_plugin_flags %%{vdr_plugin_ldflags} \${VDR_PLUGIN_EXTRA_FLAGS}
%%vdr_plugin_ldflags	%%(echo "%%{?ldflags}" | sed 's@-Wl,--no-undefined@@')

%%_vdr_plugin_dir	%{vdr_plugin_dir}
%%_vdr_plugin_datadir	%{vdr_plugin_datadir}
%%_vdr_plugin_cfgdir	%{vdr_plugin_cfgdir}
%%_vdr_plugin_paramdir	%{vdr_plugin_paramdir}
%%_vdr_plugin_cachedir	%{vdr_plugin_cachedir}
%%_vdr_videodir		%{vdr_videodir}
%%_vdr_cfgdir		%{vdr_cfgdir}
%%_vdr_chanlogodir	%{vdr_chanlogodir}
%%_vdr_themedir		%{vdr_themedir}
%%_vdr_epgimagesdir	%{vdr_epgimagesdir}

%%vdr_plugin_prep \\
for file in po/*.po; do \\
	# drop empty translations \\
	grep -Eq 'msgstr ".+"' \$file || rm -f \$file \\
done \\
set +x \\
echo Silent renaming of locales \\
for file in po/*_*.po; do \\
	[ -f \$file ] || continue \\
	[ \$(basename \$file .po) == "zh_CN" ] && continue \\
	# VDR wrongly uses the _COUNTRY identification always \\
	rm -rf \${file%_*.po}.po \\
	mv \$file \${file%_*.po}.po \\
done \\
set -x \\
touch vdr_plugin_prep.done

%%vdr_plugin_build \\
    %%make all							\\\\\\
    CFLAGS="%%{vdr_plugin_flags}"				\\\\\\
    CXXFLAGS="%%{vdr_plugin_flags}"				\\\\\\
    LDFLAGS="%%{vdr_plugin_ldflags}"				\\\\\\
    PLUGINLIBDIR=%%{_vdr_plugin_dir}				\\\\\\
    VIDEODIR=%%{_vdr_videodir}					\\\\\\
    LIBDIR=.							\\\\\\
    LOCALEDIR=locale						\\\\\\
    VDRLOCALE='""'						\\\\\\
    DVBDIR=%%{_prefix}						\\\\\\
    VDRDIR=%{_includedir}/vdr					\\\\\\
    VDRVERSION=%%{vdr_version}					\\\\\\
    VDRVERSNUM=%%(echo %%{vdr_rpmversion} |			\\\\\\
        %__awk -F'.' '{ print \$1*10000+\$2*100+\$3 }')		\\\\\\
    APIVERSION=%%{vdr_apiversion}				\\\\\\
    APIVERSNUM=%%(echo %%{vdr_apiversion} |			\\\\\\
        %__awk -F'.' '{ print \$1*10000+\$2*100+\$3 }')

%%vdr_plugin_install \\
    if ! [ -e vdr_plugin_prep.done ]; then \\
        echo "Missing %%%%vdr_plugin_prep, aborting!" \\
        exit 1 \\
    fi \\
    rename .so.%%{vdr_version} .so.%%{vdr_apiversion} *.so.%%{vdr_version} &>/dev/null || : \\
    for f in libvdr-*.so.%%{vdr_apiversion}; do \\
        install -D -m755 \$f %%{buildroot}%%{_vdr_plugin_dir}/\$f \\
        install -d -m755 %%{buildroot}%%{_datadir} \\
        [ -d locale ] && cp -r locale %%{buildroot}%%{_datadir} \\
        NAME=\$(echo \$f | perl -pe "s/^libvdr-(.*).so.%%{vdr_apiversion}/\\\\1/") \\
        echo %%{_vdr_plugin_dir}/\$f > \$NAME.vdr \\
        %%find_lang vdr-\$NAME \\
        cat vdr-\$NAME.lang >> \$NAME.vdr \\
        if [ -f "\$NAME.mandriva-params" ]; then \\
            install -D -m644 \$NAME.mandriva-defaults %%{buildroot}%%{_vdr_plugin_paramdir}/\$NAME.defaults \\
            install -D -m644 \$NAME.mandriva-params %%{buildroot}%%{_vdr_plugin_paramdir}/\$NAME.params \\
            install -D -m644 \$NAME.mandriva-sysconfig %%{buildroot}%%{_sysconfdir}/sysconfig/vdr-\$NAME \\
            echo "%%config(noreplace) %%{_sysconfdir}/sysconfig/vdr-\$NAME" >> \$NAME.vdr \\
            echo "%%{_vdr_plugin_paramdir}/\$NAME.defaults" >> \$NAME.vdr \\
            echo "%%{_vdr_plugin_paramdir}/\$NAME.params" >> \$NAME.vdr \\
        fi \\
    done

%%vdr_chanlogo_notice This skin is able to display channel logos. In order to use this \\
functionality, channel logos must be put in %%{_vdr_chanlogodir}. The \\
recommended format is 64x48px 16-color xpm. When using dxr3 as the \\
output device, the recommended maximum number of colors is 6.

%%vdr_plugin_params_begin() \\
vdr_plugin_params_do() { \\
	vdr_plugin_params_handle() { \\
		if echo "\$gotparam" | grep -q "\$gotvar"; then \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-sysconfig \\
			gotparam="\${gotparam//\$gotvar/'\\\\$\$gotvar'}" \\
			echo "[ -n \\\\"\\\\$\$gotvar\\\\" ] && echo \\\\"\$gotparam\\\\"" >> %%1.mandriva-params \\
		elif echo "\$gotparam" | grep -q "MULTIPLE_PARAMS"; then \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-sysconfig \\
			echo "local gotparam=\\\\"\$gotparam\\\\"" >> %%1.mandriva-params \\
			echo "echo \\\\"\\\\$\$gotvar\\\\" | xargs -n1 | while read subvar &&" >> %%1.mandriva-params \\
			echo "	[ -n \\\\"\\\\\$subvar\\\\" ]; do" >> %%1.mandriva-params \\
			echo "	echo \\\\"\\\\\${gotparam//MULTIPLE_PARAMS/'\\\\\$subvar'}\\\\"" >> %%1.mandriva-params \\
			echo "done" >> %%1.mandriva-params \\
		else \\
			[ -z "\$gotdefault" ] && gotdefault=no \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-sysconfig \\
			echo "[ \\\\"\\\\$\$gotvar\\\\" == yes ] && echo \\\\"\$gotparam\\\\"" >> %%1.mandriva-params \\
		fi \\
		echo >> %%1.mandriva-sysconfig \\
		gotvar= \\
		gotparam= \\
		gotdefault= \\
	} \\
	local gotvar= \\
	local gotparam= \\
	local gotdefault= \\
	echo "# Do not modify this file, use %%{_sysconfdir}/sysconfig/%{name}-%%1 instead" > %%1.mandriva-defaults \\
	echo "# Do not modify this file, use %%{_sysconfdir}/sysconfig/%{name}-%%1 instead" > %%1.mandriva-params \\
	echo -e "# VDR plugin %%1 configuration\\\\n" > %%1.mandriva-sysconfig \\
	while read INPUT; do \\
		if echo "\$INPUT" | grep -q '^#'; then \\
			[ -n "\$gotvar" ] && [ -n "\$gotparam" ] && vdr_plugin_params_handle \\
			echo "\$INPUT" >> %%1.mandriva-sysconfig \\
			continue \\
		fi \\
		if echo "\$INPUT" | grep -q '^var='; then \\
			gotvar="\${INPUT/var=}" \\
			continue \\
		fi \\
		if echo "\$INPUT" | grep -q '^param='; then \\
			eval gotparam="\${INPUT/param=}" \\
			continue \\
		fi \\
		if echo "\$INPUT" | grep -q '^default='; then \\
			eval gotdefault="\${INPUT/default=}" \\
			continue \\
		fi \\
		exit 1 \\
	done \\
	vdr_plugin_params_handle \\
} \\
vdr_plugin_params_do <<VDR_PLUGIN_PARAMS_EOF \\
%%nil

%%vdr_plugin_params_end VDR_PLUGIN_PARAMS_EOF

%if %{mdkversion} >= 200900
%%vdr_plugin_post() %%{nil}
%%vdr_plugin_postun() %%{nil}
%else
%%vdr_plugin_post() if [ "\$1" = "1" ] && [ -e %{_initrddir}/%{name} ]; then /sbin/service vdr plugin_install %%1; fi \\
%%nil
%%vdr_plugin_postun() if [ -e %{_initrddir}/%{name} ]; then if [ "\$1" = "0" ]; then /sbin/service vdr plugin_remove %%1; else /sbin/service vdr plugin_upgrade %%1; fi; fi \\
%%nil
%endif

EOF

# Local version of the above post and postun:
%define plugin_rpmscripts() \
%post plugin-%{1} \
if [ "$1" = "1" ] && [ -e %{_initrddir}/%{name} ]; then /sbin/service vdr plugin_install %{1}; fi \
%postun plugin-%{1} \
if [ -e %{_initrddir}/%{name} ]; then if [ "$1" = "0" ]; then /sbin/service vdr plugin_remove %{1}; else /sbin/service vdr plugin_upgrade %{1}; fi; fi

%build
%make
%define vdr_plugin_ldflags %(echo "%{?ldflags}" | sed 's@-Wl,--no-undefined@@')
# [a-z] does not match v,w on fi_FI.ISO-8859-15, TODO: patch to use [[:lower:]]
# parallel make disabled, as of 2009-07-28 fails on klodia due to too many threads:
# "libgomp: Thread creation failed: Resource temporarily unavailable"
LC_ALL=C make plugins CFLAGS="%optflags %vdr_plugin_flags -I%{_includedir}/ncursesw %vdr_plugin_ldflags" CXXFLAGS="%optflags %vdr_plugin_flags -I%{_includedir}/ncursesw %vdr_plugin_ldflags"

# fix locales
for dir in locale/*_*; do
	[ $(basename $dir) == "zh_CN" ] && continue
	# VDR wrongly uses the _COUNTRY identification always
	rm -rf ${dir%_*}
	mv $dir ${dir%_*}
done

%install
rm -rf %{buildroot}

install -D -m755 vdr %{buildroot}%{_bindir}/vdr
install -d -m755 %{buildroot}%{vdr_videodir}
install -d -m755 %{buildroot}%{vdr_chanlogodir}
install -d -m755 %{buildroot}%{vdr_themedir}
install -d -m755 %{buildroot}%{vdr_cfgdir}
ln -s %{vdr_themedir} %{buildroot}%{vdr_cfgdir}/themes

install -D -m644 vdr.1 %{buildroot}%{_mandir}/man1/vdr.1
install -D -m644 vdr.5 %{buildroot}%{_mandir}/man5/vdr.5

install -d -m755 %{buildroot}%{vdr_plugin_dir}
install -m755 PLUGINS/src/*/*.so.* %{buildroot}%{vdr_plugin_dir}

install -d -m755 %{buildroot}%{_includedir}/%{name}
install -d -m755 %{buildroot}%{_includedir}/libsi
install -m644 include/%{name}/* %{buildroot}%{_includedir}/%{name}
install -m644 include/libsi/* %{buildroot}%{_includedir}/libsi

install -d -m755 %{buildroot}%{_sysconfdir}/rpm/macros.d
install -m644 vdr.macros %{buildroot}%{_sysconfdir}/rpm/macros.d

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
install -m644 {diseqc.conf,keymacros.conf,sources.conf,svdrphosts.conf} \
	%{buildroot}%{vdr_cfgdir}

install -d -m755 %{buildroot}%{vdr_plugin_dir}
install -d -m755 %{buildroot}%{vdr_plugin_datadir}
install -d -m755 %{buildroot}%{vdr_plugin_cachedir}
install -d -m755 %{buildroot}%{vdr_plugin_paramdir}
install -d -m755 %{buildroot}%{vdr_epgimagesdir}

# init stuff
install -d -m755 %{buildroot}%{_initrddir}
install -d -m755 %{buildroot}%{_sysconfdir}/sysconfig
install -m755 %SOURCE1 %{buildroot}%{_initrddir}/%{name}
install -m755 %SOURCE2 %{buildroot}%{_bindir}/runvdr
install -m644 %SOURCE4 %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# sky plugin
install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}/sky
install -m644 PLUGINS/src/sky/channels.conf.sky \
	%{buildroot}%{vdr_plugin_cfgdir}/sky
install -m755 PLUGINS/src/sky/getskyepg.pl %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_sysconfdir}/cron.daily
install -m755 %SOURCE5 %{buildroot}%{_sysconfdir}/cron.daily/getskyepg
install -m644 %SOURCE6 %{buildroot}%{_sysconfdir}/sysconfig/%{name}-sky

# pictures plugin
install -m755 PLUGINS/src/pictures/pic2mpg %{buildroot}%{_bindir}

# scripts
install -m755 *.pl %{buildroot}%{_bindir}

# locales
cp -r locale %{buildroot}%{_datadir}/

%if %{mdkversion} >= 200900
# automatic plugin post and postun actions
install -d -m755 %{buildroot}%{_var}/lib/rpm/filetriggers
install -m755 %SOURCE8 %{buildroot}%{_var}/lib/rpm/filetriggers/vdr-plugins.script
echo "^.%{_vdr_plugin_dir}/libvdr-.*\.so\." > %{buildroot}%{_var}/lib/rpm/filetriggers/vdr-plugins.filter
sed -i 's,#FILETRIGGERS#,,' %{buildroot}%{_initrddir}/%{name}
%endif

%find_lang vdr
%find_lang vdr-hello
%find_lang vdr-skincurses
%find_lang vdr-pictures

%clean
rm -rf %{buildroot}

%pre common
%_pre_useradd vdr %{_localstatedir}/lib/%{name} /bin/nologin
%{_bindir}/gpasswd -a vdr video >/dev/null

%post
# This test can be removed when ccp is updated to check that .rpmnew is
# not obsolete
if test -e %{_sysconfdir}/sysconfig/vdr.rpmnew && test $(stat -c%%Z %{_sysconfdir}/sysconfig/vdr.rpmnew) \
		-gt $(stat -c%%Z %{_sysconfdir}/sysconfig/vdr); then
	ccp --backup --delete --ifexists --set NoOrphans --oldfile \
		%{_sysconfdir}/sysconfig/vdr --newfile %{_sysconfdir}/sysconfig/vdr.rpmnew
fi
%_post_service vdr

%preun
%_preun_service vdr

%postun common
%_postun_userdel vdr

%if %{mdkversion} < 200900
# post and postun
%plugin_rpmscripts hello
%plugin_rpmscripts osddemo
%plugin_rpmscripts pictures
%plugin_rpmscripts skincurses
%plugin_rpmscripts sky
%plugin_rpmscripts status
%plugin_rpmscripts servicedemo
%plugin_rpmscripts svdrpdemo
%endif

%files -f vdr.lang
%defattr(-,root,root)
%doc HISTORY* INSTALL* MANUAL* CONTRIBUTORS* UPDATE* README*
%doc shutdown.sh.example
%attr(-,vdr,vdr) %dir %{vdr_cfgdir}
%attr(-,vdr,vdr) %dir %{vdr_plugin_cfgdir}
%attr(-,vdr,vdr) %dir %{vdr_themedir}
%config(noreplace) %{vdr_cfgdir}/*.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/vdr
%{_initrddir}/%{name}
%{_bindir}/runvdr
%{_bindir}/epg2html.pl
%{_bindir}/summary2info.pl
%{_bindir}/svdrpsend.pl
%{_mandir}/man1/vdr.1*
%{_mandir}/man5/vdr.5*
%attr(-,vdr,vdr) %dir %{vdr_videodir}
%dir %{vdr_plugin_dir}
%dir %{vdr_plugin_datadir}
%dir %{vdr_plugin_cachedir}
%dir %{vdr_chanlogodir}
%{vdr_cfgdir}/themes
%dir %{vdr_plugin_paramdir}
%dir %{vdr_epgimagesdir}
%if %{mdkversion} >= 200900
%{_var}/lib/rpm/filetriggers/vdr-plugins.filter
%{_var}/lib/rpm/filetriggers/vdr-plugins.script
%endif

%files common
%defattr(-,root,root)
%attr(-,vdr,vdr) %dir %{_localstatedir}/lib/%{name}

%files devel
%defattr(-,root,root)
%doc i18n-to-gettext/i18n-to-gettext.pl
%{_sysconfdir}/rpm/macros.d/vdr.macros
%{_includedir}/vdr
%{_includedir}/libsi

%files plugin-hello -f vdr-hello.lang
%defattr(-,root,root)
%doc PLUGINS/src/hello/HISTORY
%doc PLUGINS/src/hello/README
%{vdr_plugin_dir}/libvdr-hello.so.%{apiversion}

%files plugin-osddemo
%defattr(-,root,root)
%doc PLUGINS/src/osddemo/HISTORY
%doc PLUGINS/src/osddemo/README
%{vdr_plugin_dir}/libvdr-osddemo.so.%{apiversion}

%files plugin-pictures -f vdr-pictures.lang
%defattr(-,root,root)
%doc PLUGINS/src/pictures/HISTORY
%doc PLUGINS/src/pictures/README
%{_bindir}/pic2mpg
%{vdr_plugin_dir}/libvdr-pictures.so.%{apiversion}

%files plugin-skincurses -f vdr-skincurses.lang
%defattr(-,root,root)
%doc PLUGINS/src/skincurses/HISTORY
%doc PLUGINS/src/skincurses/README
%{vdr_plugin_dir}/libvdr-skincurses.so.%{apiversion}

%files plugin-sky
%defattr(-,root,root)
%doc PLUGINS/src/sky/HISTORY
%doc PLUGINS/src/sky/README
%doc PLUGINS/src/sky/lircd.conf.sky
%{_bindir}/getskyepg.pl
%config(noreplace) %{vdr_plugin_cfgdir}/sky/channels.conf.sky
%{_sysconfdir}/cron.daily/getskyepg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-sky
%{vdr_plugin_dir}/libvdr-sky.so.%{apiversion}

%files plugin-status
%defattr(-,root,root)
%doc PLUGINS/src/status/HISTORY
%doc PLUGINS/src/status/README
%{vdr_plugin_dir}/libvdr-status.so.%{apiversion}

%files plugin-servicedemo
%defattr(-,root,root)
%doc PLUGINS/src/servicedemo/HISTORY
%doc PLUGINS/src/servicedemo/README
%{vdr_plugin_dir}/libvdr-svccli.so.%{apiversion}
%{vdr_plugin_dir}/libvdr-svcsvr.so.%{apiversion}

%files plugin-svdrpdemo
%defattr(-,root,root)
%doc PLUGINS/src/svdrpdemo/HISTORY
%doc PLUGINS/src/svdrpdemo/README
%{vdr_plugin_dir}/libvdr-svdrpdemo.so.%{apiversion}
