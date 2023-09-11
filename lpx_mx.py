import solid as s

if __name__=='__main__':
    keycap = s.import_stl("./Cherry-MX-Low-Profile-Keycap.stl")
    keycap = s.translate([-10,0,0])(keycap)
    stem_side_cutter = 9
    stem = s.difference()(keycap, 
                            s.translate([10+stem_side_cutter/2,0,0])(s.cube(20,center=True)),
                            s.translate([-10-stem_side_cutter/2,0,0])(s.cube(20,center=True)),
                            s.translate([0,10+stem_side_cutter/2,0])(s.cube(20,center=True)),
                            s.translate([0,-10-stem_side_cutter/2,0])(s.cube(20,center=True)),
                       )
    stem = s.rotate([+41.5+90, 0, 0])(stem)
    stem = s.translate([29,5.25,6.75])(stem)

    keycap = s.import_stl("./LPX.stl")
    # centering
    cutter = s.rotate([41.5,0,0])(s.cube([5, 12, 8], center=True))
    keycap = s.difference()(keycap, s.translate([29,0,2])(cutter),)
    keycap = s.union()(stem, keycap)
    s.scad_render_to_file(keycap, "lpx_mx.scad")
