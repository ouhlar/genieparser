expected_output ={
   "address_family":{
      "ipv4":{
         "instance":{
            "1":{
               "areas":{
                  "0.0.0.0":{
                     "interfaces":{
                        "Loopback0":{
                           "router_id":"10.4.1.1",
                           "interface_type":"loopback",
                           "cost":1,
                           "demand_circuit":False,
                           "bfd":{
                              "enable":False
                           },
                           "name":"Loopback0",
                           "ip_address":"10.4.1.1/32",
                           "interface_id":11,
                           "attached":"interface enable",
                           "enable":True,
                           "line_protocol":True,
                           "topology":{
                              0:{
                                 "cost":1,
                                 "name":"Base",
                                 "disabled":False,
                                 "shutdown":False
                              }
                           },
                           "if_cfg":True,
                           "stub_host":True
                        },
                        "GigabitEthernet2":{
                           "router_id":"10.4.1.1",
                           "interface_type":"broadcast",
                           "cost":1,
                           "demand_circuit":False,
                           "bfd":{
                              "enable":False
                           },
                           "name":"GigabitEthernet2",
                           "ip_address":"10.1.2.1/24",
                           "interface_id":8,
                           "attached":"interface enable",
                           "enable":True,
                           "line_protocol":True,
                           "topology":{
                              0:{
                                 "cost":1,
                                 "name":"Base",
                                 "disabled":False,
                                 "shutdown":False
                              }
                           },
                           "if_cfg":True,
                           "transmit_delay":1,
                           "state":"dr",
                           "priority":1,
                           "dr_router_id":"10.4.1.1",
                           "dr_ip_addr":"10.1.2.1",
                           "bdr_router_id":"10.16.2.2",
                           "bdr_ip_addr":"10.1.2.2",
                           "hello_interval":10,
                           "dead_interval":40,
                           "wait_interval":40,
                           "retransmit_interval":5,
                           "oob_resync_timeout":40,
                           "passive":False,
                           "hello_timer":"00:00:05",
                           "lls":True,
                           "graceful_restart":{
                              "cisco":{
                                 "type":"cisco",
                                 "helper":True
                              },
                              "ietf":{
                                 "type":"ietf",
                                 "helper":True
                              }
                           },
                           "prefix_suppression":True,
                           "ipfrr_protected":True,
                           "ipfrr_candidate":True,
                           "ti_lfa_protected":False,
                           "index":"1/3/3",
                           "flood_queue_length":0,
                           "next":"0x0(0)/0x0(0)/0x0(0)",
                           "last_flood_scan_length":1,
                           "max_flood_scan_length":3,
                           "last_flood_scan_time_msec":0,
                           "max_flood_scan_time_msec":1,
                           "authentication":{
                              "auth_trailer_key":{
                                 "crypto_algorithm":"simple"
                              }
                           },
                           "statistics":{
                              "nbr_count":1,
                              "adj_nbr_count":1,
                              "num_nbrs_suppress_hello":0
                           },
                           "neighbors":{
                              "10.16.2.2":{
                                 "bdr_router_id":"10.16.2.2"
                              }
                           }
                        },
                        "GigabitEthernet1":{
                           "router_id":"10.4.1.1",
                           "interface_type":"broadcast",
                           "cost":1,
                           "demand_circuit":False,
                           "bfd":{
                              "enable":False
                           },
                           "name":"GigabitEthernet1",
                           "ip_address":"10.1.4.1/24",
                           "interface_id":7,
                           "attached":"interface enable",
                           "enable":True,
                           "line_protocol":True,
                           "topology":{
                              0:{
                                 "cost":1,
                                 "name":"Base",
                                 "disabled":False,
                                 "shutdown":False
                              }
                           },
                           "if_cfg":True,
                           "transmit_delay":1,
                           "state":"bdr",
                           "priority":1,
                           "dr_router_id":"10.64.4.4",
                           "dr_ip_addr":"10.1.4.4",
                           "bdr_router_id":"10.4.1.1",
                           "bdr_ip_addr":"10.1.4.1",
                           "hello_interval":10,
                           "dead_interval":40,
                           "wait_interval":40,
                           "retransmit_interval":5,
                           "oob_resync_timeout":40,
                           "passive":False,
                           "hello_timer":"00:00:08",
                           "lls":True,
                           "graceful_restart":{
                              "cisco":{
                                 "type":"cisco",
                                 "helper":True
                              },
                              "ietf":{
                                 "type":"ietf",
                                 "helper":True
                              }
                           },
                           "ipfrr_protected":True,
                           "ipfrr_candidate":True,
                           "ti_lfa_protected":False,
                           "index":"1/2/2",
                           "flood_queue_length":0,
                           "next":"0x0(0)/0x0(0)/0x0(0)",
                           "last_flood_scan_length":3,
                           "max_flood_scan_length":3,
                           "last_flood_scan_time_msec":0,
                           "max_flood_scan_time_msec":1,
                           "authentication":{
                              "auth_trailer_key":{
                                 "crypto_algorithm":"md5",
                                 "youngest_key_id":2
                              }
                           },
                           "statistics":{
                              "nbr_count":1,
                              "adj_nbr_count":1,
                              "num_nbrs_suppress_hello":0
                           },
                           "neighbors":{
                              "10.64.4.4":{
                                 "dr_router_id":"10.64.4.4"
                              }
                           }
                        }
                     }
                  }
               }
            },
            "2":{
               "areas":{
                  "0.0.0.1":{
                     "sham_links":{
                        "OSPF_SL1":{
                           "router_id":"10.229.11.11",
                           "interface_type":"sham-link",
                           "cost":111,
                           "demand_circuit":True,
                           "bfd":{
                              "enable":False
                           },
                           "name":"SL1",
                           "ip_address":"0.0.0.0/0",
                           "interface_id":14,
                           "attached":"not attached",
                           "enable":True,
                           "line_protocol":True,
                           "topology":{
                              0:{
                                 "cost":111,
                                 "name":"Base",
                                 "disabled":False,
                                 "shutdown":False
                              }
                           },
                           "transmit_delay":1,
                           "state":"point-to-point",
                           "hello_interval":10,
                           "dead_interval":40,
                           "wait_interval":40,
                           "retransmit_interval":5,
                           "oob_resync_timeout":40,
                           "passive":False,
                           "hello_timer":"00:00:00",
                           "lls":True,
                           "graceful_restart":{
                              "cisco":{
                                 "type":"cisco",
                                 "helper":True
                              },
                              "ietf":{
                                 "type":"ietf",
                                 "helper":True
                              }
                           },
                           "ttl_security":{
                              "enable":True,
                              "hops":3
                           },
                           "ti_lfa_protected":False,
                           "index":"1/2/2",
                           "flood_queue_length":0,
                           "next":"0x0(0)/0x0(0)/0x0(0)",
                           "last_flood_scan_length":1,
                           "max_flood_scan_length":5,
                           "last_flood_scan_time_msec":0,
                           "max_flood_scan_time_msec":1,
                           "statistics":{
                              "nbr_count":1,
                              "adj_nbr_count":1,
                              "num_nbrs_suppress_hello":0
                           }
                        }
                     },
                     "interfaces":{
                        "GigabitEthernet3":{
                           "router_id":"10.229.11.11",
                           "interface_type":"broadcast",
                           "cost":1,
                           "demand_circuit":False,
                           "bfd":{
                              "enable":False
                           },
                           "name":"GigabitEthernet3",
                           "ip_address":"10.186.5.1/24",
                           "interface_id":9,
                           "attached":"interface enable",
                           "enable":True,
                           "line_protocol":True,
                           "topology":{
                              0:{
                                 "cost":1,
                                 "name":"Base",
                                 "disabled":False,
                                 "shutdown":False
                              }
                           },
                           "if_cfg":True,
                           "transmit_delay":1,
                           "state":"dr",
                           "priority":1,
                           "dr_router_id":"10.229.11.11",
                           "dr_ip_addr":"10.186.5.1",
                           "bdr_router_id":"10.115.55.55",
                           "bdr_ip_addr":"10.186.5.5",
                           "hello_interval":10,
                           "dead_interval":40,
                           "wait_interval":40,
                           "retransmit_interval":5,
                           "oob_resync_timeout":40,
                           "passive":False,
                           "hello_timer":"00:00:08",
                           "lls":True,
                           "graceful_restart":{
                              "cisco":{
                                 "type":"cisco",
                                 "helper":True
                              },
                              "ietf":{
                                 "type":"ietf",
                                 "helper":True
                              }
                           },
                           "ipfrr_protected":True,
                           "ipfrr_candidate":True,
                           "ti_lfa_protected":False,
                           "index":"1/1/1",
                           "flood_queue_length":0,
                           "next":"0x0(0)/0x0(0)/0x0(0)",
                           "last_flood_scan_length":0,
                           "max_flood_scan_length":7,
                           "last_flood_scan_time_msec":0,
                           "max_flood_scan_time_msec":1,
                           "statistics":{
                              "nbr_count":1,
                              "adj_nbr_count":1,
                              "num_nbrs_suppress_hello":0
                           },
                           "neighbors":{
                              "10.115.55.55":{
                                 "bdr_router_id":"10.115.55.55"
                              }
                           }
                        }
                     }
                  }
               }
            }
         }
      }
   }
}