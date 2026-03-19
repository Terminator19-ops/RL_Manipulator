import mujoco
import mujoco.viewer
import time

model = mujoco.MjModel.from_xml_path("urdf/manipulator_v1.xml") # type: ignore
data = mujoco.MjData(model) # pyright: ignore[reportAttributeAccessIssue]

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data) # type: ignore
        time.sleep(0.01)
