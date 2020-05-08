from tespy.networks import load_network

path = 'powerplant/hp_discharge'
nw = load_network(path)
nw.imp_busses["heat system"].set_attr(P=1e6)
nw.imp_conns["condenser:out2_system feed:in1"].set_attr(T=70)
nw.imp_conns["system return:out1_condenser:in2"].set_attr(T=57)
nw.imp_conns["evaporator:out1_storage feed:in1"].set_attr(T=15)
nw.imp_conns["storage return:out1_superheater:in1"].set_attr(T=25)

nw.solve('design')
nw.print_results()
nw.save('test')
nw.print_results()

nw.imp_conns["condenser:out2_system feed:in1"].set_attr(T=80.3)
nw.imp_conns["system return:out1_condenser:in2"].set_attr(T=47.6)
nw.imp_conns["storage return:out1_superheater:in1"].set_attr(T=20)
nw.solve('offdesign', design_path='test')

nw.imp_conns["condenser:out2_system feed:in1"].set_attr(T=80.3)
nw.imp_conns["system return:out1_condenser:in2"].set_attr(T=47.6)
nw.imp_conns["storage return:out1_superheater:in1"].set_attr(T=16.26)
nw.solve('offdesign', design_path='test')
print(nw.imp_conns["evaporator:out1_storage feed:in1"].T.val)

nw.imp_conns["condenser:out2_system feed:in1"].set_attr(T=83.9)
nw.imp_conns["system return:out1_condenser:in2"].set_attr(T=48.4)
nw.imp_conns["storage return:out1_superheater:in1"].set_attr(T=16.26)
nw.solve('offdesign', design_path='test')
print(nw.imp_conns["evaporator:out1_storage feed:in1"].T.val)
