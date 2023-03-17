from main import app
import logging
import argparse
from helpers import Bot, set_server_url, set_bot, set_gpt_key, get_server_url

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO)


def main() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-c", "--cert", help="Path to certificate")
    arg_parser.add_argument("-k", "--key", help="Path to certificate key")
    arg_parser.add_argument("-p", "--port", help="REQUIRED Port number where to run app")
    arg_parser.add_argument("-b", "--bot", help="Bot ID")
    arg_parser.add_argument("-s", "--server", help="Server URL without https://")
    arg_parser.add_argument("-a", "--api", help="mluvii API key")
    arg_parser.add_argument("-x", "--secret", help="mluvii API secret")
    arg_parser.add_argument("-g", "--gpt", help="Chat GPT key")
    args = arg_parser.parse_args()
    logging.info(f'args: {args}')

    set_server_url(args.server)
    set_gpt_key(args.gpt)

    server_url = get_server_url()

    api_key = args.api
    api_secret = args.secret
    bot_id = args.bot

    if args.port is None:
        logging.error('No port set in arguments')
        exit(1)
    if (server_url or api_key or api_secret or bot_id) and not (server_url and api_key and api_secret and bot_id):
        logging.error('You need to set server url,bot id, mluvii api key and mluvii api secret together')
        exit(1)
    if server_url and api_key and api_secret and bot_id:
        bot = Bot(bot_id, api_key, api_secret)
        set_bot(bot)
    if args.cert is not None and args.key is not None:
        context = (args.cert, args.key)
        app.run(host='0.0.0.0', port=args.port, ssl_context=context)
    else:
        app.run(host='0.0.0.0', port=args.port)


if __name__ == "__main__":
    main()
