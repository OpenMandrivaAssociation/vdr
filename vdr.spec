
%define name	vdr
%define version	1.4.7
%define maintpatch 0
%define apiversion 1.4.5
%define rel	8

# Increased when ABI compatibility is broken by patches
# Reset to 1 when %apiversion is raised
%define vdr_sub_abi 6
%define vdr_abi	%{apiversion}_%{_lib}_abi_%{vdr_sub_abi}

%define subtitles_version	0.5.0
%define ttxtsubs_version	0.0.5
%define liemikuutio_version 	1.13
%define jumpplay_version	0.9
%define submenu_version		0.7
%define timerinfo_version	0.4
%define cmdsubmenu_version	0.7

%define vdr_plugin_dir		%{_libdir}/%{name}
%define vdr_plugin_datadir	%{vdr_datadir}
%define vdr_plugin_cfgdir	%{vdr_cfgdir}/plugins
%define vdr_plugin_paramdir	%{vdr_datadir}/defaults
%define vdr_plugin_cachedir	%{_var}/cache/%{name}
%define vdr_videodir		%{_localstatedir}/%{name}/video
%define vdr_cfgdir		%{_localstatedir}/%{name}/config
%define	vdr_datadir		%{_datadir}/%{name}
%define vdr_chanlogodir		%{vdr_datadir}/chanlogos
%define vdr_themedir		%{_localstatedir}/%{name}/themes
%define vdr_epgimagesdir	%{_var}/cache/%{name}/epgimages

%define vdr_plugin_flags	%{optflags} -fPIC

Summary:	Video Disk Recorder - PVR software
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.cadsoft.de/vdr/
Source:		ftp://ftp.cadsoft.de/vdr/%{name}-%{version}.tar.bz2

Source1:	vdr.init
Source2:	vdr-runvdr
Source3:	vdr-shutdown.sh.example
Source4:	vdr.sysconfig
Source5:	vdr-sky.cron
Source6:	vdr-sky.sysconfig
Source7:	vdr-README.mdv

# Patches last checked for updates: 2007/10/29

Patch1:		vdr-translationerror-only-when-debug.patch
Patch2:		vdr-maxdevices.diff
Patch3:		vdr-1.4.2-getdevice.diff
Patch4:		vdr-1.4.6-rsvps.patch

# From http://users.tkk.fi/~rahrenbe/vdr/
# and http://www.saunalahti.fi/~rahrenbe/vdr/patches/
# Updated with each version, gunzipped
# Note that they are usually just rediffed, no actual changes
Patch11:	vdr-1.4.7-subtitles-%subtitles_version-and-ttxtsubs-%ttxtsubs_version.diff
Patch12:	vdr-1.4.5-liemikuutio-%liemikuutio_version.diff

# From iptv
Patch16:	vdr-1.4.7-closefilter.patch
Patch17:	vdr-1.4.7-pluginparam.patch

# From http://e-tobi.net/ Debian repository
Patch20:	vdr-1.4.0-analogtv.patch
Patch21:	vdr-sort-options.patch
Patch22:	vdr-1.4.1-dd-record-option.patch

# From http://www.hoochvdr.info/modules.php?name=Forums&file=index
# http://www.hoochvdr.info/files/vdr-%version-core-yaepg.diff
Patch30:	http://www.hoochvdr.info/files/vdr-1.4.0-core-yaepg.diff

# From graphtft
Patch32:	vdr-1.4.3.plain-menu-column.diff

# From http://www.lötzke.de/dvb/VDR_LNB_sharing_patch/
# Context slightly modified to resolve conflicts
Patch34:	configurableLNBshare-VDR_1.4.3.mod.patch

# From VDR mailinglist
# Context slightly modified to resolve conflicts
Patch36:	SourceCaps-1.3.39.mod.patch

# From rotor plugin
Patch40:	vdr-1.3.45-Rotor.diff

# From noepgmenu
# Context slightly modified to resolve conflicts
Patch42:	vdr-1.3.41-noepgmenu.mod.patch

# From decruft
Patch45:	vdr-1.3.20-SetGroupSep.diff

# From reelchannelscan
Patch47:	channelscan-vdr.patch

# From http://toms-cafe.de/vdr/download/
# Context slightly modified to resolve conflicts
Patch50:	http://toms-cafe.de/vdr/download/vdr-jumpplay-%jumpplay_version-1.4.0.mod.diff
Patch51:	http://toms-cafe.de/vdr/download/vdr-submenu-%submenu_version-1.3.38+.diff
Patch52:	http://toms-cafe.de/vdr/download/vdr-timer-info-%timerinfo_version-1.3.45.mod.diff
Patch53:	http://toms-cafe.de/vdr/download/vdr-cmdsubmenu-%cmdsubmenu_version-1.4.0.diff

