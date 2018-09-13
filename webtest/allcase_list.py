# coding=utf-8
from test_case.start_address import start_address
from test_case.start_admin_config import start_admin_config
from test_case.start_alarm import start_alarm
from test_case.start_area import start_area
from test_case.start_dhcp import start_dhcp
from test_case.start_interface import start_interface
from test_case.start_log import start_log
from test_case.start_map66 import start_map66
from test_case.start_nat import start_nat
from test_case.start_pf import start_pf
from test_case.start_resource_monitor import start_resource_monitor
from test_case.start_Route import start_Route
from test_case.start_server import start_server
from test_case.start_service import start_service
from test_case.start_snmp import start_snmp
from test_case.start_system_config import start_system_config
from test_case.start_system_set import start_system_set
from test_case.start_time import start_time
from test_case.start_user_manage import start_user_manage
from test_case.start_vif import start_vif
from test_case.start_vlan import start_vlan
from test_case.start_vsys import start_vsys

# 获取测试用例列表，用例执行时会按照列表中的顺序来执行
def caselist():
    alltestnames = [
        start_admin_config.ADMIN_CONFIG,
        start_user_manage.USER_MANAGE,
        start_system_set.SYSTEM_SET,
        start_resource_monitor.MONITOR,
        start_snmp.SNMP,
        start_log.LOG,
        start_interface.INTERFACE,
        start_vlan.VLAN,
        start_Route.ROUTE,
        start_vif.VIF,
        start_pf.PF,
        start_area.AREA,
        start_address.ADDRESS,
        start_time.TIME,
        start_service.SERVICE,
        start_server.SERVER,
        start_nat.NAT,
        start_map66.MAP66,
        start_dhcp.DHCP,
        start_alarm.ALARM,
        start_vsys.VSYS,
        start_system_config.SYSTEM_CONFIG,

        ]

    return alltestnames
