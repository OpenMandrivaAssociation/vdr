%define maintpatch 0
%define oapiversion 2.0.6

# Increased when ABI compatibility is broken by patches
# Reset to 1 when %oapiversion is raised
%define vdr_sub_abi	1
%define vdr_abi		%{oapiversion}_%{_lib}_abi_%{vdr_sub_abi}
%define apiversion	%{oapiversion}.%{vdr_sub_abi}

%define vdr_plugin_dir		%{_libdir}/%{name}
%define vdr_plugin_datadir	%{vdr_datadir}/plugins
%define vdr_plugin_cfgdir	%{vdr_cfgdir}/plugins
%define vdr_plugin_paramdir	%{vdr_datadir}/defaults
%define vdr_plugin_cachedir	%{_var}/cache/%{name}
%define vdr_videodir		%{_localstatedir}/lib/%{name}/video
%define vdr_cfgdir		%{_localstatedir}/lib/%{name}/config
%define	vdr_datadir		%{_datadir}/%{name}
%define vdr_chanlogodir		%{vdr_datadir}/chanlogos
%define vdr_themedir		%{_localstatedir}/lib/%{name}/themes
%define vdr_epgimagesdir	%{_var}/cache/%{name}/epgimages

# shared libraries need to be built with -fPIC
%define vdr_plugin_flags	-fPIC

%if %{maintpatch}
%define fullversion		%{version}-%{maintpatch}
%else
%define fullversion		%{version}
%endif

Summary:	Video Disk Recorder - PVR suite
Name:		vdr
Version:	2.0.7
Release:	2
Group:		Video
License:	GPLv2+
URL:		https://www.tvdr.de/
Source0:	ftp://ftp.tvdr.de/vdr/%{name}-%{version}.tar.bz2

Source2:	vdr-runvdr
Source3:	vdr-shutdown.sh.example
Source4:	vdr.sysconfig
Source8:	vdr-plugin-filetriggers.script
Source9:	vdr2.service.example
Source10:	plugin-update.sh
Source11:	vdr.service

# Patches last checked for updates: 2012/02/17

# ===============
# Patches from upstream (Patch000..099):

# VDR maintenance release patches from upstream
%if %maintpatch
%(for n in {1..%maintpatch}; do
	echo "Patch$((n+70)): ftp://ftp.cadsoft.de/vdr/Developer/vdr-%{version}-$n.diff"
done)
%endif

# ===============
# Patches that are upstreamable (TODO: do it) (Patch100..199):

# add VdrVersion() function for determining VDR version at run-time:
Patch100:       vdr-1.6.0-vdrversion.patch

# submitted a long time ago without reply, TODO: try again
Patch101:	vdr-1.6.0-rsvps.patch

# ===============
# From http://www.saunalahti.fi/~rahrenbe/vdr/patches/ by Rolf Ahrenberg.
# Updated with each version, gunzipped.
# Note that they are usually just rediffed, no actual changes.
# Upstreaming handled by author.
# Not all patches are applied, only those that are generally useful or
# unintrusive.
# (Patch200..299)

Patch200:	vdr-2.0.6-kamalasamala.patch
Patch202:	vdr-2.0.6-lcn-base.patch
Patch203:	vdr-2.1.6-lcn-support.patch

# ===============
# Patches from various sources (Patch300..499):
# Presumed to be upstreamed by the authors.

# From epgsearch
Patch310:	vdr.epgsearch-exttimeredit-0.0.2.diff
Patch312:	timercmd-0.1_1.7.17.diff

# From ttxtsubs
# -2.0.6 = identical
Patch320:	vdr-1.7.40-ttxtsubs.patch

# From Fedora
# http://pkgs.fedoraproject.org/cgit/vdr.git/tree/
Patch420:	vdr-channel+epg.patch
Patch423:	http://toms-cafe.de/vdr/download/vdr-timer-info-0.5-1.7.13.diff
Patch424:	vdr-timer-info-1.7.28.patch
# for epgsearch:
Patch425:	http://pkgs.fedoraproject.org/cgit/vdr.git/plain/vdr-2.0.4-mainmenuhooks101.patch
#
Patch426:	http://www.udo-richter.de/vdr/files/vdr-2.1.5-naludump-0.1.diff