# From xineliboutput
Patch56:	vdr-1.4.6-Smooth_FastForward.patch

# From pin
# Context modified to resolve conflicts
# Added check for pin plugin existence before showing pin-specific options
# in timer screen.
Patch58:	vdr-1.4.5-pin.mod.diff

# Hooks that allow plugins to do stuff instead of unconditionally patching
# the default VDR behaviour
Patch60:	vdr-1.4.3-exthooks.patch

# From sc
Patch63:	vdr-1.4.x-sc7.diff

# From epgsearch
Patch65:	MainMenuHooks-v1_0.patch

# http://phivdr.dyndns.org/vdr/.h264/
# Conflicts resolved
Patch67:	vdr-1.4.7-v2-h264.patch

%if %maintpatch
%(for n in {1..%maintpatch}; do
	echo "Patch7$n: ftp://ftp.cadsoft.de/vdr/Developer/vdr-%version-$n.diff"
done)
%endif

BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libcap-devel libjpeg-devel ncurses-devel
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(post):	vdr-common = %{version}
Requires:	vdr-common = %{version}
Provides:	vdr-abi = %{vdr_abi}
Provides:	vdr-core-standard vdr-core-vanilla vdr-core-bigpatch
Obsoletes:	vdr-core-standard vdr-core-vanilla vdr-core-bigpatch
Requires(post):	ccp >= 0.4.1
# Plugins:
Requires:	ccp >= 0.4.1

%description
VDR (Video Disk Recorder) is a very powerful and customizable PVR
program. One of the most common usage cases of VDR is as a digital
set-top-box with the picture displayed on a television set. VDR can
also be used on desktop or even without any video output devices.
There are also lots of different plugins available to extend VDR's
capabilities.

See http://www.linuxtv.org/vdrwiki/ for more information.

VDR in this package is patched with the patches known as
liemikuutio, sort-options, dd-record-option, configurableLNBshare,
sourcecaps, jumpplay, submenu, timer-info, cmdsubmenu, and with
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
VDR (Video Disc Recorder) is a very powerful and customizable PVR
software.

This package contains the default "vdr" user required by VDR and
some other related tools.

%package devel
Summary:	VDR development headers
Group:		Development/C++

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

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch11 -p1
%patch12 -p1
%patch16 -p1
%patch17 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch30 -p1
%patch32 -p2
%patch34 -p1
%patch36 -p1
%patch40 -p1
%patch42 -p1
%patch45 -p1
%patch47 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch56 -p1
%patch58 -p2
%patch60 -p1
%patch63 -p1
%patch65 -p1
%patch67 -p1

%if %maintpatch
%(for n in {1..%maintpatch}; do
	echo "%%patch7$n -p1"
done)
%endif

sed -i "/isyslog(\"VDR version %%s started\", VDRVERSION);/s/VDRVERSION/\0 \" (%version-%release)\"/" vdr.c

# check that the %apiversion is set correctly
[ $(sed -rn '/define APIVERSION/s/^.*"(.*)".*$/\1/p' config.h) == %apiversion ]

cp -a %SOURCE3 shutdown.sh.example

cat %SOURCE7 | sed 's,@vdr_plugin_dir@,%{vdr_plugin_dir},' > README.mdv

# Comment default examples out
perl -pi -e "s/^S/# S/" diseqc.conf

cat > Make.config <<EOF
CFLAGS   = %optflags
CXXFLAGS = %optflags

BINDIR   = %{_bindir}
MANDIR   = %{_mandir}

PLUGINLIBDIR = %{vdr_plugin_dir}
VIDEODIR = %{vdr_videodir}
LIBDIR = .
EOF

## TODO: move this out of .spec
cat > vdr.macros <<EOF
## VDR plugin macros ##

%if %maintpatch
%%vdr_version		%version-%maintpatch
%else
%%vdr_version		%version
%endif
%%vdr_rpmversion	%version
%%vdr_apiversion	%apiversion
%%vdr_abi		%vdr_abi

%%vdr_plugin_flags	%vdr_plugin_flags
%%vdr_add_optflags	%%nil

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

