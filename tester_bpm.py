# %%
from setupimp import  RUN_FULL_MODEL
import pandas

import sys
from pathlib import Path

sys.path.append(str(Path.cwd() / "Dev" / "07_Orbit_Correction"))

from orbit_correction import bpm_measurements_from_twiss

# %%
pip install nbimporter

# %%
pip install nbformat




# %%
import nbimporter
import nbformat
from pathlib import Path

# Read and execute the notebook to get the snapshot
nb_path = Path("Nominal_error_corr_orbit.ipynb")
with open(nb_path) as f:
    nb = nbformat.read(f, as_version=4)

# Extract and execute code cells
for cell in nb.cells:
    if cell.cell_type == "code":
        exec(cell.source, globals())

# Now we have nominal_orbit_snapshot available
print(f"nominal_orbit_snapshot: {nominal_orbit_snapshot}")


# %%
# Example measured orbit table using real BPM-style names and known s positions.
# The earlier dummy names produced NaN s/error columns because those optional columns were not supplied.
# The backend can resolve BPM labels against TWISS names with resolve_bpm_to_twiss_name(...),
# and bpm_measurements_from_twiss(...) is the safest way to get real names and s positions from a model table.
if RUN_FULL_MODEL:
    measured_bpm_table = bpm_measurements_from_twiss(nominal_orbit_snapshot.table("twiss"), plane="H").head(8)
    measured_bpm_table = measured_bpm_table.copy()
    measured_bpm_table["closed_orbit_mm"] = [0.8, -0.6, 1.1, -0.9, 0.4, -0.3, 0.7, -0.5]
else:
    raw_measured_orbit = pd.DataFrame(
        [
            {"bpm": "sp0_r0hm1", "plane": "H", "closed_orbit_mm": 0.8, "closed_orbit_mm_err": 0.1, "s": 0.730500, "enabled": True},
            {"bpm": "sp0_r0hm2", "plane": "H", "closed_orbit_mm": -0.6, "closed_orbit_mm_err": 0.1, "s": 5.971000, "enabled": True},
            {"bpm": "sp1_r1hm1", "plane": "H", "closed_orbit_mm": 1.1, "closed_orbit_mm_err": 0.1, "s": 22.285282, "enabled": True},
            {"bpm": "sp1_r1hm2", "plane": "H", "closed_orbit_mm": -0.9, "closed_orbit_mm_err": 0.1, "s": 24.416282, "enabled": True},
        ]
    )
    measured_bpm_table = normalise_bpm_table(raw_measured_orbit)

measured_bpm_table


