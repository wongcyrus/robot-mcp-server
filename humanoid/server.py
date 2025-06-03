from action_executor import ActionExecutor
from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage
import io

mcp = FastMCP("Echo")

# Instantiate the executor
executor = ActionExecutor()


@mcp.tool()
def add_action_to_queue(action_name: str) -> str:
    """Add a new action to the queue."""
    executor.add_action_to_queue(action_name)
    return f"Action '{action_name}' added to queue."


@mcp.tool()
def remove_action_from_queue(action_id: str) -> str:
    """Remove an action from the queue by its ID."""
    executor.remove_action_from_queue(action_id)
    return f"Action with ID '{action_id}' removed from queue."


@mcp.tool()
def clear_action_queue() -> str:
    """Clear all actions from the queue."""
    executor.clear_action_queue()
    return "Action queue cleared."


@mcp.tool()
def get_queue_status() -> dict:
    """Get the current status of the action queue."""
    return executor.get_queue_status()


@mcp.tool()
def back_fast() -> str:
    """Command the robot to move backward quickly."""
    executor.add_action_to_queue("back_fast")
    return "The robot is moving backward quickly."


@mcp.tool()
def bow() -> str:
    """Command the robot to bow."""
    executor.add_action_to_queue("bow")
    return "The robot is bowing."


@mcp.tool()
def chest() -> str:
    """Command the robot to perform chest exercises."""
    executor.add_action_to_queue("chest")
    return "The robot is performing chest exercises."


@mcp.tool()
def dance_eight() -> str:
    """Command the robot to perform dance eight."""
    executor.add_action_to_queue("dance_eight")
    return "The robot is performing dance eight."


@mcp.tool()
def dance_five() -> str:
    """Command the robot to perform dance five."""
    executor.add_action_to_queue("dance_five")
    return "The robot is performing dance five."


@mcp.tool()
def dance_four() -> str:
    """Command the robot to perform dance four."""
    executor.add_action_to_queue("dance_four")
    return "The robot is performing dance four."


@mcp.tool()
def dance_nine() -> str:
    """Command the robot to perform dance nine."""
    executor.add_action_to_queue("dance_nine")
    return "The robot is performing dance nine."


@mcp.tool()
def dance_seven() -> str:
    """Command the robot to perform dance seven."""
    executor.add_action_to_queue("dance_seven")
    return "The robot is performing dance seven."


@mcp.tool()
def dance_six() -> str:
    """Command the robot to perform dance six."""
    executor.add_action_to_queue("dance_six")
    return "The robot is performing dance six."


@mcp.tool()
def dance_ten() -> str:
    """Command the robot to perform dance ten."""
    executor.add_action_to_queue("dance_ten")
    return "The robot is performing dance ten."


@mcp.tool()
def dance_three() -> str:
    """Command the robot to perform dance three."""
    executor.add_action_to_queue("dance_three")
    return "The robot is performing dance three."


@mcp.tool()
def dance_two() -> str:
    """Command the robot to perform dance two."""
    executor.add_action_to_queue("dance_two")
    return "The robot is performing dance two."


@mcp.tool()
def go_forward() -> str:
    """Command the robot to move forward in the direction it is currently facing."""
    executor.add_action_to_queue("go_forward")
    return "The robot is moving forward."


@mcp.tool()
def kung_fu() -> str:
    """Command the robot to perform kung fu moves."""
    executor.add_action_to_queue("kung_fu")
    return "The robot is performing kung fu moves."


@mcp.tool()
def left_kick() -> str:
    """Command the robot to perform a left kick."""
    executor.add_action_to_queue("left_kick")
    return "The robot is performing a left kick."


@mcp.tool()
def left_move_fast() -> str:
    """Command the robot to move left quickly."""
    executor.add_action_to_queue("left_move_fast")
    return "The robot is moving left quickly."


@mcp.tool()
def left_shot_fast() -> str:
    """Command the robot to perform a fast left punch."""
    executor.add_action_to_queue("left_shot_fast")
    return "The robot is performing a fast left punch."


@mcp.tool()
def left_uppercut() -> str:
    """Command the robot to perform a left uppercut."""
    executor.add_action_to_queue("left_uppercut")
    return "The robot is performing a left uppercut."


@mcp.tool()
def push_ups() -> str:
    """Command the robot to perform push-ups."""
    executor.add_action_to_queue("push_ups")
    return "The robot is performing push-ups."


@mcp.tool()
def right_kick() -> str:
    """Command the robot to perform a right kick."""
    executor.add_action_to_queue("right_kick")
    return "The robot is performing a right kick."


@mcp.tool()
def right_move_fast() -> str:
    """Command the robot to move right quickly."""
    executor.add_action_to_queue("right_move_fast")
    return "The robot is moving right quickly."


@mcp.tool()
def right_shot_fast() -> str:
    """Command the robot to perform a fast right punch."""
    executor.add_action_to_queue("right_shot_fast")
    return "The robot is performing a fast right punch."


@mcp.tool()
def right_uppercut() -> str:
    """Command the robot to perform a right uppercut."""
    executor.add_action_to_queue("right_uppercut")
    return "The robot is performing a right uppercut."


@mcp.tool()
def sit_ups() -> str:
    """Command the robot to perform sit-ups."""
    executor.add_action_to_queue("sit_ups")
    return "The robot is performing sit-ups."


@mcp.tool()
def squat() -> str:
    """Command the robot to squat down."""
    executor.add_action_to_queue("squat")
    return "The robot is squatting down."


@mcp.tool()
def squat_up() -> str:
    """Command the robot to stand up from a squat."""
    executor.add_action_to_queue("squat_up")
    return "The robot is standing up from a squat."


@mcp.tool()
def stand() -> str:
    """Command the robot to stand up and maintain a standing position."""
    executor.add_action_to_queue("stand")
    return "The robot is standing up."


@mcp.tool()
def stand_up_back() -> str:
    """Command the robot to stand up from the back."""
    executor.add_action_to_queue("stand_up_back")
    return "The robot is standing up from the back."


@mcp.tool()
def stand_up_front() -> str:
    """Command the robot to stand up from the front."""
    executor.add_action_to_queue("stand_up_front")
    return "The robot is standing up from the front."


@mcp.tool()
def stepping() -> str:
    """Command the robot to perform stepping motions."""
    executor.add_action_to_queue("stepping")
    return "The robot is performing stepping motions."


@mcp.tool(name="stop")
def stop() -> str:
    """Command the robot to perform stopping motions."""
    executor.add_action_to_queue("stop")
    return "The robot is stopping."


@mcp.tool()
def turn_left() -> str:
    """Command the robot to turn left."""
    executor.add_action_to_queue("turn_left")
    return "The robot is turning left."


@mcp.tool()
def turn_right() -> str:
    """Command the robot to turn right."""
    executor.add_action_to_queue("turn_right")
    return "The robot is turning right."


@mcp.tool()
def twist() -> str:
    """Command the robot to twist its body."""
    executor.add_action_to_queue("twist")
    return "The robot is twisting its body."


@mcp.tool()
def wave() -> str:
    """Command the robot to wave its hand."""
    executor.add_action_to_queue("wave")
    return "The robot is waving its hand."


@mcp.tool()
def weightlifting() -> str:
    """Command the robot to perform weightlifting."""
    executor.add_action_to_queue("weightlifting")
    return "The robot is performing weightlifting."


@mcp.tool()
def wing_chun() -> str:
    """Command the robot to perform Wing Chun moves."""
    executor.add_action_to_queue("wing_chun")
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
