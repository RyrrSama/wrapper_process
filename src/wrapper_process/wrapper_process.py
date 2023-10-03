# Default imports
import subprocess
from future.utils import raise_from

# Local imports
from .exceptions import WrapperProcessException


def run_process(
    cmd,
    is_shell_cmd=False,
    print_output=True,
    output_stream=None,
    error_stream=None,
    raise_exception=True,
    convert_response_text=True,
):
    """
    Runs the given cmd Sequence in the process and wait to complete.
    Return: subprocess.CompletedProcess Object
    """
    if not isinstance(cmd, list):
        raise WrapperProcessException(
            f"args value for 'cmd' parameter must be a 'list' type but got {cmd.type()}"
        )

    args = {
        "args": cmd,
        "shell": is_shell_cmd,
        "check": raise_exception,
        "text": convert_response_text,
        "universal_newlines": True,
    }
    if print_output:
        if output_stream:
            args["stdout"] = output_stream
        if error_stream:
            args["stderr"] = error_stream
    else:
        args["capture_output"] = True

    try:
        called_process_instance = subprocess.run(**args)

    except FileNotFoundError as exc:
        raise_from(
            WrapperProcessException(
                f"'Program' or 'Script' not found in target system. please validate cmd sequence provided. For more details refer the execution output {exc}"
            ),
            exc,
        )
    except subprocess.TimeoutExpired as exc:
        raise_from(
            WrapperProcessException(
                f"Process cmd Took long time complete. For more details refer the execution output {exc}"
            ),
            exc,
        )
    except subprocess.CalledProcessError as exc:
        raise_from(
            WrapperProcessException(
                f"Process cmd return non zero return code. For more details refer the execution output {exc}"
            ),
            exc,
        )
    return called_process_instance
