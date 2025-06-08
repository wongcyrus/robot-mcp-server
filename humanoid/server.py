import io

from action_executor import ActionExecutor
from api_proxy import ApiProxy
import os
from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage

mcp = FastMCP(
    name="Humanoid Controller",
    description="Controller for humanoid robot actions",
    settings={
        "port": 8000,
        "host": "0.0.0.0",
    },
)

if os.getenv("USE_API_PROXY", "true").lower() == "true":
# Instantiate the executor
    executor = ApiProxy()
else
    executor = ActionExecutor()


@mcp.tool()
def back_fast() -> str:
    """Command the robot to move backward quickly."""
    executor.execute_action("back_fast")
    return "The robot is moving backward quickly."


@mcp.tool()
def bow() -> str:
    """Command the robot to bow."""
    executor.execute_action("bow")
    return "The robot is bowing."


@mcp.tool()
def chest() -> str:
    """Command the robot to perform chest exercises."""
    executor.execute_action("chest")
    return "The robot is performing chest exercises."


@mcp.tool()
def dance_eight() -> str:
    """Command the robot to perform dance eight."""
    executor.execute_action("dance_eight")
    return "The robot is performing dance eight."


@mcp.tool()
def dance_five() -> str:
    """Command the robot to perform dance five."""
    executor.execute_action("dance_five")
    return "The robot is performing dance five."


@mcp.tool()
def dance_four() -> str:
    """Command the robot to perform dance four."""
    executor.execute_action("dance_four")
    return "The robot is performing dance four."


@mcp.tool()
def dance_nine() -> str:
    """Command the robot to perform dance nine."""
    executor.execute_action("dance_nine")
    return "The robot is performing dance nine."


@mcp.tool()
def dance_seven() -> str:
    """Command the robot to perform dance seven."""
    executor.execute_action("dance_seven")
    return "The robot is performing dance seven."


@mcp.tool()
def dance_six() -> str:
    """Command the robot to perform dance six."""
    executor.execute_action("dance_six")
    return "The robot is performing dance six."


@mcp.tool()
def dance_ten() -> str:
    """Command the robot to perform dance ten."""
    executor.execute_action("dance_ten")
    return "The robot is performing dance ten."


@mcp.tool()
def dance_three() -> str:
    """Command the robot to perform dance three."""
    executor.execute_action("dance_three")
    return "The robot is performing dance three."


@mcp.tool()
def dance_two() -> str:
    """Command the robot to perform dance two."""
    executor.execute_action("dance_two")
    return "The robot is performing dance two."


@mcp.tool()
def go_forward() -> str:
    """Command the robot to move forward in the direction it is currently facing."""
    executor.execute_action("go_forward")
    return "The robot is moving forward."


@mcp.tool()
def kung_fu() -> str:
    """Command the robot to perform kung fu moves."""
    executor.execute_action("kung_fu")
    return "The robot is performing kung fu moves."


@mcp.tool()
def left_kick() -> str:
    """Command the robot to perform a left kick."""
    executor.execute_action("left_kick")
    return "The robot is performing a left kick."


@mcp.tool()
def left_move_fast() -> str:
    """Command the robot to move left quickly."""
    executor.execute_action("left_move_fast")
    return "The robot is moving left quickly."


@mcp.tool()
def left_shot_fast() -> str:
    """Command the robot to perform a fast left punch."""
    executor.execute_action("left_shot_fast")
    return "The robot is performing a fast left punch."


@mcp.tool()
def left_uppercut() -> str:
    """Command the robot to perform a left uppercut."""
    executor.execute_action("left_uppercut")
    return "The robot is performing a left uppercut."


@mcp.tool()
def push_ups() -> str:
    """Command the robot to perform push-ups."""
    executor.execute_action("push_ups")
    return "The robot is performing push-ups."


@mcp.tool()
def right_kick() -> str:
    """Command the robot to perform a right kick."""
    executor.execute_action("right_kick")
    return "The robot is performing a right kick."


@mcp.tool()
def right_move_fast() -> str:
    """Command the robot to move right quickly."""
    executor.execute_action("right_move_fast")
    return "The robot is moving right quickly."


@mcp.tool()
def right_shot_fast() -> str:
    """Command the robot to perform a fast right punch."""
    executor.execute_action("right_shot_fast")
    return "The robot is performing a fast right punch."


@mcp.tool()
def right_uppercut() -> str:
    """Command the robot to perform a right uppercut."""
    executor.execute_action("right_uppercut")
    return "The robot is performing a right uppercut."


@mcp.tool()
def sit_ups() -> str:
    """Command the robot to perform sit-ups."""
    executor.execute_action("sit_ups")
    return "The robot is performing sit-ups."


@mcp.tool()
def squat() -> str:
    """Command the robot to squat down."""
    executor.execute_action("squat")
    return "The robot is squatting down."


@mcp.tool()
def squat_up() -> str:
    """Command the robot to stand up from a squat."""
    executor.execute_action("squat_up")
    return "The robot is standing up from a squat."


@mcp.tool()
def stand() -> str:
    """Command the robot to stand up and maintain a standing position."""
    executor.execute_action("stand")
    return "The robot is standing up."


@mcp.tool()
def stand_up_back() -> str:
    """Command the robot to stand up from the back."""
    executor.execute_action("stand_up_back")
    return "The robot is standing up from the back."


@mcp.tool()
def stand_up_front() -> str:
    """Command the robot to stand up from the front."""
    executor.execute_action("stand_up_front")
    return "The robot is standing up from the front."


@mcp.tool()
def stepping() -> str:
    """Command the robot to perform stepping motions."""
    executor.execute_action("stepping")
    return "The robot is performing stepping motions."


@mcp.tool(name="stop")
def stop() -> str:
    """Command the robot to perform stopping motions."""
    executor.execute_action("stop")
    return "The robot is stopping."


@mcp.tool()
def turn_left() -> str:
    """Command the robot to turn left."""
    executor.execute_action("turn_left")
    return "The robot is turning left."


@mcp.tool()
def turn_right() -> str:
    """Command the robot to turn right."""
    executor.execute_action("turn_right")
    return "The robot is turning right."


@mcp.tool()
def twist() -> str:
    """Command the robot to twist its body."""
    executor.execute_action("twist")
    return "The robot is twisting its body."


@mcp.tool()
def wave() -> str:
    """Command the robot to wave its hand."""
    executor.execute_action("wave")
    return "The robot is waving its hand."


@mcp.tool()
def weightlifting() -> str:
    """Command the robot to perform weightlifting."""
    executor.execute_action("weightlifting")
    return "The robot is performing weightlifting."


@mcp.tool()
def wing_chun() -> str:
    """Command the robot to perform Wing Chun moves."""
    executor.execute_action("wing_chun")
    return "The robot is performing Wing Chun moves."


@mcp.tool()
def get_image() -> str:
    """Get the current image from the robot's camera."""

    image_path = executor.get_image()
    if not image_path:
        return "No image available."
    # Return the image path or URL
    else:
        img = PILImage.open(image_path)
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        img_bytes = buf.getvalue()
        return Image(data=img_bytes, format="jpeg")


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()
