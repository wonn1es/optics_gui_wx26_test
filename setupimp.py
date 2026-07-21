


from pathlib import Path
import sys

repo_root = Path.cwd()
if repo_root.name == "12_IO":
    repo_root = repo_root.parents[1]
elif (repo_root / "Dev" / "12_IO").is_dir():
    pass

src_path = repo_root / "src"
if src_path.is_dir() and str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

RUN_FULL_MODEL = True
RUN_ORBIT_CORRECTION_EXAMPLE = True

print(f"repo_root = {repo_root}")
print(f"RUN_FULL_MODEL = {RUN_FULL_MODEL}")
print(f"RUN_ORBIT_CORRECTION_EXAMPLE = {RUN_ORBIT_CORRECTION_EXAMPLE}")


import pandas as pd
import matplotlib.pyplot as plt

from optics_gui.cycle_time import RCSRamp
from optics_gui.machine_state import MachineState
from optics_gui.correctors import current_to_kick_rad, kick_rad_to_current
from optics_gui.errors import (
    read_error_table,
    summarise_error_table,
    write_zeroed_error_table_copy,
    zero_error_table_magnets,
)
from optics_gui.error_plots import error_table_to_misalignment_offsets, plot_error_table_misalignment_offsets
from optics_gui.tune import (
    build_tune_programme_table,
    build_working_point_table,
    generate_resonance_lines,
    evaluate_resonance_proximity,
    make_tune_diagram_inputs,
)
from optics_gui.snapshot import (
    SnapshotConfig,
    SnapshotSeriesConfig,
    SnapshotOrbitCorrectionConfig,
    build_machine_snapshot,
    build_full_cycle_snapshot_series,
    copy_snapshot_config,
)
from optics_gui.envelope import EnvelopeInputs, plot_envelope, plot_sigma, plot_envelope_comparison
from optics_gui.orbit_correction import (
    bpm_measurements_from_twiss,
    normalise_corrector_selection,
    plot_corrector_suggestions,
    plot_orbit_with_bpm,
)
from optics_gui.aperture import (
    read_source_aperture_csv,
    plot_aperture_envelope_with_margin,
    plot_margin,
)
from optics_gui.tune_plots import plot_tune_diagram_inputs
from optics_gui.io import (
    config_to_record,
    config_from_record,
    corrector_settings_from_table,
    normalise_bpm_table,
    normalise_corrector_table,
    snapshot_configs_from_table,
    write_snapshot_bundle,
    read_run_bundle,
    write_snapshot_config,
    read_snapshot_config,
    series_config_to_record,
    series_config_from_record,
    write_snapshot_series_config,
    read_snapshot_series_config,
)

print("Imports worked")

# %%
basic_config = SnapshotConfig(
    cycle_time_ms=0.0,
    requested_qx=4.31,
    requested_qy=3.83,
    output_dir=str(repo_root / "Dev" / "12_IO" / "student_runs"),
    run_envelope=False,
    run_aperture=False,
)

record = config_to_record(basic_config)
restored = config_from_record(record)

print(record["__type__"])
print(restored.resolved_label())
print(restored.requested_qx, restored.requested_qy)


