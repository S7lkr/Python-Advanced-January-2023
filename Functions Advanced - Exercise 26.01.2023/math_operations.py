def math_operations(*numbers, **kwargs):

    for ind in range(len(numbers)):
        key = list(kwargs.keys())[ind % 4]

        if key == "a":
            kwargs["a"] += numbers[ind]
        elif key == "s":
            kwargs["s"] -= numbers[ind]
        elif key == "d":
            if numbers[ind] != 0:
                kwargs["d"] /= numbers[ind]
        elif key == "m":
            kwargs["m"] *= numbers[ind]

    return "\n".join([f"{k}: {v:.1f}" for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))