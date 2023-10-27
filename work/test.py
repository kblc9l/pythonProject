a = []


class NamedArgError(Exception):
    pass


class ShortResultError(Exception):
    pass


def oll_uncorrect(args, smells):
    count = 0
    for i in args:

        for j in str(smells):
            if j in str(len(str(i))):
                count += 1
                if count == len(args):
                    raise NamedArgError('Unsuitable named argument;')
                break
            else:
                a.append(i)


def oll_is_not_degit(args):
    for i in args:

        if str(i).isdigit():
            raise ValueError('Number has no len')


def check_len(args):
    if len(args) < 2:
        raise ShortResultError('Too short returned list')


def flavours(*args, smells=301):
    args = list(args)

    oll_uncorrect(args, smells)

    oll_is_not_degit(args)

    check_len(args)

    return sorted(list(set(a)), key=lambda x: (len(x), x[::-1]))
