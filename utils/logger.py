from datetime import datetime
from pathlib import Path


class Logger:


    def __init__(self, output_file: str = "logs.txt") -> None:

        self.output_file: str = output_file

    def log(self,   message: str = None,
                    is_start: bool = False
    ) -> str:

        now_time: str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        
        with open(Path(self.output_file), 'a') as file:

            if is_start:

                file.write("\n%s - %s\n" % (now_time, message))

            else:

                file.write("%s - %s\n" % (now_time, message))


        return "%s - %s" % (now_time, message) 

    