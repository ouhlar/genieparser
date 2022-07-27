expected_output = {
    "interface": {
        "Tunnel100": {
            "interface_state_event_stats": {
                "r_up": 2,
                "r_up_error": 0,
                "r_down": 0,
                "r_down_error": 0,
                "r_admin_down": 0,
                "r_admin_down_error": 0,
                "r_deleted": 0,
                "r_deleted_error": 0,
                "r_addr_changed": 0,
                "r_addr_changed_error": 0,
                "r_vrf_changed": 0,
                "r_vrf_changed_error": 0,
                "r_packets_received": 3808,
                "r_packets_received_error": 0,
            },
            "tunnel_stats": {
                "s_endpoint_addition": 264,
                "s_endpoint_addition_error": 0,
                "s_endpoint_deletion": 160,
                "s_endpoint_deletion_error": 0,
                "r_o_ep_sb_created": 0,
                "r_o_ep_sb_created_error": 0,
                "r_t_ep_sb_created": 0,
                "r_t_ep_sb_created_error": 0,
                "r_to_ep_deleted": 0,
                "r_to_ep_deleted_error": 0,
                "s_pre_delete": 0,
                "s_pre_delete_error": 0,
                "r_src_change": 1,
                "r_src_change_error": 0,
                "r_mode_change": 3,
                "r_mode_change_error": 0,
                "r_leave_mode": 2,
                "r_leave_mode_error": 0,
                "r_decap_intercept": 0,
                "r_decap_intercept_error": 0,
                "r_delayed_event_unlink_ep": 0,
                "r_delayed_event_unlink_ep_error": 0,
            },
            "tunnel_protection_stats": {
                "s_create_tp_socket": 0,
                "s_create_tp_socket_error": 0,
                "s_del_tp_socket": 0,
                "s_del_tp_socket_error": 0,
                "s_create_va": 0,
                "s_create_va_error": 0,
                "s_del_va": 0,
                "s_del_va_error": 0,
                "r_up": 44,
                "r_up_error": 0,
                "r_down": 19,
                "r_down_error": 0,
                "s_reset_socket": 0,
                "s_reset_socket_error": 0,
                "r_process_delayed_event": 40,
                "r_process_delayed_event_error": 0,
                "r_update_delayed_event": 0,
                "r_update_delayed_event_error": 0,
            },
            "tunnel_qos_stats": {
                "s_qos_apply": 0,
                "s_qos_apply_error": 0,
                "s_qos_remove": 0,
                "s_qos_remove_error": 0,
                "r_qos_polocy_removed": 0,
                "r_qos_polocy_removed_error": 0,
                "r_cli_policy_map_deleted": 0,
                "r_cli_policy_map_deleted_error": 0,
                "r_cli_policy_map_rename": 0,
                "r_cli_policy_map_rename_error": 0,
            },
            "rib_event_stats": {
                "s_add_route": 80,
                "s_add_route_error": 0,
                "s_del_route": 80,
                "s_del_route_error": 0,
                "s_add_nho": 0,
                "s_add_nho_error": 0,
                "s_del_nho": 0,
                "s_del_nho_error": 0,
                "s_rwatch_wo_route": 0,
                "s_rwatch_wo_route_error": 0,
                "s_init_ipdb": 0,
                "s_init_ipdb_error": 0,
                "s_add_ipdb": 0,
                "s_add_ipdb_error": 0,
                "s_del_ipdb": 0,
                "s_del_ipdb_error": 0,
                "s_remove_ipdb": 0,
                "s_remove_ipdb_error": 0,
                "s_rt_revise": 0,
                "s_rt_revise_error": 0,
                "r_redist_callback": 0,
                "r_redist_callback_error": 0,
                "r_route_add_callback": 0,
                "r_route_add_callback_error": 0,
                "r_route_evicted": 0,
                "r_route_evicted_error": 0,
                "s_route_query": 0,
                "s_route_query_error": 0,
            },
            "mpls_stats": {
                "s_label_alloc": 0,
                "s_label_alloc_error": 0,
                "s_label_release": 0,
                "s_label_release_error": 0,
                "s_mpls_ip_key_bind": 0,
                "s_mpls_ip_key_bind_error": 0,
                "s_mpls_vpn_key_bind": 0,
                "s_mpls_vpn_key_bind_error": 0,
                "s_inject_packet": 0,
                "s_inject_packet_error": 0,
                "r_nhrp_mpls_mgmt_ch_cb": 0,
                "r_nhrp_mpls_mgmt_ch_cb_error": 0,
                "r_redirect": 0,
                "r_redirect_error": 0,
                "s_label_oi_bind": 0,
                "s_label_oi_bind_error": 0,
                "s_register_mpls": 0,
                "s_register_mpls_error": 0,
                "s_unregister_mpls": 0,
                "s_unregister_mpls_error": 0,
            },
            "bfd_stats": {
                "s_client_create": 0,
                "s_client_create_error": 0,
                "s_client_destroy": 0,
                "s_client_destroy_error": 0,
                "s_session_create": 0,
                "s_session_create_error": 0,
                "s_session_destroy": 0,
                "s_session_destroy_error": 0,
                "r_callback": 0,
                "r_callback_error": 0,
                "r_session_down": 0,
                "r_session_down_error": 0,
                "r_session_up": 0,
                "r_session_up_error": 0,
                "r_session_default": 0,
                "r_session_default_error": 0,
            },
            "cef_stats": {
                "s_adjacency_used": 0,
                "s_adjacency_used_error": 0,
                "s_adjacency_mark_stale": 194,
                "s_adjacency_mark_stale_error": 0,
            },
            "bgp_stats": {
                "s_route_export": 0,
                "s_route_export_error": 0,
                "s_route_withdrawal": 0,
                "s_route_withdrawal_error": 0,
                "s_route_import": 0,
                "s_route_import_error": 0,
                "r_imported_route_changed": 0,
                "r_imported_route_changed_error": 0,
                "s_route_marked": 0,
                "s_route_marked_error": 0,
                "s_route_unmarked": 0,
                "s_route_unmarked_error": 0,
                "r_route_change_notification": 0,
                "r_route_change_notification_error": 0,
                "r_exported_route_deleted": 0,
                "r_exported_route_deleted_error": 0,
                "r_withdrawal_all_route": 0,
                "r_withdrawal_all_route_error": 0,
            },
            "platform_stats": {
                "r_state_change": 0,
                "r_state_change_error": 0,
                "r_redirect_request": 0,
                "r_redirect_request_error": 0,
                "s_enable": 0,
                "s_enable_error": 0,
                "s_disable": 0,
                "s_disable_error": 0,
            },
        },
        "Tunnel111": {
            "interface_state_event_stats": {
                "r_up": 3,
                "r_up_error": 0,
                "r_down": 4,
                "r_down_error": 0,
                "r_admin_down": 1,
                "r_admin_down_error": 0,
                "r_deleted": 0,
                "r_deleted_error": 0,
                "r_addr_changed": 0,
                "r_addr_changed_error": 0,
                "r_vrf_changed": 0,
                "r_vrf_changed_error": 0,
                "r_packets_received": 0,
                "r_packets_received_error": 0,
            },
            "tunnel_stats": {
                "s_endpoint_addition": 8,
                "s_endpoint_addition_error": 0,
                "s_endpoint_deletion": 2,
                "s_endpoint_deletion_error": 0,
                "r_o_ep_sb_created": 0,
                "r_o_ep_sb_created_error": 0,
                "r_t_ep_sb_created": 0,
                "r_t_ep_sb_created_error": 0,
                "r_to_ep_deleted": 0,
                "r_to_ep_deleted_error": 0,
                "s_pre_delete": 0,
                "s_pre_delete_error": 0,
                "r_src_change": 0,
                "r_src_change_error": 0,
                "r_mode_change": 3,
                "r_mode_change_error": 0,
                "r_leave_mode": 2,
                "r_leave_mode_error": 0,
                "r_decap_intercept": 0,
                "r_decap_intercept_error": 0,
                "r_delayed_event_unlink_ep": 0,
                "r_delayed_event_unlink_ep_error": 0,
            },
            "tunnel_protection_stats": {
                "s_create_tp_socket": 0,
                "s_create_tp_socket_error": 0,
                "s_del_tp_socket": 0,
                "s_del_tp_socket_error": 0,
                "s_create_va": 0,
                "s_create_va_error": 0,
                "s_del_va": 0,
                "s_del_va_error": 0,
                "r_up": 0,
                "r_up_error": 0,
                "r_down": 0,
                "r_down_error": 0,
                "s_reset_socket": 0,
                "s_reset_socket_error": 0,
                "r_process_delayed_event": 0,
                "r_process_delayed_event_error": 0,
                "r_update_delayed_event": 0,
                "r_update_delayed_event_error": 0,
            },
            "tunnel_qos_stats": {
                "s_qos_apply": 0,
                "s_qos_apply_error": 0,
                "s_qos_remove": 0,
                "s_qos_remove_error": 0,
                "r_qos_polocy_removed": 0,
                "r_qos_polocy_removed_error": 0,
                "r_cli_policy_map_deleted": 0,
                "r_cli_policy_map_deleted_error": 0,
                "r_cli_policy_map_rename": 0,
                "r_cli_policy_map_rename_error": 0,
            },
            "rib_event_stats": {
                "s_add_route": 0,
                "s_add_route_error": 0,
                "s_del_route": 0,
                "s_del_route_error": 0,
                "s_add_nho": 0,
                "s_add_nho_error": 0,
                "s_del_nho": 0,
                "s_del_nho_error": 0,
                "s_rwatch_wo_route": 0,
                "s_rwatch_wo_route_error": 0,
                "s_init_ipdb": 0,
                "s_init_ipdb_error": 0,
                "s_add_ipdb": 0,
                "s_add_ipdb_error": 0,
                "s_del_ipdb": 0,
                "s_del_ipdb_error": 0,
                "s_remove_ipdb": 0,
                "s_remove_ipdb_error": 0,
                "s_rt_revise": 0,
                "s_rt_revise_error": 0,
                "r_redist_callback": 0,
                "r_redist_callback_error": 0,
                "r_route_add_callback": 0,
                "r_route_add_callback_error": 0,
                "r_route_evicted": 0,
                "r_route_evicted_error": 0,
                "s_route_query": 0,
                "s_route_query_error": 0,
            },
            "mpls_stats": {
                "s_label_alloc": 0,
                "s_label_alloc_error": 0,
                "s_label_release": 0,
                "s_label_release_error": 0,
                "s_mpls_ip_key_bind": 0,
                "s_mpls_ip_key_bind_error": 0,
                "s_mpls_vpn_key_bind": 0,
                "s_mpls_vpn_key_bind_error": 0,
                "s_inject_packet": 0,
                "s_inject_packet_error": 0,
                "r_nhrp_mpls_mgmt_ch_cb": 0,
                "r_nhrp_mpls_mgmt_ch_cb_error": 0,
                "r_redirect": 0,
                "r_redirect_error": 0,
                "s_label_oi_bind": 0,
                "s_label_oi_bind_error": 0,
                "s_register_mpls": 0,
                "s_register_mpls_error": 0,
                "s_unregister_mpls": 0,
                "s_unregister_mpls_error": 0,
            },
            "bfd_stats": {
                "s_client_create": 0,
                "s_client_create_error": 0,
                "s_client_destroy": 0,
                "s_client_destroy_error": 0,
                "s_session_create": 0,
                "s_session_create_error": 0,
                "s_session_destroy": 0,
                "s_session_destroy_error": 0,
                "r_callback": 0,
                "r_callback_error": 0,
                "r_session_down": 0,
                "r_session_down_error": 0,
                "r_session_up": 0,
                "r_session_up_error": 0,
                "r_session_default": 0,
                "r_session_default_error": 0,
            },
            "cef_stats": {
                "s_adjacency_used": 0,
                "s_adjacency_used_error": 0,
                "s_adjacency_mark_stale": 0,
                "s_adjacency_mark_stale_error": 0,
            },
            "bgp_stats": {
                "s_route_export": 0,
                "s_route_export_error": 0,
                "s_route_withdrawal": 0,
                "s_route_withdrawal_error": 0,
                "s_route_import": 0,
                "s_route_import_error": 0,
                "r_imported_route_changed": 0,
                "r_imported_route_changed_error": 0,
                "s_route_marked": 0,
                "s_route_marked_error": 0,
                "s_route_unmarked": 0,
                "s_route_unmarked_error": 0,
                "r_route_change_notification": 0,
                "r_route_change_notification_error": 0,
                "r_exported_route_deleted": 0,
                "r_exported_route_deleted_error": 0,
                "r_withdrawal_all_route": 0,
                "r_withdrawal_all_route_error": 0,
            },
            "platform_stats": {
                "r_state_change": 0,
                "r_state_change_error": 0,
                "r_redirect_request": 0,
                "r_redirect_request_error": 0,
                "s_enable": 0,
                "s_enable_error": 0,
                "s_disable": 0,
                "s_disable_error": 0,
            },
        },
    }
}