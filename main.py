from utils import Config, Logger
from app import Session, Filter

from time import sleep as wait


# Init objects
config: Config = Config(config="config.json")
logger: Logger = Logger(output_file="logs.txt")


def main():
    try:

        print(logger.log(
            '[+] Started - Message Telegram Hunter',
            is_start=True
        ))

        # Config load
        if not config.load_config():

            print(logger.log(
                '[-] [File] Config not found : "%s" - not found' % config.config
                ))

            return

        print(logger.log(
            '[+] [File] Config loaded successfully <- "%s"' % config.config
            ))

        message_filter: Filter = Filter(words_file = "words.json",
                                        memory_limit = config.MEMORY_LIMIT)

        session: Session = Session(
            api_id=config.API_ID, 
            api_hash=config.API_HASH, 
            session_name=config.SESSION_NAME,
            report_score=config.REPORT_SCORE

        )

        if not session.check_session():

            print(logger.log(
                '[-] [Telegram] Session not authorized : Error'
                ))

            return

        print(logger.log(
            '[+] [Telegram] Session loaded successfully <- "%s"' % session.session_name
        ))

        print(
            logger.log(
                '[Session] ID: %i | Username: @%s | First Name: %s -> Logged in' % (
                session.user_id, session.username, session.first_name)
            )
        )

        if not message_filter.load():

            print(logger.log(
                '[-] [Filter] words file found : "%s" - not found' % message_filter.words_file
            ))

            return

        print(logger.log(
            '[+] [Filter] loaded successfully <- "%s"' % message_filter.words_file
        ))

        if not session.push_start(config.FORWARD_TO_ID):

            print(logger.log(
                    '[-] [Session] -> System not started : Error, Forward to chat not found'
                )
            )

            return

        print(logger.log(
            '[+] [Session] -> System suscessfully started, set home chat: "%s"' % (
                session.home_chat.name)
        ))

        print(logger.log(
            "[INFO] [Session] Targets: %s -> Get message pool " % (
                len(session.chats)-1
            )
        ))

        if not session.get_pool(config.MESSAGE_POOL):

            print(logger.log(
                '[-] [Session] -> System not started : Error get message pool'
            ))
            return

        print(logger.log(
            '[INFO] [Session] Getted message pool -> Start Parser system [wait new messages]'
        ))



        while True:

            wait(config.WAIT_TIME)

            try:

                new_message, trigger_message = session.check_new_message(config.MESSAGE_POOL, message_filter)

                if new_message == 0:

                    continue

                print(logger.log(
                '[PARSER] New messages: %i | Trigger messages: %i %s' % (
                    new_message, trigger_message,
                    '-> Home chat' if trigger_message != 0 else '')
                ))



            except Exception as err:

                wait(120)

                print(logger.log(
                    '[-] Error : %s' % err
                ))


    except Exception as err:

        session.disconnect()

        print(logger.log(
            '[-] Error : %s' % err
        ))



if __name__ == "__main__":
    main()