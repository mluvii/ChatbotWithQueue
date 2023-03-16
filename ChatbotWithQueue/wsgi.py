from main import app
import logging
import argparse

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO)

def main() -> None:
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-c", "--cert", help="Path to certificate")
    argParser.add_argument("-k", "--key", help="Path to certificate key")
    argParser.add_argument("-p", "--port", help="Port number where to run app")
    args = argParser.parse_args()
    logging.info(f'args: {args}')
    if args.port is None:
        logging.error('No port set in arguments')
        exit(1)
    if args.cert is not None and args.key is not None:
        context = (args.cert, args.key)
        app.run(host='0.0.0.0', port=args.port, ssl_context=context)
    else:
        app.run(host='0.0.0.0', port=args.port)


if __name__ == "__main__":
    main()
