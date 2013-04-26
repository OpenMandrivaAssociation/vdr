
%define maintpatch 2
%define oapiversion 1.6.0

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
Name:	vdr
Version:	1.6.0
Release:	26
Group:		Video
License:	GPLv2+
URL:		http://www.tvdr.de/
Source:		ftp://ftp.tvdr.de/vdr/%{name}-%{version}.tar.bz2

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
# fix overlapping strcpy in command-line parsing causing corruption:
Patch37:	vdr-fix-overlapping-strcpy.patch
# fix build with GCC 4.6
Patch39:	vdr-gcc4.6.patch

# From upstream
# Switch from V4L1 to V4L2
Patch38:	vdr-adapt-to-v4l2.patch

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

BuildRequires:	libcap-devel
BuildRequires:	jpeg-devel
BuildRequires:	ncursesw-devel
BuildRequires:	fontconfig-devel
BuildRequires:	pkgconfig(freetype2)
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(post):	vdr-common = %{version}
Requires:	vdr-common = %{version}
Provides:	vdr-abi = %{vdr_abi}
Obsoletes:	vdr-plugin-subtitles < 0.5.0-8
Requires(post):	ccp >= 0.4.1
# Plugins:
Requires:	ccp >= 0.4.1

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
%patch37 -p1
%patch38 -p1
%patch39 -p1

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

LIRC_DEVICE = %{_var}/run/lirc/lircd
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

# The escaping gets a little messy:
# \$	= plain $ in macros
# \\	= multiline macro
# \\\\	= plain \ in macros
# these and their combinations are the only types of escaping present below:
cat > vdr.macros <<EOF
## VDR plugin macros ##

%%vdr_version		%{version}-%{release}
%%vdr_rpmversion	%version
%%vdr_apiversion	%apiversion
%%vdr_abi		%vdr_abi

%%vdr_plugin_flags	%%{optflags} %vdr_plugin_flags %%{vdr_plugin_ldflags} \${VDR_PLUGIN_EXTRA_FLAGS}
%%vdr_plugin_ldflags	%%(echo "%%{?ldflags}" | sed 's@-Wl,--no-undefined@@')

%%vdr_plugin_dir	%{_libdir}/%{name}
%%vdr_plugin_datadir	%{vdr_datadir}
%%vdr_plugin_cfgdir	%{vdr_cfgdir}/plugins
%%vdr_plugin_paramdir	%{vdr_datadir}/defaults
%%vdr_plugin_cachedir	%{_var}/cache/%{name}
%%vdr_videodir		%{_localstatedir}/lib/%{name}/video
%%vdr_cfgdir		%{_localstatedir}/lib/%{name}/config
%%vdr_datadir		%{_datadir}/%{name}
%%vdr_chanlogodir	%{vdr_datadir}/chanlogos
%%vdr_themedir		%{_localstatedir}/lib/%{name}/themes
%%vdr_epgimagesdir	%{_var}/cache/%{name}/epgimages

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
    PLUGINLIBDIR=%%{vdr_plugin_dir}				\\\\\\
    VIDEODIR=%%{vdr_videodir}					\\\\\\
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
        install -D -m755 \$f %%{buildroot}%%{vdr_plugin_dir}/\$f \\
        install -d -m755 %%{buildroot}%%{_datadir} \\
        [ -d locale ] && cp -r locale %%{buildroot}%%{_datadir} \\
        NAME=\$(echo \$f | perl -pe "s/^libvdr-(.*).so.%%{vdr_apiversion}/\\\\1/") \\
        echo %%{vdr_plugin_dir}/\$f > \$NAME.vdr \\
        %%find_lang vdr-\$NAME || touch $NAME.lang \\
        cat vdr-\$NAME.lang >> \$NAME.vdr \\
        if [ -f "\$NAME.mandriva-params" ]; then \\
            install -D -m644 \$NAME.mandriva-defaults %%{buildroot}%%{vdr_plugin_paramdir}/\$NAME.defaults \\
            install -D -m644 \$NAME.mandriva-params %%{buildroot}%%{vdr_plugin_paramdir}/\$NAME.params \\
            install -D -m644 \$NAME.mandriva-sysconfig %%{buildroot}%%{_sysconfdir}/sysconfig/vdr-\$NAME \\
            echo "%%config(noreplace) %%{_sysconfdir}/sysconfig/vdr-\$NAME" >> \$NAME.vdr \\
            echo "%%{vdr_plugin_paramdir}/\$NAME.defaults" >> \$NAME.vdr \\
            echo "%%{vdr_plugin_paramdir}/\$NAME.params" >> \$NAME.vdr \\
        fi \\
    done