# ===============
# From http://e-tobi.net/ Debian repository (current only).
# Patch headers contain additional information.
# Unknown upstreaming status.
# (Patch500..599)
Patch501:	vdr-1.7.11-yaepg.patch
Patch502:	vdr-1.6.0-menuorg.patch
Patch504:	vdr-1.7.13-graphtft.patch

# From yavdr:
Patch503:	vdr-2.0.3-pin.patch
Patch550:	vdr-1.7.23-rotor.patch

# ===============
# Patches that are unsuitable to be upstreamed
# as-is (Patch600..699):

# CanHandleOver2BitSubtitles() hack:
Patch600:	vdr-1.6.0-dxr3.patch

# Use monospace as default monospace font,
# sans serif as default large font:
Patch601:	vdr-1.6.0-default-fonts-mdv.patch

# Show more font aliases instead of only the per-category defaults (this could
# possibly be upstreamed if made more generic):
Patch602:	vdr-1.6.0-show-more-aliasfonts.patch

BuildRequires:	libcap-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	fribidi-devel
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

VDR in this package is patched with the liemikuutio patch and several
other patches.
%if %maintpatch
This build is additionally patched to the maintenance release
%{version}-%maintpatch.
%endif

%files -f vdr.lang
%doc HISTORY* INSTALL* MANUAL* CONTRIBUTORS* UPDATE* README*
%doc shutdown.sh.example
%doc vdr2.service.example
%attr(-,vdr,vdr) %dir %{vdr_cfgdir}
%attr(-,vdr,vdr) %dir %{vdr_plugin_cfgdir}
%attr(-,vdr,vdr) %dir %{vdr_themedir}
%config(noreplace) %{vdr_cfgdir}/*.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/vdr
%{_unitdir}/%{name}.service
%{_bindir}/runvdr
%{_bindir}/epg2html
%{_bindir}/summary2info
%{_bindir}/svdrpsend
%{_mandir}/man1/vdr.1*
%{_mandir}/man1/svdrpsend.1*
%{_mandir}/man5/vdr.5*
%attr(-,vdr,vdr) %dir %{vdr_videodir}
%dir %{vdr_plugin_dir}
%dir %{vdr_datadir}
%dir %{vdr_plugin_datadir}
%attr(-,vdr,vdr) %dir %{vdr_plugin_cachedir}
%dir %{vdr_chanlogodir}
# symlink
%{vdr_cfgdir}/themes
%dir %{vdr_plugin_paramdir}
%attr(-,vdr,vdr) %dir %{vdr_epgimagesdir}
%{_var}/lib/rpm/filetriggers/vdr-plugins.filter
%{_var}/lib/rpm/filetriggers/vdr-plugins.script
%{_datadir}/%{name}/plugin-update.sh


%post
# This test can be removed when ccp is updated to check that .rpmnew is
# not obsolete (via ctime, not mtime) -Anssi
if test -e %{_sysconfdir}/sysconfig/vdr.rpmnew && test $(stat -c%%Z %{_sysconfdir}/sysconfig/vdr.rpmnew) \
		-gt $(stat -c%%Z %{_sysconfdir}/sysconfig/vdr); then
	ccp --backup --delete --ifexists --set NoOrphans --oldfile \
		%{_sysconfdir}/sysconfig/vdr --newfile %{_sysconfdir}/sysconfig/vdr.rpmnew
fi
%_post_unit vdr

%preun
%_preun_unit vdr

#----------------------------------------------------------------------------

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

%files common
%attr(-,vdr,vdr) %dir %{_localstatedir}/lib/%{name}

%pre common
%_pre_useradd vdr %{_localstatedir}/lib/%{name} /bin/nologin
%{_bindir}/gpasswd -a vdr video >/dev/null

%postun common
%_postun_userdel vdr


#----------------------------------------------------------------------------

%package devel
Summary:	VDR development headers
Group:		Development/C++
Requires:	gettext

%description devel
This package contains the headers that are needed to build
plugins for VDR.

%files devel
%{_sysconfdir}/rpm/macros.d/vdr.macros
%{_includedir}/vdr
%{_includedir}/libsi
%{_libdir}/pkgconfig/vdr.pc

#----------------------------------------------------------------------------

%package plugin-dvbhddevice
Summary:	VDR plugin: HD Full Featured DVB device
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-dvbhddevice
This plugin implements the output device for the
"Full Featured TechnoTrend S2-6400" DVB cards.

%files plugin-dvbhddevice -f vdr-dvbhddevice.lang
%doc PLUGINS/src/dvbhddevice/HISTORY
%doc PLUGINS/src/dvbhddevice/README
%{vdr_plugin_dir}/libvdr-dvbhddevice.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-dvbsddevice
Summary:	VDR plugin: SD Full Featured DVB device
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-dvbsddevice
This plugin implements the output device for the
"Full Featured" DVB cards based on the TechnoTrend/Fujitsu-Siemens
design. This code was originally part of the core VDR source, and
was moved into this plugin in VDR version 1.7.11.

%files plugin-dvbsddevice
%doc PLUGINS/src/dvbsddevice/HISTORY
%doc PLUGINS/src/dvbsddevice/README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-dvbsddevice
%{vdr_plugin_dir}/libvdr-dvbsddevice.so.%{apiversion}
%{vdr_plugin_paramdir}/dvbsddevice.*

#----------------------------------------------------------------------------

%package plugin-epgtableid0
Summary:	VDR plugin: EPG handler for events with table id 0x00
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-epgtableid0
The special handling of EPG events with table id 0x00 has been dropped
in VDR version 1.7.26, and replaced by a more felxible "EPG Handler"
concept. You can use this plugin to get the previous functionality back.

%files plugin-epgtableid0
%doc PLUGINS/src/epgtableid0/HISTORY
%doc PLUGINS/src/epgtableid0/README
%{vdr_plugin_dir}/libvdr-epgtableid0.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-hello
Summary:	VDR plugin: A friendly greeting
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-hello
This is a small demo of the VDR plugin interface.

%files plugin-hello -f vdr-hello.lang
%doc PLUGINS/src/hello/HISTORY
%doc PLUGINS/src/hello/README
%{vdr_plugin_dir}/libvdr-hello.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-osddemo
Summary:	VDR plugin: Demo of arbitrary OSD setup
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-osddemo
Demonstration of how a plugin can have its very own OSD setup.

It's a very primitive game that opens a small window in which the
user can draw lines with the Up, Down, Left and Right buttons.
The color buttons are used to switch color.
Press Ok to close the window.

%files plugin-osddemo
%doc PLUGINS/src/osddemo/HISTORY
%doc PLUGINS/src/osddemo/README
%{vdr_plugin_dir}/libvdr-osddemo.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-rcu
Summary:	VDR plugin: Remote Control Unit
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-rcu
This VDR plugin implements support for the RCU (Remote Control Unit),
a custom device with an infrared receiver and a four digit display:
http://tvdr.de/remote.htm

%files plugin-rcu
%doc PLUGINS/src/rcu/HISTORY
%doc PLUGINS/src/rcu/README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-rcu
%{vdr_plugin_dir}/libvdr-rcu.so.%{apiversion}
%{vdr_plugin_paramdir}/rcu.*

#----------------------------------------------------------------------------

%package plugin-skincurses
Summary:	VDR plugin: A text only skin
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-skincurses
The 'skincurses' plugin implements a VDR skin that works in a
shell window, using only plain text output. It re-implements
what used to be available by compiling VDR versions before 1.3.7
with the DEBUG_OSD macro set.

%files plugin-skincurses -f vdr-skincurses.lang
%doc PLUGINS/src/skincurses/HISTORY
%doc PLUGINS/src/skincurses/README
%{vdr_plugin_dir}/libvdr-skincurses.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-status
Summary:	VDR plugin: Status monitor test
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-status
This is an example that shows the use of cStatus.

%files plugin-status
%doc PLUGINS/src/status/HISTORY
%doc PLUGINS/src/status/README
%{vdr_plugin_dir}/libvdr-status.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-servicedemo
Summary:	VDR plugin: Service demo
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-servicedemo
Demonstration of how plugins can communicate with each other.

%files plugin-servicedemo
%doc PLUGINS/src/servicedemo/HISTORY
%doc PLUGINS/src/servicedemo/README
%{vdr_plugin_dir}/libvdr-svccli.so.%{apiversion}
%{vdr_plugin_dir}/libvdr-svcsvr.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-svdrpdemo
Summary:	VDR plugin: How to add SVDRP support to a plugin
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-svdrpdemo
This plugin shows how to add SVDRP support to a plugin.

%files plugin-svdrpdemo
%doc PLUGINS/src/svdrpdemo/HISTORY
%doc PLUGINS/src/svdrpdemo/README
%{vdr_plugin_dir}/libvdr-svdrpdemo.so.%{apiversion}

#----------------------------------------------------------------------------

%package plugin-pictures
Summary:	VDR plugin: A simple picture viewer
Group:		Video
Requires:	vdr-abi = %{vdr_abi}

%description plugin-pictures
The 'pictures' plugin implements a simple picture viewer.

There is already an 'image' plugin out there which has a lot more
functionality than this one but is also more complex.

This plugin assumes that the pictures have already been converted to
MPEG frames (with the 'pic2mpg' script that comes with this package),
and doesn't implement any fancy features like zooming, panning or
tiled previews. It's just a very simple viewer.

%files plugin-pictures -f vdr-pictures.lang
%doc PLUGINS/src/pictures/HISTORY
%doc PLUGINS/src/pictures/README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-pictures
%{_bindir}/pic2mpg
%{_bindir}/pic2mpg-sd
%{vdr_plugin_dir}/libvdr-pictures.so.%{apiversion}
%{vdr_plugin_paramdir}/pictures.*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

cp %{SOURCE9} .

# drop backups for documentation to avoid them ending up in the rpm
rm -f {README,CONTRIBUTORS,HISTORY,INSTALL,MANUAL,README}.[0-9][0-9][0-9][0-9]

sed -i "/isyslog(\"VDR version %%s started\", VDRVERSION);/s/VDRVERSION/\"%{fullversion} (%{version}-%{release})\"/" vdr.c
sed -ri '/define APIVERSION/s/^(.*")%{oapiversion}(".*)$/\1%{apiversion}\2/' config.h
sed -ri '/define VDRVERSION/s/^(.*")%{fullversion}(".*)$/\1%{version}-%{release}\2/' config.h

# check that the macros are set correctly
[ $(sed -rn '/define APIVERSION/s/^.*"(.*)".*$/\1/p' config.h) == "%{apiversion}" ]
[ $(sed -rn '/define VDRVERSION/s/^.*"(.*)".*$/\1/p' config.h) == "%{version}-%{release}" ]

cp -a %{SOURCE3} shutdown.sh.example

cat > README.%{vendor}.custom-plugins <<EOF
=========================================
Installing additional plugins manually
=========================================

In some cases you want to be able to build and install a plugin manually
against %{product_distribution} VDR, such as when you are developing a new plugin or the
plugin does not yet have a %{product_distribution} package. (Note that in the latter case,
you can send me a packaging request).

You need to have the packages vdr-devel and rpm-build installed.

1. cd into the plugin source directory
2. execute:
     eval \$(rpm --eval %%vdr_plugin_build)
3. copy the resulting libvdr-*.so.* into %{vdr_plugin_dir}

You can give the plugins parameters as instructed in /etc/sysconfig/vdr.
EOF

cat > README.%{vendor}.multi-vdr <<EOF
You can setup a system that runs multiple vdr daemons simultaneusly by doing
the following:
# cp /usr/share/doc/vdr/vdr2.service.sample /etc/systemd/system/vdr2.service
# cp /etc/sysconfig/vdr /etc/sysconfig/vdr2
and editing the files accordingly.

To set plugin parameters individually, you need to set them using
VDR_PLUGIN_ARGS_ in the instance sysconfig fie ("vdr2" above).

The extra VDR daemons will not be restarted automatically on upgrades.
EOF

# Comment default examples out
perl -pi -e "s/^S/# S/" diseqc.conf

cat > README.1.7.0.upgrade.urpmi <<EOF
VDR 1.7 series is a major upgrade and you may need to make configuration
changes to adapt for this new series.

Notable changes that may require user action are:
- DVB output devices ("FF cards") are now supported by the dvbsddevice
  plugin instead of being supported by VDR core.
- Default SVDRP port has been changed to 6419 as assigned for SVDRP use by
  IANA.
- Some scripts have had their '.pl' suffix removed, notably 'svdrpsend'.
- VDR now uses the TS recording format instead of PES. Old recordings
  are still playable.
- LNB sharing is now implemented in VDR core and is now configured
  differently.

See HISTORY in the documentation directory for the full list of changes.
EOF

cat > Make.config <<EOF
CFLAGS   = %{optflags} %{?ldflags}
CXXFLAGS = \$(CFLAGS) -Werror=overloaded-virtual

BINDIR   = %{_bindir}
INCDIR   = %{_includedir}
MANDIR   = %{_mandir}
LOCDIR   = %{_datadir}/locale
PCDIR    = %{_libdir}/pkgconfig

LIBDIR   = %{vdr_plugin_dir}
VIDEODIR = %{vdr_videodir}
CONFDIR  = %{vdr_cfgdir}
RESDIR   = %{vdr_datadir}
CACHEDIR = %{vdr_plugin_cachedir}

LIRC_DEVICE = %{_var}/run/lirc/lircd
BIDI = 1
EOF

cat > README.install.urpmi <<EOF
VDR is an advanced PVR suite and configuring it may not be straight-forward.
Please take a look at the provided documentation first.

Note that VDR does not support output to X11 or framebuffer without
additional plugins, such as xineliboutput or softdevice.

VDR service is provided for your convenience. Instead of running vdr
directly, you should use the vdr service.

%{product_distribution} VDR packages have the following filesystem layout:

%{_sysconfdir}/sysconfig/vdr
%{product_distribution} VDR configuration file; the settings in this file are used to
construct the VDR parameters.

%{_sysconfdir}/sysconfig/vdr-PLUGINNAME
%{product_distribution} VDR plugin configuration files; the settings in these files are used
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
%%vdr_rpmversion	%{version}
%%vdr_apiversion	%{apiversion}
%%vdr_abi		%{vdr_abi}

%%vdr_plugin_flags	%%{optflags} %vdr_plugin_flags %%{vdr_plugin_ldflags} \${VDR_PLUGIN_EXTRA_FLAGS}
%%vdr_plugin_ldflags	%%(echo "%%{?ldflags}" | sed 's@-Wl,--no-undefined@@')

%%vdr_plugin_dir        %{_libdir}/%{name}
%%vdr_plugin_datadir    %{vdr_datadir}
%%vdr_plugin_cfgdir     %{vdr_cfgdir}/plugins
%%vdr_plugin_paramdir   %{vdr_datadir}/defaults
%%vdr_plugin_cachedir   %{_var}/cache/%{name}
%%vdr_videodir          %{_localstatedir}/lib/%{name}/video
%%vdr_cfgdir            %{_localstatedir}/lib/%{name}/config
%%vdr_datadir           %{_datadir}/%{name}
%%vdr_chanlogodir       %{vdr_datadir}/chanlogos
%%vdr_themedir          %{_localstatedir}/lib/%{name}/themes
%%vdr_epgimagesdir      %{_var}/cache/%{name}/epgimages

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
    if grep -q "^install:" Makefile; then \\
        %%makeinstall_std \\
    fi \\
    rename .so.%%{vdr_version} .so.%%{vdr_apiversion} *.so.%%{vdr_version} &>/dev/null || : \\
    for f in libvdr-*.so.%%{vdr_apiversion}; do \\
        [ -e "\$f" ] || continue \\
        install -D -m755 \$f %%{buildroot}%%{vdr_plugin_dir}/\$f \\
        install -d -m755 %%{buildroot}%%{_datadir} \\
        [ -d locale ] && cp -r locale %%{buildroot}%%{_datadir} \\
    done \\
    for f in %%{buildroot}%%{vdr_plugin_dir}/libvdr-*.so.%%{vdr_apiversion}; do \\
        NAME=\$(echo \$f | perl -pe "s/^.*libvdr-(.*).so.%%{vdr_apiversion}/\\\\1/") \\
        echo %%{vdr_plugin_dir}/\$(basename "\$f") > \$NAME.vdr \\
        %%find_lang vdr-\$NAME || touch $NAME.lang \\
        cat vdr-\$NAME.lang >> \$NAME.vdr \\
        if [ -f "\$NAME.rpm-params" ]; then \\
            install -D -m644 \$NAME.rpm-defaults %%{buildroot}%%{vdr_plugin_paramdir}/\$NAME.defaults \\
            install -D -m644 \$NAME.rpm-params %%{buildroot}%%{vdr_plugin_paramdir}/\$NAME.params \\
            install -D -m644 \$NAME.rpm-sysconfig %%{buildroot}%%{_sysconfdir}/sysconfig/vdr-\$NAME \\
            echo "%%config(noreplace) %%{_sysconfdir}/sysconfig/vdr-\$NAME" >> \$NAME.vdr \\
            echo "%%{vdr_plugin_paramdir}/\$NAME.defaults" >> \$NAME.vdr \\
            echo "%%{vdr_plugin_paramdir}/\$NAME.params" >> \$NAME.vdr \\
        fi \\
    done \\
    if [ -e "%%{buildroot}%%{vdr_cfgdir}/themes" ]; then \\
        mv "%%{buildroot}%%{vdr_cfgdir}/themes" "%%{buildroot}%%{vdr_themedir}" \\
    fi

%%vdr_chanlogo_notice This skin is able to display channel logos. In order to use this \\
functionality, channel logos must be put in %%{vdr_chanlogodir}. The \\
recommended format is 64x48px 16-color xpm. When using dxr3 as the \\
output device, the recommended maximum number of colors is 6.

%%vdr_plugin_params_begin() \\
vdr_plugin_params_do() { \\
	vdr_plugin_params_handle() { \\
		if echo "\$gotparam" | grep -q "\$gotvar"; then \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.rpm-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.rpm-sysconfig \\
			gotparam="\$(echo "\$gotparam" | sed "s/\$gotvar/'\\\\\$\$gotvar'/")" \\
			echo "[ -n \\\\"\\\\\$\$gotvar\\\\" ] && echo \\\\"\$gotparam\\\\"" >> %%1.rpm-params \\
		elif echo "\$gotparam" | grep -q "MULTIPLE_PARAMS"; then \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.rpm-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.rpm-sysconfig \\
			echo "local gotparam=\\\\"\$gotparam\\\\"" >> %%1.rpm-params \\
			echo "echo \\\\"\\\\\$\$gotvar\\\\" | xargs -n1 | while read subvar &&" >> %%1.rpm-params \\
			echo "	[ -n \\\\"\\\\\$subvar\\\\" ]; do" >> %%1.rpm-params \\
			echo "	echo \\\\"\\\\\$gotparam\\\\" | sed \\\\"s/MULTIPLE_PARAMS/'\\\\\$subvar'/\\\\"" >> %%1.rpm-params \\
			echo "done" >> %%1.rpm-params \\
		else \\
			[ -z "\$gotdefault" ] && gotdefault=no \\
			echo "local \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.rpm-defaults \\
			echo "# \$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.rpm-sysconfig \\
			echo "[ \\\\"\\\\\$\$gotvar\\\\" = \\\\"yes\\\\" ] && echo \\\\"\$gotparam\\\\"" >> %%1.rpm-params \\
		fi \\
		echo >> %%1.rpm-sysconfig \\
		gotvar= \\
		gotparam= \\
		gotdefault= \\
	} \\
	local gotvar= \\
	local gotparam= \\
	local gotdefault= \\
	echo "# Do not modify this file, use %%{_sysconfdir}/sysconfig/%{name}-%%1 instead" > %%1.rpm-defaults \\
	echo "# Do not modify this file, use %%{_sysconfdir}/sysconfig/%{name}-%%1 instead" > %%1.rpm-params \\
	echo "# VDR plugin %%1 configuration" > %%1.rpm-sysconfig \\
	echo >> %%1.rpm-sysconfig \\
	echo "# You can also define the plugin arguments manually by using the" >> %%1.rpm-sysconfig \\
	echo "# VDR_PLUGIN_ARGS variable below. Note that setting VDR_PLUGIN_ARGS will" >> %%1.rpm-sysconfig \\
	echo "# override all the other settings in this file and that setting" >> %%1.rpm-sysconfig \\
	echo "# VDR_PLUGIN_ARGS_%%1 in the main VDR sysconfig file will" >> %%1.rpm-sysconfig \\
	echo "# override this file completely." >> %%1.rpm-sysconfig \\
	echo "# VDR_PLUGIN_ARGS=\\\\"\\\\"" >> %%1.rpm-sysconfig \\
	echo >> %%1.rpm-sysconfig \\
	while read INPUT; do \\
		if [ -z "\$INPUT" ]; then \\
			continue \\
		fi \\
		if echo "\$INPUT" | grep -q '^#'; then \\
			[ -n "\$gotvar" ] && [ -n "\$gotparam" ] && vdr_plugin_params_handle \\
			echo "\$INPUT" >> %%1.rpm-sysconfig \\
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

%%vdr_plugin_post() %%{nil}
%%vdr_plugin_postun() %%{nil}
EOF

%build
%make vdr i18n CC=%{__cc} CXX=%{__cxx}

%define vdr_plugin_ldflags %(echo "%{?ldflags}" | sed 's@-Wl,--no-undefined@@')
# [a-z] does not match v,w on fi_FI.ISO-8859-15, TODO: patch to use [[:lower:]]
LC_ALL=C %make plugins CC=%{__cc} CXX=%{__cxx} \
	CFLAGS="%{optflags} %vdr_plugin_flags -I%{_includedir}/ncursesw %vdr_plugin_ldflags" \
	CXXFLAGS="%{optflags} %vdr_plugin_flags -I%{_includedir}/ncursesw %vdr_plugin_ldflags"

%install
%makeinstall_std

rm -f %{buildroot}%{vdr_cfgdir}/channels.conf

install -d -m755 %{buildroot}%{vdr_plugin_datadir}
install -d -m755 %{buildroot}%{vdr_chanlogodir}
install -d -m755 %{buildroot}%{vdr_themedir}
ln -s %{vdr_themedir} %{buildroot}%{vdr_cfgdir}/themes

# included by plugin makefiles, in includedir because plugin makefiles
# may use $(VDRDIR) for both Make.global and grepping VDR headers:
install -m644 Make.global %{buildroot}%{_includedir}/%{name}

# required at least by sc:
install -d -m755 %{buildroot}%{_includedir}/%{name}/dvb{sd,hd}device/
install -m644 PLUGINS/src/dvbsddevice/dvbsdffdevice.h %{buildroot}%{_includedir}/%{name}/dvbsddevice/
install -m644 PLUGINS/src/dvbhddevice/dvbhdffdevice.h %{buildroot}%{_includedir}/%{name}/dvbhddevice/
# deps of dvbhdffdevice.h:
install -m644 PLUGINS/src/dvbhddevice/hdffcmd.h %{buildroot}%{_includedir}/%{name}/dvbhddevice/
install -d -m755 %{buildroot}%{_includedir}/%{name}/dvbhddevice/libhdffcmd
install -m644 PLUGINS/src/dvbhddevice/libhdffcmd/hdffcmd*.h %{buildroot}%{_includedir}/%{name}/dvbhddevice/libhdffcmd/

install -d -m755 %{buildroot}%{_sysconfdir}/rpm/macros.d
install -m644 vdr.macros %{buildroot}%{_sysconfdir}/rpm/macros.d

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}

install -d -m755 %{buildroot}%{vdr_plugin_paramdir}
install -d -m755 %{buildroot}%{vdr_epgimagesdir}

# init stuff
install -d -m755 %{buildroot}%{_unitdir}
install -d -m755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m755 %{buildroot}%{_datadir}/%{name}
install -m755 %{SOURCE11} %{buildroot}%{_unitdir}/vdr.service
install -m755 %{SOURCE2} %{buildroot}%{_bindir}/runvdr
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m755 %{SOURCE10} %{buildroot}%{_datadir}/%{name}/plugin-update.sh


# fix locales
for dir in %{buildroot}%{_datadir}/locale/*_*; do
	[ $(basename $dir) == "zh_CN" ] && continue
	# VDR wrongly uses the _COUNTRY identification always
	rm -rf ${dir%_*}
	mv $dir ${dir%_*}
done

# pictures plugin
install -m755 PLUGINS/src/pictures/pic2mpg{,-sd} %{buildroot}%{_bindir}
# We don't have the nice %%vdr_plugin_params_begin available yet, so hardcode..:
cat > %{buildroot}%{vdr_plugin_paramdir}/pictures.defaults <<EOF
# Do not modify this file, use /etc/sysconfig/vdr-pictures instead
local DIR=""
EOF
cat > %{buildroot}%{vdr_plugin_paramdir}/pictures.params <<EOF
# Do not modify this file, use /etc/sysconfig/vdr-pictures instead
[ -n "\$DIR" ] && echo "--remote='\$DIR'"
EOF
cat > %{buildroot}%{_sysconfdir}/sysconfig/vdr-pictures <<EOF
# VDR plugin pictures configuration

# Set a custom picture directory
# DIR=""
EOF

# dvbsddevice
# We don't have the nice %%vdr_plugin_params_begin available yet, so hardcode..:
cat > %{buildroot}%{vdr_plugin_paramdir}/dvbsddevice.defaults <<EOF
# Do not modify this file, use /etc/sysconfig/vdr-dvbsddevice instead
local OUTPUT_ONLY=""
EOF
cat > %{buildroot}%{vdr_plugin_paramdir}/dvbsddevice.params <<EOF
# Do not modify this file, use /etc/sysconfig/vdr-dvbsddevice instead
[ "\$OUTPUT_ONLY" = "yes" ] && echo "-o"
EOF
cat > %{buildroot}%{_sysconfdir}/sysconfig/vdr-dvbsddevice <<EOF
# VDR plugin dvbsddevice configuration

# Use the device as output device only
# OUTPUT_ONLY="no"
EOF

# rcu
# We don't have the nice %%vdr_plugin_params_begin available yet, so hardcode..:
cat > %{buildroot}%{vdr_plugin_paramdir}/rcu.defaults <<EOF
# Do not modify this file, use /etc/sysconfig/vdr-rcu instead
local DEVICE=""
EOF
cat > %{buildroot}%{vdr_plugin_paramdir}/rcu.params <<EOF
# Do not modify this file, use /etc/sysconfig/vdr-rcu instead
[ -n "\$DEVICE" ] && echo "--device='\$DEVICE'"
EOF
cat > %{buildroot}%{_sysconfdir}/sysconfig/vdr-rcu <<EOF
# VDR plugin rcu configuration

# Set the serial device to be used (default: /dev/ttyS1).
# Note that the vdr user has to have proper permissions to it.
# DEVICE=""
EOF

# scripts
install -m755 epg2html summary2info %{buildroot}%{_bindir}

# automatic plugin post and postun actions
install -d -m755 %{buildroot}%{_var}/lib/rpm/filetriggers
install -m755 %{SOURCE8} %{buildroot}%{_var}/lib/rpm/filetriggers/vdr-plugins.script
echo "^.%{vdr_plugin_dir}/libvdr-.*\.so\." > %{buildroot}%{_var}/lib/rpm/filetriggers/vdr-plugins.filter

%find_lang vdr
%find_lang vdr-dvbhddevice
%find_lang vdr-hello
%find_lang vdr-skincurses
%find_lang vdr-pictures

