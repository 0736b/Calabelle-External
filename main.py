from core.core import Core, Process

if __name__ == '__main__':
    
    process_name = input('Enter game process (without .exe): ') + '.exe'
    
    pls_not_ban_me = Core(process_name)
    if pls_not_ban_me.is_game_running():
        pls_not_ban_me.get_addresses()
    
    try:
        while pls_not_ban_me.is_game_running():
            Process.sleep(1)
            pls_not_ban_me.gm_on()
            pls_not_ban_me.range_on()
            pls_not_ban_me.aoe_on()
            pls_not_ban_me.movespd_on()
            pls_not_ban_me.autocast_on()
            pls_not_ban_me.auracd_on()
            pls_not_ban_me.bm1cd_on()
            pls_not_ban_me.bm2cd_on()
            pls_not_ban_me.bm3cd_on()
            pls_not_ban_me.wallhack_on()
    except KeyboardInterrupt:
        pass
    print('Exit')