
from Psychopy_util import Intermediater, Event_manager, Input_interface_manager, Psy_display_manager
from Psychopy_util import Text_st_unit

intermediater = Intermediater()

event_manager = Event_manager(is_activate=True)
interface = Input_interface_manager(start_keys=["s"], stop_keys=["q"], intermediater=intermediater, devices="keyboard")
p = Psy_display_manager(intermediater=intermediater)

intermediater.set_event_manager(event_manager)
intermediater.set_input_interface_manager(interface)
intermediater.set_display_manager(p)

p.open_window([200, 200], [-1, -1, -1])

p.show_stimuluses([Text_st_unit("1", showing_time=2), Text_st_unit("2", showing_time=3)])

interface.monitoring()
p.close_window()
