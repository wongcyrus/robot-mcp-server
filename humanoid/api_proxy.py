import logging
import os
import tempfile
from typing import Any, Dict, Optional

import requests

# Load environment variables for robot API
ROBOT_API_HOST = os.environ.get("ROBOT_API_HOST", "localhost")
ROBOT_API_PORT = os.environ.get("ROBOT_API_PORT", "9030")
ROBOT_IMAGE_API_PORT = os.environ.get("ROBOT_IMAGE_API_PORT", "8080")
ROBOT_API_PROTOCOL = os.environ.get("ROBOT_API_PROTOCOL", "http")
ROBOT_IMAGE_API_URL = os.environ.get(
    "ROBOT_IMAGE_API_URL",
    f"{ROBOT_API_PROTOCOL}://{ROBOT_API_HOST}:{ROBOT_IMAGE_API_PORT}/?action=snapshot",
)
ROBOT_API_URL = os.environ.get(
    "ROBOT_API_URL", f"{ROBOT_API_PROTOCOL}://{ROBOT_API_HOST}:{ROBOT_API_PORT}/"
)

# 動作配置字典 (Action configuration dictionary)
actions: Dict[str, Dict[str, Any]] = {
    # ...existing code for actions dictionary...
    "back_fast": {"sleep_time": 4.5, "action": ["2", "4"], "name": "back_fast"},
    "bow": {"sleep_time": 4, "action": ["10", "1"], "name": "bow"},
    "chest": {"sleep_time": 9, "action": ["12", "1"], "name": "chest"},
    "dance_eight": {"sleep_time": 85, "action": ["42", "1"], "name": "dance_eight"},
    "dance_five": {"sleep_time": 59, "action": ["39", "1"], "name": "dance_five"},
    "dance_four": {"sleep_time": 59, "action": ["38", "1"], "name": "dance_four"},
    "dance_nine": {"sleep_time": 84, "action": ["43", "1"], "name": "dance_nine"},
    "dance_seven": {"sleep_time": 67, "action": ["41", "1"], "name": "dance_seven"},
    "dance_six": {"sleep_time": 69, "action": ["40", "1"], "name": "dance_six"},
    "dance_ten": {"sleep_time": 85, "action": ["44", "1"], "name": "dance_ten"},
    "dance_three": {"sleep_time": 70, "action": ["37", "1"], "name": "dance_three"},
    "dance_two": {"sleep_time": 52, "action": ["36", "1"], "name": "dance_two"},
    "go_forward": {"sleep_time": 3.5, "action": ["1", "4"], "name": "go_forward"},
    "kung_fu": {"sleep_time": 2, "action": ["46", "2"], "name": "kung_fu"},
    "left_kick": {"sleep_time": 2, "action": ["18", "1"], "name": "left_kick"},
    "left_move_fast": {"sleep_time": 3, "action": ["3", "4"], "name": "left_move_fast"},
    "left_shot_fast": {
        "sleep_time": 4,
        "action": ["13", "1"],
        "name": "left_shot_fast",
    },
    "left_uppercut": {"sleep_time": 2, "action": ["16", "1"], "name": "left_uppercut"},
    "push_ups": {"sleep_time": 9, "action": ["5", "1"], "name": "push_ups"},
    "right_kick": {"sleep_time": 2, "action": ["19", "1"], "name": "right_kick"},
    "right_move_fast": {
        "sleep_time": 3,
        "action": ["4", "4"],
        "name": "right_move_fast",
    },
    "right_shot_fast": {
        "sleep_time": 4,
        "action": ["14", "1"],
        "name": "right_shot_fast",
    },
    "right_uppercut": {
        "sleep_time": 2,
        "action": ["17", "1"],
        "name": "right_uppercut",
    },
    "sit_ups": {"sleep_time": 12, "action": ["6", "1"], "name": "sit_ups"},
    "squat": {"sleep_time": 1, "action": ["11", "1"], "name": "squat"},
    "squat_up": {"sleep_time": 6, "action": ["45", "1"], "name": "squat_up"},
    "stand": {"sleep_time": 1, "action": ["0", "1"], "name": "站立"},
    "stand_up_back": {"sleep_time": 5, "action": ["21", "1"], "name": "stand_up_back"},
    "stand_up_front": {
        "sleep_time": 5,
        "action": ["20", "1"],
        "name": "stand_up_front",
    },
    "stepping": {"sleep_time": 3, "action": ["24", "2"], "name": "stepping"},
    "stop": {"sleep_time": 3, "action": ["24", "2"], "name": "stop"},
    "turn_left": {"sleep_time": 4, "action": ["7", "4"], "name": "turn_left"},
    "turn_right": {"sleep_time": 4, "action": ["8", "4"], "name": "turn_right"},
    "twist": {"sleep_time": 4, "action": ["22", "1"], "name": "twist"},
    "wave": {"sleep_time": 3.5, "action": ["9", "1"], "name": "wave"},
    "weightlifting": {"sleep_time": 9, "action": ["35", "1"], "name": "weightlifting"},
    "wing_chun": {"sleep_time": 2, "action": ["15", "1"], "name": "wing_chun"},
}

idle_action: Dict[str, Any] = {"name": None, "sleep_time": 0}


class ApiProxy:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _sanitize_action_name(action_name: str) -> str:
        """Sanitize action_name to remove extra info or whitespace."""
        return action_name.strip().split()[0]

    @staticmethod
    def _get_action(action_name: str) -> Optional[Dict[str, Any]]:
        """Get action config by name, or None if not found."""
        return actions.get(action_name)

    def execute_action(self, robot_id: str, action_name: str) -> None:
        clean_name = self._sanitize_action_name(action_name)
        if clean_name == "stop":
            self._send_request(
                method="StopBusServo",
                robot_id=robot_id,
                action="StopAction",
                log_msg="Action run_stop_action() successful.",
            )
            self.logger.info("Stop action requested, stopping current action.")
            return
        action = self._get_action(clean_name)
        if not action:
            self.logger.error("Action '%s' not found.", clean_name)
            return
        self._send_request(
            method="RunAction",
            robot_id=robot_id,
            action=clean_name,
            log_msg=f"Action run_action({clean_name}) successful.",
        )

    def _send_request(
        self,
        method: str,
        robot_id: str,
        action: str,
        log_msg: str,
    ) -> Optional[Dict[str, Any]]:
        data = {"method": method, "action": action}
        try:
            response = requests.post(ROBOT_API_URL + robot_id, json=data, timeout=3)
            response.raise_for_status()
            self.logger.info("%s Response: %s", log_msg, response.json())
            return response.json()
        except requests.RequestException as e:
            self.logger.error("%s", e)
            return None

    def get_image(self, robot_id: str) -> Optional[str]:
        try:
            response = requests.get(ROBOT_IMAGE_API_URL + robot_id, timeout=3)
            response.raise_for_status()
            if response.headers.get("Content-Type") == "image/jpeg":
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".jpg", mode="wb"
                ) as tmp_file:
                    tmp_file.write(response.content)
                    return tmp_file.name
            self.logger.error(
                "Unexpected content type: %s", response.headers.get("Content-Type")
            )
            return None
        except requests.RequestException as e:
            self.logger.error("Error fetching image: %s", e)
            return None
