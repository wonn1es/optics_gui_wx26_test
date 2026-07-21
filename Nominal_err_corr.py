# %%
from setupimp import repo_root, RUN_FULL_MODEL

import pandas 
import matplotlib
from IPython.display import display

from optics_gui.snapshot import (
    SnapshotConfig,
    build_machine_snapshot,
    copy_snapshot_config,
)



# %%
from optics_gui.snapshot import SnapshotConfig

orbit_base_config = SnapshotConfig(
    cycle_time_ms=0.0,
    requested_qx=4.31,
    requested_qy=3.83,
    lattice_folder=str(repo_root / "optics_gui_wx26_test" /"Dev" / "Lattice_Files" / "00_Simplified_Lattice"),
    output_dir=str(repo_root / "Dev" / "12_IO" / "student_runs" / "orbit"),
    run_envelope=False,
    run_aperture=False,
)

print(orbit_base_config.resolved_label())


# %%
print(type(orbit_base_config))
print(SnapshotConfig)
print(type(orbit_base_config) is SnapshotConfig) 
#should say true

print(type(orbit_base_config))
print(isinstance(orbit_base_config, SnapshotConfig))

print(copy_snapshot_config.__module__)
print(SnapshotConfig.__module__)

# %%
#simplest orbit config, try this first  THIS IS NOMINAL ERROR CONGIG WAHHHHHH
nominal_orbit_config = copy_snapshot_config(
    orbit_base_config,
    snapshot_id="student_nominal_orbit",
    label="student nominal orbit",
    error_table_paths=[],
    orbit_correction_configs=[],
)

if RUN_FULL_MODEL:
    nominal_orbit_snapshot = build_machine_snapshot(nominal_orbit_config)
    orbit_snapshot = nominal_orbit_snapshot
    display(nominal_orbit_snapshot.table("orbit_summary"))
    display(nominal_orbit_snapshot.table("orbit").head())
else:
    print("Set RUN_FULL_MODEL = True to run MAD-X and create nominal_orbit_snapshot.")
    print("The Streamlit orbit GUI will mainly consume: snapshot.table('orbit') and snapshot.table('orbit_summary').")

# %%
#error table model 
# Bare nominal model orbit plot
if RUN_FULL_MODEL:
    ax = nominal_orbit_snapshot.table("orbit").plot(x="s", y=["x_mm", "y_mm"], figsize=(10, 4))
    ax.set_xlabel("s [m]")
    ax.set_ylabel("closed orbit [mm]")
    ax.set_title("Bare nominal model orbit")
else:
    print("Bare orbit plot skipped because RUN_FULL_MODEL is False.")