%%vdr_chanlogo_notice This skin is able to display channel logos. In order to use this \\
functionality, channel logos must be put in %%{vdr_chanlogodir}. The \\
recommended format is 64x48px 16-color xpm. When using dxr3 as the \\
output device, the recommended maximum number of colors is 6.

%%vdr_plugin_params_begin() \\
vdr_plugin_params_do() { \\
	vdr_plugin_params_handle() { \\
		if echo "\$gotparam" | grep -q "\$gotvar"; then \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-sysconfig \\
			gotparam="\${gotparam//\$gotvar/'\\\\\$\$gotvar'}" \\
			echo "[ -n \\\\"\\\\\$\$gotvar\\\\" ] && echo \\\\"\$gotparam\\\\"" >> %%1.mandriva-params \\
		elif echo "\$gotparam" | grep -q "MULTIPLE_PARAMS"; then \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-sysconfig \\
			echo "local gotparam=\\\\"\$gotparam\\\\"" >> %%1.mandriva-params \\
			echo "echo \\\\"\\\\\$\$gotvar\\\\" | xargs -n1 | while read subvar &&" >> %%1.mandriva-params \\
			echo "	[ -n \\\\"\\\\\$subvar\\\\" ]; do" >> %%1.mandriva-params \\
			echo "	echo \\\\"\\\\\${gotparam//MULTIPLE_PARAMS/'\\\\\$subvar'}\\\\"" >> %%1.mandriva-params \\
			echo "done" >> %%1.mandriva-params \\
		else \\
			[ -z "\$gotdefault" ] && gotdefault=no \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-sysconfig \\
			echo "[ \\\\"\\\\\$\$gotvar\\\\" == yes ] && echo \\\\"\$gotparam\\\\"" >> %%1.mandriva-params \\
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
echo "^.%{vdr_plugin_dir}/libvdr-.*\.so\." > %{buildroot}%{_var}/lib/rpm/filetriggers/vdr-plugins.filter
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


%changelog
* Fri May 13 2011 Anssi Hannula <anssi@mandriva.org> 1.6.0-19mdv2011.0
+ Revision: 674005
- revert incorrect changes made in 18mdv
- adapt for V4L2 (fixes build with with recent linux headers, patch
  adapt-to-v4l2.patch from upstream)
- fix build with GCC 4.6 (gcc4.6.patch)

* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 1.6.0-18mdv2011.0
+ Revision: 567114
- deal with our flags

  + Anssi Hannula <anssi@mandriva.org>
    - make the escaping in .spec more consistent and add a comment explaining
      it

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 1.6.0-17mdv2010.1
+ Revision: 492262
- rebuild for new libjpegv8

* Wed Jan 06 2010 Anssi Hannula <anssi@mandriva.org> 1.6.0-16mdv2010.1
+ Revision: 486591
- fix plugin arguments corruption on x86_64 with glibc 2.11+
  (P37: fix-overlapping-strcpy.patch)

* Sun Dec 13 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-15mdv2010.1
+ Revision: 478264
- adapt for new location of lirc socket on 2010.0+
- update URL

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 1.6.0-14mdv2010.0
+ Revision: 419763
- rebuild for new libjpeg v7

* Mon Aug 03 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-13mdv2010.0
+ Revision: 407680
- start vdr after dkms, if present

* Fri Jul 31 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-12mdv2010.0
+ Revision: 405053
- fix an error in filetriggers handling preventing VDR from restarting
  when the plugins were explicitely listed in sysconfig file
- fix filetriggers filter

* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-10mdv2010.0
+ Revision: 404798
- enable filetriggers on 2009.1 as well, with a requirement on the fixed
  rpm in main/updates

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-9mdv2010.0
+ Revision: 402631
- fix a bug in Reinhard Nissl's h264 patch that would cause "Illegal
  instruction" error when trying to emit an error into syslog in one
  specific case (h264-non-pod-type.patch)

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-8mdv2010.0
+ Revision: 401086
- disable parallel make for included plugins due to errors with klodia
  buildhost
- apply ldflags in main vdr package as well
- VDR 1.6.0-2
- embed patch version numbers into Patch lines in spec
- use filetriggers for plugin %%post and %%postun handling on 2009.0 and
  cooker (2009.1 will follow after rpm update #52470)
- apply %%ldflags for plugins
- replace $VDR_PLUGIN_FLAGS with $VDR_PLUGIN_EXTRA_FLAGS
- do not wait for harddrake on boot
- fix typo in initscript description
- do not print success/failure twice when shutting down VDR
- add condrestart support for initscript
- add patches:
  o fix build with gcc4.4 (grab.diff from upstream, const.diff from
    Ludwig Nussel)
  o add subtitles selection button into Setup/DVB menu
    (subtitles-button.patch from Rolf Ahrenberg)
  o use cap_sys_nice capabilities (cap_sys_nice.patch from Rolf Ahrenberg,
    applied in upstream devel)
  o add keymacro support for hitk SVDRP command (hitk.patch from Rolf
    Ahrenberg)
  o set thread specific I/O priorities (ionice.patch from Rolf Ahrenberg,
  o add timercmd patch from epgsearch (timercmd-0.1_1.6.0.diff)
  o disable CA updates for pluginparam devices
    (plugindev-disable-ca-updates.patch from iptv plugin)
  o allow epgsearch plugin to replace timer edit screen (exttimeredit.diff
    from epgsearch)
- update patches:
  o update liemikuutio patchset to 1.27 (Rolf Ahrenberg)
  o update parentalrating-content.diff with new broadcaster-defined
    ratings (Rolf Ahrenberg)
  o update ttxtsubs support patch from ttxtsubs (ttxtsubs.patch)
  o update noepg support patch from e-tobi / noepgmenu plugin
  o update menuorg support patch from e-tobi / menuorg plugin
  o update graphtft support patch from e-tobi / graphtft plugin
  o update timer-info patch to 0.5 (Thomas G?\195?\188nther)
  o update jumpplay patch to 1.0 (Thomas G?\195?\188nther)
  o update pvrinput support patch from e-tobi (add CA ids A0 and A2,
    suggested by Christian Jarczyk)
- ABI is modified by patches, plugins have to be rebuilt
- rediff patches: configurable lnbshare, pluginparam.patch, Reinhard
  Nissl's h264+etc patch, cmdsubmenu.patch, MainMenuHooks.patch,
  pin.patch
- fix init script containing return outside function, called when vdr
  is already started

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-6mdv2009.1
+ Revision: 359268
- bump ABI version due to patch changes, plugins have to be rebuilt
- fix printf format strings (printf-format.patch and hunks in h264 patch)
- drop kernel dvb api check (drop-dvbapi-check.patch) as the api
  version is bumped arbitrarily
- update liemikuutio patchset to 1.24
- drop oldsubs.patch, merged into liemikuutio
- add frontend-facilities.patch
- rediff patches rotor, pin, mainmenuhooks
- rediff patches lnbshare, graphtft, shared-devices, sourcecaps,
  h264, cmdsubmenu, rotor, jumpplay, mainmenuhooks
- build plugins with current optflags instead of vdr optflags
- check for already running vdr in initscript

  + Funda Wang <fwang@mandriva.org>
    - really rediff
    - rediff vdrversion patch

* Mon Jul 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-5mdv2009.0
+ Revision: 232374
- rebuilt against new libcap

  + Anssi Hannula <anssi@mandriva.org>
    - define %%_localstatedir locally for backportability

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Thu May 15 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-4mdv2009.0
+ Revision: 207713
- add an introductory README.install.urpmi file
- fix default configdir path when running outside runvdr (#40641)
- add configurable logident for multi-vdr systems (logident.patch), not
  added to sysconfig until accepted upstream
- fix HasDecoder() when in pmExtern playmode (hasdecoder.patch)
- detach runvdr from controlling terminal using setsid
- start vdr only after all filesystems have been mounted
  (Should-Start: $local_fs $remote_fs)

* Sun May 04 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-3mdv2009.0
+ Revision: 201088
- play subtitles automatically on old recordings (oldsubs.patch)

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-2mdv2009.0
+ Revision: 197884
- handle shared devices with --only-in= and --only-out (P9)
- add patch to properly handle CA with streamdev (P10)
- patches modify the ABI, plugins have to rebuilt

* Fri Apr 25 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 197497
- adapt cflags for ncursesw
- add urpmi readme file for upgrades
- VDR 1.6.0-1
- subtitles support integrated, drop the patch and add obsoletes
  on vdr-plugin-subtitles
- minor description and summary updates
- drop unneeded translationerror-only-when-debug patch (P1)
- drop maxdevices patch, applied upstream (P2)
- drop getdevices patch, applied upstream (P3)
- rediff rsvps patch (P4)
- hack around bad subtitle support of DXR3 (P6)
- set monospace as default monospace font and sans serif as default
  large font (P7)
- show more font aliases in the font lists (P8)
- update liemikuutio patchset to 1.19 (P12)
- add Rolf Ahrenberg's cutter-marks, parentalrating-content and
  thread-name patches (P13, P14, P15)
- drop closefilter patch, applied upstream (P16)
- update sort-options and dd-record-option patches from e-tobi
  (P21, P22)
- switch to e-tobi versions of yaepg, pin, graphtft, sourcecaps, and
  reelchannelscan patches (P23, P25, P26, P27, P29)
- replace submenu patch with menuorg patch from e-tobi (P24)
- replace noepgmenu patch with noepg patch from e-tobi (P28)
- add pvrinput support patch from e-tobi (P30)
- update lnbshare patch (P34)
- update rotor support patch (P40)
- drop unneeded decruft patch (P45)
- update jumpplay, timer-info and cmdsubmenu patches (P50, P52, P53)
- drop smooth-fastforward patch, applied upstream (P56)
- drop unneeded exthooks patch (P60)
- drop sc patch, applied upstream (P63)
- update h264 patch (P67)
- add a fix for h264 patch (P68)
- now buildrequires libncursesw-devel instead of ncurses-devel
- buildrequires fontconfig-devel and freetype2-devel
- drop old obsoletes on vdr-core packages
- add the new pictures plugin
- adapt build macros for gettext localization, and rename the locales to
  standard names
- require gettext in vdr-devel
- fix vdr_plugin_post and vdr_plugin_postun macros to not consume the
  line after them
- do not disable UTF-8 anymore, vdr now supports it
- add new options into sysconfig file

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.4.7-9mdv2008.1
+ Revision: 144612
- add handling for plugin parameters that can be specified multiple
  times (MULTIPLE_PARAMS)
- provide VdrVersion() for fetching version at runtime
- get rid of %%vdr_add_optflags for specifying additional compiler flags
  and use more standard and robust VDR_PLUGIN_FLAGS variable that
  overrides %%{vdr_plugin_flags}, in the same way as CFLAGS=>%%{optflags}
- set VDRVERSION to version-release
- add vdr_sub_abi number to APIVERSION
- adapt license tag for new policy
- P67: add H.264 support by Reinhard Nissl, adapted for 1.4.7 by Petri
  Hintukainen (http://phivdr.dyndns.org/vdr/.h264/), adapted for
  Mandriva package by Petri Suvila
- the VDR ABI is modified, plugins have to be rebuilt

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-8mdv2008.1
+ Revision: 103023
- add support for smooth fast forward with output plugins that support it
  (P56, from xineliboutput plugin)
- add pluginparam and closefilter patches for iptv plugin (P16, P17)
- patches modify the VDR ABI, plugins have to be rebuilt

* Sat Oct 27 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-7mdv2008.1
+ Revision: 102679
- minor description fixes
- update subtitles+ttxtsubs patch (fixes bug in PES_EXTENSION insertion)
- raise maximum number of DVB devices to 8 (patch2)
- use silent grep in module check in runvdr

* Wed Sep 05 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-6mdv2008.0
+ Revision: 80287
- add dummy LOCALEDIR to plugin build call to allow building plugins
  that contain support for both the new and the legacy i18n handling

* Thu Jul 12 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-5mdv2008.0
+ Revision: 51440
- call modprobe and rmmod with exact path
- set HOME to VDR_USER homedir (default /var/lib/vdr), fixes crash with dvd
  plugin, reported by Johan Schuring

* Tue Jul 10 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-4mdv2008.0
+ Revision: 51060
- use BASH_ENV instead of --login to load system variables
- provide global macro %%vdr_plugin_flags

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-3mdv2008.0
+ Revision: 49956
- patches modify the ABI, plugins have to be rebuilt
- do not show "no translation" errors when running under low logging
  level (patch1)
- add clean support for external CI handlers (patch63), drop now
  unneeded hunks from patch60
- add %%_vdr_epgimagesdir as global macro
- set plugin configuration variables as local to prevent namespace clashes
- do not show pin plugin specific options when it is not loaded
- reset environment when launching runvdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-2mdv2008.0
+ Revision: 42043
- add menu patch for graphtft plugin (P32)
- add patch for reelchannelscan plugin (P47)
- add patch for pin plugin (P58)
- patches break plugin ABI, plugins have to be rebuilt
- plugins now require vdr with specific arch
- add README.mdv regarding manually compiling plugins
- load capability kernel module in runvdr if needed

* Sat May 12 2007 Anssi Hannula <anssi@mandriva.org> 1.4.7-1mdv2008.0
+ Revision: 26424
- 1.4.7

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.4.6-8mdv2008.0
+ Revision: 23261
- fix VDRVERSION during plugin build

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.4.6-6mdv2008.0
+ Revision: 22669
- VDR 1.4.6-1
- drop patch2, no longer needed by streamdev
- re-enable patch4
  o breaks ABI, plugins have to be rebuilt
- drop patch5, applied upstream
- update Ahrenberg's subtitles+ttxtsubs patch
- minor improvements in description
- add epg2html.pl and summary2info.pl

* Fri May 04 2007 Anssi Hannula <anssi@mandriva.org> 1.4.6-3mdv2008.0
+ Revision: 22557
- disable patch4 for now

* Tue May 01 2007 Anssi Hannula <anssi@mandriva.org> 1.4.6-2mdv2008.0
+ Revision: 19858
- patch4: allow using running status as VPS fallback
- patch5: fix NIT handling on Finnish Digita DVB-T
- patch65: menu hooks for epgsearch plugin


* Sun Mar 04 2007 Anssi Hannula <anssi@mandriva.org> 1.4.6-1mdv2007.0
+ Revision: 132164
- VDR 1.4.6

* Sat Jan 20 2007 Anssi Hannula <anssi@mandriva.org> 1.4.5-1mdv2007.1
+ Revision: 111087
- VDR 1.4.5
- update urls of Rolf Ahrenberg's patches
- make VDR_PLUGIN_ARGS usable in plugin-specific sysconfig files as well
- add some comments into the vdr sysconfig file

* Mon Dec 04 2006 Anssi Hannula <anssi@mandriva.org> 1.4.4-2mdv2007.1
+ Revision: 90489
- raise release
- VDR 1.4.4-2
- upgrade modifies the ABI, plugins have to be rebuilt
- lirc is hotpluggable, remove from should-start
- add harddrake to should-start

* Sat Nov 04 2006 Anssi Hannula <anssi@mandriva.org> 1.4.4-1mdv2007.1
+ Revision: 76610
- VDR 1.4.4

* Sun Oct 29 2006 Anssi Hannula <anssi@mandriva.org> 1.4.3-1mdv2007.1
+ Revision: 73620
- VDR 1.4.3-4
- upgrade modifies the ABI, plugins have to be rebuilt
- liemikuutio 1.13
- upgrade to fixed configurableLNBshare
- drop patch1, patch3, applied upstream
- fix patch60
- add better comments to files in /usr/share/vdr/defaults/
- fix uninstalling plugins if rpm didn't honor Requires(preun)
- fix missing backslash from runvdr
- Import vdr

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 1.4.2-3mdv2007.0
- patch4: fix cTimer assignment
- patch1: raise APIVERSION as patch4 is from upstream
- patch4 modifies the ABI, plugins have to be rebuilt
- remove /etc/vdr symlink, it only adds confusion

* Mon Sep 04 2006 Anssi Hannula <anssi@mandriva.org> 1.4.2-2mdv2007.0
- VDR 1.4.2-1 (bugfixes)
- add note about permissions to VDR_RCU comment in sysconfig

* Fri Sep 01 2006 Anssi Hannula <anssi@mandriva.org> 1.4.2-1mdv2007.0
- VDR 1.4.2
- liemikuutio 1.10
- no audio group by default
- rediff patch3

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-7mdv2007.0
- use underscore instead of dash in vdr_abi

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-6mdv2007.0
- VDR 1.4.1-5
- upgrade modifies the ABI, plugins have to be rebuilt
- patch3: fix device selection
- stricter ABI requires for plugins
- build plugins with -fPIC by default on x86, add macro for overriding
- rediff patch34

* Fri Aug 11 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-5mdv2007.0
- fix runvdr to check for UTF-8 before disabling it

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-4mdv2007.0
- VDR 1.4.1-3
- upgrade modifies the ABI, plugins have to be rebuilt
- update runvdr to disable UTF-8 (#24155)
- better description
- remove reference to the non-existent .vdr_plugins from runvdr
- rediff patch60

* Tue Jul 25 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-3mdv2007.0
- VDR 1.4.1-2
- liemikuutio 1.8
- do not use -b for patches
- eval the default keyword in plugin params macro
- use ccp for sysconfig files
- modify comments in main sysconfig file
- post and postun for plugins included with vdr
- do not use conditional patches, other patches depend on them
- patch22: separate "record DD" and "use DD" options
- patch45: support for decruft plugin
- patch60: hooks for plugins
- patches modify the ABI, plugins have to be rebuilt

* Mon Jun 19 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-2mdv2007.0
- use _ prefix for system path macros as per convention
- VDR 1.4.1-1
- patch20: better support for analogtv plugin
- patch21: new recording sort options
- patch34: configurable LNB sharing
- patch36: per-device source configuration, aka sourcecaps
- patch42: support for noepgmenu plugin
- patch51: submenu support
- patch52: show if enough space for a recording, aka timer-info
- patch53: hierarchical command menu support

* Mon Jun 12 2006 Anssi Hannula <anssi@mandriva.org> 1.4.1-1mdv2007.0
- VDR 1.4.1
- liemikuutio 1.6
- fix a typo in the VDR initial logmessage
- drop Finnish patch, upstream

* Sun Jun 11 2006 Anssi Hannula <anssi@mandriva.org> 1.4.0-6mdv2007.0
- do not use -fPIC on x86

* Fri Jun 09 2006 Anssi Hannula <anssi@mandriva.org> 1.4.0-5mdv2007.0
- silence rename in vdr_plugin_install
- rotor patch
- buildrequires ncurses-devel
- drop the multiple cores thing, too complicated with plugins
- ship standard core only, add build switches
- drop COPYING, vdr is GPL

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 1.4.0-4mdv2007.0
- maintenance patch 1.4.0-3
- use getenv to get the user homedir
- fix requires of plugins shipped with vdr
- update bigpatch core to 1.4.0-1
- fix VDRVERSION
- modify diseqc.conf earlier

* Fri Jun 02 2006 Anssi Hannula <anssi@mandriva.org> 1.4.0-3mdv2007.0
- patch2: add friend declaration in dvbsub.h for streamdev
- fix build switches for building a custom core

* Thu Jun 01 2006 Anssi Hannula <anssi@mandriva.org> 1.4.0-2mdv2007.0
- fix missing backslash in vdr.macros
- use the real config dir instead of the symlink as the default VDR_CONFIGDIR
- touch channels.conf in run-time, drop from package

* Wed May 31 2006 Anssi Hannula <anssi@mandriva.org> 1.4.0-1mdv2007.0
- initial Mandriva release

