<<<<<<< HEAD
# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Timing for Adafruit LED Animation library.

Author(s): Kattni Rembor
"""

try:
    from micropython import const
except ImportError:

    def const(value):  # pylint: disable=missing-docstring
        return value


try:
    from time import monotonic_ns

    monotonic_ns()  # Test monotonic_ns in 6.x

    def monotonic_ms():
        """
        Return monotonic time in milliseconds.
        """
        return monotonic_ns() // NANOS_PER_MS


except (ImportError, NotImplementedError):
    import time

    def monotonic_ms():
        """
        Implementation of monotonic_ms for platforms without time.monotonic_ns
        """
        return int(time.monotonic() * MS_PER_SECOND)


NANOS_PER_MS = const(1000000)
MS_PER_SECOND = const(1000)
=======
# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Timing for Adafruit LED Animation library.

Author(s): Kattni Rembor
"""

try:
    from micropython import const
except ImportError:

    def const(value):  # pylint: disable=missing-docstring
        return value


try:
    from time import monotonic_ns

    monotonic_ns()  # Test monotonic_ns in 6.x

    def monotonic_ms():
        """
        Return monotonic time in milliseconds.
        """
        return monotonic_ns() // NANOS_PER_MS


except (ImportError, NotImplementedError):
    import time

    def monotonic_ms():
        """
        Implementation of monotonic_ms for platforms without time.monotonic_ns
        """
        return int(time.monotonic() * MS_PER_SECOND)


NANOS_PER_MS = const(1000000)
MS_PER_SECOND = const(1000)
>>>>>>> bd7426db7ef11dff3ca508ff91a56c1e33f7dd28
