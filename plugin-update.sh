#!/bin/sh

DAEMONNAME="vdr"
RUNVDRNAME="runvdr"
RETVAL=0

# Get config.
VDR_PLUGINS="any"
VDR_RESTART_ON_INSTALL=no
VDR_RESTART_ON_REMOVE=no
VDR_RESTART_ON_UPGRADE=yes
. /etc/sysconfig/vdr

run_ccp_for_plugin() {
	PLUGIN="$1"
	if test -e /etc/sysconfig/vdr-$PLUGIN.rpmnew && test -e /etc/sysconfig/vdr-$PLUGIN && \
			test $(stat -c%Z /etc/sysconfig/vdr-$PLUGIN.rpmnew) -gt $(stat -c%Z /etc/sysconfig/vdr-$PLUGIN); then
		ccp --backup --delete --ifexists --set NoOrphans --oldfile \
			/etc/sysconfig/vdr-$PLUGIN --newfile /etc/sysconfig/vdr-$PLUGIN.rpmnew
	fi
}

case "$1" in
  plugins_changed)
  	restart_vdr_plugins=
	while [ -n "$2" ] && [ -n "$3" ]; do
		case "$2" in
		  --install)
			run_ccp_for_plugin $3
			[ "$VDR_RESTART_ON_INSTALL" = "yes" ] && restart_vdr_plugins="$restart_vdr_plugins $3"
			break
			;;
		  --upgrade)
			run_ccp_for_plugin $3
			[ "$VDR_RESTART_ON_UPGRADE" = "yes" ] && restart_vdr_plugins="$restart_vdr_plugins $3"
			break
			;;
		  --remove)
			[ "$VDR_RESTART_ON_REMOVE" = "yes" ] && restart_vdr_plugins="$restart_vdr_plugins $3"
		esac
		shift 2
	done

	for plugin in $restart_vdr_plugins; do
		case " $VDR_PLUGINS " in *" $plugin "*|*" any "*)
		  	systemctl try-restart vdr.service
			break 2
		esac
	done
  	;;
  *)
  	echo "Not intended for manual use."
  	exit 1
esac

exit $RETVAL
