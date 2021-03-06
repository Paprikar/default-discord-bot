import argparse
import os

from bot import DiscordBot


def run(config_path, no_chdir=False):
    if not no_chdir:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    bot = DiscordBot(config_path)
    bot.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config',
        default='config.json',
        type=str,
        help='path to configuration file',
        metavar='PATH')
    parser.add_argument(
        '--no-chdir',
        action='store_true',
        help='do not change the current working directory '
             'to one containing launch.py')
    args = parser.parse_args()

    run(args.config, args.no_chdir)
