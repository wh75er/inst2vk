import argparse

parser = argparse.ArgumentParser(description="Exports instagram's posts to vk's public page via VK API token.")

parser.add_argument("-config", metavar="config-fname", nargs=1,
                    dest = "config",
                    default = "config",
                    help = "Config file with all properties.(dafult: 'config')")
parser.add_argument("-token", metavar='token-fname', nargs=1,
                    dest = "token",
                    default = "../token",
                    help = "File with required token(VK API).(default: '../token')")
parser.add_argument("-urls", metavar='file', nargs=1, 
                    dest = "urls",
                    default = "../urls",
                    help = "File with all instagram profiles urls.(default: '../urls')")

args = parser.parse_args()
