# We can mix keyword arguments and positional arguments.
# But the positional arguments must appear first followed by the keyword arguments
# Otherwise we get an error

showInterest(1000.0, rate=0.1, periods=10)