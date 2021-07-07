expected_output = {
    "Vlan355": {
        "directed_broadcast": "disabled",
        "icmp_port_unreachable": "enabled",
        "icmp_redirects": "enabled",
        "icmp_unreachable": "disabled",
        "int_stat_last_reset": "never",
        "interface_status": "protocol-up/link-up/admin-up",
        "iod": 2,
        "ip_forwarding": "disabled",
        "ip_mtu": 9216,
        "ipv4": {
            "10.170.153.133/28": {
                "broadcast_address": "255.255.255.255",
                "ip": "10.170.153.133",
                "ip_subnet": "10.170.153.128",
                "prefix_length": "28",
                "route_preference": "0",
                "route_tag": "0",
                "secondary": False,
            },
            "counters": {
                "broadcast_bytes_consumed": 0,
                "broadcast_bytes_forwarded": 0,
                "broadcast_bytes_originated": 0,
                "broadcast_bytes_received": 0,
                "broadcast_bytes_sent": 0,
                "broadcast_packets_consumed": 0,
                "broadcast_packets_forwarded": 0,
                "broadcast_packets_originated": 0,
                "broadcast_packets_received": 0,
                "broadcast_packets_sent": 0,
                "labeled_bytes_consumed": 0,
                "labeled_bytes_forwarded": 0,
                "labeled_bytes_originated": 0,
                "labeled_bytes_received": 0,
                "labeled_bytes_sent": 0,
                "labeled_packets_consumed": 0,
                "labeled_packets_forwarded": 0,
                "labeled_packets_originated": 0,
                "labeled_packets_received": 0,
                "labeled_packets_sent": 0,
                "multicast_bytes_consumed": 0,
                "multicast_bytes_forwarded": 0,
                "multicast_bytes_originated": 0,
                "multicast_bytes_received": 5070291600,
                "multicast_bytes_sent": 0,
                "multicast_packets_consumed": 0,
                "multicast_packets_forwarded": 0,
                "multicast_packets_originated": 0,
                "multicast_packets_received": 50702916,
                "multicast_packets_sent": 0,
                "unicast_bytes_consumed": 691502626,
                "unicast_bytes_forwarded": 0,
                "unicast_bytes_originated": 1012679263,
                "unicast_bytes_received": 691502626,
                "unicast_bytes_sent": 1012679263,
                "unicast_packets_consumed": 5436721,
                "unicast_packets_forwarded": 0,
                "unicast_packets_originated": 5498120,
                "unicast_packets_received": 5436721,
                "unicast_packets_sent": 5498120,
            },
        },
        "load_sharing": "none",
        "local_proxy_arp": "disabled",
        "multicast_groups_address": "none",
        "multicast_routing": "disabled",
        "proxy_arp": "disabled",
        "unicast_reverse_path": "none",
        "vrf": "default",
        "wccp_redirect_exclude": "disabled",
        "wccp_redirect_inbound": "disabled",
        "wccp_redirect_outbound": "disabled",
    },
}