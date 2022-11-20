from core.proc import *
import const.addr as c_addr
import const.offset as c_offset
import const.value as c_val

class Core:
    
    def __init__(self, proc_name):
        self.mem = Process(proc_name)
        self.player_base = c_addr.base
        self.gm = c_addr.gm
        self.aoe = c_addr.aoe
        self.range = c_addr.range
        self.wall_base = c_addr.wall_base
    
    def is_game_running(self):
        return self.mem.is_running()
    
    def get_addresses(self):
        self.player_x = self.mem.get_ptr_addr(self.player_base, c_offset.player_pos_x)
        self.player_y = self.mem.get_ptr_addr(self.player_base, c_offset.player_pos_y)
        self.aura_cd = self.mem.get_ptr_addr(self.player_base, c_offset.aura_cd)
        self.bm1_cd = self.mem.get_ptr_addr(self.player_base, c_offset.bm1_cd)
        self.bm2_cd = self.mem.get_ptr_addr(self.player_base, c_offset.bm2_cd)
        self.bm3_cd = self.mem.get_ptr_addr(self.player_base, c_offset.bm3_cd)
        self.nsd = self.mem.get_ptr_addr(self.player_base, c_offset.nsd)
        self.no_stun = self.mem.get_ptr_addr(self.player_base, c_offset.no_stun)
        self.combo_point = self.mem.get_ptr_addr(self.player_base, c_offset.combo_point)
        self.combo_bar = self.mem.get_ptr_addr(self.player_base, c_offset.combo_bar)
        self.move_spd = self.mem.get_ptr_addr(self.player_base, c_offset.move_spd)
        self.kill_gate = self.mem.get_ptr_addr(self.player_base, c_offset.kill_gate)
        self.auto_cast = self.mem.get_ptr_addr(self.player_base, c_offset.auto_cast)
        self.map_in = self.mem.get_ptr_addr(self.player_base, c_offset.map_in)

    def gm_on(self):
        self.mem.w_int(self.gm, c_val.en_gm)
    
    def aoe_on(self):
        self.mem.w_int(self.aoe, c_val.en_aoe)

    def range_on(self):
        self.mem.w_int(self.range, c_val.en_range)

    def movespd_on(self):
        self.mem.w_float(self.move_spd, c_val.en_move_spd)
    
    def combopoint_on(self):
        self.mem.w_int(self.combo_point, c_val.en_combo_point)
    
    def combobar_on(self):
        self.mem.w_int(self.combo_bar, c_val.en_combo_bar)
    
    def auracd_on(self):
        self.mem.w_int(self.aura_cd, c_val.en_aura_cd)
    
    def bm1cd_on(self):
        self.mem.w_int(self.bm1_cd, c_val.en_bm1_cd)
    
    def bm2cd_on(self):
        self.mem.w_int(self.bm2_cd, c_val.en_bm2_cd)

    def bm3cd_on(self):
        self.mem.w_int(self.bm3_cd, c_val.en_bm3_cd)

    def autocast_on(self):
        self.mem.w_int(self.auto_cast, c_val.en_auto_cast)
    
    def killgate_on(self):
        self.mem.w_int(self.kill_gate, c_val.en_kill_gate)
    
    def nostun_on(self):
        self.mem.w_int(self.no_stun, c_val.en_nostun)
    
    def nsd_on(self):
        self.mem.w_int(self.nsd, c_val.en_nsd)

    def wallhack_on(self):
        wallbase_val = self.mem.r_int(self.wall_base)
        start = wallbase_val + 0x40814
        patch_byte = b"\x00"
        for i in range(0, 0x3FFFF, 4):
            self.mem.w_bytes((start + i), patch_byte, 1)