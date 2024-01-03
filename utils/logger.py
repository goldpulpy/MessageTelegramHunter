from datetime import datetime
from pathlib import Path

class Logger:

    def __init__(self, output_file: str = "logs.txt") -> None:

        # Initialize the Logger with an output file, defaulting to "logs.txt"
        self.output_file: str = output_file

    def log(self, message: str = None, 
            is_start: bool = False) -> str:

        # Get the current timestamp in the format "dd.mm.YYYY HH:MM:SS"
        now_time: str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        
        with open(Path(self.output_file), 'a') as file:

            # If is_start is True, log a message with a new line before it
            if is_start:

                file.write("\n%s - %s\n" % (now_time, message))

            else:

                # Log a message without a new line before it
                file.write("%s - %s\n" % (now_time, message))

        # Return the formatted log message
        return "%s - %s" % (now_time, message)