%%vdr_plugin_build \\
    %%make all							\\\\\\
    CFLAGS="%%vdr_plugin_flags %%vdr_add_optflags"		\\\\\\
    CXXFLAGS="%%vdr_plugin_flags %%vdr_add_optflags"		\\\\\\
    PLUGINLIBDIR=%%{_vdr_plugin_dir}				\\\\\\
    VIDEODIR=%%{_vdr_videodir}					\\\\\\
    LIBDIR=.							\\\\\\
    LOCALEDIR=locale						\\\\\\
    DVBDIR=%%{_prefix}						\\\\\\
    VDRDIR=%{_includedir}/vdr					\\\\\\
    VDRVERSION=%%{vdr_version}					\\\\\\
    VDRVERSNUM=%%(echo %%{vdr_rpmversion} |			\\\\\\
        %__awk -F'.' '{ print \$1*10000+\$2*100+\$3 }')		\\\\\\
    APIVERSION=%%{vdr_apiversion}				\\\\\\
    APIVERSNUM=%%(echo %%{vdr_apiversion} |			\\\\\\
        %__awk -F'.' '{ print \$1*10000+\$2*100+\$3 }')

%%vdr_plugin_install \\
    rename .so.%%{vdr_version} .so.%%{vdr_apiversion} *.so.%%{vdr_version} &>/dev/null || : \\
    for f in libvdr-*.so.%%{vdr_apiversion}; do \\
        install -D -m755 \$f %%{buildroot}%%{_vdr_plugin_dir}/\$f \\
        NAME=\$(echo \$f | perl -pe "s/^libvdr-(.*).so.%%{vdr_apiversion}/\\\\1/") \\
        echo %%{_vdr_plugin_dir}/\$f > \$NAME.vdr \\
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
		else \\
			[ -z "\$gotdefault" ] && gotdefault=no \\
			echo "\$gotvar=\\\\"\$gotdefault\\\\"" >> %%1.mandriva-defaults \\
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
	I=0 \\
	while read INPUT; do \\
		[ \$I == 0 ] && INPUT="\${INPUT#VDR_PLUGIN_PARAMS_BEGIN}" && I=1 \\
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
VDR_PLUGIN_PARAMS_BEGIN

%%vdr_plugin_params_end VDR_PLUGIN_PARAMS_EOF

%%vdr_plugin_post() if [ "\$1" = "1" ] && [ -e %{_initrddir}/%{name} ]; then /sbin/service vdr plugin_install %%1; fi
%%vdr_plugin_postun() if [ -e %{_initrddir}/%{name} ]; then if [ "\$1" = "0" ]; then /sbin/service vdr plugin_remove %%1; else /sbin/service vdr plugin_upgrade %%1; fi; fi

EOF

# Local version of the above post and postun:
%define plugin_rpmscripts() \
%post plugin-%{1} \
if [ "$1" = "1" ] && [ -e %{_initrddir}/%{name} ]; then /sbin/service vdr plugin_install %{1}; fi \
%postun plugin-%{1} \
if [ -e %{_initrddir}/%{name} ]; then if [ "$1" = "0" ]; then /sbin/service vdr plugin_remove %{1}; else /sbin/service vdr plugin_upgrade %{1}; fi; fi

%build
%make
# [a-z] does not match v,w on fi_FI.ISO-8859-15, TODO: patch to use [[:lower:]]
LC_ALL=C %make plugins CFLAGS="%vdr_plugin_flags" CXXFLAGS="%vdr_plugin_flags"

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

# scripts
install -m755 *.pl %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%pre common
%_pre_useradd vdr %{_localstatedir}/%{name} /bin/nologin
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

# post and postun
%plugin_rpmscripts hello
%plugin_rpmscripts osddemo
%plugin_rpmscripts skincurses
%plugin_rpmscripts sky
%plugin_rpmscripts status
%plugin_rpmscripts servicedemo
%plugin_rpmscripts svdrpdemo

%files
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

%files common
%defattr(-,root,root)
%attr(-,vdr,vdr) %dir %{_localstatedir}/%{name}

%files devel
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.d/vdr.macros
%{_includedir}/vdr
%{_includedir}/libsi

%files plugin-hello
%defattr(-,root,root)
%doc PLUGINS/src/hello/HISTORY
%doc PLUGINS/src/hello/README
%{vdr_plugin_dir}/libvdr-hello.so.%{apiversion}

%files plugin-osddemo
%defattr(-,root,root)
%doc PLUGINS/src/osddemo/HISTORY
%doc PLUGINS/src/osddemo/README
%{vdr_plugin_dir}/libvdr-osddemo.so.%{apiversion}

%files plugin-skincurses
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
