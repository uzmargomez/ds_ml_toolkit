import sys

def progress(count, total, status=""):
    """
    Code taken from the repository
    https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    It has the MIT licence
    """
    bar_len = 36
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = "=" * filled_len + "-" * (bar_len - filled_len)

    sys.stdout.write(
        "[%s] %s%s %s Total grid points:%s\r"
        % (bar, percents, "%", status, total)
    )
    sys.stdout.flush()

def get_logger(name="",level=None):
    if level is not None:
        # read logging level from yaml CONFIG file
        if level == "INFO":
            level = logging.INFO
        elif level == "DEBUG":
            level = logging.DEBUG
        elif level == "ERROR":
            level = logging.ERROR
        elif level == "CRITICAL":
            level = logging.CRITICAL
        else:
            level = logging.INFO
    else:
        level = logging.INFO

    logger = logging.getLogger(name=name)
    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)8s] (%(filename)s:%(lineno)s) %(message)s ", 
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        )
    return logger