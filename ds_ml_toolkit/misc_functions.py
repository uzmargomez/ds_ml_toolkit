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