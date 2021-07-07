expected_output = {
        'legend': 'pp = Partially Programmed.',
        'bridge_group': {
            'midlay': {
                'bridge_domain': {
                    'bd601': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'BVI',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'disabled',
                        'igmp_snooping_profile': 'none',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'disabled',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '1',
                        'p2mp_pw': 'disabled',
                        'create_time': '11/07/2019 13:01:43 (13w4d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 0,
                            'interfaces': {
                                'BVI601': {
                                    'state': 'down (Segment-down)',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x8000000d',
                                    'interworking': 'none',
                                    'error': 'Need at least 1 bridge port up',
                                    'bvi_mac_address': ['00c1.64ff.f53f'],
                                    'split_horizon_group': 'Access',
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'access_pw': {
                            'EVPN': {
                                'neighbor': {
                                    '0.0.0.0': {
                                        'pw_id': {
                                            'evi 601': {
                                                'ac_id': '1',
                                                'state': 'down ( local ready ) (Transport LSP Down)',
                                                'xc_id': '0xa0000009',
                                                'encapsulation': 'MPLS',
                                                'source_address': '10.154.219.85',
                                                'encap_type': 'Ethernet',
                                                'control_word': 'enabled',
                                                'sequencing': 'not set',
                                                'lsp': {
                                                    'state': 'Up',
                                                    'evpn': {
                                                        'label': {
                                                            'local': '100482',
                                                            'remote': 'unknown',
                                                        },
                                                        'mtu': {
                                                            'local': '1500',
                                                            'remote': 'unknown',
                                                        },
                                                        'control_word': {
                                                            'local': 'enabled',
                                                            'remote': 'unknown',
                                                        },
                                                        'ac_id': {
                                                            'local': '1',
                                                            'remote': '1',
                                                        },
                                                        'evpn_type': {
                                                            'local': 'Ethernet',
                                                            'remote': 'unknown',
                                                        },
                                                    },
                                                },
                                                'create_time': '11/07/2019 13:01:43 (13w4d ago)',
                                                'last_time_status_changed': '11/07/2019 13:06:41 (13w4d ago)',
                                                'mac_withdraw_message': {
                                                    'send': 0,
                                                    'receive': 0,
                                                },
                                                'forward_class': '0',
                                                'mac_learning': 'enabled',
                                                'flooding': {
                                                    'broadcast_multicast': 'enabled',
                                                    'unknown_unicast': 'enabled',
                                                },
                                                'mac_aging_time': 300,
                                                'mac_aging_type': 'inactivity',
                                                'mac_limit': 4000,
                                                'mac_limit_action': 'none',
                                                'mac_limit_notification': 'syslog',
                                                'mac_limit_reached': 'no',
                                                'mac_limit_threshold': '75%',
                                                'mac_port_down_flush': 'enabled',
                                                'mac_secure': 'disabled',
                                                'mac_secure_logging': 'disabled',
                                                'split_horizon_group': 'none',
                                                'dhcp_v4_snooping': 'disabled',
                                                'dhcp_v4_snooping_profile': 'none',
                                                'igmp_snooping': 'disabled',
                                                'igmp_snooping_profile': 'none',
                                                'mld_snooping_profile': 'none',
                                                'storm_control': 'bridge-domain policer',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'EVPN-Mulicast': {
                'bridge_domain': {
                    'EVPN-Multicast-Genie': {
                        'state': 'up',
                        'id': 1,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'EVPN-IRB',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'disabled',
                        'igmp_snooping_profile': 'none',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'bridge-domain policer',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '2',
                        'p2mp_pw': 'disabled',
                        'create_time': '11/07/2019 13:01:43 (13w4d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 3,
                            'num_ac_up': 0,
                            'interfaces': {
                                'BVI100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x8000000b',
                                    'interworking': 'none',
                                    'error': 'Need at least 1 bridge port up',
                                    'bvi_mac_address': ['1000.10ff.1000'],
                                    'split_horizon_group': 'Access',
                                },
                                'Bundle-Ether3.100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xc0000004',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                },
                                'Bundle-Ether4.100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xc0000006',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 0,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'evpn': {
                            'EVPN': {
                                'state': 'up',
                                'evi': '1000',
                                'xc_id': '0x80000007',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 10305221406,
                                        'send': 41020743245,
                                    },
                                    'byte_totals': {
                                        'receive': 10474510995022,
                                        'send': 41841158015034,
                                    },
                                    'mac_move': '0',
                                },
                            },
                        },
                    },
                },
            },
        },
    }